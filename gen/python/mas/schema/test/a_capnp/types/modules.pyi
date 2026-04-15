"""Module helper types for `a.capnp`."""

from collections.abc import Awaitable
from typing import override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _InterfaceModule,
)

from . import _all as _all

class _AInterfaceModule(_InterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.AClient: ...
    class Server(_DynamicCapabilityServer):
        def method(
            self,
            param: str,
            _context: _all.MethodCallContext,
            **kwargs: object,
        ) -> Awaitable[str | _all.MethodResultTuple | None]: ...
        def method_context(
            self,
            context: _all.MethodCallContext,
        ) -> Awaitable[None]: ...
