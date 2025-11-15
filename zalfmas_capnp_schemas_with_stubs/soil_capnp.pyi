"""This is an automatically generated stub for `soil.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, MutableSequence, Sequence
from enum import Enum
from typing import Any, Literal, NamedTuple, Protocol, TypeAlias, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _Request,
    _StructModule,
)

from .common_capnp import Identifiable, IdentifiableClient, _IdentifiableModule
from .persistence_capnp import Persistent, PersistentClient, _PersistentModule

class _STypeModule(Enum):
    unknown = 0
    ka5 = 1

SType: TypeAlias = _STypeModule

class _PropertyNameModule(Enum):
    soilType = 0
    sand = 1
    clay = 2
    silt = 3
    pH = 4
    sceleton = 5
    organicCarbon = 6
    organicMatter = 7
    bulkDensity = 8
    rawDensity = 9
    fieldCapacity = 10
    permanentWiltingPoint = 11
    saturation = 12
    soilMoisture = 13
    soilWaterConductivityCoefficient = 14
    ammonium = 15
    nitrate = 16
    cnRatio = 17
    inGroundwater = 18
    impenetrable = 19

PropertyName: TypeAlias = _PropertyNameModule

class _LayerModule(_StructModule):
    class _PropertyModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def name(self) -> _PropertyNameModule: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @property
            def f32Value(self) -> float: ...
            @property
            def bValue(self) -> bool: ...
            @property
            def type(self) -> str: ...
            @property
            def unset(self) -> None: ...
            @override
            def which(self) -> Literal["f32Value", "bValue", "type", "unset"]: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _LayerModule._PropertyModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def name(self) -> _PropertyNameModule: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @name.setter
            def name(
                self,
                value: _PropertyNameModule
                | Literal["soilType", "sand", "clay", "silt", "pH", "sceleton", "organicCarbon", "organicMatter", "bulkDensity", "rawDensity", "fieldCapacity", "permanentWiltingPoint", "saturation", "soilMoisture", "soilWaterConductivityCoefficient", "ammonium", "nitrate", "cnRatio", "inGroundwater", "impenetrable"],
            ) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @property
            def f32Value(self) -> float: ...
            @f32Value.setter
            def f32Value(self, value: float) -> None: ...
            @property
            def bValue(self) -> bool: ...
            @bValue.setter
            def bValue(self, value: bool) -> None: ...
            @property
            def type(self) -> str: ...
            @type.setter
            def type(self, value: str) -> None: ...
            @property
            def unset(self) -> None: ...
            @unset.setter
            def unset(self, value: None) -> None: ...
            @override
            def which(self) -> Literal["f32Value", "bValue", "type", "unset"]: ...
            @override
            def as_reader(self) -> _LayerModule._PropertyModule.Reader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            name: _PropertyNameModule
            | Literal["soilType", "sand", "clay", "silt", "pH", "sceleton", "organicCarbon", "organicMatter", "bulkDensity", "rawDensity", "fieldCapacity", "permanentWiltingPoint", "saturation", "soilMoisture", "soilWaterConductivityCoefficient", "ammonium", "nitrate", "cnRatio", "inGroundwater", "impenetrable"]
            | None = None,
            f32Value: float | None = None,
            bValue: bool | None = None,
            type: str | None = None,
            unset: None | None = None,
        ) -> _LayerModule._PropertyModule.Builder: ...

    PropertyReader: TypeAlias = _PropertyModule.Reader
    PropertyBuilder: TypeAlias = _PropertyModule.Builder
    Property: _PropertyModule
    class Reader(_DynamicStructReader):
        @property
        def properties(self) -> Sequence[_LayerModule._PropertyModule.Reader]: ...
        @property
        def size(self) -> float: ...
        @property
        def description(self) -> str: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _LayerModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def properties(self) -> MutableSequence[_LayerModule._PropertyModule.Builder]: ...
        @properties.setter
        def properties(self, value: Sequence[_LayerModule._PropertyModule.Builder | _LayerModule._PropertyModule.Reader] | Sequence[dict[str, Any]]) -> None: ...
        @property
        def size(self) -> float: ...
        @size.setter
        def size(self, value: float) -> None: ...
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str) -> None: ...
        def init(self, field: Literal["properties"], size: int | None = None) -> MutableSequence[_LayerModule._PropertyModule.Builder]: ...
        @override
        def as_reader(self) -> _LayerModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, properties: Sequence[_LayerModule._PropertyModule.Builder] | Sequence[dict[str, Any]] | None = None, size: float | None = None, description: str | None = None) -> _LayerModule.Builder: ...

LayerReader: TypeAlias = _LayerModule.Reader
LayerBuilder: TypeAlias = _LayerModule.Builder
Layer: _LayerModule

class _QueryModule(_StructModule):
    class _ResultModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def failed(self) -> bool: ...
            @property
            def mandatory(self) -> Sequence[_PropertyNameModule]: ...
            @property
            def optional(self) -> Sequence[_PropertyNameModule]: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _QueryModule._ResultModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def failed(self) -> bool: ...
            @failed.setter
            def failed(self, value: bool) -> None: ...
            @property
            def mandatory(self) -> MutableSequence[_PropertyNameModule]: ...
            @mandatory.setter
            def mandatory(self, value: Sequence[_PropertyNameModule]) -> None: ...
            @property
            def optional(self) -> MutableSequence[_PropertyNameModule]: ...
            @optional.setter
            def optional(self, value: Sequence[_PropertyNameModule]) -> None: ...
            @overload
            def init(self, field: Literal["mandatory"], size: int | None = None) -> MutableSequence[_PropertyNameModule]: ...
            @overload
            def init(self, field: Literal["optional"], size: int | None = None) -> MutableSequence[_PropertyNameModule]: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> _QueryModule._ResultModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, failed: bool | None = None, mandatory: Sequence[_PropertyNameModule] | None = None, optional: Sequence[_PropertyNameModule] | None = None) -> _QueryModule._ResultModule.Builder: ...

    ResultReader: TypeAlias = _ResultModule.Reader
    ResultBuilder: TypeAlias = _ResultModule.Builder
    Result: _ResultModule
    class Reader(_DynamicStructReader):
        @property
        def mandatory(self) -> Sequence[_PropertyNameModule]: ...
        @property
        def optional(self) -> Sequence[_PropertyNameModule]: ...
        @property
        def onlyRawData(self) -> bool: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _QueryModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def mandatory(self) -> MutableSequence[_PropertyNameModule]: ...
        @mandatory.setter
        def mandatory(self, value: Sequence[_PropertyNameModule]) -> None: ...
        @property
        def optional(self) -> MutableSequence[_PropertyNameModule]: ...
        @optional.setter
        def optional(self, value: Sequence[_PropertyNameModule]) -> None: ...
        @property
        def onlyRawData(self) -> bool: ...
        @onlyRawData.setter
        def onlyRawData(self, value: bool) -> None: ...
        @overload
        def init(self, field: Literal["mandatory"], size: int | None = None) -> MutableSequence[_PropertyNameModule]: ...
        @overload
        def init(self, field: Literal["optional"], size: int | None = None) -> MutableSequence[_PropertyNameModule]: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> _QueryModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, mandatory: Sequence[_PropertyNameModule] | None = None, optional: Sequence[_PropertyNameModule] | None = None, onlyRawData: bool | None = None) -> _QueryModule.Builder: ...

QueryReader: TypeAlias = _QueryModule.Reader
QueryBuilder: TypeAlias = _QueryModule.Builder
Query: _QueryModule

class _ProfileDataModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def layers(self) -> Sequence[_LayerModule.Reader]: ...
        @property
        def percentageOfArea(self) -> float: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ProfileDataModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def layers(self) -> MutableSequence[_LayerModule.Builder]: ...
        @layers.setter
        def layers(self, value: Sequence[_LayerModule.Builder | _LayerModule.Reader] | Sequence[dict[str, Any]]) -> None: ...
        @property
        def percentageOfArea(self) -> float: ...
        @percentageOfArea.setter
        def percentageOfArea(self, value: float) -> None: ...
        def init(self, field: Literal["layers"], size: int | None = None) -> MutableSequence[_LayerModule.Builder]: ...
        @override
        def as_reader(self) -> _ProfileDataModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, layers: Sequence[_LayerModule.Builder] | Sequence[dict[str, Any]] | None = None, percentageOfArea: float | None = None) -> _ProfileDataModule.Builder: ...

ProfileDataReader: TypeAlias = _ProfileDataModule.Reader
ProfileDataBuilder: TypeAlias = _ProfileDataModule.Builder
ProfileData: _ProfileDataModule

class _ProfileModule(_IdentifiableModule, _PersistentModule):
    class DataRequest(Protocol):
        def send(self) -> _ProfileModule.ProfileClient.DataResult: ...

    class GeolocationRequest(Protocol):
        def send(self) -> _ProfileModule.ProfileClient.GeolocationResult: ...

    @classmethod
    def _new_client(cls, server: _ProfileModule.Server | _IdentifiableModule.Server | _PersistentModule.Server) -> _ProfileModule.ProfileClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class DataResult(Awaitable[DataResult], Protocol):
            layers: Sequence[_LayerModule.Builder | _LayerModule.Reader]
            percentageOfArea: float

        class GeolocationResult(Awaitable[GeolocationResult], Protocol):
            lat: float
            lon: float

        class DataResultTuple(NamedTuple):
            layers: Sequence[_LayerModule]
            percentageOfArea: float

        class GeolocationResultTuple(NamedTuple):
            lat: float
            lon: float

        class DataCallContext(Protocol):
            params: _ProfileModule.DataRequest
            results: _ProfileModule.Server.DataResult

        class GeolocationCallContext(Protocol):
            params: _ProfileModule.GeolocationRequest
            results: _ProfileModule.Server.GeolocationResult

        def data(self, _context: _ProfileModule.Server.DataCallContext, **kwargs: Any) -> Awaitable[_ProfileModule.Server.DataResultTuple | None]: ...
        def data_context(self, context: _ProfileModule.Server.DataCallContext) -> Awaitable[None]: ...
        def geoLocation(self, _context: _ProfileModule.Server.GeolocationCallContext, **kwargs: Any) -> Awaitable[_ProfileModule.Server.GeolocationResultTuple | None]: ...
        def geoLocation_context(self, context: _ProfileModule.Server.GeolocationCallContext) -> Awaitable[None]: ...

    class ProfileClient(_IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient):
        class DataResult(Awaitable[DataResult], Protocol):
            layers: Sequence[_LayerModule.Builder | _LayerModule.Reader]
            percentageOfArea: float

        class GeolocationResult(Awaitable[GeolocationResult], Protocol):
            lat: float
            lon: float

        def data(self) -> _ProfileModule.ProfileClient.DataResult: ...
        def geoLocation(self) -> _ProfileModule.ProfileClient.GeolocationResult: ...
        def data_request(self) -> _ProfileModule.DataRequest: ...
        def geoLocation_request(self) -> _ProfileModule.GeolocationRequest: ...

Profile: _ProfileModule
ProfileClient: TypeAlias = _ProfileModule.ProfileClient

class _ServiceModule(_IdentifiableModule, _PersistentModule):
    class _StreamModule(_InterfaceModule):
        class NextprofilesRequest(Protocol):
            maxCount: int
            def send(self) -> _ServiceModule._StreamModule.StreamClient.NextprofilesResult: ...

        @classmethod
        def _new_client(cls, server: _ServiceModule._StreamModule.Server) -> _ServiceModule._StreamModule.StreamClient: ...
        class Server(_DynamicCapabilityServer):
            class NextprofilesResult(Awaitable[NextprofilesResult], Protocol):
                profiles: Sequence[_ProfileModule]

            class NextprofilesResultTuple(NamedTuple):
                profiles: Sequence[_ProfileModule]

            class NextprofilesCallContext(Protocol):
                params: _ServiceModule._StreamModule.NextprofilesRequest
                results: _ServiceModule._StreamModule.Server.NextprofilesResult

            def nextProfiles(self, maxCount: int, _context: _ServiceModule._StreamModule.Server.NextprofilesCallContext, **kwargs: Any) -> Awaitable[_ServiceModule._StreamModule.Server.NextprofilesResultTuple | None]: ...
            def nextProfiles_context(self, context: _ServiceModule._StreamModule.Server.NextprofilesCallContext) -> Awaitable[None]: ...

        class StreamClient(_DynamicCapabilityClient):
            class NextprofilesResult(Awaitable[NextprofilesResult], Protocol):
                profiles: Sequence[_ProfileModule]

            def nextProfiles(self, maxCount: int | None = None) -> _ServiceModule._StreamModule.StreamClient.NextprofilesResult: ...
            def nextProfiles_request(self, maxCount: int | None = None) -> _ServiceModule._StreamModule.NextprofilesRequest: ...

    Stream: _StreamModule
    StreamClient: TypeAlias = _ServiceModule._StreamModule.StreamClient
    class CheckavailableparametersRequest(Protocol):
        mandatory: Sequence[_PropertyNameModule]
        optional: Sequence[_PropertyNameModule]
        onlyRawData: bool
        @overload
        def init(self, name: Literal["mandatory"], size: int = ...) -> MutableSequence[_PropertyNameModule]: ...
        @overload
        def init(self, name: Literal["optional"], size: int = ...) -> MutableSequence[_PropertyNameModule]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _ServiceModule.ServiceClient.CheckavailableparametersResult: ...

    class GetallavailableparametersRequest(Protocol):
        onlyRawData: bool
        def send(self) -> _ServiceModule.ServiceClient.GetallavailableparametersResult: ...

    class ClosestprofilesatRequest(Protocol):
        query: _QueryModule.Builder
        @overload
        def init(self, name: Literal["query"]) -> _QueryModule.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _ServiceModule.ServiceClient.ClosestprofilesatResult: ...

    class StreamallprofilesRequest(Protocol):
        mandatory: Sequence[_PropertyNameModule]
        optional: Sequence[_PropertyNameModule]
        onlyRawData: bool
        @overload
        def init(self, name: Literal["mandatory"], size: int = ...) -> MutableSequence[_PropertyNameModule]: ...
        @overload
        def init(self, name: Literal["optional"], size: int = ...) -> MutableSequence[_PropertyNameModule]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _ServiceModule.ServiceClient.StreamallprofilesResult: ...

    @classmethod
    def _new_client(cls, server: _ServiceModule.Server | _IdentifiableModule.Server | _PersistentModule.Server) -> _ServiceModule.ServiceClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class CheckavailableparametersResult(Awaitable[CheckavailableparametersResult], Protocol):
            failed: bool
            mandatory: Sequence[_PropertyNameModule]
            optional: Sequence[_PropertyNameModule]

        class GetallavailableparametersResult(Awaitable[GetallavailableparametersResult], Protocol):
            mandatory: Sequence[_PropertyNameModule]
            optional: Sequence[_PropertyNameModule]

        class ClosestprofilesatResult(Awaitable[ClosestprofilesatResult], Protocol):
            profiles: Sequence[_ProfileModule]

        class StreamallprofilesResult(Awaitable[StreamallprofilesResult], Protocol):
            allProfiles: _ServiceModule._StreamModule.StreamClient

        class CheckavailableparametersResultTuple(NamedTuple):
            failed: bool
            mandatory: Sequence[_PropertyNameModule]
            optional: Sequence[_PropertyNameModule]

        class GetallavailableparametersResultTuple(NamedTuple):
            mandatory: Sequence[_PropertyNameModule]
            optional: Sequence[_PropertyNameModule]

        class ClosestprofilesatResultTuple(NamedTuple):
            profiles: Sequence[_ProfileModule]

        class StreamallprofilesResultTuple(NamedTuple):
            allProfiles: _ServiceModule._StreamModule.Server

        class CheckavailableparametersCallContext(Protocol):
            params: _ServiceModule.CheckavailableparametersRequest
            results: _ServiceModule.Server.CheckavailableparametersResult

        class GetallavailableparametersCallContext(Protocol):
            params: _ServiceModule.GetallavailableparametersRequest
            results: _ServiceModule.Server.GetallavailableparametersResult

        class ClosestprofilesatCallContext(Protocol):
            params: _ServiceModule.ClosestprofilesatRequest
            results: _ServiceModule.Server.ClosestprofilesatResult

        class StreamallprofilesCallContext(Protocol):
            params: _ServiceModule.StreamallprofilesRequest
            results: _ServiceModule.Server.StreamallprofilesResult

        def checkAvailableParameters(self, mandatory: Sequence[_PropertyNameModule], optional: Sequence[_PropertyNameModule], onlyRawData: bool, _context: _ServiceModule.Server.CheckavailableparametersCallContext, **kwargs: Any) -> Awaitable[_ServiceModule.Server.CheckavailableparametersResultTuple | None]: ...
        def checkAvailableParameters_context(self, context: _ServiceModule.Server.CheckavailableparametersCallContext) -> Awaitable[None]: ...
        def getAllAvailableParameters(self, onlyRawData: bool, _context: _ServiceModule.Server.GetallavailableparametersCallContext, **kwargs: Any) -> Awaitable[_ServiceModule.Server.GetallavailableparametersResultTuple | None]: ...
        def getAllAvailableParameters_context(self, context: _ServiceModule.Server.GetallavailableparametersCallContext) -> Awaitable[None]: ...
        def closestProfilesAt(self, query: _QueryModule.Reader, _context: _ServiceModule.Server.ClosestprofilesatCallContext, **kwargs: Any) -> Awaitable[_ServiceModule.Server.ClosestprofilesatResultTuple | None]: ...
        def closestProfilesAt_context(self, context: _ServiceModule.Server.ClosestprofilesatCallContext) -> Awaitable[None]: ...
        def streamAllProfiles(
            self, mandatory: Sequence[_PropertyNameModule], optional: Sequence[_PropertyNameModule], onlyRawData: bool, _context: _ServiceModule.Server.StreamallprofilesCallContext, **kwargs: Any
        ) -> Awaitable[_ServiceModule._StreamModule.Server | _ServiceModule.Server.StreamallprofilesResultTuple | None]: ...
        def streamAllProfiles_context(self, context: _ServiceModule.Server.StreamallprofilesCallContext) -> Awaitable[None]: ...

    class ServiceClient(_IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient):
        class CheckavailableparametersResult(Awaitable[CheckavailableparametersResult], Protocol):
            failed: bool
            mandatory: Sequence[_PropertyNameModule]
            optional: Sequence[_PropertyNameModule]

        class GetallavailableparametersResult(Awaitable[GetallavailableparametersResult], Protocol):
            mandatory: Sequence[_PropertyNameModule]
            optional: Sequence[_PropertyNameModule]

        class ClosestprofilesatResult(Awaitable[ClosestprofilesatResult], Protocol):
            profiles: Sequence[_ProfileModule]

        class StreamallprofilesResult(Awaitable[StreamallprofilesResult], Protocol):
            allProfiles: _ServiceModule._StreamModule.StreamClient

        def checkAvailableParameters(self, mandatory: Sequence[_PropertyNameModule] | None = None, optional: Sequence[_PropertyNameModule] | None = None, onlyRawData: bool | None = None) -> _ServiceModule.ServiceClient.CheckavailableparametersResult: ...
        def getAllAvailableParameters(self, onlyRawData: bool | None = None) -> _ServiceModule.ServiceClient.GetallavailableparametersResult: ...
        def closestProfilesAt(self, query: _QueryModule | dict[str, Any] | None = None) -> _ServiceModule.ServiceClient.ClosestprofilesatResult: ...
        def streamAllProfiles(self, mandatory: Sequence[_PropertyNameModule] | None = None, optional: Sequence[_PropertyNameModule] | None = None, onlyRawData: bool | None = None) -> _ServiceModule.ServiceClient.StreamallprofilesResult: ...
        def checkAvailableParameters_request(self, mandatory: Sequence[_PropertyNameModule] | None = None, optional: Sequence[_PropertyNameModule] | None = None, onlyRawData: bool | None = None) -> _ServiceModule.CheckavailableparametersRequest: ...
        def getAllAvailableParameters_request(self, onlyRawData: bool | None = None) -> _ServiceModule.GetallavailableparametersRequest: ...
        def closestProfilesAt_request(self, query: _QueryModule.Builder | None = None) -> _ServiceModule.ClosestprofilesatRequest: ...
        def streamAllProfiles_request(self, mandatory: Sequence[_PropertyNameModule] | None = None, optional: Sequence[_PropertyNameModule] | None = None, onlyRawData: bool | None = None) -> _ServiceModule.StreamallprofilesRequest: ...

Service: _ServiceModule
ServiceClient: TypeAlias = _ServiceModule.ServiceClient

# Top-level type aliases for use in type annotations
PropertyBuilder: TypeAlias = _LayerModule._PropertyModule.Builder
PropertyReader: TypeAlias = _LayerModule._PropertyModule.Reader
ResultBuilder: TypeAlias = _QueryModule._ResultModule.Builder
ResultReader: TypeAlias = _QueryModule._ResultModule.Reader
StreamClient: TypeAlias = _ServiceModule._StreamModule.StreamClient
