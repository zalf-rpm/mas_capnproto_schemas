"""This is an automatically generated stub for `crop.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable
from typing import Any, NamedTuple, Protocol

from .common_capnp import Identifiable, IdentifiableClient
from .persistence_capnp import Persistent, PersistentClient
from .registry_capnp import Registry, RegistryClient

class Crop:
    class ParametersRequest(Protocol):
        def send(self) -> Crop.ParametersResult: ...

    class ParametersResult(Awaitable[ParametersResult], Protocol):
        params: Any

    class CultivarRequest(Protocol):
        def send(self) -> Crop.CultivarResult: ...

    class CultivarResult(Awaitable[CultivarResult], Protocol):
        info: Any

    class SpeciesRequest(Protocol):
        def send(self) -> Crop.SpeciesResult: ...

    class SpeciesResult(Awaitable[SpeciesResult], Protocol):
        info: Any

    @classmethod
    def _new_client(
        cls, server: Crop.Server | Identifiable.Server | Persistent.Server
    ) -> CropClient: ...
    class Server(Identifiable.Server, Persistent.Server):
        class ParametersResultTuple(NamedTuple):
            params: Any

        class CultivarResultTuple(NamedTuple):
            pass

        class SpeciesResultTuple(NamedTuple):
            pass

        class ParametersCallContext(Protocol):
            params: Crop.ParametersRequest
            results: Crop.ParametersResult

        class CultivarCallContext(Protocol):
            params: Crop.CultivarRequest
            results: Crop.CultivarResult

        class SpeciesCallContext(Protocol):
            params: Crop.SpeciesRequest
            results: Crop.SpeciesResult

        def parameters(
            self, _context: Crop.Server.ParametersCallContext, **kwargs: Any
        ) -> Awaitable[Crop.Server.ParametersResultTuple | None]: ...
        def parameters_context(
            self, context: Crop.Server.ParametersCallContext
        ) -> Awaitable[None]: ...
        def cultivar(
            self, _context: Crop.Server.CultivarCallContext, **kwargs: Any
        ) -> Awaitable[Crop.Server.CultivarResultTuple | None]: ...
        def cultivar_context(
            self, context: Crop.Server.CultivarCallContext
        ) -> Awaitable[None]: ...
        def species(
            self, _context: Crop.Server.SpeciesCallContext, **kwargs: Any
        ) -> Awaitable[Crop.Server.SpeciesResultTuple | None]: ...
        def species_context(
            self, context: Crop.Server.SpeciesCallContext
        ) -> Awaitable[None]: ...

class CropClient(IdentifiableClient, PersistentClient):
    def parameters(self) -> Crop.ParametersResult: ...
    def cultivar(self) -> Crop.CultivarResult: ...
    def species(self) -> Crop.SpeciesResult: ...
    def parameters_request(self) -> Crop.ParametersRequest: ...
    def cultivar_request(self) -> Crop.CultivarRequest: ...
    def species_request(self) -> Crop.SpeciesRequest: ...

class Service:
    @classmethod
    def _new_client(
        cls, server: Service.Server | Identifiable.Server | Registry.Server
    ) -> ServiceClient: ...
    class Server(Registry.Server): ...

class ServiceClient(RegistryClient): ...
