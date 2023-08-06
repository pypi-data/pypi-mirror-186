import logging
import time
import httpx
from aioayla.const import AYLA_URL

_LOGGER = logging.getLogger(__name__)


class AylaDevice:
    """An Ayla IoT Device."""

    def __init__(
        self,
        api: "AylaApi",
        product_name: str,
        model: str,
        dsn: str,
        gateway_dsn: str,
        oem_model: str,
        sw_version: str,
        template_id: int,
        mac: str,
        unique_hardware_id: str,
        hwsig: str,
        lan_ip: str,
        connected_at: str,
        key: int,
        lan_enabled: bool,
        has_properties: bool,
        product_class: str,
        connection_status: str,
        lat: str,
        lng: str,
        locality: str,
        device_type: str,
        gateway_type: str,
        dealer: str,
        manuf_model: str,
    ):

        self._api = api
        self._product_name = product_name
        self._model = model
        self._dsn = dsn
        self._gateway_dsn = gateway_dsn
        self._oem_model = oem_model
        self._sw_version = sw_version
        self._template_id = template_id
        self._mac = mac
        self._unique_hardware_id = unique_hardware_id
        self._hwsig = hwsig
        self._lan_ip = lan_ip
        self._connected_at = connected_at
        self._key = key
        self._lan_enabled = lan_enabled
        self._has_properties = has_properties
        self._product_class = product_class
        self._connection_status = connection_status
        self._lat = lat
        self._lng = lng
        self._locality = locality
        self._device_type = device_type
        self._gateway_type = gateway_type
        self._dealer = dealer
        self._manuf_model = manuf_model

    @property
    def product_name(self) -> str:
        """Retrieve the product name."""
        return self._product_name

    @property
    def model(self) -> str:
        """Retrieve the model name."""
        return self._model

    @property
    def dsn(self) -> str:
        """Retrieve the DSN."""
        return self._dsn

    @property
    def gateway_dsn(self) -> str:
        """Retrieve the gateway DSN."""
        return self._gateway_dsn

    @property
    def oem_model(self) -> str:
        """Retrieve the OEM model name."""
        return self._oem_model

    @property
    def sw_version(self) -> str:
        """Retrieve the software version."""
        return self._sw_version

    @property
    def template_id(self) -> int:
        """Retrieve the template id."""
        return self._template_id

    @property
    def mac(self) -> str:
        """Retrieve the MAC address."""
        return self._mac

    @property
    def unique_hardware_id(self) -> str:
        """Retrieve the unique hardware id."""
        return self._unique_hardware_id

    @property
    def hwsig(self) -> str:
        """Retrieve the hwardware signature."""
        return self._hwsig

    @property
    def lan_ip(self) -> str:
        """Retrieve the LAN IP."""
        return self._lan_ip

    @property
    def connected_at(self) -> str:
        """Retrieve the connected at time."""
        return self._connected_at

    @property
    def key(self) -> int:
        """Retrieve the device key."""
        return self._key

    @property
    def lan_enabled(self) -> bool:
        """Retrieve whether or not the device is LAN enabled."""
        return self._lan_enabled

    @property
    def has_properties(self) -> bool:
        """Retrieve whether or not the device has properties."""
        return self._has_properties

    @property
    def product_class(self) -> str:
        """Retrieve the product class."""
        return self._product_class

    @property
    def connection_status(self) -> str:
        """Retrieve the connection status."""
        return self._connection_status

    @property
    def lat(self) -> str:
        """Retrieve the device latitude."""
        return self._lat

    @property
    def lng(self) -> str:
        """Retrieve the device longitude."""
        return self._lng

    @property
    def locality(self) -> str:
        """Retrieve the device locality."""
        return self._locality

    @property
    def device_type(self) -> str:
        """Retrieve the device type."""
        return self._device_type

    @property
    def gateway_type(self) -> str:
        """Retrieve the gateway type."""
        return self._gateway_type

    @property
    def dealer(self) -> str:
        """Retrieve the dealer."""
        return self._dealer

    @property
    def manuf_model(self) -> str:
        """Retrieve the manufacturer model name."""
        return self._manuf_model

    async def get_data(self):
        """Retrieve device data points."""
        data = await self._api.api_get(f"/apiv1/dsns/{self._dsn}/data")
        result = {}
        for record in data:
            item = record["datum"]
            result[item["key"]] = item["value"]
        return result

    async def get_properties(self):
        """Retrieve device properties."""
        properties = await self._api.api_get(f"/apiv1/dsns/{self._dsn}/properties")

        result = {}
        for record in properties:
            property = record["property"]
            result[property["name"]] = property["value"]
        return result


