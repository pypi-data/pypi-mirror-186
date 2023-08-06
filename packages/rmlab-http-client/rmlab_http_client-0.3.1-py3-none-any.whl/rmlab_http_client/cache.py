from typing import Any, Mapping, Optional, Union

from rmlab_errors import ValueError

from rmlab_http_client import (
    Endpoint,
    AsyncEndpoint,
)

_EndpointType = Union[Endpoint, AsyncEndpoint]


class Cache:
    """Singleton cache to store credentials and endpoints,
    meant to be initialized once.

    Raises:
        RuntimeError: _description_
        RuntimeError: _description_
        ValueError: _description_
        RuntimeError: _description_
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """

    _credentials: Mapping[str, Any] = None
    _endpoints: Mapping[str, _EndpointType] = None

    @classmethod
    def get_credential(cls, cred_key: str) -> Optional[str]:
        """Returns single credential from key if exists

        Args:
            cred_key (str): Credential key.

        Returns:
            Optional[str]: Credential value or None
        """
        if cls._credentials is not None and cred_key in cls._credentials:
            return cls._credentials[cred_key]

    @classmethod
    def set_credential(cls, cred_key: str, cred_value: str):

        if cls._credentials is None:
            cls._credentials = dict()

        cls._credentials[cred_key] = cred_value

    @classmethod
    def get_endpoint(cls, endpoint_id: str) -> Union[Endpoint, AsyncEndpoint]:
        """Return specific endpoint from its ID.

        Args:
            endpoint_id (str): Endpoint ID

        Raises:
            RuntimeError: If endpoint has not been initialized.

        Returns:
            Union[Endpoint, AsyncEndpoint]: Endpoint instance.
        """

        if cls._endpoints is None or endpoint_id not in cls._endpoints:
            raise RuntimeError(f"Undefined endpoint `{endpoint_id}`")

        return cls._endpoints[endpoint_id]

    @classmethod
    def add_endpoints(cls, **kwargs):
        """Add all endpoints in argument.

        Raises:
            ValueError: If endpoint has unrecognized ID.
            ValueError: If endpoint has unknown communication type.
        """

        if cls._endpoints is None:
            cls._endpoints = dict()

        for ep_id, ep_json in kwargs.items():

            if ep_json["communication"] == "sync":
                cls._endpoints[ep_id] = Endpoint.make_from_json(ep_json)
            elif ep_json["communication"] == "async":
                cls._endpoints[ep_id] = AsyncEndpoint.make_from_json(ep_json)
            else:
                raise ValueError(f"Unknown endpoint communication type `{ep_json}`")
