"""This is an automatically generated stub for `config.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable
from typing import Any, Protocol

class Service(Protocol):
    class NextconfigResult(Awaitable[NextconfigResult], Protocol):
        config: Any
        noFurtherConfigs: bool

    def nextConfig(self) -> NextconfigResult: ...
    class NextconfigRequest(Protocol):
        def send(self) -> Service.NextconfigResult: ...

    def nextConfig_request(self) -> NextconfigRequest: ...
    class Server:
        def nextConfig(self, **kwargs) -> Awaitable[Service.NextconfigResult]: ...
