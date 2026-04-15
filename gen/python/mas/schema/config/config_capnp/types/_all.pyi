"""This is an automatically generated stub for `config.capnp`."""

from collections.abc import Awaitable
from typing import NamedTuple, Protocol, override

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

class _ServiceInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> ServiceClient: ...
    class Server(_DynamicCapabilityServer):
        def nextConfig(
            self,
            _context: NextconfigCallContext,
            **kwargs: object,
        ) -> Awaitable[NextconfigResultTuple | None]: ...
        def nextConfig_context(
            self,
            context: NextconfigCallContext,
        ) -> Awaitable[None]: ...

class NextconfigRequest(Protocol):
    def send(self) -> NextconfigResult: ...

class NextconfigResult(Awaitable[NextconfigResult], Protocol):
    config: _DynamicObjectReader
    noFurtherConfigs: bool

class NextconfigServerResult(_DynamicStructBuilder):
    @property
    def config(self) -> AnyPointer: ...
    @config.setter
    def config(self, value: AnyPointer) -> None: ...
    @property
    def noFurtherConfigs(self) -> bool: ...
    @noFurtherConfigs.setter
    def noFurtherConfigs(self, value: bool) -> None: ...

class NextconfigParams(Protocol): ...

class NextconfigCallContext(Protocol):
    params: NextconfigParams
    @property
    def results(self) -> NextconfigServerResult: ...

class NextconfigResultTuple(NamedTuple):
    config: AnyPointer
    noFurtherConfigs: bool

class ServiceClient(_DynamicCapabilityClient):
    def nextConfig(self) -> NextconfigResult: ...
    def nextConfig_request(self) -> NextconfigRequest: ...

Service: _ServiceInterfaceModule

# Top-level type aliases for use in type annotations
ServiceServer = _ServiceInterfaceModule.Server
