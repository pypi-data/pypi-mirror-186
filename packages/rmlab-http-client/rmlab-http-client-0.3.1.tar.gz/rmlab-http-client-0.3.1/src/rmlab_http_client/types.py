import os, io
from dataclasses import dataclass
from typing import Callable, List, Optional
from inspect import signature, Parameter
from typing import Any, List, Mapping

from rmlab_errors import ValueError

from enum import Enum

import aiohttp


class EnumStrings(Enum):
    @classmethod
    def str_to_enum_value(cls, v: str):
        return cls.__dict__["_value2member_map_"][v.lower()]


class MethodType(EnumStrings):
    """All accepted HTTP request methods."""

    GET = "get"
    POST = "post"


class FileExtensionType(EnumStrings):
    """All accepted HTTP file extensions."""

    JSON = "json"
    CSV = "csv"


class PayloadType(EnumStrings):
    """All payload types."""

    NONE = "none"
    MATCH = "match"
    JSON = "json"
    MULTIPART = "multipart"


class AuthType(EnumStrings):
    """All auth types."""

    PUBLIC = "public"
    BASIC = "basic"
    APIKEY = "api-key"
    JWT = "jwt"
    JWT_EXPIRABLE = "jwt-expirable"
    WS = "ws"


class ResponseType(EnumStrings):
    """All HTTP response types."""

    NONE = "none"
    JSON = "json"


class CommunicationType(EnumStrings):
    """All Communication types."""

    SYNC = "sync"
    ASYNC = "async"
    WS = "ws"


class FileType:
    """Type to mark file arguments in endpoints."""

    pass


JSONTypes = {cls.__name__: cls for cls in [bool, str, int, float, list, dict, FileType]}

_LimitableTypesString = {cls.__name__: cls for cls in [int, float, list, dict]}
_LimitableNumericTypesString = {cls.__name__: cls for cls in [int, float]}
_LimitableContainerTypesString = {cls.__name__: cls for cls in [list, dict]}


@dataclass
class Argument:
    """An endpoint argument."""

    arg_type: type
    default_value: Any = None
    limit: int = None

    def __post_init__(self):

        if isinstance(self.arg_type, str):
            self.arg_type = JSONTypes[self.arg_type]

        if (
            self.limit is not None
            and self.arg_type.__name__ not in _LimitableTypesString
        ):
            raise ValueError(
                f"Argument cannot be limited with `{self.limit}` if `{self.arg_type}` is not limitable"
            )


class PayloadArguments:
    """All argument properties (name/type/default value) of an endpoint."""

    REQUIRED_STR = "REQUIRED"
    ASYNC_ID_KEY = "operation_id"

    def __init__(self, **kwargs):

        assert all([isinstance(v, Argument) for v in kwargs.values()])

        self.args: Mapping[str, Argument] = {k: v for k, v in kwargs.items()}

    @classmethod
    def make_from_function(
        cls, fn: Optional[Callable] = None, limits: Optional[Mapping[str, int]] = None
    ):

        args: Mapping[str, Argument] = dict()

        if fn is not None:
            sig = signature(fn)

            if limits is not None:
                assert all([lk in sig.parameters for lk in limits.keys()])

            for k, val in sig.parameters.items():
                default = (
                    PayloadArguments.REQUIRED_STR
                    if val.default == Parameter.empty
                    else val.default
                )
                limit = limits[k] if limits and k in limits else None
                args[k] = Argument(
                    arg_type=val.annotation, default_value=default, limit=limit
                )

        return cls(**args)

    @classmethod
    def make_from_json(cls, args: Mapping[str, Mapping[str, Any]]):

        return cls(
            **{
                k: Argument(arg["type"], arg["default"], arg["limit"])
                for k, arg in args.items()
            }
        )

    @property
    def json(self) -> Mapping[str, Mapping[str, Any]]:
        return {
            k: {
                "type": arg.arg_type.__name__,
                "default": arg.default_value,
                "limit": arg.limit,
            }
            for k, arg in self.args.items()
        }

    @property
    def keys(self) -> List[str]:
        return list(self.args.keys())

    @property
    def types_str(self) -> List[str]:
        return [arg.arg_type.__name__ for arg in self.args.values()]

    @property
    def defaults(self) -> List[Any]:
        return [arg.default_value for arg in self.args.values()]

    @property
    def limits(self) -> List[int]:
        return [arg.limit for arg in self.args.values()]

    def limit_of(self, arg_name: str) -> int:
        if arg_name in self.args:
            return self.args[arg_name].limit
        else:
            return None


# Maximum time to await for the completion of a sync operation
# Operations taking longer should be asynchronous
SyncResponseDefaultTimeout = 10

# Maximum time to await for the completion of a long-running async op
AsyncOperationDefaultTimeout = 3600

# Short sleep before poll, to return much sooner in case this op:
# * lasts much less than self._poll_seconds seconds
# * lasts more than the time to make the first poll call without sleep
# * less than _prepoll_wait_seconds
AsyncOperationDefaultPrePollWait = 1

# Poll status of poll operation each seconds
AsyncOperationDefaultPollInterval = 10

