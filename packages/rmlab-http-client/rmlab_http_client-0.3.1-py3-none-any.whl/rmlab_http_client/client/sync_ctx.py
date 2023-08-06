import logging
from typing import Any, Optional, Union
import aiohttp

from rmlab_http_client.cache import Cache

from rmlab_errors import (
    ExpiredTokenError,
    ValueError,
)

from rmlab_http_client.types import (
    AuthType,
    Endpoint,
)

from rmlab_http_client.client._core import (
    _HTTPClientBase,
    HTTPClientApiKey,
    HTTPClientBasic,
    HTTPClientJWT,
    HTTPClientPublic,
)


class HTTPClientJWTExpirable:
    """HTTP Client context requring jwt auth, recovers at expiration given a refresh token"""

    def __init__(
        self,
        endpoint: Endpoint,
        address: str,
        *,
        refresh_address: str,
        refresh_endpoint: Endpoint,
        access_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ):
        """Initializes instance.

        Args:
            endpoint (Endpoint): _description_
            address (str): _description_
            refresh_address (str): _description_
            refresh_endpoint (Endpoint): _description_
            access_token (Optional[str], optional): Access JWT. Defaults to None.
            refresh_token (Optional[str], optional): Refresh JWT. Defaults to None.

        Raises:
            ValueError: _description_
            ValueError: _description_
        """

        self._access_endpoint = endpoint

        self._request_address = address
        self._refresh_address = refresh_address
        self._access_token = access_token or Cache.get_credential("access_token")
        self._refresh_token = refresh_token or Cache.get_credential("refresh_token")
        if self._access_token is None:
            raise ValueError(f"Undefined access token")
        if self._refresh_token is None:
            raise ValueError(f"Undefined refresh token")

        self._retry = False

        self._refresh_endpoint = refresh_endpoint

    async def __aenter__(self):
        """Initializes asynchronous context manager for resources behind expiration-aware JWT auth.

        Returns:
            HTTPClientJWTExpirable: This client instance.
        """

        self._retry = True

        return self

    async def __aexit__(self, exc_ty, exc_val, tb):

        if exc_ty is not None:
            logging.error(
                f"HTTPClientJWTExpirable context manager got error {exc_ty}. Re-raising"
            )
            # Return None or False => re-raise
        else:
            return True

    async def submit_request(
        self, data: Optional[Union[aiohttp.FormData, dict]] = None
    ) -> Any:
        """Submit requests resilient to access token expiration.

        Args:
            data (Optional[Union[aiohttp.FormData, dict]], optional): Data payload. Defaults to None.

        Returns:
            Any: Response data payload or None
        """

        while self._retry:

            try:

                # We won't retry unless a ExpiredTokenError is raised
                if self._retry:
                    self._retry = False

                async with SyncClient(
                    self._access_endpoint,
                    address=self._request_address,
                    access_token=self._access_token,
                ) as access_client:

                    return await access_client.submit_request(data)

            except ExpiredTokenError:

                async with SyncClient(
                    self._refresh_endpoint,
                    address=self._refresh_address,
                    access_token=self._refresh_token,
                ) as refresh_client:

                    auth_resp = await refresh_client.submit_request()

                # Re-set credentials
                self._access_token = None
                self._refresh_token = None
                Cache.set_credential("refresh_token", auth_resp["refresh_token"])
                Cache.set_credential("access_token", auth_resp["access_token"])

                self._retry = True


def SyncClient(
    endpoint: Endpoint,
    *,
    address: str,
    basic_auth: Optional[str] = None,
    api_key: Optional[str] = None,
    access_token: Optional[str] = None,
    refresh_token: Optional[str] = None,
    refresh_address: Optional[str] = None,
    refresh_endpoint: Optional[Endpoint] = None,
) -> _HTTPClientBase:
    """Creates a context for a synchronous HTTP client.

    Args:
        endpoint (Endpoint): Endpoint instance.
        address (str): Base address.
        basic_auth (Optional[str], optional): Basic auth data, required if endpoint.auth is BASIC. Defaults to None.
        api_key (Optional[str], optional): Api key auth data, required if endpoint.auth is APIKEY. Defaults to None.
        access_token (Optional[str], optional): Access jwt data, required if endpoint.auth is JWT. Defaults to None.
        refresh_token (Optional[str], optional): Refresh jwt data, required if endpoint.auth is JWT_EXPIRABLE. Defaults to None.
        refresh_address (Optional[str], optional): Address for token refresh, required if endpoint.auth is JWT_EXPIRABLE. Defaults to None.
        refresh_endpoint (Optional[List[str]], optional): Resource for token refresh, required if endpoint.auth is JWT_EXPIRABLE. Defaults to None.

    Raises:
        ValueError: If any argument dependent on endpoint.auth is not passed

    Returns:
        HTTPClientBase: A synchronous http client context.
    """

    if endpoint.auth == AuthType.PUBLIC:

        return HTTPClientPublic(endpoint=endpoint, address=address)

    elif endpoint.auth == AuthType.BASIC:

        return HTTPClientBasic(
            endpoint=endpoint, address=address, basic_auth=basic_auth
        )

    elif endpoint.auth == AuthType.APIKEY:

        return HTTPClientApiKey(endpoint=endpoint, address=address, api_key=api_key)

    elif endpoint.auth == AuthType.JWT:

        return HTTPClientJWT(
            endpoint=endpoint,
            address=address,
            jwt=access_token,
        )

    elif endpoint.auth == AuthType.JWT_EXPIRABLE:

        if refresh_address is None:
            raise ValueError(f"Require `refresh_address` for endpoint")
        if refresh_endpoint is None:
            raise ValueError(f"Require `refresh_endpoint` for endpoint")

        endpoint_as_jwt = Endpoint(
            id=endpoint.id,
            resource=endpoint.resource,
            method=endpoint.method,
            payload=endpoint.payload,
            auth=AuthType.JWT,
            communication=endpoint.communication,
            response=endpoint.response,
            arguments=endpoint.arguments,
        )

        return HTTPClientJWTExpirable(
            endpoint=endpoint_as_jwt,
            address=address,
            access_token=access_token,
            refresh_token=refresh_token,
            refresh_address=refresh_address,
            refresh_endpoint=refresh_endpoint,
        )

    else:

        raise ValueError(f"Unhandled auth type `{endpoint.auth}`")
