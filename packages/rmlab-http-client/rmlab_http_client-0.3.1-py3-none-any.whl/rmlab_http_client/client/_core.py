import logging, base64
from typing import Any, Optional, Union
import aiohttp
from rmlab_http_client.cache import Cache

_Logger = logging.getLogger(__name__)

from rmlab_errors import (
    HTTPRequestError,
    UnknownError,
    make_errors_from_json,
    http_code_to_exception,
)

from rmlab_http_client.types import (
    Endpoint,
    PayloadType,
    ResponseType,
)


class _HTTPClientBase:
    """Base class for HTTP clients handling different auth methods"""

    def __init__(self, endpoint: Endpoint, *, address: str):
        """Initializes instance.

        Args:
            address (str): Resource endpoint
        """

        self._endpoint = endpoint
        self._address: str = address
        self._session: aiohttp.ClientSession = None  # To be set in derived class
        self._verb2coro = dict()

    async def __aenter__(self):

        assert self._session is not None

        return self

    async def __aexit__(self, exc_ty, exc_val, tb):

        if not self._session.closed:
            await self._session.close()

        if exc_ty is not None:
            _Logger.error(
                f"HTTPClientBase context manager got error {exc_ty}: {exc_val}. Re-raising"
            )
            # Return None or False => re-raise
        else:
            return True

    async def submit_request(
        self, data: Optional[Union[aiohttp.FormData, dict]] = None
    ):

        err_obj = None

        if self._endpoint.payload == PayloadType.MATCH:

            addr = self._endpoint.address

            for key, value in data.items():
                addr = addr.replace("{" + key + "}", str(value))

            url = self._address + addr
            payload_args = dict()

        elif self._endpoint.payload == PayloadType.JSON:

            assert isinstance(data, dict) or isinstance(data, list)

            url = self._address + self._endpoint.address
            payload_args = {"json": data}

        elif self._endpoint.payload == PayloadType.MULTIPART:

            assert isinstance(data, aiohttp.FormData)

            url = self._address + self._endpoint.address
            payload_args = {"data": data}

        else:

            url = self._address + self._endpoint.address
            payload_args = dict()

        async with getattr(self._session, self._endpoint.method.value.lower())(
            url, **payload_args, timeout=self._endpoint.timeout
        ) as resp:

            resp: aiohttp.ClientResponse

            if 400 <= resp.status:

                if resp.content_type == "application/json":

                    resp_json = await resp.json()

                    if "errors" in resp_json:
                        err_obj = make_errors_from_json(*resp_json["errors"])
                    else:
                        resp_txt = await resp.text()
                        err_obj = UnknownError(resp_txt)
                else:
                    text = await resp.text()
                    err_obj = http_code_to_exception(
                        resp.status, text, HTTPRequestError
                    )

            elif self._endpoint.response == ResponseType.JSON:
                return await resp.json()

        if err_obj is not None:
            raise err_obj


class HTTPClientPublic(_HTTPClientBase):
    """Simple HTTP Client context without auth"""

    def __init__(self, endpoint: Endpoint, *, address: str):
        """Initializes instance.

        Args:
            address (str): Public resource endpoint
        """

        super(HTTPClientPublic, self).__init__(endpoint=endpoint, address=address)

    async def __aenter__(self):
        """Initializes asynchronous context manager, creating a http client for public resources.

        Returns:
            HTTPClientPublic: This client instance.
        """

        self._session = aiohttp.ClientSession(raise_for_status=False)

        return await super(HTTPClientPublic, self).__aenter__()


class HTTPClientBasic(_HTTPClientBase):
    """Simple HTTP Client context with basic auth"""

    def __init__(
        self, endpoint: Endpoint, address: str, *, basic_auth: Optional[str] = None
    ):
        """Initializes instance.

        Args:
            address (str): Resource endpoint behind the basic auth
            basic_auth (Optional[str]): Basic authentication data. Defaults to None.
        """

        super(HTTPClientBasic, self).__init__(endpoint=endpoint, address=address)

        basic_auth = basic_auth or Cache.get_credential("basic_auth")

        if basic_auth is None:
            raise ValueError(f"Undefined Basic auth")

        self._basic_auth = base64.b64encode(basic_auth.encode()).decode("utf-8")

    async def __aenter__(self):
        """Initializes asynchronous context manager, creating a http client session
        for resources behind basic auth.

        Returns:
            HTTPClientBasic: This client instance.
        """

        auth_headers = {"Authorization": "Basic " + self._basic_auth}

        self._session = aiohttp.ClientSession(
            headers=auth_headers, raise_for_status=False
        )

        return await super(HTTPClientBasic, self).__aenter__()


class HTTPClientApiKey(_HTTPClientBase):
    """HTTP Client context requring api key auth"""

    def __init__(
        self, endpoint: Endpoint, address: str, *, api_key: Optional[str] = None
    ):
        """Initializes instance.

        Args:
            address (str): Resource endpoint behind the api key
            api_key (Optional[str]): Api key. Defaults to None.
        """

        super(HTTPClientApiKey, self).__init__(endpoint=endpoint, address=address)

        self._api_key = api_key or Cache.get_credential("api_key")

        if self._api_key is None:
            raise ValueError(f"Undefined Api Key")

    async def __aenter__(self):
        """Initializes asynchronous context manager, creating a http client session
        for resources behind a API key.

        Returns:
            HTTPClientApiKey: This client instance.
        """

        auth_headers = {"X-Api-Key": self._api_key}

        self._session = aiohttp.ClientSession(
            headers=auth_headers, raise_for_status=False
        )

        return await super(HTTPClientApiKey, self).__aenter__()


class HTTPClientJWT(_HTTPClientBase):
    """HTTP Client context requring jwt auth"""

    def __init__(self, endpoint: Endpoint, address: str, *, jwt: Optional[str] = None):
        """Initializes instance.

        Args:
            address (str): Resource endpoint behind the access token
            jwt (Optional[str]): JWT (access or refresh). Defaults to None.
        """

        super(HTTPClientJWT, self).__init__(endpoint=endpoint, address=address)

        self._jwt = jwt or Cache.get_credential("access_token")

        if self._jwt is None:
            raise ValueError(f"Undefined JWT")

    async def __aenter__(self):
        """Initializes asynchronous context manager, creating a http client session
        for resources behind JWT auth.

        Returns:
            HTTPClientJWT: This client instance.
        """

        auth_headers = {"Authorization": "Bearer " + self._jwt}

        self._session = aiohttp.ClientSession(
            headers=auth_headers, raise_for_status=False
        )

        return await super(HTTPClientJWT, self).__aenter__()
