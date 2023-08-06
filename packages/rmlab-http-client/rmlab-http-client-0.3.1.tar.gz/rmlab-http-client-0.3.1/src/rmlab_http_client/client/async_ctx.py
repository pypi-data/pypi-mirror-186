import logging, asyncio
from typing import Any, Optional, Union
import aiohttp

from rmlab_errors import (
    TimeoutError,
)
from rmlab_http_client.client.sync_ctx import SyncClient

from rmlab_http_client.types import (
    AsyncEndpoint,
    AsyncResponseDefaultTimeout,
    DataRequestContext,
    Endpoint,
    CommunicationType,
    ResponseType,
)


class AsyncClient:
    """Wrapper over a client context to provide status polling and result fetching
    of a long-running asynchronous operation"""

    def __init__(
        self,
        address: str,
        async_endpoint: AsyncEndpoint,
        poll_endpoint: Endpoint,
        result_endpoint: Endpoint,
        **client_kwargs,
    ):
        """Initializes instance.
        * Creates sync access endpoint to trigger the operation and get the id
        * Stores the poll endpoint to poll server to get the operation status
        * Stores the result endpoint to get the result of the operation when finished

        Args:
            address (str): Base address
            async_endpoint (AsyncEndpoint): Async endpoint instance.
        """

        assert isinstance(async_endpoint, AsyncEndpoint)

        self._address = address
        self._timeout_seconds = async_endpoint.timeout
        self._prepoll_wait_seconds = async_endpoint.async_prepoll_wait
        self._poll_seconds = async_endpoint.async_poll_interval
        self._client_kwargs = client_kwargs

        self._access_endpoint = Endpoint(
            id=async_endpoint.id,
            resource=async_endpoint.resource,
            method=async_endpoint.method,
            payload=async_endpoint.payload,
            auth=async_endpoint.auth,
            communication=CommunicationType.SYNC,
            response=ResponseType.JSON,
            arguments=async_endpoint.arguments,
            timeout=AsyncResponseDefaultTimeout,
        )

        assert poll_endpoint.id == async_endpoint.async_poll_endpoint_id
        assert result_endpoint.id == async_endpoint.async_result_endpoint_id

        self._poll_endpoint = poll_endpoint
        self._result_endpoint = result_endpoint

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_ty, exc_val, tb):

        if exc_ty is not None:
            logging.error(f"AsyncClient context manager got error {exc_ty}. Re-raising")
            # Return None or False => re-raise
        else:
            return True

    async def submit_request(
        self, data: Optional[Union[aiohttp.FormData, dict]] = None
    ) -> Any:
        """Submits request to asynchronous endpoint,
        polling for the status and retrieving the result after completion.

        Args:
            data (Optional[Union[aiohttp.FormData, dict]], optional): Request data payload. Defaults to None.

        Raises:
            TimeoutError: If timeout exceeded.

        Returns:
            _type_: Data response payload of the asynchronous operation or None
        """

        passed_seconds = 0

        async with SyncClient(
            self._access_endpoint, address=self._address, **self._client_kwargs
        ) as async_client:

            async_resp = await async_client.submit_request(data)

        await asyncio.sleep(self._prepoll_wait_seconds)

        req_data_poll = DataRequestContext.make_data(self._poll_endpoint, **async_resp)
        req_data_result = DataRequestContext.make_data(
            self._result_endpoint, **async_resp
        )

        while passed_seconds < self._timeout_seconds:

            async with SyncClient(
                self._poll_endpoint, address=self._address, **self._client_kwargs
            ) as poll_client:

                poll_resp = await poll_client.submit_request(req_data_poll)

            if poll_resp["status"] == "pending":

                logging.debug(
                    f"Awaiting for pending {async_resp}. {passed_seconds} / {self._timeout_seconds}"
                )

                await asyncio.sleep(self._poll_seconds)

                passed_seconds += self._poll_seconds

            else:

                async with SyncClient(
                    self._result_endpoint, address=self._address, **self._client_kwargs
                ) as result_client:

                    result_resp = await result_client.submit_request(req_data_result)

                return (
                    result_resp
                    if self._result_endpoint.response == ResponseType.JSON
                    else None
                )

        raise TimeoutError(f"While awaiting for operation `{async_resp}`")
