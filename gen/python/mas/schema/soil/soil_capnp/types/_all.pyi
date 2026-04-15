"""This is an automatically generated stub for `soil.capnp`."""

from collections.abc import Awaitable, Callable, Iterator, Sequence
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

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)

class _STypeEnumModule:
    unknown: int
    ka5: int

class _PropertyNameEnumModule:
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

class PropertyReader(_DynamicStructReader):
    @property
    def name(self) -> PropertyNameEnum: ...
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> PropertyBuilder: ...

class PropertyBuilder(_DynamicStructBuilder):
    @property
    def name(self) -> PropertyNameEnum: ...
    @name.setter
    def name(self, value: PropertyNameEnum) -> None: ...
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

class _PropertyList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> PropertyReader: ...
        @override
        def __iter__(self) -> Iterator[PropertyReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> PropertyBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: PropertyReader | PropertyBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[PropertyBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> PropertyBuilder: ...

class _LayerStructModule(_StructModule):
    class _PropertyStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            name: PropertyNameEnum | None = None,
            f32Value: float | None = None,
            bValue: bool | None = None,
            type: str | None = None,
            unset: None | None = None,
            **kwargs: object,
        ) -> PropertyBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[PropertyReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[PropertyReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[PropertyBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> PropertyReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> PropertyReader: ...

    Property: _PropertyStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        properties: PropertyListBuilder | dict[str, Any] | None = None,
        size: float | None = None,
        description: str | None = None,
        **kwargs: object,
    ) -> LayerBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[LayerReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[LayerReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[LayerBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> LayerReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> LayerReader: ...

class LayerReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> LayerBuilder: ...

class LayerBuilder(_DynamicStructBuilder):
    @property
    def properties(self) -> PropertyListBuilder: ...
    @properties.setter
    def properties(
        self,
        value: PropertyListBuilder | PropertyListReader | dict[str, Any],
    ) -> None: ...
    @property
    def size(self) -> float: ...
    @size.setter
    def size(self, value: float) -> None: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str) -> None: ...
    @override
    def init(
        self,
        field: Literal["properties"],
        size: int | None = None,
    ) -> PropertyListBuilder: ...
    @override
    def as_reader(self) -> LayerReader: ...

Layer: _LayerStructModule

class _PropertyNameEnumList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> PropertyNameEnum: ...
        @override
        def __iter__(self) -> Iterator[PropertyNameEnum]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> PropertyNameEnum: ...
        @override
        def __setitem__(self, key: int, value: PropertyNameEnum) -> None: ...
        @override
        def __iter__(self) -> Iterator[PropertyNameEnum]: ...

class ResultReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ResultBuilder: ...

class ResultBuilder(_DynamicStructBuilder):
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
    @override
    @overload
    def init(
        self,
        field: Literal["mandatory"],
        size: int | None = None,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["optional"],
        size: int | None = None,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> ResultReader: ...

class _QueryStructModule(_StructModule):
    class _ResultStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            failed: bool | None = None,
            mandatory: PropertyNameEnumListBuilder | dict[str, Any] | None = None,
            optional: PropertyNameEnumListBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> ResultBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[ResultReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ResultReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ResultBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> ResultReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> ResultReader: ...

    Result: _ResultStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        mandatory: PropertyNameEnumListBuilder | dict[str, Any] | None = None,
        optional: PropertyNameEnumListBuilder | dict[str, Any] | None = None,
        onlyRawData: bool | None = None,
        **kwargs: object,
    ) -> QueryBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[QueryReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[QueryReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[QueryBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> QueryReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> QueryReader: ...

class QueryReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> QueryBuilder: ...

class QueryBuilder(_DynamicStructBuilder):
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
    @override
    @overload
    def init(
        self,
        field: Literal["mandatory"],
        size: int | None = None,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["optional"],
        size: int | None = None,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> QueryReader: ...

Query: _QueryStructModule

class _LayerList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> LayerReader: ...
        @override
        def __iter__(self) -> Iterator[LayerReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> LayerBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: LayerReader | LayerBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[LayerBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> LayerBuilder: ...

class _ProfileDataStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        layers: LayerListBuilder | dict[str, Any] | None = None,
        percentageOfArea: float | None = None,
        **kwargs: object,
    ) -> ProfileDataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[ProfileDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[ProfileDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[ProfileDataBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> ProfileDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> ProfileDataReader: ...

class ProfileDataReader(_DynamicStructReader):
    @property
    def layers(self) -> LayerListReader: ...
    @property
    def percentageOfArea(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ProfileDataBuilder: ...

class ProfileDataBuilder(_DynamicStructBuilder):
    @property
    def layers(self) -> LayerListBuilder: ...
    @layers.setter
    def layers(
        self,
        value: LayerListBuilder | LayerListReader | dict[str, Any],
    ) -> None: ...
    @property
    def percentageOfArea(self) -> float: ...
    @percentageOfArea.setter
    def percentageOfArea(self, value: float) -> None: ...
    @override
    def init(
        self,
        field: Literal["layers"],
        size: int | None = None,
    ) -> LayerListBuilder: ...
    @override
    def as_reader(self) -> ProfileDataReader: ...

ProfileData: _ProfileDataStructModule

class _ProfileInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> ProfileClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def data(
            self,
            _context: DataCallContext,
            **kwargs: object,
        ) -> Awaitable[DataResultTuple | None]: ...
        def data_context(self, context: DataCallContext) -> Awaitable[None]: ...
        def geoLocation(
            self,
            _context: GeolocationCallContext,
            **kwargs: object,
        ) -> Awaitable[GeolocationResultTuple | None]: ...
        def geoLocation_context(
            self,
            context: GeolocationCallContext,
        ) -> Awaitable[None]: ...

class DataRequest(Protocol):
    def send(self) -> DataResult: ...

class DataResult(Awaitable[DataResult], Protocol):
    layers: LayerListReader
    percentageOfArea: float

class DataParams(Protocol): ...

class DataCallContext(Protocol):
    params: DataParams
    @property
    def results(self) -> ProfileDataBuilder: ...

class DataResultTuple(NamedTuple):
    layers: LayerListBuilder | LayerListReader | Sequence[Any]
    percentageOfArea: float

class GeolocationRequest(Protocol):
    def send(self) -> GeolocationResult: ...

class GeolocationResult(Awaitable[GeolocationResult], Protocol):
    lat: float
    lon: float

class GeolocationParams(Protocol): ...

class GeolocationCallContext(Protocol):
    params: GeolocationParams
    @property
    def results(self) -> LatLonCoordBuilder: ...

class GeolocationResultTuple(NamedTuple):
    lat: float
    lon: float

class ProfileClient(IdentifiableClient, PersistentClient):
    def data(self) -> DataResult: ...
    def geoLocation(self) -> GeolocationResult: ...
    def data_request(self) -> DataRequest: ...
    def geoLocation_request(self) -> GeolocationRequest: ...

Profile: _ProfileInterfaceModule

class _ServiceInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _StreamInterfaceModule(_InterfaceModule):
        @override
        def _new_client(self, server: _DynamicCapabilityServer) -> StreamClient: ...
        class Server(_DynamicCapabilityServer):
            def nextProfiles(
                self,
                maxCount: int,
                _context: NextprofilesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                ProfileClientListBuilder
                | ProfileClientListReader
                | Sequence[Any]
                | NextprofilesResultTuple
                | None
            ]: ...
            def nextProfiles_context(
                self,
                context: NextprofilesCallContext,
            ) -> Awaitable[None]: ...

    Stream: _StreamInterfaceModule
    type StreamServer = _ServiceInterfaceModule._StreamInterfaceModule.Server
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> ServiceClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def checkAvailableParameters(
            self,
            mandatory: PropertyNameEnumListReader,
            optional: PropertyNameEnumListReader,
            onlyRawData: bool,
            _context: CheckavailableparametersCallContext,
            **kwargs: object,
        ) -> Awaitable[CheckavailableparametersResultTuple | None]: ...
        def checkAvailableParameters_context(
            self,
            context: CheckavailableparametersCallContext,
        ) -> Awaitable[None]: ...
        def getAllAvailableParameters(
            self,
            onlyRawData: bool,
            _context: GetallavailableparametersCallContext,
            **kwargs: object,
        ) -> Awaitable[GetallavailableparametersResultTuple | None]: ...
        def getAllAvailableParameters_context(
            self,
            context: GetallavailableparametersCallContext,
        ) -> Awaitable[None]: ...
        def closestProfilesAt(
            self,
            coord: LatLonCoordReader,
            query: QueryReader,
            _context: ClosestprofilesatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            ProfileClientListBuilder
            | ProfileClientListReader
            | Sequence[Any]
            | ClosestprofilesatResultTuple
            | None
        ]: ...
        def closestProfilesAt_context(
            self,
            context: ClosestprofilesatCallContext,
        ) -> Awaitable[None]: ...
        def streamAllProfiles(
            self,
            mandatory: PropertyNameEnumListReader,
            optional: PropertyNameEnumListReader,
            onlyRawData: bool,
            _context: StreamallprofilesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _ServiceInterfaceModule._StreamInterfaceModule.Server
            | StreamClient
            | StreamallprofilesResultTuple
            | None
        ]: ...
        def streamAllProfiles_context(
            self,
            context: StreamallprofilesCallContext,
        ) -> Awaitable[None]: ...

class NextprofilesRequest(Protocol):
    maxCount: int
    def send(self) -> NextprofilesResult: ...

class _ProfileClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> ProfileClient: ...
        @override
        def __iter__(self) -> Iterator[ProfileClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> ProfileClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: ProfileClient | _ProfileInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[ProfileClient]: ...

class NextprofilesResult(Awaitable[NextprofilesResult], Protocol):
    profiles: ProfileClientListReader

class NextprofilesServerResult(_DynamicStructBuilder):
    @property
    def profiles(self) -> ProfileClientListBuilder: ...
    @profiles.setter
    def profiles(
        self,
        value: ProfileClientListBuilder | ProfileClientListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["profiles"],
        size: int | None = None,
    ) -> ProfileClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class NextprofilesParams(Protocol):
    maxCount: int

class NextprofilesCallContext(Protocol):
    params: NextprofilesParams
    @property
    def results(self) -> NextprofilesServerResult: ...

class NextprofilesResultTuple(NamedTuple):
    profiles: ProfileClientListBuilder | ProfileClientListReader | Sequence[Any]

class StreamClient(_DynamicCapabilityClient):
    def nextProfiles(self, maxCount: int | None = None) -> NextprofilesResult: ...
    def nextProfiles_request(
        self,
        maxCount: int | None = None,
    ) -> NextprofilesRequest: ...

class CheckavailableparametersRequest(Protocol):
    mandatory: PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any]
    optional: PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any]
    onlyRawData: bool
    @overload
    def init(
        self,
        name: Literal["mandatory"],
        size: int = ...,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(
        self,
        name: Literal["optional"],
        size: int = ...,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> CheckavailableparametersResult: ...

class CheckavailableparametersResult(
    Awaitable[CheckavailableparametersResult],
    Protocol,
):
    failed: bool
    mandatory: PropertyNameEnumListReader
    optional: PropertyNameEnumListReader

class CheckavailableparametersCallContext(Protocol):
    params: QueryReader
    @property
    def results(self) -> ResultBuilder: ...

class CheckavailableparametersResultTuple(NamedTuple):
    failed: bool
    mandatory: PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any]
    optional: PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any]

class GetallavailableparametersRequest(Protocol):
    onlyRawData: bool
    def send(self) -> GetallavailableparametersResult: ...

class GetallavailableparametersResult(
    Awaitable[GetallavailableparametersResult],
    Protocol,
):
    mandatory: PropertyNameEnumListReader
    optional: PropertyNameEnumListReader

class GetallavailableparametersServerResult(_DynamicStructBuilder):
    @property
    def mandatory(self) -> PropertyNameEnumListBuilder: ...
    @mandatory.setter
    def mandatory(
        self,
        value: PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any],
    ) -> None: ...
    @property
    def optional(self) -> PropertyNameEnumListBuilder: ...
    @optional.setter
    def optional(
        self,
        value: PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["mandatory"],
        size: int | None = None,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["optional"],
        size: int | None = None,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class GetallavailableparametersParams(Protocol):
    onlyRawData: bool

class GetallavailableparametersCallContext(Protocol):
    params: GetallavailableparametersParams
    @property
    def results(self) -> GetallavailableparametersServerResult: ...

class GetallavailableparametersResultTuple(NamedTuple):
    mandatory: PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any]
    optional: PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any]

class ClosestprofilesatRequest(Protocol):
    coord: LatLonCoordBuilder
    query: QueryBuilder
    @overload
    def init(self, name: Literal["coord"]) -> LatLonCoordBuilder: ...
    @overload
    def init(self, name: Literal["query"]) -> QueryBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> ClosestprofilesatResult: ...

class ClosestprofilesatResult(Awaitable[ClosestprofilesatResult], Protocol):
    profiles: ProfileClientListReader

class ClosestprofilesatServerResult(_DynamicStructBuilder):
    @property
    def profiles(self) -> ProfileClientListBuilder: ...
    @profiles.setter
    def profiles(
        self,
        value: ProfileClientListBuilder | ProfileClientListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["profiles"],
        size: int | None = None,
    ) -> ProfileClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ClosestprofilesatParams(Protocol):
    coord: LatLonCoordReader
    query: QueryReader

class ClosestprofilesatCallContext(Protocol):
    params: ClosestprofilesatParams
    @property
    def results(self) -> ClosestprofilesatServerResult: ...

class ClosestprofilesatResultTuple(NamedTuple):
    profiles: ProfileClientListBuilder | ProfileClientListReader | Sequence[Any]

class StreamallprofilesRequest(Protocol):
    mandatory: PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any]
    optional: PropertyNameEnumListBuilder | PropertyNameEnumListReader | Sequence[Any]
    onlyRawData: bool
    @overload
    def init(
        self,
        name: Literal["mandatory"],
        size: int = ...,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(
        self,
        name: Literal["optional"],
        size: int = ...,
    ) -> PropertyNameEnumListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> StreamallprofilesResult: ...

class StreamallprofilesResult(Awaitable[StreamallprofilesResult], Protocol):
    allProfiles: StreamClient

class StreamallprofilesServerResult(_DynamicStructBuilder):
    @property
    def allProfiles(
        self,
    ) -> _ServiceInterfaceModule._StreamInterfaceModule.Server | StreamClient: ...
    @allProfiles.setter
    def allProfiles(
        self,
        value: _ServiceInterfaceModule._StreamInterfaceModule.Server | StreamClient,
    ) -> None: ...

class StreamallprofilesCallContext(Protocol):
    params: QueryReader
    @property
    def results(self) -> StreamallprofilesServerResult: ...

class StreamallprofilesResultTuple(NamedTuple):
    allProfiles: _ServiceInterfaceModule._StreamInterfaceModule.Server | StreamClient

class ServiceClient(IdentifiableClient, PersistentClient):
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
    ) -> CheckavailableparametersResult: ...
    def getAllAvailableParameters(
        self,
        onlyRawData: bool | None = None,
    ) -> GetallavailableparametersResult: ...
    def closestProfilesAt(
        self,
        coord: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any] | None = None,
        query: QueryBuilder | QueryReader | dict[str, Any] | None = None,
    ) -> ClosestprofilesatResult: ...
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
    ) -> StreamallprofilesResult: ...
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
    ) -> CheckavailableparametersRequest: ...
    def getAllAvailableParameters_request(
        self,
        onlyRawData: bool | None = None,
    ) -> GetallavailableparametersRequest: ...
    def closestProfilesAt_request(
        self,
        coord: LatLonCoordBuilder | None = None,
        query: QueryBuilder | None = None,
    ) -> ClosestprofilesatRequest: ...
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
    ) -> StreamallprofilesRequest: ...

Service: _ServiceInterfaceModule

# Top-level type aliases for use in type annotations
type LayerListBuilder = _LayerList.Builder
type LayerListReader = _LayerList.Reader
type ProfileClientListBuilder = _ProfileClientList.Builder
type ProfileClientListReader = _ProfileClientList.Reader
ProfileServer = _ProfileInterfaceModule.Server
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
type STypeEnum = int | Literal["unknown", "ka5"]
ServiceServer = _ServiceInterfaceModule.Server
StreamServer = _ServiceInterfaceModule._StreamInterfaceModule.Server
