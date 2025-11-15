"""This is an automatically generated stub for `crop.capnp`."""

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

from .common_capnp import Identifiable, IdentifiableClient, _IdentifiableModule
from .persistence_capnp import Persistent, PersistentClient, _PersistentModule
from .registry_capnp import Registry, RegistryClient, _RegistryModule

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer

class _CropModule(_IdentifiableModule, _PersistentModule):
    class ParametersRequest(Protocol):
        def send(self) -> _CropModule.CropClient.ParametersResult: ...

    class CultivarRequest(Protocol):
        def send(self) -> _CropModule.CropClient.CultivarResult: ...

    class SpeciesRequest(Protocol):
        def send(self) -> _CropModule.CropClient.SpeciesResult: ...

    @classmethod
    def _new_client(cls, server: _CropModule.Server | _IdentifiableModule.Server | _PersistentModule.Server) -> _CropModule.CropClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class ParametersResult(Awaitable[ParametersResult], Protocol):
            params: AnyPointer

        class CultivarResult(Awaitable[CultivarResult], Protocol):
            info: Any

        class SpeciesResult(Awaitable[SpeciesResult], Protocol):
            info: Any

        class ParametersResultTuple(NamedTuple):
            params: AnyPointer

        class CultivarResultTuple(NamedTuple):
            pass

        class SpeciesResultTuple(NamedTuple):
            pass

        class ParametersCallContext(Protocol):
            params: _CropModule.ParametersRequest
            results: _CropModule.Server.ParametersResult

        class CultivarCallContext(Protocol):
            params: _CropModule.CultivarRequest
            results: _CropModule.Server.CultivarResult

        class SpeciesCallContext(Protocol):
            params: _CropModule.SpeciesRequest
            results: _CropModule.Server.SpeciesResult

        def parameters(self, _context: _CropModule.Server.ParametersCallContext, **kwargs: Any) -> Awaitable[_CropModule.Server.ParametersResultTuple | None]: ...
        def parameters_context(self, context: _CropModule.Server.ParametersCallContext) -> Awaitable[None]: ...
        def cultivar(self, _context: _CropModule.Server.CultivarCallContext, **kwargs: Any) -> Awaitable[_CropModule.Server.CultivarResultTuple | None]: ...
        def cultivar_context(self, context: _CropModule.Server.CultivarCallContext) -> Awaitable[None]: ...
        def species(self, _context: _CropModule.Server.SpeciesCallContext, **kwargs: Any) -> Awaitable[_CropModule.Server.SpeciesResultTuple | None]: ...
        def species_context(self, context: _CropModule.Server.SpeciesCallContext) -> Awaitable[None]: ...

    class CropClient(_IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient):
        class ParametersResult(Awaitable[ParametersResult], Protocol):
            params: _DynamicObjectReader

        class CultivarResult(Awaitable[CultivarResult], Protocol):
            info: Any

        class SpeciesResult(Awaitable[SpeciesResult], Protocol):
            info: Any

        def parameters(self) -> _CropModule.CropClient.ParametersResult: ...
        def cultivar(self) -> _CropModule.CropClient.CultivarResult: ...
        def species(self) -> _CropModule.CropClient.SpeciesResult: ...
        def parameters_request(self) -> _CropModule.ParametersRequest: ...
        def cultivar_request(self) -> _CropModule.CultivarRequest: ...
        def species_request(self) -> _CropModule.SpeciesRequest: ...

Crop: _CropModule

class _ServiceModule(_RegistryModule):
    @classmethod
    def _new_client(cls, server: _ServiceModule.Server | _IdentifiableModule.Server | _RegistryModule.Server) -> _ServiceModule.ServiceClient: ...
    class Server(_RegistryModule.Server): ...
    class ServiceClient(_RegistryModule.RegistryClient): ...

Service: _ServiceModule

# Top-level type aliases for use in type annotations
type CropClient = _CropModule.CropClient
type ServiceClient = _ServiceModule.ServiceClient
