"""This is an automatically generated stub for `config.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable
from typing import Any, NamedTuple, Protocol

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
)

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = (
    str
    | bytes
    | _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicListBuilder
    | _DynamicListReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class _ServiceModule(_InterfaceModule):
    class NextconfigRequest(Protocol):
        def send(self) -> _ServiceModule.ServiceClient.NextconfigResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _ServiceModule.ServiceClient: ...
    class Server(_DynamicCapabilityServer):
        class NextconfigResult(Awaitable[NextconfigResult], Protocol):
            config: AnyPointer
            noFurtherConfigs: bool

        class NextconfigResultTuple(NamedTuple):
            config: AnyPointer
            noFurtherConfigs: bool

        class NextconfigParams(Protocol): ...

        class NextconfigCallContext(Protocol):
            params: _ServiceModule.Server.NextconfigParams
            @property
            def results(self) -> _ServiceModule.Server.NextconfigResult: ...

        def nextConfig(
            self,
            _context: _ServiceModule.Server.NextconfigCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_ServiceModule.Server.NextconfigResultTuple | None]: ...
        def nextConfig_context(
            self, context: _ServiceModule.Server.NextconfigCallContext
        ) -> Awaitable[None]: ...

    class ServiceClient(_DynamicCapabilityClient):
        class NextconfigResult(Awaitable[NextconfigResult], Protocol):
            config: _DynamicObjectReader
            noFurtherConfigs: bool

        def nextConfig(self) -> _ServiceModule.ServiceClient.NextconfigResult: ...
        def nextConfig_request(self) -> _ServiceModule.NextconfigRequest: ...

Service: _ServiceModule

# Top-level type aliases for use in type annotations
type NextconfigResult = _ServiceModule.ServiceClient.NextconfigResult
type ServiceClient = _ServiceModule.ServiceClient
type ServiceServer = _ServiceModule.Server
