"""This is an automatically generated stub for `crop.capnp`."""

from collections.abc import Awaitable
from typing import Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
)

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)
from mas.schema.registry.registry_capnp.types.clients import RegistryClient
from mas.schema.registry.registry_capnp.types.modules import _RegistryInterfaceModule

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

class _CropInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> CropClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def parameters(
            self,
            _context: ParametersCallContext,
            **kwargs: object,
        ) -> Awaitable[AnyPointer | ParametersResultTuple | None]: ...
        def parameters_context(
            self,
            context: ParametersCallContext,
        ) -> Awaitable[None]: ...
        def cultivar(
            self,
            _context: CultivarCallContext,
            **kwargs: object,
        ) -> Awaitable[
            IdInformationBuilder
            | IdInformationReader
            | dict[str, Any]
            | CultivarResultTuple
            | None
        ]: ...
        def cultivar_context(self, context: CultivarCallContext) -> Awaitable[None]: ...
        def species(
            self,
            _context: SpeciesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            IdInformationBuilder
            | IdInformationReader
            | dict[str, Any]
            | SpeciesResultTuple
            | None
        ]: ...
        def species_context(self, context: SpeciesCallContext) -> Awaitable[None]: ...

class ParametersRequest(Protocol):
    def send(self) -> ParametersResult: ...

class ParametersResult(Awaitable[ParametersResult], Protocol):
    params: _DynamicObjectReader

class ParametersServerResult(_DynamicStructBuilder):
    @property
    def params(self) -> AnyPointer: ...
    @params.setter
    def params(self, value: AnyPointer) -> None: ...

class ParametersParams(Protocol): ...

class ParametersCallContext(Protocol):
    params: ParametersParams
    @property
    def results(self) -> ParametersServerResult: ...

class ParametersResultTuple(NamedTuple):
    params: AnyPointer

class CultivarRequest(Protocol):
    def send(self) -> CultivarResult: ...

class CultivarResult(Awaitable[CultivarResult], Protocol):
    info: IdInformationReader

class CultivarServerResult(_DynamicStructBuilder):
    @property
    def info(self) -> IdInformationBuilder: ...
    @info.setter
    def info(
        self,
        value: IdInformationBuilder | IdInformationReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["info"],
        size: int | None = None,
    ) -> IdInformationBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class CultivarParams(Protocol): ...

class CultivarCallContext(Protocol):
    params: CultivarParams
    @property
    def results(self) -> CultivarServerResult: ...

class CultivarResultTuple(NamedTuple):
    info: IdInformationBuilder | IdInformationReader | dict[str, Any]

class SpeciesRequest(Protocol):
    def send(self) -> SpeciesResult: ...

class SpeciesResult(Awaitable[SpeciesResult], Protocol):
    info: IdInformationReader

class SpeciesServerResult(_DynamicStructBuilder):
    @property
    def info(self) -> IdInformationBuilder: ...
    @info.setter
    def info(
        self,
        value: IdInformationBuilder | IdInformationReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["info"],
        size: int | None = None,
    ) -> IdInformationBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class SpeciesParams(Protocol): ...

class SpeciesCallContext(Protocol):
    params: SpeciesParams
    @property
    def results(self) -> SpeciesServerResult: ...

class SpeciesResultTuple(NamedTuple):
    info: IdInformationBuilder | IdInformationReader | dict[str, Any]

class CropClient(IdentifiableClient, PersistentClient):
    def parameters(self) -> ParametersResult: ...
    def cultivar(self) -> CultivarResult: ...
    def species(self) -> SpeciesResult: ...
    def parameters_request(self) -> ParametersRequest: ...
    def cultivar_request(self) -> CultivarRequest: ...
    def species_request(self) -> SpeciesRequest: ...

Crop: _CropInterfaceModule

class _ServiceInterfaceModule(_RegistryInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> ServiceClient: ...
    class Server(_RegistryInterfaceModule.Server): ...

class ServiceClient(RegistryClient): ...

Service: _ServiceInterfaceModule

# Top-level type aliases for use in type annotations
CropServer = _CropInterfaceModule.Server
ServiceServer = _ServiceInterfaceModule.Server
