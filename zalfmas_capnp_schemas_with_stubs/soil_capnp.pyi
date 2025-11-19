"""This is an automatically generated stub for `soil.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, MutableSequence, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from .common_capnp import _IdentifiableModule
from .persistence_capnp import _PersistentModule

class _STypeModule:
    unknown: int
    ka5: int

class _PropertyNameModule:
    soilType: int
    sand: int
    clay: int
    silt: int
    pH: int
    sceleton: int
    organicCarbon: int
    organicMatter: int
    bulkDensity: int
    rawDensity: int
    fieldCapacity: int
    permanentWiltingPoint: int
    saturation: int
    soilMoisture: int
    soilWaterConductivityCoefficient: int
    ammonium: int
    nitrate: int
    cnRatio: int
    inGroundwater: int
    impenetrable: int

class _LayerModule(_StructModule):
    class _PropertyModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def name(self) -> PropertyNameEnum: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
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
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> PropertyBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def name(self) -> PropertyNameEnum: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @name.setter
            def name(self, value: PropertyNameEnum) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
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
            def as_reader(self) -> PropertyReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            name: PropertyNameEnum | None = None,
            f32Value: float | None = None,
            bValue: bool | None = None,
            type: str | None = None,
            unset: None | None = None,
            **kwargs: Any,
        ) -> PropertyBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[PropertyReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[PropertyReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[PropertyBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> PropertyReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> PropertyReader: ...

    type PropertyReader = _PropertyModule.Reader
    type PropertyBuilder = _PropertyModule.Builder
    Property: _PropertyModule
    class Reader(_DynamicStructReader):
        @property
        def properties(self) -> Sequence[PropertyReader]: ...
        @property
        def size(self) -> float: ...
        @property
        def description(self) -> str: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> LayerBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def properties(self) -> MutableSequence[PropertyBuilder]: ...
        @properties.setter
        def properties(
            self,
            value: Sequence[PropertyBuilder | PropertyReader]
            | Sequence[dict[str, Any]],
        ) -> None: ...
        @property
        def size(self) -> float: ...
        @size.setter
        def size(self, value: float) -> None: ...
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str) -> None: ...
        def init(
            self, field: Literal["properties"], size: int | None = None
        ) -> MutableSequence[PropertyBuilder]: ...
        @override
        def as_reader(self) -> LayerReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        properties: Sequence[PropertyBuilder] | Sequence[dict[str, Any]] | None = None,
        size: float | None = None,
        description: str | None = None,
        **kwargs: Any,
    ) -> LayerBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[LayerReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[LayerReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[LayerBuilder]: ...
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> LayerReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> LayerReader: ...

Layer: _LayerModule

class _QueryModule(_StructModule):
    class _ResultModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def failed(self) -> bool: ...
            @property
            def mandatory(self) -> Sequence[PropertyNameEnum]: ...
            @property
            def optional(self) -> Sequence[PropertyNameEnum]: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> ResultBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def failed(self) -> bool: ...
            @failed.setter
            def failed(self, value: bool) -> None: ...
            @property
            def mandatory(self) -> MutableSequence[PropertyNameEnum]: ...
            @mandatory.setter
            def mandatory(self, value: Sequence[PropertyNameEnum]) -> None: ...
            @property
            def optional(self) -> MutableSequence[PropertyNameEnum]: ...
            @optional.setter
            def optional(self, value: Sequence[PropertyNameEnum]) -> None: ...
            @overload
            def init(
                self, field: Literal["mandatory"], size: int | None = None
            ) -> MutableSequence[PropertyNameEnum]: ...
            @overload
            def init(
                self, field: Literal["optional"], size: int | None = None
            ) -> MutableSequence[PropertyNameEnum]: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> ResultReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            failed: bool | None = None,
            mandatory: Sequence[PropertyNameEnum] | None = None,
            optional: Sequence[PropertyNameEnum] | None = None,
            **kwargs: Any,
        ) -> ResultBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[ResultReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ResultReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ResultBuilder]: ...
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> ResultReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> ResultReader: ...

    type ResultReader = _ResultModule.Reader
    type ResultBuilder = _ResultModule.Builder
    Result: _ResultModule
    class Reader(_DynamicStructReader):
        @property
        def mandatory(self) -> Sequence[PropertyNameEnum]: ...
        @property
        def optional(self) -> Sequence[PropertyNameEnum]: ...
        @property
        def onlyRawData(self) -> bool: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> QueryBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def mandatory(self) -> MutableSequence[PropertyNameEnum]: ...
        @mandatory.setter
        def mandatory(self, value: Sequence[PropertyNameEnum]) -> None: ...
        @property
        def optional(self) -> MutableSequence[PropertyNameEnum]: ...
        @optional.setter
        def optional(self, value: Sequence[PropertyNameEnum]) -> None: ...
        @property
        def onlyRawData(self) -> bool: ...
        @onlyRawData.setter
        def onlyRawData(self, value: bool) -> None: ...
        @overload
        def init(
            self, field: Literal["mandatory"], size: int | None = None
        ) -> MutableSequence[PropertyNameEnum]: ...
        @overload
        def init(
            self, field: Literal["optional"], size: int | None = None
        ) -> MutableSequence[PropertyNameEnum]: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> QueryReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        mandatory: Sequence[PropertyNameEnum] | None = None,
        optional: Sequence[PropertyNameEnum] | None = None,
        onlyRawData: bool | None = None,
        **kwargs: Any,
    ) -> QueryBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[QueryReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[QueryReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[QueryBuilder]: ...
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> QueryReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> QueryReader: ...

Query: _QueryModule

class _ProfileDataModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def layers(self) -> Sequence[LayerReader]: ...
        @property
        def percentageOfArea(self) -> float: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> ProfileDataBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def layers(self) -> MutableSequence[LayerBuilder]: ...
        @layers.setter
        def layers(
            self, value: Sequence[LayerBuilder | LayerReader] | Sequence[dict[str, Any]]
        ) -> None: ...
        @property
        def percentageOfArea(self) -> float: ...
        @percentageOfArea.setter
        def percentageOfArea(self, value: float) -> None: ...
        def init(
            self, field: Literal["layers"], size: int | None = None
        ) -> MutableSequence[LayerBuilder]: ...
        @override
        def as_reader(self) -> ProfileDataReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        layers: Sequence[LayerBuilder] | Sequence[dict[str, Any]] | None = None,
        percentageOfArea: float | None = None,
        **kwargs: Any,
    ) -> ProfileDataBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[ProfileDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[ProfileDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[ProfileDataBuilder]: ...
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ProfileDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ProfileDataReader: ...

ProfileData: _ProfileDataModule

class _ProfileModule(_IdentifiableModule, _PersistentModule):
    class DataRequest(Protocol):
        def send(self) -> _ProfileModule.ProfileClient.DataResult: ...

    class GeolocationRequest(Protocol):
        def send(self) -> _ProfileModule.ProfileClient.GeolocationResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _ProfileModule.ProfileClient: ...
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

        def data(
            self, _context: _ProfileModule.Server.DataCallContext, **kwargs: Any
        ) -> Awaitable[_ProfileModule.Server.DataResultTuple | None]: ...
        def data_context(
            self, context: _ProfileModule.Server.DataCallContext
        ) -> Awaitable[None]: ...
        def geoLocation(
            self, _context: _ProfileModule.Server.GeolocationCallContext, **kwargs: Any
        ) -> Awaitable[_ProfileModule.Server.GeolocationResultTuple | None]: ...
        def geoLocation_context(
            self, context: _ProfileModule.Server.GeolocationCallContext
        ) -> Awaitable[None]: ...

    class ProfileClient(
        _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
    ):
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

class _ServiceModule(_IdentifiableModule, _PersistentModule):
    class _StreamModule(_InterfaceModule):
        class NextprofilesRequest(Protocol):
            maxCount: int
            def send(
                self,
            ) -> _ServiceModule._StreamModule.StreamClient.NextprofilesResult: ...

        def _new_client(
            self, server: _DynamicCapabilityServer
        ) -> _ServiceModule._StreamModule.StreamClient: ...
        class Server(_DynamicCapabilityServer):
            class NextprofilesResult(Awaitable[NextprofilesResult], Protocol):
                profiles: Sequence[_ProfileModule]

            class NextprofilesResultTuple(NamedTuple):
                profiles: Sequence[_ProfileModule]

            class NextprofilesCallContext(Protocol):
                params: _ServiceModule._StreamModule.NextprofilesRequest
                results: _ServiceModule._StreamModule.Server.NextprofilesResult

            def nextProfiles(
                self,
                maxCount: int,
                _context: _ServiceModule._StreamModule.Server.NextprofilesCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                _ServiceModule._StreamModule.Server.NextprofilesResultTuple | None
            ]: ...
            def nextProfiles_context(
                self,
                context: _ServiceModule._StreamModule.Server.NextprofilesCallContext,
            ) -> Awaitable[None]: ...

        class StreamClient(_DynamicCapabilityClient):
            class NextprofilesResult(Awaitable[NextprofilesResult], Protocol):
                profiles: Sequence[_ProfileModule]

            def nextProfiles(
                self, maxCount: int | None = None
            ) -> _ServiceModule._StreamModule.StreamClient.NextprofilesResult: ...
            def nextProfiles_request(
                self, maxCount: int | None = None
            ) -> _ServiceModule._StreamModule.NextprofilesRequest: ...

    Stream: _StreamModule
    type StreamClient = _ServiceModule._StreamModule.StreamClient
    class CheckavailableparametersRequest(Protocol):
        mandatory: Sequence[PropertyNameEnum]
        optional: Sequence[PropertyNameEnum]
        onlyRawData: bool
        @overload
        def init(
            self, name: Literal["mandatory"], size: int = ...
        ) -> MutableSequence[PropertyNameEnum]: ...
        @overload
        def init(
            self, name: Literal["optional"], size: int = ...
        ) -> MutableSequence[PropertyNameEnum]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(
            self,
        ) -> _ServiceModule.ServiceClient.CheckavailableparametersResult: ...

    class GetallavailableparametersRequest(Protocol):
        onlyRawData: bool
        def send(
            self,
        ) -> _ServiceModule.ServiceClient.GetallavailableparametersResult: ...

    class ClosestprofilesatRequest(Protocol):
        query: _QueryModule.Builder
        @overload
        def init(self, name: Literal["query"]) -> QueryBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _ServiceModule.ServiceClient.ClosestprofilesatResult: ...

    class StreamallprofilesRequest(Protocol):
        mandatory: Sequence[PropertyNameEnum]
        optional: Sequence[PropertyNameEnum]
        onlyRawData: bool
        @overload
        def init(
            self, name: Literal["mandatory"], size: int = ...
        ) -> MutableSequence[PropertyNameEnum]: ...
        @overload
        def init(
            self, name: Literal["optional"], size: int = ...
        ) -> MutableSequence[PropertyNameEnum]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _ServiceModule.ServiceClient.StreamallprofilesResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _ServiceModule.ServiceClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class CheckavailableparametersResult(
            Awaitable[CheckavailableparametersResult], Protocol
        ):
            failed: bool
            mandatory: Sequence[PropertyNameEnum]
            optional: Sequence[PropertyNameEnum]

        class GetallavailableparametersResult(
            Awaitable[GetallavailableparametersResult], Protocol
        ):
            mandatory: Sequence[PropertyNameEnum]
            optional: Sequence[PropertyNameEnum]

        class ClosestprofilesatResult(Awaitable[ClosestprofilesatResult], Protocol):
            profiles: Sequence[_ProfileModule]

        class StreamallprofilesResult(Awaitable[StreamallprofilesResult], Protocol):
            allProfiles: _ServiceModule._StreamModule.StreamClient

        class CheckavailableparametersResultTuple(NamedTuple):
            failed: bool
            mandatory: Sequence[PropertyNameEnum]
            optional: Sequence[PropertyNameEnum]

        class GetallavailableparametersResultTuple(NamedTuple):
            mandatory: Sequence[PropertyNameEnum]
            optional: Sequence[PropertyNameEnum]

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

        def checkAvailableParameters(
            self,
            mandatory: Sequence[PropertyNameEnum],
            optional: Sequence[PropertyNameEnum],
            onlyRawData: bool,
            _context: _ServiceModule.Server.CheckavailableparametersCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            _ServiceModule.Server.CheckavailableparametersResultTuple | None
        ]: ...
        def checkAvailableParameters_context(
            self, context: _ServiceModule.Server.CheckavailableparametersCallContext
        ) -> Awaitable[None]: ...
        def getAllAvailableParameters(
            self,
            onlyRawData: bool,
            _context: _ServiceModule.Server.GetallavailableparametersCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            _ServiceModule.Server.GetallavailableparametersResultTuple | None
        ]: ...
        def getAllAvailableParameters_context(
            self, context: _ServiceModule.Server.GetallavailableparametersCallContext
        ) -> Awaitable[None]: ...
        def closestProfilesAt(
            self,
            query: _QueryModule.Reader,
            _context: _ServiceModule.Server.ClosestprofilesatCallContext,
            **kwargs: Any,
        ) -> Awaitable[_ServiceModule.Server.ClosestprofilesatResultTuple | None]: ...
        def closestProfilesAt_context(
            self, context: _ServiceModule.Server.ClosestprofilesatCallContext
        ) -> Awaitable[None]: ...
        def streamAllProfiles(
            self,
            mandatory: Sequence[PropertyNameEnum],
            optional: Sequence[PropertyNameEnum],
            onlyRawData: bool,
            _context: _ServiceModule.Server.StreamallprofilesCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            _ServiceModule._StreamModule.Server
            | _ServiceModule.Server.StreamallprofilesResultTuple
            | None
        ]: ...
        def streamAllProfiles_context(
            self, context: _ServiceModule.Server.StreamallprofilesCallContext
        ) -> Awaitable[None]: ...

    class ServiceClient(
        _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
    ):
        class CheckavailableparametersResult(
            Awaitable[CheckavailableparametersResult], Protocol
        ):
            failed: bool
            mandatory: Sequence[PropertyNameEnum]
            optional: Sequence[PropertyNameEnum]

        class GetallavailableparametersResult(
            Awaitable[GetallavailableparametersResult], Protocol
        ):
            mandatory: Sequence[PropertyNameEnum]
            optional: Sequence[PropertyNameEnum]

        class ClosestprofilesatResult(Awaitable[ClosestprofilesatResult], Protocol):
            profiles: Sequence[_ProfileModule]

        class StreamallprofilesResult(Awaitable[StreamallprofilesResult], Protocol):
            allProfiles: _ServiceModule._StreamModule.StreamClient

        def checkAvailableParameters(
            self,
            mandatory: Sequence[PropertyNameEnum] | None = None,
            optional: Sequence[PropertyNameEnum] | None = None,
            onlyRawData: bool | None = None,
        ) -> _ServiceModule.ServiceClient.CheckavailableparametersResult: ...
        def getAllAvailableParameters(
            self, onlyRawData: bool | None = None
        ) -> _ServiceModule.ServiceClient.GetallavailableparametersResult: ...
        def closestProfilesAt(
            self, query: QueryBuilder | QueryReader | dict[str, Any] | None = None
        ) -> _ServiceModule.ServiceClient.ClosestprofilesatResult: ...
        def streamAllProfiles(
            self,
            mandatory: Sequence[PropertyNameEnum] | None = None,
            optional: Sequence[PropertyNameEnum] | None = None,
            onlyRawData: bool | None = None,
        ) -> _ServiceModule.ServiceClient.StreamallprofilesResult: ...
        def checkAvailableParameters_request(
            self,
            mandatory: Sequence[PropertyNameEnum] | None = None,
            optional: Sequence[PropertyNameEnum] | None = None,
            onlyRawData: bool | None = None,
        ) -> _ServiceModule.CheckavailableparametersRequest: ...
        def getAllAvailableParameters_request(
            self, onlyRawData: bool | None = None
        ) -> _ServiceModule.GetallavailableparametersRequest: ...
        def closestProfilesAt_request(
            self, query: _QueryModule.Builder | None = None
        ) -> _ServiceModule.ClosestprofilesatRequest: ...
        def streamAllProfiles_request(
            self,
            mandatory: Sequence[PropertyNameEnum] | None = None,
            optional: Sequence[PropertyNameEnum] | None = None,
            onlyRawData: bool | None = None,
        ) -> _ServiceModule.StreamallprofilesRequest: ...

Service: _ServiceModule

# Top-level type aliases for use in type annotations
type CheckavailableparametersResult = (
    _ServiceModule.ServiceClient.CheckavailableparametersResult
)
type ClosestprofilesatResult = _ServiceModule.ServiceClient.ClosestprofilesatResult
type DataResult = _ProfileModule.ProfileClient.DataResult
type GeolocationResult = _ProfileModule.ProfileClient.GeolocationResult
type GetallavailableparametersResult = (
    _ServiceModule.ServiceClient.GetallavailableparametersResult
)
type LayerBuilder = _LayerModule.Builder
type LayerReader = _LayerModule.Reader
type NextprofilesResult = _ServiceModule._StreamModule.StreamClient.NextprofilesResult
type ProfileClient = _ProfileModule.ProfileClient
type ProfileDataBuilder = _ProfileDataModule.Builder
type ProfileDataReader = _ProfileDataModule.Reader
type PropertyBuilder = _LayerModule._PropertyModule.Builder
type PropertyNameEnum = (
    int
    | Literal[
        "soilType",
        "sand",
        "clay",
        "silt",
        "pH",
        "sceleton",
        "organicCarbon",
        "organicMatter",
        "bulkDensity",
        "rawDensity",
        "fieldCapacity",
        "permanentWiltingPoint",
        "saturation",
        "soilMoisture",
        "soilWaterConductivityCoefficient",
        "ammonium",
        "nitrate",
        "cnRatio",
        "inGroundwater",
        "impenetrable",
    ]
)
type PropertyReader = _LayerModule._PropertyModule.Reader
type QueryBuilder = _QueryModule.Builder
type QueryReader = _QueryModule.Reader
type ResultBuilder = _QueryModule._ResultModule.Builder
type ResultReader = _QueryModule._ResultModule.Reader
type STypeEnum = int | Literal["unknown", "ka5"]
type ServiceClient = _ServiceModule.ServiceClient
type StreamClient = _ServiceModule._StreamModule.StreamClient
type StreamallprofilesResult = _ServiceModule.ServiceClient.StreamallprofilesResult
