# RMLab HTTP Client

Small python module wrapping a HTTP client based on `asyncio`, providing several utilities required on RMLab server:

* Basic/key/jwt authentication.

* Token refresh.

* State polling and result fetching of long-running asynchronous operations.

* Server-defined type/value-safe endpoints to minimize API breaking changes.

* Capture ill-formed requests before submission.

* Custom error handling unified for client and server.

## Installation

```
pip install rmlab-http-client
```

## Requirements

* python 3.9+
* aiohttp 3.8.1

## License

This package is offered under a [MIT License](LICENSE).
