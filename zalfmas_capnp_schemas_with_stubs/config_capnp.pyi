"""This is an automatically generated stub for `config.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable
from typing import Any, NamedTuple, Protocol

class Service:
    class NextconfigRequest(Protocol):
        def send(self) -> Service.NextconfigResult: ...

    class NextconfigResult(Awaitable[NextconfigResult], Protocol):
        config: Any
        noFurtherConfigs: bool

    @classmethod
    def _new_client(cls, server: Service.Server) -> ServiceClient: ...
    class Server(Protocol):
        class NextconfigResultTuple(NamedTuple):
            config: Any
            noFurtherConfigs: bool

        class NextconfigCallContext(Protocol):
            params: Service.NextconfigRequest
            results: Service.NextconfigResult

        def nextConfig(
            self, _context: Service.Server.NextconfigCallContext, **kwargs: Any
        ) -> Awaitable[Service.Server.NextconfigResultTuple | None]: ...
        def nextConfig_context(
            self, context: Service.Server.NextconfigCallContext
        ) -> Awaitable[None]: ...

class ServiceClient(Protocol):
    def nextConfig(self) -> Service.NextconfigResult: ...
    def nextConfig_request(self) -> Service.NextconfigRequest: ...
