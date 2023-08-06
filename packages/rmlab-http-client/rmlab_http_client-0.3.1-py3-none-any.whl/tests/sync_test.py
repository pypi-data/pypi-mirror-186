import pytest
import json, base64
from aiohttp import web

from aiohttp.test_utils import TestClient

from rmlab_http_client import (
    SyncClient,
)

from rmlab_errors import (
    ClientError,
    ExpiredSessionError,
    ExpiredTokenError,
    ForbiddenError,
    error_handler,
    exception_to_http_code,
)

from rmlab_http_client.types import (
    AuthType,
    DataRequestContext,
    DataRequestContextMultipart,
    Endpoint,
    FileType,
    MethodType,
    PayloadType,
    ResponseType,
    PayloadArguments,
)

_CorrectData = "correct"


async def backend_resource(request_data: str, method: str = "", auth: str = ""):

    if request_data == _CorrectData:
        return {"resource-key": "resource-value"}
    else:
        raise ClientError("Emulating a client error")


async def server_generic(request: web.Request):

    try:

        if request.can_read_body:
            data = await request.json()
        else:
            data = dict()
            data["request_data"] = request.match_info["request_data"]
            data["auth"] = request.match_info["auth"]
            data["method"] = request.match_info["method"]

        assert request.method == data["method"].upper()

        if "public" in data["auth"]:
            pass
        elif "jwt" in data["auth"]:
            if "Bearer mock-jwt" != request.headers["Authorization"]:
                raise ForbiddenError(f"Wrong {data['auth']} credentials")
        elif "basic" == data["auth"] and "Authorization" in request.headers:
            auth_content = request.headers["Authorization"]
            cred = base64.b64decode(auth_content[auth_content.find(" ") + 1 :]).decode(
                "utf-8"
            )
            if cred != "mock-basic":
                raise ForbiddenError(f"Wrong {data['auth']} credentials")
        elif "api-key" == data["auth"] and "X-Api-Key" in request.headers:
            if "mock-key" != request.headers["X-Api-Key"]:
                raise ForbiddenError(f"Wrong {data['auth']} credentials")
        else:
            raise RuntimeError(f"Unable to parse auth info from request")

        response = await backend_resource(data["request_data"])

        resp_payload = {
            "status": 200,
            "content_type": "application/json",
            "body": json.dumps(response).encode(),
        }

    except Exception as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }

    finally:

        return web.Response(**resp_payload)


@pytest.mark.parametrize("method", [MethodType.GET, MethodType.POST])
@pytest.mark.parametrize("payload", [PayloadType.JSON, PayloadType.MATCH])
@pytest.mark.parametrize(
    "auth", [AuthType.PUBLIC, AuthType.APIKEY, AuthType.BASIC, AuthType.JWT]
)
async def test_method_payload_auth(aiohttp_client, method, payload, auth):

    # ---- Create synthetic endpoint (in reality, got from server)
    endpoint = Endpoint(
        resource=["my", "resource"],
        method=method,
        payload=payload,
        auth=auth,
        response=ResponseType.JSON,
        arguments=PayloadArguments.make_from_function(backend_resource),
    )

    app = web.Application()
    app.router.add_route(method.value.upper(), endpoint.address, server_generic)
    client: TestClient = await aiohttp_client(app)

    if auth == AuthType.PUBLIC:
        auth_kwargs = {}
    elif auth == AuthType.JWT:
        auth_kwargs = {"access_token": "mock-jwt"}
    elif auth == AuthType.JWT_EXPIRABLE:
        auth_kwargs = {"access_token": "mock-jwt"}
    elif auth == AuthType.BASIC:
        auth_kwargs = {"basic_auth": "mock-basic"}
    elif auth == AuthType.APIKEY:
        auth_kwargs = {"api_key": "mock-key"}

    # ---- Test correct case
    data = DataRequestContext.make_data(
        endpoint, request_data=_CorrectData, method=method.value, auth=auth.value
    )

    async with SyncClient(
        endpoint,
        address="http://" + client.host + ":" + str(client.port),
        **auth_kwargs,
    ) as http_client:

        resp_data = await http_client.submit_request(data)

    assert "resource-key" in resp_data
    assert resp_data["resource-key"] == "resource-value"

    if auth != AuthType.PUBLIC:
        # ---- Test capture forbidden error case
        wrong_auth_kwargs = {k: "wrong" for k in auth_kwargs}
        with pytest.raises(ForbiddenError):
            async with SyncClient(
                endpoint,
                address="http://" + client.host + ":" + str(client.port),
                **wrong_auth_kwargs,
            ) as http_client:

                resp_data = await http_client.submit_request(data)

    # ---- Test capture client error case
    wrong_data = DataRequestContext.make_data(
        endpoint, request_data="incorrect", method=method.value, auth=auth.value
    )

    with pytest.raises(ClientError):

        async with SyncClient(
            endpoint,
            address="http://" + client.host + ":" + str(client.port),
            **auth_kwargs,
        ) as http_client:

            resp_data = await http_client.submit_request(wrong_data)


