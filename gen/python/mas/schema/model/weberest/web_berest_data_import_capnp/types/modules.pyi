"""Module helper types for `web_berest_data_import.capnp`."""

from collections.abc import Awaitable
from typing import override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _InterfaceModule,
)

from . import _all as _all

class _DWLABImportInterfaceModule(_InterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.DWLABImportClient: ...
    class Server(_DynamicCapabilityServer):
        def importData(
            self,
            id: str,
            dwla: bytes,
            dwlb: bytes,
            _context: _all.ImportdataCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.ImportdataResultTuple | None]: ...
        def importData_context(
            self,
            context: _all.ImportdataCallContext,
        ) -> Awaitable[None]: ...