# Timeout to await first response of async op
# Should be small, as creation of async op id is fast
AsyncResponseDefaultTimeout = 5


class Endpoint:
    """Properties of an endpoint."""

    def __init__(
        self,
        *,
        resource: List[str],
        method: MethodType,
        payload: PayloadType,
        auth: AuthType,
        response: ResponseType,
        arguments: PayloadArguments,
        communication: CommunicationType = CommunicationType.SYNC,
        timeout: int = SyncResponseDefaultTimeout,
        id: str = "default-id",
    ):
        """Initializes an endpoint.

        Args:
            resource (List[str]): Resource endpoint, translate into '/'-separated resources.
            method (MethodType): Method type
            payload (PayloadType): Payload type
            auth (AuthType): Auth type
            response (ResponseType): Response type
            arguments (PayloadArguments): Payload arguments
            communication (CommunicationType, optional): Communication type. Defaults to CommunicationType.SYNC.
            timeout (int, optional): Timeout in seconds. Defaults to SyncResponseDefaultTimeout.
            id (str): Endpoint identifier
        """

        assert isinstance(arguments, PayloadArguments)

        self.id = id

        self.resource: List[str] = resource
        self.method: MethodType = (
            method
            if not isinstance(method, str)
            else MethodType.str_to_enum_value(method)
        )
        self.payload: PayloadType = (
            payload
            if not isinstance(payload, str)
            else PayloadType.str_to_enum_value(payload)
        )
        self.auth: AuthType = (
            auth if not isinstance(auth, str) else AuthType.str_to_enum_value(auth)
        )
        self.communication: CommunicationType = (
            communication
            if not isinstance(communication, str)
            else CommunicationType.str_to_enum_value(communication)
        )
        self.response: ResponseType = (
            response
            if not isinstance(response, str)
            else ResponseType.str_to_enum_value(response)
        )
        self.arguments: PayloadArguments = arguments
        self.timeout: int = timeout

        if self.payload == PayloadType.NONE:
            assert len(arguments.keys) == 0
        else:
            assert len(arguments.keys) > 0

    @classmethod
    def make_from_json(cls, ep_json: dict):
        """Creates an endpoint from a JSON-compatible dictionary.

        Args:
            ep_json (dict): JSON-compatible dictionary

        Returns:
            Endpoint: Instance
        """
        args_json = ep_json.pop("arguments")
        args = PayloadArguments.make_from_json(args_json)
        return cls(arguments=args, **ep_json)

    @property
    def address(self) -> str:
        """Returns endpoint address."""

        endpoint_addr = self.resource + (
            ["{" + k + "}" for k in self.arguments.keys]
            if self.payload == PayloadType.MATCH
            else []
        )

        return "/" + "/".join(endpoint_addr)

    @property
    def json(self) -> Mapping[str, Any]:
        """Returns a JSON-compatible dictionary of the endpoint."""

        return {
            "id": self.id,
            "resource": self.resource,
            "method": self.method.value,
            "payload": self.payload.value,
            "auth": self.auth.value,
            "communication": self.communication.value,
            "response": self.response.value,
            "arguments": self.arguments.json,
            "timeout": self.timeout,
        }


class AsyncEndpoint(Endpoint):
    """Properties of an asynchronous endpoint."""

    ASYNC_INFO_KEY = "async_info"

    def __init__(
        self,
        *,
        prepoll_wait: int = AsyncOperationDefaultPrePollWait,
        poll_interval: int = AsyncOperationDefaultPollInterval,
        poll_endpoint_id: str,
        result_endpoint_id: str,
        **base_kwargs,
    ):
        """Initializes an asynchronous endpoint instance.

        Args:
            poll_endpoint_id (str): ID of endpoint where status is polled from
            result_endpoint_id (str): ID of endpoint where result is fetched from
            prepoll_wait (int, optional): Await seconds before entering the polling loop. Defaults to AsyncOperationDefaultPrePollWait.
            poll_interval (int, optional): Poll interval in seconds. Defaults to AsyncOperationDefaultPollInterval.
        """

        self.async_prepoll_wait: int = prepoll_wait
        self.async_poll_interval: int = poll_interval
        self.async_poll_endpoint_id: str = poll_endpoint_id
        self.async_result_endpoint_id: str = result_endpoint_id

        super(AsyncEndpoint, self).__init__(
            communication=CommunicationType.ASYNC, **base_kwargs
        )

    @classmethod
    def make_from_json(cls, aep_json: dict):
        """Creates an asynchronous endpoint from a JSON-compatible dictionary.

        Args:
            ep_json (dict): JSON-compatible dictionary

        Returns:
            Endpoint: Instance
        """

        async_info = aep_json.pop(AsyncEndpoint.ASYNC_INFO_KEY)

        if "communication" in aep_json:
            assert aep_json["communication"] == "async"
            aep_json.pop("communication")

        args = aep_json.pop("arguments")
        pargs = PayloadArguments.make_from_json(args)

        return cls(arguments=pargs, **async_info, **aep_json)

    @property
    def json(self) -> Mapping[str, Any]:
        """Returns a JSON-compatible dictionary of the asynchronous endpoint."""

        return {
            **super(AsyncEndpoint, self).json,
            AsyncEndpoint.ASYNC_INFO_KEY: {
                "prepoll_wait": self.async_prepoll_wait,
                "poll_interval": self.async_poll_interval,
                "poll_endpoint_id": self.async_poll_endpoint_id,
                "result_endpoint_id": self.async_result_endpoint_id,
            },
        }


