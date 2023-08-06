from collections import defaultdict
import json, asyncio, random, logging
from typing import List, Mapping
import pytest

from aiohttp import web
from aiohttp.test_utils import TestClient
from rmlab_errors import (
    ClientError,
    error_handler,
    exception_to_http_code,
    RuntimeError,
    ClientError,
    TimeoutError,
    ExpiredSessionError,
)

from rmlab_http_client import (
    AsyncClient,
)
from rmlab_http_client.types import (
    AsyncEndpoint,
    AuthType,
    AsyncEndpoint,
    DataRequestContext,
    Endpoint,
    MethodType,
    PayloadArguments,
    PayloadType,
    ResponseType,
)

_EventsLog: Mapping[str, List[str]] = defaultdict(list)
_Tasks: Mapping[str, asyncio.Task] = dict()

logging.basicConfig(level=logging.DEBUG)


_ContextArgs = {
    "basic_auth": "mock-basic",
    "api_key": "mock-key",
    "access_token": "mock-jwt",
    "refresh_token": "refresh-jwt",
    "refresh_endpoint": Endpoint(
        resource=["refresh"],
        method=MethodType.POST,
        payload=PayloadType.NONE,
        auth=AuthType.JWT,
        response=ResponseType.JSON,
        arguments=PayloadArguments(),
    ),
}


async def async_task_signature(request_data: str):
    pass


async def async_task(data: dict, operation_id: str):

    mock_events = ["a", "b", "c"]

    _EventsLog[operation_id].append("started")

    for mock_event in mock_events:
        await asyncio.sleep(1)
        print(f"Mock event {mock_event}")
        _EventsLog[operation_id].append("processing-" + mock_event)

    if data["request_data"] == "correct":
        _EventsLog[operation_id].append("success")
    else:
        _EventsLog[operation_id].append("failure")


async def backend_poll_status(operation_id: str):

    return {
        "status": _EventsLog[operation_id][-1]
        if _EventsLog[operation_id][-1] == "success"
        or _EventsLog[operation_id][-1] == "failure"
        else "pending"
    }


async def server_operation_status(request):

    resp_payload = dict()

    try:

        assert request.method == "GET"
        operation_id = request.match_info["operation_id"]

        resp_data = await backend_poll_status(operation_id)

        resp_payload = {
            "status": 200,
            "content_type": "application/json",
            "body": json.dumps(resp_data).encode(),
        }

    except Exception as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }

    finally:

        return web.Response(**resp_payload)


async def backend_result(operation_id: str):

    resp_status = await backend_poll_status(operation_id)
    status = resp_status["status"]

    if status == "pending":
        raise ClientError(f"Cannot fetch result of pending operation")
    elif status == "success":
        return {"async-resource-key": "async-resource-value"}
    elif status == "failure":
        # Does not matter the exception type, but be different than ClientError
        raise RuntimeError(f"Async operation failed")


async def server_operation_result(request):

    resp_payload = dict()

    try:

        assert request.method == "GET"
        operation_id = request.match_info["operation_id"]

        result = await backend_result(operation_id)

        resp_payload = {
            "status": 200,
            "content_type": "application/json",
            "body": json.dumps(result).encode(),
        }

    except Exception as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }

    finally:

        del _EventsLog[operation_id]

        del _Tasks[operation_id]

        return web.Response(**resp_payload)


async def server(request):

    resp_payload = dict()

    try:

        assert request.method == "POST"

        data = await request.json()

        operation_id = str(random.randint(1000, 9999))

        task = asyncio.get_running_loop().create_task(async_task(data, operation_id))

        _EventsLog[operation_id].append("created")
        _Tasks[operation_id] = task

        resp_payload = {
            "status": 202,
            "content_type": "application/json",
            "body": json.dumps(
                {
                    PayloadArguments.ASYNC_ID_KEY: operation_id,
                }
            ).encode(),
        }

    except Exception as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }
    finally:

        return web.Response(**resp_payload)


