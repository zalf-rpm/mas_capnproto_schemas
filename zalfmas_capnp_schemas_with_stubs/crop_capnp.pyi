"""This is an automatically generated stub for `crop.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable
from typing import Any, NamedTuple, Protocol

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
)

from .common_capnp import (
    IdInformationBuilder,
    IdInformationReader,
    _IdentifiableModule,
)
from .persistence_capnp import _PersistentModule
from .registry_capnp import _RegistryModule

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
)

class _CropModule(_IdentifiableModule, _PersistentModule):
    class ParametersRequest(Protocol):
        def send(self) -> _CropModule.CropClient.ParametersResult: ...

    class CultivarRequest(Protocol):
        def send(self) -> _CropModule.CropClient.CultivarResult: ...

    class SpeciesRequest(Protocol):
        def send(self) -> _CropModule.CropClient.SpeciesResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _CropModule.CropClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class ParametersResult(Awaitable[ParametersResult], Protocol):
            params: AnyPointer

        class CultivarResult(Awaitable[CultivarResult], Protocol):
            info: IdInformationBuilder | IdInformationReader

        class SpeciesResult(Awaitable[SpeciesResult], Protocol):
            info: IdInformationBuilder | IdInformationReader

        class ParametersResultTuple(NamedTuple):
            params: AnyPointer

        class CultivarResultTuple(NamedTuple):
            info: IdInformationBuilder | IdInformationReader

        class SpeciesResultTuple(NamedTuple):
            info: IdInformationBuilder | IdInformationReader

        class ParametersParams(Protocol): ...

        class ParametersCallContext(Protocol):
            params: _CropModule.Server.ParametersParams
            results: _CropModule.Server.ParametersResult

        class CultivarParams(Protocol): ...

        class CultivarCallContext(Protocol):
            params: _CropModule.Server.CultivarParams
            results: _CropModule.Server.CultivarResult

        class SpeciesParams(Protocol): ...

        class SpeciesCallContext(Protocol):
            params: _CropModule.Server.SpeciesParams
            results: _CropModule.Server.SpeciesResult

        def parameters(
            self,
            _context: _CropModule.Server.ParametersCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_CropModule.Server.ParametersResultTuple | None]: ...
        def parameters_context(
            self, context: _CropModule.Server.ParametersCallContext
        ) -> Awaitable[None]: ...
        def cultivar(
            self,
            _context: _CropModule.Server.CultivarCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_CropModule.Server.CultivarResultTuple | None]: ...
        def cultivar_context(
            self, context: _CropModule.Server.CultivarCallContext
        ) -> Awaitable[None]: ...
        def species(
            self,
            _context: _CropModule.Server.SpeciesCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_CropModule.Server.SpeciesResultTuple | None]: ...
        def species_context(
            self, context: _CropModule.Server.SpeciesCallContext
        ) -> Awaitable[None]: ...

    class CropClient(
        _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
    ):
        class ParametersResult(Awaitable[ParametersResult], Protocol):
            params: _DynamicObjectReader

        class CultivarResult(Awaitable[CultivarResult], Protocol):
            info: IdInformationReader

        class SpeciesResult(Awaitable[SpeciesResult], Protocol):
            info: IdInformationReader

        def parameters(self) -> _CropModule.CropClient.ParametersResult: ...
        def cultivar(self) -> _CropModule.CropClient.CultivarResult: ...
        def species(self) -> _CropModule.CropClient.SpeciesResult: ...
        def parameters_request(self) -> _CropModule.ParametersRequest: ...
        def cultivar_request(self) -> _CropModule.CultivarRequest: ...
        def species_request(self) -> _CropModule.SpeciesRequest: ...

Crop: _CropModule

class _ServiceModule(_RegistryModule):
    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _ServiceModule.ServiceClient: ...
    class Server(_RegistryModule.Server): ...
    class ServiceClient(_RegistryModule.RegistryClient): ...

Service: _ServiceModule

# Top-level type aliases for use in type annotations
type CropClient = _CropModule.CropClient
type CultivarResult = _CropModule.CropClient.CultivarResult
type ParametersResult = _CropModule.CropClient.ParametersResult
type ServiceClient = _ServiceModule.ServiceClient
type SpeciesResult = _CropModule.CropClient.SpeciesResult
