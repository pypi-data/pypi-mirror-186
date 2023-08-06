from enum import Enum
import json
import pytest
from rmlab_http_client.types import (
    Argument,
    AsyncEndpoint,
    AuthType,
    CommunicationType,
    Endpoint,
    MethodType,
    PayloadArguments,
    PayloadType,
    ResponseType,
)


def test_payload_arguments():

    pargs = PayloadArguments(
        foo=Argument(str, "default"),
        bar=Argument(int, PayloadArguments.REQUIRED_STR),
        zee=Argument(float, 13.7),
    )

    expect_keys = ["foo", "bar", "zee"]
    expect_types_str = ["str", "int", "float"]
    expect_defaults = ["default", PayloadArguments.REQUIRED_STR, 13.7]

    assert pargs.keys == expect_keys
    assert pargs.types_str == expect_types_str
    assert pargs.defaults == expect_defaults

    json_pargs = pargs.json

    assert list(json_pargs["types"].keys()) == expect_keys
    assert list(json_pargs["types"].values()) == expect_types_str
    assert list(json_pargs["defaults"].keys()) == expect_keys
    assert list(json_pargs["defaults"].values()) == expect_defaults


def args_fn(*, foo: str, bar: int = 42, zee: str = None):
    pass


def no_args_fn():
    pass


def test_payload_arguments():

    pargs = PayloadArguments.make_from_function(args_fn)

    json_pargs = pargs.json

    assert json_pargs["foo"]["type"] == "str"
    assert json_pargs["bar"]["type"] == "int"
    assert json_pargs["zee"]["type"] == "str"

    assert json_pargs["foo"]["default"] == PayloadArguments.REQUIRED_STR
    assert json_pargs["bar"]["default"] == 42
    assert json_pargs["zee"]["default"] == None

    assert pargs.keys == ["foo", "bar", "zee"]
    assert pargs.types_str == ["str", "int", "str"]
    assert pargs.defaults == [PayloadArguments.REQUIRED_STR, 42, None]


Payloads = [
    PayloadType.NONE,
    PayloadType.MATCH,
    PayloadType.JSON,
    PayloadType.MULTIPART,
]
Methods = [MethodType.GET, MethodType.POST]
Auths = [
    AuthType.PUBLIC,
    AuthType.BASIC,
    AuthType.APIKEY,
    AuthType.JWT,
    AuthType.JWT_EXPIRABLE,
]
Responses = [ResponseType.NONE, ResponseType.JSON]
Comms = [CommunicationType.SYNC, CommunicationType.ASYNC]
InputFormats = ["enum", "str"]


@pytest.mark.parametrize("payload", Payloads)
@pytest.mark.parametrize("method", Methods)
@pytest.mark.parametrize("auth", Auths)
@pytest.mark.parametrize("resp", Responses)
@pytest.mark.parametrize("in_format", InputFormats)
@pytest.mark.parametrize("comm", Comms)
def test_endpoint(
    payload: Enum, method: Enum, auth: Enum, resp: Enum, in_format: str, comm: Enum
):

    if payload == PayloadType.NONE:
        fn = no_args_fn
    else:
        fn = args_fn

    if in_format == "str":
        payload = payload.value
        method = method.value
        auth = auth.value
        resp = resp.value

    if comm == CommunicationType.SYNC:
        ep = Endpoint(
            resource=["my", "end", "point"],
            method=method,
            payload=payload,
            auth=auth,
            response=resp,
            arguments=PayloadArguments.make_from_function(fn),
        )

        assert ep.communication == CommunicationType.SYNC

    else:

        ep = AsyncEndpoint(
            resource=["my", "end", "point"],
            method=method,
            payload=payload,
            auth=auth,
            response=resp,
            arguments=PayloadArguments.make_from_function(fn),
            poll_endpoint_id="my_poll_endpoint_id",
            result_endpoint_id="my_result_endpoint_id",
        )
        assert ep.communication == CommunicationType.ASYNC

    expect_json_keys = [
        "resource",
        "method",
        "payload",
        "auth",
        "communication",
        "response",
        "arguments",
        "timeout",
    ]

    if ep == CommunicationType.ASYNC:
        expect_async_json_keys = [
            "prepoll_wait",
            "poll_interval",
            "poll_endpoint_id",
            "result_endpoint_id",
        ]
        assert all(
            [k in ep.json[AsyncEndpoint.ASYNC_INFO_KEY] for k in expect_async_json_keys]
        )

    assert all([k in ep.json for k in expect_json_keys])

    if ep.payload == PayloadType.MATCH:
        assert all(["{" + k + "}" in ep.address for k in ep.arguments.keys])
    else:
        assert not any(["{" + k + "}" in ep.address for k in ep.arguments.keys])
        assert ep.address == "/" + "/".join(ep.resource)

    if comm == CommunicationType.SYNC:
        copied_ep = Endpoint.make_from_json(ep.json)
    else:
        copied_ep = AsyncEndpoint.make_from_json(ep.json)

    assert json.dumps(copied_ep.json) == json.dumps(ep.json)