async def server_jwt_refresh(request):

    resp_payload = {}

    try:

        assert request.method == "POST"

        auth_content = request.headers["Authorization"]
        assert "Bearer " in auth_content

        if "expired" in auth_content:
            raise ExpiredSessionError("Refresh token is expired")
        else:

            resp_payload = {
                "status": 200,
                "content_type": "application/json",
                "body": json.dumps(
                    {"access_token": "new-access", "refresh_token": "new-refresh"}
                ).encode(),
            }

    except ExpiredSessionError as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }
    finally:

        return web.Response(**resp_payload)


async def case_async(aiohttp_client, auth, arg_data, expect_exception, timeout):

    app = web.Application()
    app.router.add_route("POST", "/async_resource", server)

    app.router.add_route(
        "GET", "/async_resource/status/{operation_id}", server_operation_status
    )
    app.router.add_route(
        "GET", "/async_resource/result/{operation_id}", server_operation_result
    )
    app.router.add_route("POST", "/refresh", server_jwt_refresh)
    client: TestClient = await aiohttp_client(app)

    addr = "http://" + client.host + ":" + str(client.port)

    poll_endpoint = Endpoint(
        id="poll-endpoint-id",
        resource=["async_resource", "status"],
        method=MethodType.GET,
        payload=PayloadType.MATCH,
        auth=AuthType.PUBLIC,
        response=ResponseType.JSON,
        arguments=PayloadArguments.make_from_function(backend_poll_status),
    )

    result_endpoint = Endpoint(
        id="result-endpoint-id",
        resource=["async_resource", "result"],
        method=MethodType.GET,
        payload=PayloadType.MATCH,
        auth=AuthType.PUBLIC,
        response=ResponseType.JSON,
        arguments=PayloadArguments.make_from_function(backend_result),
    )

    async_endpoint = AsyncEndpoint(
        resource=["async_resource"],
        method=MethodType.POST,
        payload=PayloadType.JSON,
        auth=auth,
        response=ResponseType.JSON,
        arguments=PayloadArguments.make_from_function(async_task_signature),
        timeout=timeout,
        poll_interval=0.2,
        poll_endpoint_id=poll_endpoint.id,
        result_endpoint_id=result_endpoint.id,
    )

    data = DataRequestContext.make_data(async_endpoint, request_data=arg_data)

    if expect_exception is None:

        async with AsyncClient(
            address=addr,
            refresh_address=addr,
            async_endpoint=async_endpoint,
            poll_endpoint=poll_endpoint,
            result_endpoint=result_endpoint,
            **_ContextArgs,
        ) as async_client:

            resp_data = await async_client.submit_request(data)

        assert "async-resource-key" in resp_data
        assert resp_data["async-resource-key"] == "async-resource-value"

    else:

        with pytest.raises(expect_exception):

            async with AsyncClient(
                address=addr,
                refresh_address=addr,
                async_endpoint=async_endpoint,
                poll_endpoint=poll_endpoint,
                result_endpoint=result_endpoint,
                **_ContextArgs,
            ) as async_client:

                resp_data = await async_client.submit_request(data)


_EnoughTimeSec = 4
_NotEnoughTimeSec = 1


Auths = [
    AuthType.PUBLIC,
    AuthType.BASIC,
    AuthType.APIKEY,
    AuthType.JWT,
    AuthType.JWT_EXPIRABLE,
]
RequestData = ["correct", "incorrect"]
Timeout = [_EnoughTimeSec, _NotEnoughTimeSec]


@pytest.mark.parametrize("auth", Auths)
@pytest.mark.parametrize("req_data", RequestData)
@pytest.mark.parametrize("timeout", Timeout)
async def test_auth(aiohttp_client, auth, req_data, timeout):

    if timeout == _EnoughTimeSec:
        if req_data == "correct":
            expect_exception = None
        else:
            expect_exception = RuntimeError
    else:
        expect_exception = TimeoutError

    await case_async(
        aiohttp_client,
        auth,
        arg_data=req_data,
        expect_exception=expect_exception,
        timeout=timeout,
    )