class AylaApi:
    """Ayla IoT API connection."""

    def __init__(
        self, app_id: str, app_secret: str, client_session: httpx.AsyncClient = None
    ):
        self._expires_at = 0
        self._refresh_token = None
        self._access_token = None
        self._user_id = None
        self._app_id = app_id
        self._app_secret = app_secret
        self._client_session = client_session

    def __get_client(self) -> httpx.AsyncClient:
        """Return the httpx session to use."""
        if self._client_session is None:
            return httpx.AsyncClient()
        else:
            return self._client_session

    def __get_headers(self) -> dict[str, str]:
        """Retrieve the headers needed to make api calls."""

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if self._access_token is not None:
            headers["Authorization"] = "Bearer " + self._access_token

        return headers

    async def async_refresh_token(self) -> None:
        """Refresh the access token."""
        client = self.__get_client()

        res = await client.post(
            AYLA_URL + "/users/refresh_token",
            headers=self.__get_headers(),
            json={"user": {"refresh_token": self._refresh_token}},
        )
        res.raise_for_status()
        json_response = res.json()
        self._access_token = json_response["access_token"]
        self._refresh_token = json_response["refresh_token"]
        self._expires_at = time.time() + json_response["expires_in"]

    async def login(self, username: str, password: str) -> bool:
        """Login to the API."""
        client = self.__get_client()

        res = await client.post(
            AYLA_URL + "/users/sign_in",
            headers=self.__get_headers(),
            timeout=30,
            json={
                "user": {
                    "email": username,
                    "password": password,
                    "application": {
                        "app_id": self._app_id,
                        "app_secret": self._app_secret,
                    },
                }
            },
        )
        res.raise_for_status()
        json_content = res.json()
        self._access_token = json_content["access_token"]
        self._refresh_token = json_content["refresh_token"]
        self._expires_at = time.time() + json_content["expires_in"]
        return True

    async def api_get(self, path: str) -> any:
        """Make a get api call."""
        client = self.__get_client()

        if self._expires_at < time.time() + 100:
            await self.async_refresh_token()
        try:
            res = await client.get(AYLA_URL + path, headers=self.__get_headers())

            res.raise_for_status()
        except httpx.HTTPStatusError as err:
            if err.response.status_code == 403:
                await self.async_refresh_token()

                res = await client.get(AYLA_URL + path, headers=self.__get_headers())

                res.raise_for_status()
            else:
                raise

        return res.json()

    async def get_devices(self) -> list[AylaDevice]:
        json_content = await self.api_get("/apiv1/devices")

        self._devices = []

        for device in json_content:
            device_data = device.get("device", None)
            product_name = device_data.get("product_name", None)
            model = device_data.get("model", None)
            dsn = device_data.get("dsn", None)
            gateway_dsn = device_data.get("gateway_dsn", None)
            oem_model = device_data.get("oem_model", None)
            sw_version = device_data.get("sw_version", None)
            template_id = device_data.get("template_id", None)
            mac = device_data.get("mac", None)
            unique_hardware_id = device_data.get("unique_hardware_id", None)
            hwsig = device_data.get("hwsig", None)
            lan_ip = device_data.get("lan_ip", None)
            connected_at = device_data.get("connected_at", None)
            key = device_data.get("key", None)
            lan_enabled = device_data.get("lan_enabled", None)
            has_properties = device_data.get("has_properties", None)
            product_class = device_data.get("product_class", None)
            connection_status = device_data.get("connection_status", None)
            lat = device_data.get("lat", None)
            lng = device_data.get("lng", None)
            locality = device_data.get("locality", None)
            device_type = device_data.get("device_type", None)
            gateway_type = device_data.get("gateway_type", None)
            dealer = device_data.get("dealer", None)
            manuf_model = device_data.get("manuf_model", None)

            self._devices.append(
                AylaDevice(
                    self,
                    product_name,
                    model,
                    dsn,
                    gateway_dsn,
                    oem_model,
                    sw_version,
                    template_id,
                    mac,
                    unique_hardware_id,
                    hwsig,
                    lan_ip,
                    connected_at,
                    key,
                    lan_enabled,
                    has_properties,
                    product_class,
                    connection_status,
                    lat,
                    lng,
                    locality,
                    device_type,
                    gateway_type,
                    dealer,
                    manuf_model,
                )
            )

        return self._devices
