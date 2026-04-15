"""Module helper types for `modam.capnp`."""

from collections.abc import Awaitable
from typing import override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _InterfaceModule,
)

from . import _all as _all

class _ModamWrapperServiceInterfaceModule(_InterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.ModamWrapperServiceClient: ...
    class Server(_DynamicCapabilityServer):
        def runAemModel(
            self,
            input: str,
            _context: _all.RunaemmodelCallContext,
            **kwargs: object,
        ) -> Awaitable[str | _all.RunaemmodelResultTuple | None]: ...
        def runAemModel_context(
            self,
            context: _all.RunaemmodelCallContext,
        ) -> Awaitable[None]: ...
        def runFieldModel(
            self,
            input: str,
            _context: _all.RunfieldmodelCallContext,
            **kwargs: object,
        ) -> Awaitable[str | _all.RunfieldmodelResultTuple | None]: ...
        def runFieldModel_context(
            self,
            context: _all.RunfieldmodelCallContext,
        ) -> Awaitable[None]: ...
