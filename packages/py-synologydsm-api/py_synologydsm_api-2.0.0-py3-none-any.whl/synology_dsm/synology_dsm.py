"""Class to interact with Synology DSM."""
import logging
import socket
from json import JSONDecodeError
from urllib.parse import quote

import aiohttp
import async_timeout
from requests.exceptions import RequestException

from .api.core.security import SynoCoreSecurity
from .api.core.share import SynoCoreShare
from .api.core.system import SynoCoreSystem
from .api.core.upgrade import SynoCoreUpgrade
from .api.core.utilization import SynoCoreUtilization
from .api.download_station import SynoDownloadStation
from .api.dsm.information import SynoDSMInformation
from .api.dsm.network import SynoDSMNetwork
from .api.storage.storage import SynoStorage
from .api.surveillance_station import SynoSurveillanceStation
from .const import API_AUTH, API_INFO, SENSITIV_PARAMS
from .exceptions import (
    SynologyDSMAPIErrorException,
    SynologyDSMAPINotExistsException,
    SynologyDSMLogin2SAFailedException,
    SynologyDSMLogin2SAForcedException,
    SynologyDSMLogin2SARequiredException,
    SynologyDSMLoginDisabledAccountException,
    SynologyDSMLoginFailedException,
    SynologyDSMLoginInvalidException,
    SynologyDSMLoginPermissionDeniedException,
    SynologyDSMRequestException,
)

_LOGGER = logging.getLogger(__name__)


