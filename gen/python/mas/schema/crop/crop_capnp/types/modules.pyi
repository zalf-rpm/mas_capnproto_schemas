"""Module helper types for `crop.capnp`."""

from collections.abc import Awaitable
from typing import Any, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
)

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)
from mas.schema.registry.registry_capnp.types.modules import _RegistryInterfaceModule

from . import _all as _all

class _CropInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.CropClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def parameters(
            self,
            _context: _all.ParametersCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.AnyPointer | _all.ParametersResultTuple | None]: ...
        def parameters_context(
            self,
            context: _all.ParametersCallContext,
        ) -> Awaitable[None]: ...
        def cultivar(
            self,
            _context: _all.CultivarCallContext,
            **kwargs: object,
        ) -> Awaitable[
            IdInformationBuilder
            | IdInformationReader
            | dict[str, Any]
            | _all.CultivarResultTuple
            | None
        ]: ...
        def cultivar_context(
            self,
            context: _all.CultivarCallContext,
        ) -> Awaitable[None]: ...
        def species(
            self,
            _context: _all.SpeciesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            IdInformationBuilder
            | IdInformationReader
            | dict[str, Any]
            | _all.SpeciesResultTuple
            | None
        ]: ...
        def species_context(
            self,
            context: _all.SpeciesCallContext,
        ) -> Awaitable[None]: ...

class _ServiceInterfaceModule(_RegistryInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.ServiceClient: ...
    class Server(_RegistryInterfaceModule.Server): ...