async def backend_file_resource(
    *, req_int: int, req_ext: str, req_file1: FileType, req_file2: FileType
):

    if req_int != 23:
        raise ClientError(f"Unexpected `req_int`")
    if req_ext != "json":
        raise ClientError(f"Unexpected `req_str`")
    if json.dumps(json.loads(req_file1)) != json.dumps({"my": "filecontent"}):
        raise ClientError(f"Unexpected `req_file1`")
    if json.dumps(json.loads(req_file2)) != json.dumps({"my": "filecontent"}):
        raise ClientError(f"Unexpected `req_file2`")

    return {"resource-key": "resource-value"}


async def server_multipart(request: web.Request):

    try:

        args_keys = ["req_int", "req_ext", "req_file1", "req_file2"]

        data = {}
        mp = await request.multipart()
        async for obj in mp:
            if obj.name in args_keys:
                data[obj.name] = (await obj.read()).decode("utf-8")
                if obj.name == "req_int":
                    # Hack to convert to int, as aiohttp returns error
                    # when trying to add an integer as a form-data field
                    data[obj.name] = int(data[obj.name])

        response = await backend_file_resource(**data)

        resp_payload = {
            "status": 200,
            "content_type": "application/json",
            "body": json.dumps(response).encode(),
        }

    except Exception as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }

    finally:

        return web.Response(**resp_payload)


async def test_payload_multipart(aiohttp_client):

    endpoint = Endpoint(
        resource=["my", "file", "resource"],
        method=MethodType.GET,
        payload=PayloadType.MULTIPART,
        auth=AuthType.PUBLIC,
        response=ResponseType.JSON,
        arguments=PayloadArguments.make_from_function(backend_file_resource),
    )

    app = web.Application()
    app.router.add_route("GET", endpoint.address, server_multipart)
    client: TestClient = await aiohttp_client(app)

    import pathlib

    path = pathlib.Path(__file__).parent.resolve()
    filename = str(path) + "/sample.json"

    # ---- Test correct case
    with DataRequestContextMultipart(
        endpoint, req_int=23, req_ext="json", req_file1=filename, req_file2=filename
    ) as data_req:

        async with SyncClient(
            endpoint,
            address="http://" + client.host + ":" + str(client.port),
        ) as http_client:

            resp_data = await http_client.submit_request(data_req.data)

    assert "resource-key" in resp_data
    assert resp_data["resource-key"] == "resource-value"


async def backend_resource_optionals_none_echo(
    *, opt_str: str = None, opt_int: int = None, opt_float: float = None
):

    return {"opt_str": opt_str, "opt_int": opt_int, "opt_float": opt_float}


async def server_optionals_none(request: web.Request):

    try:

        arg_names = ["opt_str", "opt_int", "opt_float"]
        arg_types = [str, int, float]
        arg_defaults = [None, None, None]

        if request.can_read_body:
            data = await request.json()
        else:
            data = dict()
            for idx, k in enumerate(arg_names):
                value = request.match_info[k]
                if value == str(arg_defaults[idx]):
                    data[k] = arg_defaults[idx]
                else:
                    data[k] = arg_types[idx](value)

        response = await backend_resource_optionals_none_echo(**data)

        resp_payload = {
            "status": 200,
            "content_type": "application/json",
            "body": json.dumps(response).encode(),
        }

    except Exception as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }

    finally:

        return web.Response(**resp_payload)


