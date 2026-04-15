"""Module helper types for `config.capnp`."""

from collections.abc import Awaitable
from typing import override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _InterfaceModule,
)

from . import _all as _all

class _ServiceInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.ServiceClient: ...
    class Server(_DynamicCapabilityServer):
        def nextConfig(
            self,
            _context: _all.NextconfigCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.NextconfigResultTuple | None]: ...
        def nextConfig_context(
            self,
            context: _all.NextconfigCallContext,
        ) -> Awaitable[None]: ...