class SynologyDSM:
    """Class containing the main Synology DSM functions."""

    DSM_5_WEIRD_URL_API = [
        SynoStorage.API_KEY,
    ]

    def __init__(
        self,
        session: aiohttp.ClientSession,
        dsm_ip: str,
        dsm_port: int,
        username: str,
        password: str,
        use_https: bool = False,
        timeout: int = 10,
        device_token: str = None,
        debugmode: bool = False,
    ):
        """Constructor method."""
        self.username = username
        self._password = password
        self._timeout = timeout
        self._debugmode = debugmode

        # Session
        self._session = session

        # Login
        self._session_id = None
        self._syno_token = None
        self._device_token = device_token

        # Services
        self._apis = {
            "SYNO.API.Info": {"maxVersion": 1, "minVersion": 1, "path": "query.cgi"}
        }
        self._download = None
        self._information = None
        self._network = None
        self._security = None
        self._share = None
        self._storage = None
        self._surveillance = None
        self._system = None
        self._utilisation = None
        self._upgrade = None

        # Build variables
        if use_https:
            self._base_url = f"https://{dsm_ip}:{dsm_port}"
        else:
            self._base_url = f"http://{dsm_ip}:{dsm_port}"

    def _debuglog(self, message: str):
        """Outputs message if debug mode is enabled."""
        _LOGGER.debug(message)
        if self._debugmode:
            print("DEBUG: " + message)

    def _is_weird_api_url(self, api: str) -> bool:
        """Returns True if the API URL is not common.

        Common template is nas_base_url/webapi/path?params
        Only handles DSM 5 for now.
        """
        return (
            api in self.DSM_5_WEIRD_URL_API
            and self._information
            and self._information.version
            and int(self._information.version) < 7321  # < DSM 6
        )

    def _build_url(self, api: str) -> str:
        if self._is_weird_api_url(api):
            if api == SynoStorage.API_KEY:
                return (
                    f"{self._base_url}/webman/modules/StorageManager/"
                    f"storagehandler.cgi?"
                )

        return f"{self._base_url}/webapi/{self.apis[api]['path']}?"

    async def discover_apis(self):
        """Retreives available API infos from the NAS."""
        if self._apis.get(API_AUTH):
            return
        data = await self.get(API_INFO, "query")
        self._apis = data["data"]

    @property
    def apis(self):
        """Gets available API infos from the NAS."""
        return self._apis

    async def login(self, otp_code: str = None) -> bool:
        """Create a logged session."""
        # First reset the session
        self._debuglog("Creating new session")

        params = {
            "account": self.username,
            "passwd": self._password,
            # "enable_syno_token": "yes",
            "enable_device_token": "yes",
            "device_name": socket.gethostname(),
        }

        if otp_code:
            params["otp_code"] = otp_code
        if self._device_token:
            params["device_id"] = self._device_token

        # Request login
        result = await self.get(API_AUTH, "login", params)

        # Handle errors
        if result.get("error"):
            switcher = {
                400: SynologyDSMLoginInvalidException(self.username),
                401: SynologyDSMLoginDisabledAccountException(self.username),
                402: SynologyDSMLoginPermissionDeniedException(self.username),
                403: SynologyDSMLogin2SARequiredException(self.username),
                404: SynologyDSMLogin2SAFailedException(),
                406: SynologyDSMLogin2SAForcedException(self.username),
            }
            raise switcher.get(
                result["error"]["code"],
                SynologyDSMLoginFailedException(result["error"]["code"], self.username),
            )

        # Parse result if valid
        self._session_id = result["data"]["sid"]
        if result["data"].get("synotoken"):
            # Not available on API version < 3
            self._syno_token = result["data"]["synotoken"]
        if result["data"].get("did"):
            # Not available on API version < 6 && device token is given once
            # per device_name
            self._device_token = result["data"]["did"]
        if result["data"].get("device_id"):
            # Not available on API version < 7
            self._device_token = result["data"]["device_id"]
        self._debuglog("Authentication successful, token: " + str(self._session_id))

        if not self._information:
            self._information = SynoDSMInformation(self)
            await self._information.update()

        return result["success"]

    async def logout(self) -> bool:
        """Log out of the session."""
        result = await self.get(API_AUTH, "logout")
        return result["success"]

    @property
    def device_token(self) -> str:
        """Gets the device token.

        Used to remember the 2SA access was granted on this device.
        """
        return self._device_token

    async def get(self, api: str, method: str, params: dict = None, **kwargs):
        """Handles API GET request."""
        return await self._request("GET", api, method, params, **kwargs)

    async def post(self, api: str, method: str, params: dict = None, **kwargs):
        """Handles API POST request."""
        return await self._request("POST", api, method, params, **kwargs)

    async def _request(
        self,
        request_method: str,
        api: str,
        method: str,
        params: dict = None,
        retry_once: bool = True,
        **kwargs,
    ):
        """Handles API request."""
        # Discover existing APIs
        if api != API_INFO:
            await self.discover_apis()

        # Check if logged
        if not self._session_id and api not in [API_AUTH, API_INFO]:
            await self.login()

        # Build request params
        if not params:
            params = {}
        params["api"] = api
        params["version"] = 1

        if not self._is_weird_api_url(api):
            # Check if API is available
            if not self.apis.get(api):
                raise SynologyDSMAPINotExistsException(api)
            params["version"] = self.apis[api]["maxVersion"]
            max_version = kwargs.pop("max_version", None)
            if max_version and params["version"] > max_version:
                params["version"] = max_version

        params["method"] = method

        if api == SynoStorage.API_KEY:
            params["action"] = method
        if self._session_id:
            params["_sid"] = self._session_id
        if self._syno_token:
            params["SynoToken"] = self._syno_token

        url = self._build_url(api)

        # Request data
        self._debuglog("API: " + api)
        self._debuglog("Request Method: " + request_method)
        response = await self._execute_request(request_method, url, params, **kwargs)
        self._debuglog("Successful returned data")
        self._debuglog("RESPONSE: " + str(response))

        # Handle data errors
        if isinstance(response, dict) and response.get("error") and api != API_AUTH:
            self._debuglog("Session error: " + str(response["error"]["code"]))
            if response["error"]["code"] == 119 and retry_once:
                # Session ID not valid
                # see https://github.com/aerialls/synology-srm/pull/3
                self._session_id = None
                self._syno_token = None
                self._device_token = None
                return self._request(request_method, api, method, params, False)
            raise SynologyDSMAPIErrorException(
                api, response["error"]["code"], response["error"].get("errors")
            )

        return response

    async def _execute_request(self, method: str, url: str, params: dict, **kwargs):
        """Function to execute and handle a request."""
        # Execute Request
        try:
            if method == "GET":
                encoded_params = "&".join(
                    f"{key}={quote(str(value))}" for key, value in params.items()
                )
                async with async_timeout.timeout(self._timeout):
                    response = await self._session.get(
                        url, params=encoded_params, **kwargs
                    )
            elif method == "POST":
                data = {}
                data.update(params)
                data.update(kwargs.pop("data", {}))
                data["mimeType"] = "application/json"
                kwargs["data"] = data
                self._debuglog("POST data: " + str(data))

                async with async_timeout.timeout(self._timeout):
                    response = await self._session.post(url, params=params, **kwargs)

            response_url = str(response.url)
            for param in SENSITIV_PARAMS:
                if params.get(param):
                    response_url = response_url.replace(
                        quote(params[param]), "********"
                    )
            self._debuglog("Request url: " + response_url)
            self._debuglog("Response status_code: " + str(response.status))
            self._debuglog("Response headers: " + str(dict(response.headers)))

            if response.status == 200:
                # We got a DSM response
                content_type = response.headers.get("Content-Type", "").split(";")[0]

                if content_type in [
                    "application/json",
                    "text/json",
                    "text/plain",  # Can happen with some API
                ]:
                    return await response.json()

                return await response.text()

            # We got a 400, 401 or 404 ...
            raise RequestException(response)

        except (aiohttp.ClientError, JSONDecodeError) as exp:
            raise SynologyDSMRequestException(exp) from exp

    async def update(self, with_information: bool = False, with_network: bool = False):
        """Updates the various instanced modules."""
        if self._download:
            await self._download.update()

        if self._information and with_information:
            await self._information.update()

        if self._network and with_network:
            await self._network.update()

        if self._security:
            await self._security.update()

        if self._utilisation:
            await self._utilisation.update()

        if self._storage:
            await self._storage.update()

        if self._share:
            await self._share.update()

        if self._surveillance:
            await self._surveillance.update()

        if self._system:
            await self._system.update()

        if self._upgrade:
            await self._upgrade.update()

    def reset(self, api: any) -> bool:
        """Reset an API to avoid fetching in on update."""
        if isinstance(api, str):
            if api in ("information", SynoDSMInformation.API_KEY):
                return False
            if hasattr(self, "_" + api):
                setattr(self, "_" + api, None)
                return True
            if api == SynoCoreSecurity.API_KEY:
                self._security = None
                return True
            if api == SynoCoreShare.API_KEY:
                self._share = None
                return True
            if api == SynoCoreSystem.API_KEY:
                self._system = None
                return True
            if api == SynoCoreUpgrade.API_KEY:
                self._upgrade = None
                return True
            if api == SynoCoreUtilization.API_KEY:
                self._utilisation = None
                return True
            if api == SynoDownloadStation.API_KEY:
                self._download = None
                return True
            if api == SynoStorage.API_KEY:
                self._storage = None
                return True
            if api == SynoSurveillanceStation.API_KEY:
                self._surveillance = None
                return True
        if isinstance(api, SynoCoreSecurity):
            self._security = None
            return True
        if isinstance(api, SynoCoreShare):
            self._share = None
            return True
        if isinstance(api, SynoCoreSystem):
            self._system = None
            return True
        if isinstance(api, SynoCoreUpgrade):
            self._upgrade = None
            return True
        if isinstance(api, SynoCoreUtilization):
            self._utilisation = None
            return True
        if isinstance(api, SynoDownloadStation):
            self._download = None
            return True
        if isinstance(api, SynoStorage):
            self._storage = None
            return True
        if isinstance(api, SynoSurveillanceStation):
            self._surveillance = None
            return True
        return False

    @property
    def download_station(self) -> SynoDownloadStation:
        """Gets NAS DownloadStation."""
        if not self._download:
            self._download = SynoDownloadStation(self)
        return self._download

    @property
    def information(self) -> SynoDSMInformation:
        """Gets NAS informations."""
        if not self._information:
            self._information = SynoDSMInformation(self)
        return self._information

    @property
    def network(self) -> SynoDSMNetwork:
        """Gets NAS network informations."""
        if not self._network:
            self._network = SynoDSMNetwork(self)
        return self._network

    @property
    def security(self) -> SynoCoreSecurity:
        """Gets NAS security informations."""
        if not self._security:
            self._security = SynoCoreSecurity(self)
        return self._security

    @property
    def share(self) -> SynoCoreShare:
        """Gets NAS shares information."""
        if not self._share:
            self._share = SynoCoreShare(self)
        return self._share

    @property
    def storage(self) -> SynoStorage:
        """Gets NAS storage informations."""
        if not self._storage:
            self._storage = SynoStorage(self)
        return self._storage

    @property
    def surveillance_station(self) -> SynoSurveillanceStation:
        """Gets NAS SurveillanceStation."""
        if not self._surveillance:
            self._surveillance = SynoSurveillanceStation(self)
        return self._surveillance

    @property
    def system(self) -> SynoCoreSystem:
        """Gets NAS system information."""
        if not self._system:
            self._system = SynoCoreSystem(self)
        return self._system

    @property
    def upgrade(self) -> SynoCoreUpgrade:
        """Gets NAS upgrade informations."""
        if not self._upgrade:
            self._upgrade = SynoCoreUpgrade(self)
        return self._upgrade

    @property
    def utilisation(self) -> SynoCoreUtilization:
        """Gets NAS utilisation informations."""
        if not self._utilisation:
            self._utilisation = SynoCoreUtilization(self)
        return self._utilisation