@pytest.mark.parametrize("payload", [PayloadType.MATCH, PayloadType.JSON])
async def test_payload_optional_none(aiohttp_client, payload: PayloadType):

    ep = Endpoint(
        resource=["my", "resource"],
        method=MethodType.POST,
        payload=payload,
        auth=AuthType.PUBLIC,
        response=ResponseType.JSON,
        arguments=PayloadArguments.make_from_function(
            backend_resource_optionals_none_echo
        ),
    )

    app = web.Application()
    app.router.add_route(ep.method.value.upper(), ep.address, server_optionals_none)
    client: TestClient = await aiohttp_client(app)

    rd_defined = DataRequestContext.make_data(
        ep, opt_str="foo", opt_int=23, opt_float=14.23
    )

    async with SyncClient(
        ep, address="http://" + client.host + ":" + str(client.port)
    ) as http_client:

        resp_defined = await http_client.submit_request(rd_defined)

    assert resp_defined["opt_str"] == "foo"
    assert resp_defined["opt_int"] == 23
    assert resp_defined["opt_float"] == 14.23

    rd_defaulted = DataRequestContext.make_data(ep)
    async with SyncClient(
        ep, address="http://" + client.host + ":" + str(client.port)
    ) as http_client:

        resp_defaulted = await http_client.submit_request(rd_defaulted)

    assert resp_defaulted["opt_str"] == None
    assert resp_defaulted["opt_int"] == None
    assert resp_defaulted["opt_float"] == None

    rd_expl_defaulted = DataRequestContext.make_data(
        ep, opt_str=None, opt_int=None, opt_float=None
    )
    async with SyncClient(
        ep, address="http://" + client.host + ":" + str(client.port)
    ) as http_client:

        resp_expl_defaulted = await http_client.submit_request(rd_expl_defaulted)

    assert resp_expl_defaulted["opt_str"] == None
    assert resp_expl_defaulted["opt_int"] == None
    assert resp_expl_defaulted["opt_float"] == None


# ---- Token refreshing
async def server_jwt_resource(request):

    try:

        assert request.method == "GET"
        auth_content = request.headers["Authorization"]
        assert "Bearer " in auth_content

        if "expired" in auth_content:

            raise ExpiredTokenError("Access token is expired")

        else:

            resp_data = {"resource-key": "resource-value"}

            return web.Response(
                status=200,
                content_type="application/json",
                body=json.dumps(resp_data).encode(),
            )

    except Exception as exc:

        resp_payload = {
            "status": exception_to_http_code(exc),
            "content_type": "application/json",
            "body": json.dumps(error_handler(exc)).encode(),
        }

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


async def parameterless_resource():
    pass


async def test_refresh(aiohttp_client):

    # ---- Create synthetic endpoint (in reality, got from server)
    endpoint = Endpoint(
        resource=["jwt_resource"],
        method=MethodType.GET,
        payload=PayloadType.NONE,
        auth=AuthType.JWT_EXPIRABLE,
        response=ResponseType.JSON,
        arguments=PayloadArguments.make_from_function(parameterless_resource),
    )

    refresh_endpoint = Endpoint(
        resource=["refresh"],
        method=MethodType.POST,
        payload=PayloadType.NONE,
        auth=AuthType.JWT,
        response=ResponseType.JSON,
        arguments=PayloadArguments.make_from_function(parameterless_resource),
    )

    app = web.Application()
    app.router.add_route("GET", endpoint.address, server_jwt_resource)
    app.router.add_route("POST", refresh_endpoint.address, server_jwt_refresh)

    # ---- Test usual behavior
    client: TestClient = await aiohttp_client(app)
    addr = "http://" + client.host + ":" + str(client.port)

    async with SyncClient(
        endpoint,
        address=addr,
        access_token="mock-jwt",
        refresh_token="refresh-jwt",
        refresh_address=addr,
        refresh_endpoint=refresh_endpoint,
    ) as http_client:

        resp_data_usual = await http_client.submit_request()

        assert "resource-key" in resp_data_usual
        assert resp_data_usual["resource-key"] == "resource-value"

    # ---- Test implicit token renewal
    async with SyncClient(
        endpoint,
        address=addr,
        access_token="expired-jwt",
        refresh_token="refresh-jwt",
        refresh_address=addr,
        refresh_endpoint=refresh_endpoint,
    ) as http_expire_client:

        resp_data_renew = await http_expire_client.submit_request()

        assert "resource-key" in resp_data_renew
        assert resp_data_renew["resource-key"] == "resource-value"

    # ---- Test expired session when both are expired
    with pytest.raises(ExpiredSessionError):

        async with SyncClient(
            endpoint,
            address=addr,
            access_token="expired-jwt",
            refresh_token="expired-jwt",
            refresh_address=addr,
            refresh_endpoint=refresh_endpoint,
        ) as http_expire_client:

            await http_expire_client.submit_request()