class DataRequestContextMultipart:
    """Context manager to parse a set of endpoint arguments,
    with at least one being a file, to be sent in the HTTP request
    as multipart data."""

    def __init__(self, endpoint: Endpoint, **kwargs):
        """Initializes context manager

        Args:
            endpoint (Endpoint): Endpoint instance.
            kwargs (Mapping[str,Any]): Endpoint arguments.
        """

        assert endpoint.payload == PayloadType.MULTIPART

        self._arguments: PayloadArguments = endpoint.arguments
        self._kwargs = kwargs
        self._opened_files: List[io.BufferedReader] = list()
        self.data: aiohttp.FormData = None

    def __enter__(self):
        """Parses endpoint arguments according to properties of endpoint

        Raises:
            ValueError: If mandatory argument has not been provided.
            FileNotFoundError: If a file in arguments does not exist.

        Returns:
            DataRequestContextMultipart: Instance.
        """

        self.data = aiohttp.FormData()

        for key, default, type_str in zip(
            self._arguments.keys, self._arguments.defaults, self._arguments.types_str
        ):

            if type_str == "FileType":

                assert default == PayloadArguments.REQUIRED_STR

                if key not in self._kwargs:
                    raise ValueError(f"File argument `{key}` is required")

                filename = self._kwargs[key]

                if not os.path.exists(filename):
                    raise FileNotFoundError(f"File `{filename}` does not exist")

                file = open(filename, "rb")

                self._opened_files.append(file)

                self.data.add_field(name=key, value=file, filename=filename)

            else:

                type_class = JSONTypes[type_str]
                if type_class == int:
                    type_class = str

                if default != PayloadArguments.REQUIRED_STR and key not in self._kwargs:
                    v = default
                    self.data.add_field(name=key, value=v)
                elif key in self._kwargs:
                    v = type_class(self._kwargs[key])
                    self.data.add_field(name=key, value=v)
                else:
                    raise ValueError(f"Argument `{key}` is required")

        return self

    def __exit__(self, exc_ty, exc_val, tb):
        """Closes file instances opened during enter."""

        for f in self._opened_files:
            f.close()

        pass


class DataRequestContext:
    """Context manager to parse a set of endpoint arguments,
    to be sent in the HTTP request as address- or json-arguments."""

    def __init__(self, endpoint: Endpoint, **kwargs):
        """Initializes context manager

        Args:
            endpoint (Endpoint): Endpoint instance.
            kwargs (Mapping[str,Any]): Endpoint arguments.
        """

        assert endpoint.payload != PayloadType.MULTIPART

        self._arguments: PayloadArguments = endpoint.arguments
        self._kwargs = kwargs
        self._opened_files: List[io.BufferedReader] = list()
        self.data: Mapping[str, Any] = dict()

    def __enter__(self):
        """Parses endpoint arguments according to properties of endpoint

        Raises:
            ValueError: If mandatory argument has not been provided.

        Returns:
            DataRequestContext: Instance.
        """

        for key, default, type_str, limit in zip(
            self._arguments.keys,
            self._arguments.defaults,
            self._arguments.types_str,
            self._arguments.limits,
        ):

            type_class = JSONTypes[type_str]
            if default != PayloadArguments.REQUIRED_STR:
                if key not in self._kwargs:
                    self.data[key] = default
                elif self._kwargs[key] == default:
                    self.data[key] = self._kwargs[key]
                else:
                    self.data[key] = type_class(self._kwargs[key])
            elif key in self._kwargs:
                self.data[key] = type_class(self._kwargs[key])
            else:
                raise ValueError(f"Argument `{key}` is required")

            # Check arguments is within limits, if any
            if limit is not None and self.data[key] is not None:
                if type_str in _LimitableNumericTypesString and self.data[key] > limit:
                    raise ValueError(f"Argument `{key}` exceeds limit `{limit}`")
                elif (
                    type_str in _LimitableContainerTypesString
                    and len(self.data[key]) > limit
                ):
                    raise ValueError(
                        f"Argument `{key}` number of elements `{len(self.data[key])}` exceeds limit `{limit}`"
                    )

        return self

    def __exit__(self, exc_ty, exc_val, tb):

        pass

    @classmethod
    def make_data(cls, endpoint: Endpoint, **kwargs) -> Mapping[str, Any]:
        """Returns parsed data as a JSON-compatible dictionary.

        Args:
            endpoint (Endpoint): Endpoint instance.
            kwargs (Mapping[str,Any]): Endpoint arguments.

        Returns:
            _type_: _description_
        """

        with cls(endpoint, **kwargs) as drc:
            return drc.data
