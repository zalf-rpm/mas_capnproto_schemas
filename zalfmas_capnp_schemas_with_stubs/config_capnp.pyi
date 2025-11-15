"""This is an automatically generated stub for `config.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator
from typing import Any, NamedTuple, Protocol

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _Request,
    _StructModule,
)

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

class _ServiceModule(_InterfaceModule):
    class NextconfigRequest(Protocol):
        def send(self) -> _ServiceModule.ServiceClient.NextconfigResult: ...

    @classmethod
    def _new_client(cls, server: _ServiceModule.Server) -> _ServiceModule.ServiceClient: ...
    class Server(_DynamicCapabilityServer):
        class NextconfigResult(Awaitable[NextconfigResult], Protocol):
            config: AnyPointer
            noFurtherConfigs: bool

        class NextconfigResultTuple(NamedTuple):
            config: AnyPointer
            noFurtherConfigs: bool

        class NextconfigCallContext(Protocol):
            params: _ServiceModule.NextconfigRequest
            results: _ServiceModule.Server.NextconfigResult

        def nextConfig(self, _context: _ServiceModule.Server.NextconfigCallContext, **kwargs: Any) -> Awaitable[_ServiceModule.Server.NextconfigResultTuple | None]: ...
        def nextConfig_context(self, context: _ServiceModule.Server.NextconfigCallContext) -> Awaitable[None]: ...

    class ServiceClient(_DynamicCapabilityClient):
        class NextconfigResult(Awaitable[NextconfigResult], Protocol):
            config: _DynamicObjectReader
            noFurtherConfigs: bool

        def nextConfig(self) -> _ServiceModule.ServiceClient.NextconfigResult: ...
        def nextConfig_request(self) -> _ServiceModule.NextconfigRequest: ...

Service: _ServiceModule

# Top-level type aliases for use in type annotations
type ServiceClient = _ServiceModule.ServiceClient
