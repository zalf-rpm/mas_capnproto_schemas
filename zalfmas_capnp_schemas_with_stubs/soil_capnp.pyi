"""This is an automatically generated stub for `soil.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from .common_capnp import _IdentifiableModule
from .geo_capnp import LatLonCoordBuilder, LatLonCoordReader
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

class _PropertyList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> PropertyReader: ...
        def __iter__(self) -> Iterator[PropertyReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> PropertyBuilder: ...
        def __setitem__(
            self, key: int, value: PropertyReader | PropertyBuilder | dict[str, Any]
        ) -> None: ...
        def __iter__(self) -> Iterator[PropertyBuilder]: ...
        def init(self, index: int, size: int | None = None) -> PropertyBuilder: ...

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
        def properties(self) -> PropertyListReader: ...
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
        def properties(self) -> PropertyListBuilder: ...
        @properties.setter
        def properties(
            self, value: PropertyListBuilder | PropertyListReader | dict[str, Any]
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
        ) -> PropertyListBuilder: ...
        @override
        def as_reader(self) -> LayerReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        properties: PropertyListBuilder | dict[str, Any] | None = None,
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

class _PropertyNameEnumList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> PropertyNameEnum: ...
        def __iter__(self) -> Iterator[PropertyNameEnum]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> PropertyNameEnum: ...
        def __setitem__(self, key: int, value: PropertyNameEnum) -> None: ...
        def __iter__(self) -> Iterator[PropertyNameEnum]: ...

class _QueryModule(_StructModule):
    class _ResultModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def failed(self) -> bool: ...
            @property
            def mandatory(self) -> PropertyNameEnumListReader: ...
            @property
            def optional(self) -> PropertyNameEnumListReader: ...
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
            def mandatory(self) -> PropertyNameEnumListBuilder: ...
            @mandatory.setter
            def mandatory(
                self,
                value: PropertyNameEnumListBuilder
                | PropertyNameEnumListReader
                | dict[str, Any],
            ) -> None: ...
            @property
            def optional(self) -> PropertyNameEnumListBuilder: ...
            @optional.setter
            def optional(
                self,
                value: PropertyNameEnumListBuilder
                | PropertyNameEnumListReader
                | dict[str, Any],
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["mandatory"], size: int | None = None
            ) -> PropertyNameEnumListBuilder: ...
            @overload
            def init(
                self, field: Literal["optional"], size: int | None = None
            ) -> PropertyNameEnumListBuilder: ...
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
            mandatory: PropertyNameEnumListBuilder | dict[str, Any] | None = None,
            optional: PropertyNameEnumListBuilder | dict[str, Any] | None = None,
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
        def mandatory(self) -> PropertyNameEnumListReader: ...
        @property
        def optional(self) -> PropertyNameEnumListReader: ...
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
        def mandatory(self) -> PropertyNameEnumListBuilder: ...
        @mandatory.setter
        def mandatory(
            self,
            value: PropertyNameEnumListBuilder
            | PropertyNameEnumListReader
            | dict[str, Any],
        ) -> None: ...
        @property
        def optional(self) -> PropertyNameEnumListBuilder: ...
        @optional.setter
        def optional(
            self,
            value: PropertyNameEnumListBuilder
            | PropertyNameEnumListReader
            | dict[str, Any],
        ) -> None: ...
        @property
        def onlyRawData(self) -> bool: ...
        @onlyRawData.setter
        def onlyRawData(self, value: bool) -> None: ...
        @overload
        def init(
            self, field: Literal["mandatory"], size: int | None = None
        ) -> PropertyNameEnumListBuilder: ...
        @overload
        def init(
            self, field: Literal["optional"], size: int | None = None
        ) -> PropertyNameEnumListBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> QueryReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        mandatory: PropertyNameEnumListBuilder | dict[str, Any] | None = None,
        optional: PropertyNameEnumListBuilder | dict[str, Any] | None = None,
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

class _LayerList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> LayerReader: ...
        def __iter__(self) -> Iterator[LayerReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> LayerBuilder: ...
        def __setitem__(
            self, key: int, value: LayerReader | LayerBuilder | dict[str, Any]
        ) -> None: ...
        def __iter__(self) -> Iterator[LayerBuilder]: ...
        def init(self, index: int, size: int | None = None) -> LayerBuilder: ...

class _ProfileDataModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def layers(self) -> LayerListReader: ...
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
        def layers(self) -> LayerListBuilder: ...
        @layers.setter
        def layers(
            self, value: LayerListBuilder | LayerListReader | dict[str, Any]
        ) -> None: ...
        @property
        def percentageOfArea(self) -> float: ...
        @percentageOfArea.setter
        def percentageOfArea(self, value: float) -> None: ...
        def init(
            self, field: Literal["layers"], size: int | None = None
        ) -> LayerListBuilder: ...
        @override
        def as_reader(self) -> ProfileDataReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        layers: LayerListBuilder | dict[str, Any] | None = None,
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
            layers: LayerListBuilder | LayerListReader
            percentageOfArea: float

        class GeolocationResult(Awaitable[GeolocationResult], Protocol):
            lat: float
            lon: float

        class DataResultTuple(NamedTuple):
            layers: LayerListBuilder | LayerListReader
            percentageOfArea: float

        class GeolocationResultTuple(NamedTuple):
            lat: float
            lon: float

        class DataParams(Protocol): ...

        class DataCallContext(Protocol):
            params: _ProfileModule.Server.DataParams
            @property
            def results(self) -> ProfileDataBuilder: ...

        class GeolocationParams(Protocol): ...

        class GeolocationCallContext(Protocol):
            params: _ProfileModule.Server.GeolocationParams
            @property
            def results(self) -> LatLonCoordBuilder: ...

        def data(
            self,
            _context: _ProfileModule.Server.DataCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_ProfileModule.Server.DataResultTuple | None]: ...
        def data_context(
            self, context: _ProfileModule.Server.DataCallContext
        ) -> Awaitable[None]: ...
        def geoLocation(
            self,
            _context: _ProfileModule.Server.GeolocationCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_ProfileModule.Server.GeolocationResultTuple | None]: ...
        def geoLocation_context(
            self, context: _ProfileModule.Server.GeolocationCallContext
        ) -> Awaitable[None]: ...

    class ProfileClient(
        _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
    ):
        class DataResult(Awaitable[DataResult], Protocol):
            layers: LayerListReader
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
            class NextprofilesResult(_DynamicStructBuilder):
                @property
                def profiles(self) -> ProfileClientListBuilder: ...
                @profiles.setter
                def profiles(
                    self,
                    value: ProfileClientListBuilder
                    | ProfileClientListReader
                    | Sequence[Any],
                ) -> None: ...
                @overload
                def init(
                    self, field: Literal["profiles"], size: int | None = None
                ) -> ProfileClientListBuilder: ...
                @overload
                def init(self, field: str, size: int | None = None) -> Any: ...

            class NextprofilesResultTuple(NamedTuple):
                profiles: ProfileClientListBuilder | ProfileClientListReader

            class NextprofilesParams(Protocol):
                maxCount: int

            class NextprofilesCallContext(Protocol):
                params: _ServiceModule._StreamModule.Server.NextprofilesParams
                @property
                def results(
                    self,
                ) -> _ServiceModule._StreamModule.Server.NextprofilesResult: ...

            def nextProfiles(
                self,
                maxCount: int,
                _context: _ServiceModule._StreamModule.Server.NextprofilesCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                Sequence[_ProfileModule]
                | _ServiceModule._StreamModule.Server.NextprofilesResultTuple
                | None
            ]: ...
            def nextProfiles_context(
                self,
                context: _ServiceModule._StreamModule.Server.NextprofilesCallContext,
            ) -> Awaitable[None]: ...

        class StreamClient(_DynamicCapabilityClient):
            class NextprofilesResult(Awaitable[NextprofilesResult], Protocol):
                profiles: ProfileClientListReader

            def nextProfiles(
                self, maxCount: int | None = None
            ) -> _ServiceModule._StreamModule.StreamClient.NextprofilesResult: ...
            def nextProfiles_request(
                self, maxCount: int | None = None
            ) -> _ServiceModule._StreamModule.NextprofilesRequest: ...

    Stream: _StreamModule
    type StreamClient = _ServiceModule._StreamModule.StreamClient
    type StreamServer = _ServiceModule._StreamModule.Server
    class CheckavailableparametersRequest(Protocol):
        mandatory: (
            PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any]
        )
        optional: (
            PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any]
        )
        onlyRawData: bool
        @overload
        def init(
            self, name: Literal["mandatory"], size: int = ...
        ) -> PropertyNameEnumListBuilder: ...
        @overload
        def init(
            self, name: Literal["optional"], size: int = ...
        ) -> PropertyNameEnumListBuilder: ...
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
        coord: LatLonCoordBuilder
        query: QueryBuilder
        @overload
        def init(self, name: Literal["coord"]) -> LatLonCoordBuilder: ...
        @overload
        def init(self, name: Literal["query"]) -> QueryBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _ServiceModule.ServiceClient.ClosestprofilesatResult: ...

    class StreamallprofilesRequest(Protocol):
        mandatory: (
            PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any]
        )
        optional: (
            PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any]
        )
        onlyRawData: bool
        @overload
        def init(
            self, name: Literal["mandatory"], size: int = ...
        ) -> PropertyNameEnumListBuilder: ...
        @overload
        def init(
            self, name: Literal["optional"], size: int = ...
        ) -> PropertyNameEnumListBuilder: ...
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
            mandatory: PropertyNameEnumListBuilder | PropertyNameEnumListReader
            optional: PropertyNameEnumListBuilder | PropertyNameEnumListReader

        class GetallavailableparametersResult(_DynamicStructBuilder):
            @property
            def mandatory(self) -> PropertyNameEnumListBuilder: ...
            @mandatory.setter
            def mandatory(
                self,
                value: PropertyNameEnumListBuilder
                | PropertyNameEnumListReader
                | Sequence[Any],
            ) -> None: ...
            @property
            def optional(self) -> PropertyNameEnumListBuilder: ...
            @optional.setter
            def optional(
                self,
                value: PropertyNameEnumListBuilder
                | PropertyNameEnumListReader
                | Sequence[Any],
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["mandatory"], size: int | None = None
            ) -> PropertyNameEnumListBuilder: ...
            @overload
            def init(
                self, field: Literal["optional"], size: int | None = None
            ) -> PropertyNameEnumListBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...

        class ClosestprofilesatResult(_DynamicStructBuilder):
            @property
            def profiles(self) -> ProfileClientListBuilder: ...
            @profiles.setter
            def profiles(
                self,
                value: ProfileClientListBuilder
                | ProfileClientListReader
                | Sequence[Any],
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["profiles"], size: int | None = None
            ) -> ProfileClientListBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...

        class StreamallprofilesResult(_DynamicStructBuilder):
            @property
            def allProfiles(
                self,
            ) -> (
                _ServiceModule._StreamModule.Server
                | _ServiceModule._StreamModule.StreamClient
            ): ...
            @allProfiles.setter
            def allProfiles(
                self,
                value: _ServiceModule._StreamModule.Server
                | _ServiceModule._StreamModule.StreamClient,
            ) -> None: ...

        class CheckavailableparametersResultTuple(NamedTuple):
            failed: bool
            mandatory: PropertyNameEnumListBuilder | PropertyNameEnumListReader
            optional: PropertyNameEnumListBuilder | PropertyNameEnumListReader

        class GetallavailableparametersResultTuple(NamedTuple):
            mandatory: PropertyNameEnumListBuilder | PropertyNameEnumListReader
            optional: PropertyNameEnumListBuilder | PropertyNameEnumListReader

        class ClosestprofilesatResultTuple(NamedTuple):
            profiles: ProfileClientListBuilder | ProfileClientListReader

        class StreamallprofilesResultTuple(NamedTuple):
            allProfiles: (
                _ServiceModule._StreamModule.Server
                | _ServiceModule._StreamModule.StreamClient
            )

        class CheckavailableparametersParams(Protocol):
            mandatory: PropertyNameEnumListReader
            optional: PropertyNameEnumListReader
            onlyRawData: bool

        class CheckavailableparametersCallContext(Protocol):
            params: _ServiceModule.Server.CheckavailableparametersParams
            @property
            def results(self) -> ResultBuilder: ...

        class GetallavailableparametersParams(Protocol):
            onlyRawData: bool

        class GetallavailableparametersCallContext(Protocol):
            params: _ServiceModule.Server.GetallavailableparametersParams
            @property
            def results(
                self,
            ) -> _ServiceModule.Server.GetallavailableparametersResult: ...

        class ClosestprofilesatParams(Protocol):
            coord: LatLonCoordReader
            query: QueryReader

        class ClosestprofilesatCallContext(Protocol):
            params: _ServiceModule.Server.ClosestprofilesatParams
            @property
            def results(self) -> _ServiceModule.Server.ClosestprofilesatResult: ...

        class StreamallprofilesParams(Protocol):
            mandatory: PropertyNameEnumListReader
            optional: PropertyNameEnumListReader
            onlyRawData: bool

        class StreamallprofilesCallContext(Protocol):
            params: _ServiceModule.Server.StreamallprofilesParams
            @property
            def results(self) -> _ServiceModule.Server.StreamallprofilesResult: ...

        def checkAvailableParameters(
            self,
            mandatory: PropertyNameEnumListReader,
            optional: PropertyNameEnumListReader,
            onlyRawData: bool,
            _context: _ServiceModule.Server.CheckavailableparametersCallContext,
            **kwargs: dict[str, Any],
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
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _ServiceModule.Server.GetallavailableparametersResultTuple | None
        ]: ...
        def getAllAvailableParameters_context(
            self, context: _ServiceModule.Server.GetallavailableparametersCallContext
        ) -> Awaitable[None]: ...
        def closestProfilesAt(
            self,
            coord: LatLonCoordReader,
            query: QueryReader,
            _context: _ServiceModule.Server.ClosestprofilesatCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            Sequence[_ProfileModule]
            | _ServiceModule.Server.ClosestprofilesatResultTuple
            | None
        ]: ...
        def closestProfilesAt_context(
            self, context: _ServiceModule.Server.ClosestprofilesatCallContext
        ) -> Awaitable[None]: ...
        def streamAllProfiles(
            self,
            mandatory: PropertyNameEnumListReader,
            optional: PropertyNameEnumListReader,
            onlyRawData: bool,
            _context: _ServiceModule.Server.StreamallprofilesCallContext,
            **kwargs: dict[str, Any],
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
            mandatory: PropertyNameEnumListReader
            optional: PropertyNameEnumListReader

        class GetallavailableparametersResult(
            Awaitable[GetallavailableparametersResult], Protocol
        ):
            mandatory: PropertyNameEnumListReader
            optional: PropertyNameEnumListReader

        class ClosestprofilesatResult(Awaitable[ClosestprofilesatResult], Protocol):
            profiles: ProfileClientListReader

        class StreamallprofilesResult(Awaitable[StreamallprofilesResult], Protocol):
            allProfiles: _ServiceModule._StreamModule.StreamClient

        def checkAvailableParameters(
            self,
            mandatory: PropertyNameEnumListBuilder
            | PropertyNameEnumListReader
            | Sequence[Any]
            | None = None,
            optional: PropertyNameEnumListBuilder
            | PropertyNameEnumListReader
            | Sequence[Any]
            | None = None,
            onlyRawData: bool | None = None,
        ) -> _ServiceModule.ServiceClient.CheckavailableparametersResult: ...
        def getAllAvailableParameters(
            self, onlyRawData: bool | None = None
        ) -> _ServiceModule.ServiceClient.GetallavailableparametersResult: ...
        def closestProfilesAt(
            self,
            coord: LatLonCoordBuilder
            | LatLonCoordReader
            | dict[str, Any]
            | None = None,
            query: QueryBuilder | QueryReader | dict[str, Any] | None = None,
        ) -> _ServiceModule.ServiceClient.ClosestprofilesatResult: ...
        def streamAllProfiles(
            self,
            mandatory: PropertyNameEnumListBuilder
            | PropertyNameEnumListReader
            | Sequence[Any]
            | None = None,
            optional: PropertyNameEnumListBuilder
            | PropertyNameEnumListReader
            | Sequence[Any]
            | None = None,
            onlyRawData: bool | None = None,
        ) -> _ServiceModule.ServiceClient.StreamallprofilesResult: ...
        def checkAvailableParameters_request(
            self,
            mandatory: PropertyNameEnumListBuilder
            | PropertyNameEnumListReader
            | Sequence[Any]
            | None = None,
            optional: PropertyNameEnumListBuilder
            | PropertyNameEnumListReader
            | Sequence[Any]
            | None = None,
            onlyRawData: bool | None = None,
        ) -> _ServiceModule.CheckavailableparametersRequest: ...
        def getAllAvailableParameters_request(
            self, onlyRawData: bool | None = None
        ) -> _ServiceModule.GetallavailableparametersRequest: ...
        def closestProfilesAt_request(
            self,
            coord: LatLonCoordBuilder | None = None,
            query: QueryBuilder | None = None,
        ) -> _ServiceModule.ClosestprofilesatRequest: ...
        def streamAllProfiles_request(
            self,
            mandatory: PropertyNameEnumListBuilder
            | PropertyNameEnumListReader
            | Sequence[Any]
            | None = None,
            optional: PropertyNameEnumListBuilder
            | PropertyNameEnumListReader
            | Sequence[Any]
            | None = None,
            onlyRawData: bool | None = None,
        ) -> _ServiceModule.StreamallprofilesRequest: ...

class _ProfileClientList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> ProfileClient: ...
        def __iter__(self) -> Iterator[ProfileClient]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> ProfileClient: ...
        def __setitem__(
            self, key: int, value: ProfileClient | _ProfileModule.Server
        ) -> None: ...
        def __iter__(self) -> Iterator[ProfileClient]: ...

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
type LayerListBuilder = _LayerList.Builder
type LayerListReader = _LayerList.Reader
type LayerReader = _LayerModule.Reader
type NextprofilesResult = _ServiceModule._StreamModule.StreamClient.NextprofilesResult
type ProfileClient = _ProfileModule.ProfileClient
type ProfileClientListBuilder = _ProfileClientList.Builder
type ProfileClientListReader = _ProfileClientList.Reader
type ProfileDataBuilder = _ProfileDataModule.Builder
type ProfileDataReader = _ProfileDataModule.Reader
type ProfileServer = _ProfileModule.Server
type PropertyBuilder = _LayerModule._PropertyModule.Builder
type PropertyListBuilder = _PropertyList.Builder
type PropertyListReader = _PropertyList.Reader
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
type PropertyNameEnumListBuilder = _PropertyNameEnumList.Builder
type PropertyNameEnumListReader = _PropertyNameEnumList.Reader
type PropertyReader = _LayerModule._PropertyModule.Reader
type QueryBuilder = _QueryModule.Builder
type QueryReader = _QueryModule.Reader
type ResultBuilder = _QueryModule._ResultModule.Builder
type ResultReader = _QueryModule._ResultModule.Reader
type STypeEnum = int | Literal["unknown", "ka5"]
type ServiceClient = _ServiceModule.ServiceClient
type ServiceServer = _ServiceModule.Server
type StreamClient = _ServiceModule._StreamModule.StreamClient
type StreamServer = _ServiceModule._StreamModule.Server
type StreamallprofilesResult = _ServiceModule.ServiceClient.StreamallprofilesResult
