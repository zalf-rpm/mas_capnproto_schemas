"""This is an automatically generated stub for `grid.capnp`."""

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

class _AggregationEnumModule:
    none: int
    wAvg: int
    wMedian: int
    min: int
    max: int
    sum: int
    iAvg: int
    iMedian: int
    avg: int
    median: int
    wSum: int
    iSum: int
    wMin: int
    iMin: int
    wMax: int
    iMax: int

class _GridInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _ValueStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            f: float | None = None,
            i: int | None = None,
            ui: int | None = None,
            no: bool | None = None,
            **kwargs: object,
        ) -> ValueBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[ValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ValueBuilder]: ...
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
        ) -> ValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> ValueReader: ...

    Value: _ValueStructModule
    class _ResolutionStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            meter: int | None = None,
            degree: float | None = None,
            **kwargs: object,
        ) -> ResolutionBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[ResolutionReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ResolutionReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ResolutionBuilder]: ...
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
        ) -> ResolutionReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> ResolutionReader: ...

    Resolution: _ResolutionStructModule
    class _RowColStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            row: int | None = None,
            col: int | None = None,
            **kwargs: object,
        ) -> RowColBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[RowColReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[RowColReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[RowColBuilder]: ...
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
        ) -> RowColReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> RowColReader: ...

    RowCol: _RowColStructModule
    class _AggregationPartStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            value: ValueBuilder | dict[str, Any] | None = None,
            rowCol: RowColBuilder | dict[str, Any] | None = None,
            areaFrac: float | None = None,
            iValue: float | None = None,
            **kwargs: object,
        ) -> AggregationPartBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[AggregationPartReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[AggregationPartReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[AggregationPartBuilder]: ...
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
        ) -> AggregationPartReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AggregationPartReader: ...

    AggregationPart: _AggregationPartStructModule
    class _LocationStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            latLonCoord: LatLonCoordBuilder | dict[str, Any] | None = None,
            rowCol: RowColBuilder | dict[str, Any] | None = None,
            value: ValueBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> LocationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[LocationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[LocationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[LocationBuilder]: ...
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
        ) -> LocationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> LocationReader: ...

    Location: _LocationStructModule
    class _CallbackInterfaceModule(_InterfaceModule):
        @override
        def _new_client(self, server: _DynamicCapabilityServer) -> CallbackClient: ...
        class Server(_DynamicCapabilityServer):
            def sendCells(
                self,
                maxCount: int,
                _context: SendcellsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                LocationListBuilder
                | LocationListReader
                | Sequence[Any]
                | SendcellsResultTuple
                | None
            ]: ...
            def sendCells_context(
                self,
                context: SendcellsCallContext,
            ) -> Awaitable[None]: ...

    Callback: _CallbackInterfaceModule
    type CallbackServer = _GridInterfaceModule._CallbackInterfaceModule.Server
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> GridClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def closestValueAt(
            self,
            latlonCoord: LatLonCoordReader,
            ignoreNoData: bool,
            resolution: ResolutionReader,
            agg: AggregationEnum,
            returnRowCols: bool,
            includeAggParts: bool,
            _context: ClosestvalueatCallContext,
            **kwargs: object,
        ) -> Awaitable[ClosestvalueatResultTuple | None]: ...
        def closestValueAt_context(
            self,
            context: ClosestvalueatCallContext,
        ) -> Awaitable[None]: ...
        def resolution(
            self,
            _context: ResolutionCallContext,
            **kwargs: object,
        ) -> Awaitable[
            ResolutionBuilder
            | ResolutionReader
            | dict[str, Any]
            | ResolutionResultTuple
            | None
        ]: ...
        def resolution_context(
            self,
            context: ResolutionCallContext,
        ) -> Awaitable[None]: ...
        def dimension(
            self,
            _context: DimensionCallContext,
            **kwargs: object,
        ) -> Awaitable[DimensionResultTuple | None]: ...
        def dimension_context(
            self,
            context: DimensionCallContext,
        ) -> Awaitable[None]: ...
        def noDataValue(
            self,
            _context: NodatavalueCallContext,
            **kwargs: object,
        ) -> Awaitable[
            ValueBuilder | ValueReader | dict[str, Any] | NodatavalueResultTuple | None
        ]: ...
        def noDataValue_context(
            self,
            context: NodatavalueCallContext,
        ) -> Awaitable[None]: ...
        def valueAt(
            self,
            row: int,
            col: int,
            resolution: ResolutionReader,
            agg: AggregationEnum,
            includeAggParts: bool,
            _context: ValueatCallContext,
            **kwargs: object,
        ) -> Awaitable[ValueatResultTuple | None]: ...
        def valueAt_context(self, context: ValueatCallContext) -> Awaitable[None]: ...
        def latLonBounds(
            self,
            useCellCenter: bool,
            _context: LatlonboundsCallContext,
            **kwargs: object,
        ) -> Awaitable[LatlonboundsResultTuple | None]: ...
        def latLonBounds_context(
            self,
            context: LatlonboundsCallContext,
        ) -> Awaitable[None]: ...
        def streamCells(
            self,
            topLeft: RowColReader,
            bottomRight: RowColReader,
            _context: StreamcellsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _GridInterfaceModule._CallbackInterfaceModule.Server
            | CallbackClient
            | StreamcellsResultTuple
            | None
        ]: ...
        def streamCells_context(
            self,
            context: StreamcellsCallContext,
        ) -> Awaitable[None]: ...
        def unit(
            self,
            _context: UnitCallContext,
            **kwargs: object,
        ) -> Awaitable[str | UnitResultTuple | None]: ...
        def unit_context(self, context: UnitCallContext) -> Awaitable[None]: ...

class ValueReader(_DynamicStructReader):
    @property
    def f(self) -> float: ...
    @property
    def i(self) -> int: ...
    @property
    def ui(self) -> int: ...
    @property
    def no(self) -> bool: ...
    @override
    def which(self) -> Literal["f", "i", "ui", "no"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ValueBuilder: ...

class ValueBuilder(_DynamicStructBuilder):
    @property
    def f(self) -> float: ...
    @f.setter
    def f(self, value: float) -> None: ...
    @property
    def i(self) -> int: ...
    @i.setter
    def i(self, value: int) -> None: ...
    @property
    def ui(self) -> int: ...
    @ui.setter
    def ui(self, value: int) -> None: ...
    @property
    def no(self) -> bool: ...
    @no.setter
    def no(self, value: bool) -> None: ...
    @override
    def which(self) -> Literal["f", "i", "ui", "no"]: ...
    @override
    def as_reader(self) -> ValueReader: ...

class ResolutionReader(_DynamicStructReader):
    @property
    def meter(self) -> int: ...
    @property
    def degree(self) -> float: ...
    @override
    def which(self) -> Literal["meter", "degree"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ResolutionBuilder: ...

class ResolutionBuilder(_DynamicStructBuilder):
    @property
    def meter(self) -> int: ...
    @meter.setter
    def meter(self, value: int) -> None: ...
    @property
    def degree(self) -> float: ...
    @degree.setter
    def degree(self, value: float) -> None: ...
    @override
    def which(self) -> Literal["meter", "degree"]: ...
    @override
    def as_reader(self) -> ResolutionReader: ...

class RowColReader(_DynamicStructReader):
    @property
    def row(self) -> int: ...
    @property
    def col(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> RowColBuilder: ...

class RowColBuilder(_DynamicStructBuilder):
    @property
    def row(self) -> int: ...
    @row.setter
    def row(self, value: int) -> None: ...
    @property
    def col(self) -> int: ...
    @col.setter
    def col(self, value: int) -> None: ...
    @override
    def as_reader(self) -> RowColReader: ...

class AggregationPartReader(_DynamicStructReader):
    @property
    def value(self) -> ValueReader: ...
    @property
    def rowCol(self) -> RowColReader: ...
    @property
    def areaFrac(self) -> float: ...
    @property
    def iValue(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> AggregationPartBuilder: ...

class AggregationPartBuilder(_DynamicStructBuilder):
    @property
    def value(self) -> ValueBuilder: ...
    @value.setter
    def value(self, value: ValueBuilder | ValueReader | dict[str, Any]) -> None: ...
    @property
    def rowCol(self) -> RowColBuilder: ...
    @rowCol.setter
    def rowCol(self, value: RowColBuilder | RowColReader | dict[str, Any]) -> None: ...
    @property
    def areaFrac(self) -> float: ...
    @areaFrac.setter
    def areaFrac(self, value: float) -> None: ...
    @property
    def iValue(self) -> float: ...
    @iValue.setter
    def iValue(self, value: float) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["value"],
        size: int | None = None,
    ) -> ValueBuilder: ...
    @overload
    def init(
        self,
        field: Literal["rowCol"],
        size: int | None = None,
    ) -> RowColBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> AggregationPartReader: ...

class LocationReader(_DynamicStructReader):
    @property
    def latLonCoord(self) -> LatLonCoordReader: ...
    @property
    def rowCol(self) -> RowColReader: ...
    @property
    def value(self) -> ValueReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> LocationBuilder: ...

class LocationBuilder(_DynamicStructBuilder):
    @property
    def latLonCoord(self) -> LatLonCoordBuilder: ...
    @latLonCoord.setter
    def latLonCoord(
        self,
        value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any],
    ) -> None: ...
    @property
    def rowCol(self) -> RowColBuilder: ...
    @rowCol.setter
    def rowCol(self, value: RowColBuilder | RowColReader | dict[str, Any]) -> None: ...
    @property
    def value(self) -> ValueBuilder: ...
    @value.setter
    def value(self, value: ValueBuilder | ValueReader | dict[str, Any]) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["latLonCoord"],
        size: int | None = None,
    ) -> LatLonCoordBuilder: ...
    @overload
    def init(
        self,
        field: Literal["rowCol"],
        size: int | None = None,
    ) -> RowColBuilder: ...
    @overload
    def init(
        self,
        field: Literal["value"],
        size: int | None = None,
    ) -> ValueBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> LocationReader: ...

class SendcellsRequest(Protocol):
    maxCount: int
    def send(self) -> SendcellsResult: ...

class _LocationList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> LocationReader: ...
        @override
        def __iter__(self) -> Iterator[LocationReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> LocationBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: LocationReader | LocationBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[LocationBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> LocationBuilder: ...

class SendcellsResult(Awaitable[SendcellsResult], Protocol):
    locations: LocationListReader

class SendcellsServerResult(_DynamicStructBuilder):
    @property
    def locations(self) -> LocationListBuilder: ...
    @locations.setter
    def locations(
        self,
        value: LocationListBuilder | LocationListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["locations"],
        size: int | None = None,
    ) -> LocationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class SendcellsParams(Protocol):
    maxCount: int

class SendcellsCallContext(Protocol):
    params: SendcellsParams
    @property
    def results(self) -> SendcellsServerResult: ...

class SendcellsResultTuple(NamedTuple):
    locations: LocationListBuilder | LocationListReader | Sequence[Any]

class CallbackClient(_DynamicCapabilityClient):
    def sendCells(self, maxCount: int | None = None) -> SendcellsResult: ...
    def sendCells_request(self, maxCount: int | None = None) -> SendcellsRequest: ...

class ClosestvalueatRequest(Protocol):
    latlonCoord: LatLonCoordBuilder
    ignoreNoData: bool
    resolution: ResolutionBuilder
    agg: AggregationEnum
    returnRowCols: bool
    includeAggParts: bool
    @overload
    def init(self, name: Literal["latlonCoord"]) -> LatLonCoordBuilder: ...
    @overload
    def init(self, name: Literal["resolution"]) -> ResolutionBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> ClosestvalueatResult: ...

class _AggregationPartList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> AggregationPartReader: ...
        @override
        def __iter__(self) -> Iterator[AggregationPartReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> AggregationPartBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: AggregationPartReader | AggregationPartBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[AggregationPartBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> AggregationPartBuilder: ...

class ClosestvalueatResult(Awaitable[ClosestvalueatResult], Protocol):
    val: ValueReader
    tl: RowColReader
    br: RowColReader
    aggParts: AggregationPartListReader

class ClosestvalueatServerResult(_DynamicStructBuilder):
    @property
    def val(self) -> ValueBuilder: ...
    @val.setter
    def val(self, value: ValueBuilder | ValueReader | dict[str, Any]) -> None: ...
    @property
    def tl(self) -> RowColBuilder: ...
    @tl.setter
    def tl(self, value: RowColBuilder | RowColReader | dict[str, Any]) -> None: ...
    @property
    def br(self) -> RowColBuilder: ...
    @br.setter
    def br(self, value: RowColBuilder | RowColReader | dict[str, Any]) -> None: ...
    @property
    def aggParts(self) -> AggregationPartListBuilder: ...
    @aggParts.setter
    def aggParts(
        self,
        value: AggregationPartListBuilder | AggregationPartListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(self, field: Literal["val"], size: int | None = None) -> ValueBuilder: ...
    @overload
    def init(self, field: Literal["tl"], size: int | None = None) -> RowColBuilder: ...
    @overload
    def init(self, field: Literal["br"], size: int | None = None) -> RowColBuilder: ...
    @overload
    def init(
        self,
        field: Literal["aggParts"],
        size: int | None = None,
    ) -> AggregationPartListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ClosestvalueatParams(Protocol):
    latlonCoord: LatLonCoordReader
    ignoreNoData: bool
    resolution: ResolutionReader
    agg: AggregationEnum
    returnRowCols: bool
    includeAggParts: bool

class ClosestvalueatCallContext(Protocol):
    params: ClosestvalueatParams
    @property
    def results(self) -> ClosestvalueatServerResult: ...

class ClosestvalueatResultTuple(NamedTuple):
    val: ValueBuilder | ValueReader | dict[str, Any]
    tl: RowColBuilder | RowColReader | dict[str, Any]
    br: RowColBuilder | RowColReader | dict[str, Any]
    aggParts: AggregationPartListBuilder | AggregationPartListReader | Sequence[Any]

class ResolutionRequest(Protocol):
    def send(self) -> ResolutionResult: ...

class ResolutionResult(Awaitable[ResolutionResult], Protocol):
    res: ResolutionReader

class ResolutionServerResult(_DynamicStructBuilder):
    @property
    def res(self) -> ResolutionBuilder: ...
    @res.setter
    def res(
        self,
        value: ResolutionBuilder | ResolutionReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["res"],
        size: int | None = None,
    ) -> ResolutionBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ResolutionParams(Protocol): ...

class ResolutionCallContext(Protocol):
    params: ResolutionParams
    @property
    def results(self) -> ResolutionServerResult: ...

class ResolutionResultTuple(NamedTuple):
    res: ResolutionBuilder | ResolutionReader | dict[str, Any]

class DimensionRequest(Protocol):
    def send(self) -> DimensionResult: ...

class DimensionResult(Awaitable[DimensionResult], Protocol):
    rows: int
    cols: int

class DimensionServerResult(_DynamicStructBuilder):
    @property
    def rows(self) -> int: ...
    @rows.setter
    def rows(self, value: int) -> None: ...
    @property
    def cols(self) -> int: ...
    @cols.setter
    def cols(self, value: int) -> None: ...

class DimensionParams(Protocol): ...

class DimensionCallContext(Protocol):
    params: DimensionParams
    @property
    def results(self) -> DimensionServerResult: ...

class DimensionResultTuple(NamedTuple):
    rows: int
    cols: int

class NodatavalueRequest(Protocol):
    def send(self) -> NodatavalueResult: ...

class NodatavalueResult(Awaitable[NodatavalueResult], Protocol):
    nodata: ValueReader

class NodatavalueServerResult(_DynamicStructBuilder):
    @property
    def nodata(self) -> ValueBuilder: ...
    @nodata.setter
    def nodata(self, value: ValueBuilder | ValueReader | dict[str, Any]) -> None: ...
    @overload
    def init(
        self,
        field: Literal["nodata"],
        size: int | None = None,
    ) -> ValueBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class NodatavalueParams(Protocol): ...

class NodatavalueCallContext(Protocol):
    params: NodatavalueParams
    @property
    def results(self) -> NodatavalueServerResult: ...

class NodatavalueResultTuple(NamedTuple):
    nodata: ValueBuilder | ValueReader | dict[str, Any]

class ValueatRequest(Protocol):
    row: int
    col: int
    resolution: ResolutionBuilder
    agg: AggregationEnum
    includeAggParts: bool
    @overload
    def init(self, name: Literal["resolution"]) -> ResolutionBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> ValueatResult: ...

class ValueatResult(Awaitable[ValueatResult], Protocol):
    val: ValueReader
    aggParts: AggregationPartListReader

class ValueatServerResult(_DynamicStructBuilder):
    @property
    def val(self) -> ValueBuilder: ...
    @val.setter
    def val(self, value: ValueBuilder | ValueReader | dict[str, Any]) -> None: ...
    @property
    def aggParts(self) -> AggregationPartListBuilder: ...
    @aggParts.setter
    def aggParts(
        self,
        value: AggregationPartListBuilder | AggregationPartListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(self, field: Literal["val"], size: int | None = None) -> ValueBuilder: ...
    @overload
    def init(
        self,
        field: Literal["aggParts"],
        size: int | None = None,
    ) -> AggregationPartListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ValueatParams(Protocol):
    row: int
    col: int
    resolution: ResolutionReader
    agg: AggregationEnum
    includeAggParts: bool

class ValueatCallContext(Protocol):
    params: ValueatParams
    @property
    def results(self) -> ValueatServerResult: ...

class ValueatResultTuple(NamedTuple):
    val: ValueBuilder | ValueReader | dict[str, Any]
    aggParts: AggregationPartListBuilder | AggregationPartListReader | Sequence[Any]

class LatlonboundsRequest(Protocol):
    useCellCenter: bool
    def send(self) -> LatlonboundsResult: ...

class LatlonboundsResult(Awaitable[LatlonboundsResult], Protocol):
    tl: LatLonCoordReader
    tr: LatLonCoordReader
    br: LatLonCoordReader
    bl: LatLonCoordReader

class LatlonboundsServerResult(_DynamicStructBuilder):
    @property
    def tl(self) -> LatLonCoordBuilder: ...
    @tl.setter
    def tl(
        self,
        value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any],
    ) -> None: ...
    @property
    def tr(self) -> LatLonCoordBuilder: ...
    @tr.setter
    def tr(
        self,
        value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any],
    ) -> None: ...
    @property
    def br(self) -> LatLonCoordBuilder: ...
    @br.setter
    def br(
        self,
        value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any],
    ) -> None: ...
    @property
    def bl(self) -> LatLonCoordBuilder: ...
    @bl.setter
    def bl(
        self,
        value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["tl"],
        size: int | None = None,
    ) -> LatLonCoordBuilder: ...
    @overload
    def init(
        self,
        field: Literal["tr"],
        size: int | None = None,
    ) -> LatLonCoordBuilder: ...
    @overload
    def init(
        self,
        field: Literal["br"],
        size: int | None = None,
    ) -> LatLonCoordBuilder: ...
    @overload
    def init(
        self,
        field: Literal["bl"],
        size: int | None = None,
    ) -> LatLonCoordBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class LatlonboundsParams(Protocol):
    useCellCenter: bool

class LatlonboundsCallContext(Protocol):
    params: LatlonboundsParams
    @property
    def results(self) -> LatlonboundsServerResult: ...

class LatlonboundsResultTuple(NamedTuple):
    tl: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]
    tr: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]
    br: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]
    bl: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]

class StreamcellsRequest(Protocol):
    topLeft: RowColBuilder
    bottomRight: RowColBuilder
    @overload
    def init(self, name: Literal["topLeft"]) -> RowColBuilder: ...
    @overload
    def init(self, name: Literal["bottomRight"]) -> RowColBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> StreamcellsResult: ...

class StreamcellsResult(Awaitable[StreamcellsResult], Protocol):
    callback: CallbackClient

class StreamcellsServerResult(_DynamicStructBuilder):
    @property
    def callback(
        self,
    ) -> _GridInterfaceModule._CallbackInterfaceModule.Server | CallbackClient: ...
    @callback.setter
    def callback(
        self,
        value: _GridInterfaceModule._CallbackInterfaceModule.Server | CallbackClient,
    ) -> None: ...

class StreamcellsParams(Protocol):
    topLeft: RowColReader
    bottomRight: RowColReader

class StreamcellsCallContext(Protocol):
    params: StreamcellsParams
    @property
    def results(self) -> StreamcellsServerResult: ...

class StreamcellsResultTuple(NamedTuple):
    callback: _GridInterfaceModule._CallbackInterfaceModule.Server | CallbackClient

class UnitRequest(Protocol):
    def send(self) -> UnitResult: ...

class UnitResult(Awaitable[UnitResult], Protocol):
    unit: str

class UnitServerResult(_DynamicStructBuilder):
    @property
    def unit(self) -> str: ...
    @unit.setter
    def unit(self, value: str) -> None: ...

class UnitParams(Protocol): ...

class UnitCallContext(Protocol):
    params: UnitParams
    @property
    def results(self) -> UnitServerResult: ...

class UnitResultTuple(NamedTuple):
    unit: str

class GridClient(IdentifiableClient, PersistentClient):
    def closestValueAt(
        self,
        latlonCoord: LatLonCoordBuilder
        | LatLonCoordReader
        | dict[str, Any]
        | None = None,
        ignoreNoData: bool | None = None,
        resolution: ResolutionBuilder | ResolutionReader | dict[str, Any] | None = None,
        agg: AggregationEnum | None = None,
        returnRowCols: bool | None = None,
        includeAggParts: bool | None = None,
    ) -> ClosestvalueatResult: ...
    def resolution(self) -> ResolutionResult: ...
    def dimension(self) -> DimensionResult: ...
    def noDataValue(self) -> NodatavalueResult: ...
    def valueAt(
        self,
        row: int | None = None,
        col: int | None = None,
        resolution: ResolutionBuilder | ResolutionReader | dict[str, Any] | None = None,
        agg: AggregationEnum | None = None,
        includeAggParts: bool | None = None,
    ) -> ValueatResult: ...
    def latLonBounds(self, useCellCenter: bool | None = None) -> LatlonboundsResult: ...
    def streamCells(
        self,
        topLeft: RowColBuilder | RowColReader | dict[str, Any] | None = None,
        bottomRight: RowColBuilder | RowColReader | dict[str, Any] | None = None,
    ) -> StreamcellsResult: ...
    def unit(self) -> UnitResult: ...
    def closestValueAt_request(
        self,
        latlonCoord: LatLonCoordBuilder | None = None,
        ignoreNoData: bool | None = None,
        resolution: ResolutionBuilder | None = None,
        agg: AggregationEnum | None = None,
        returnRowCols: bool | None = None,
        includeAggParts: bool | None = None,
    ) -> ClosestvalueatRequest: ...
    def resolution_request(self) -> ResolutionRequest: ...
    def dimension_request(self) -> DimensionRequest: ...
    def noDataValue_request(self) -> NodatavalueRequest: ...
    def valueAt_request(
        self,
        row: int | None = None,
        col: int | None = None,
        resolution: ResolutionBuilder | None = None,
        agg: AggregationEnum | None = None,
        includeAggParts: bool | None = None,
    ) -> ValueatRequest: ...
    def latLonBounds_request(
        self,
        useCellCenter: bool | None = None,
    ) -> LatlonboundsRequest: ...
    def streamCells_request(
        self,
        topLeft: RowColBuilder | None = None,
        bottomRight: RowColBuilder | None = None,
    ) -> StreamcellsRequest: ...
    def unit_request(self) -> UnitRequest: ...

Grid: _GridInterfaceModule

# Top-level type aliases for use in type annotations
type AggregationEnum = (
    int
    | Literal[
        "none",
        "wAvg",
        "wMedian",
        "min",
        "max",
        "sum",
        "iAvg",
        "iMedian",
        "avg",
        "median",
        "wSum",
        "iSum",
        "wMin",
        "iMin",
        "wMax",
        "iMax",
    ]
)
type AggregationPartListBuilder = _AggregationPartList.Builder
type AggregationPartListReader = _AggregationPartList.Reader
CallbackServer = _GridInterfaceModule._CallbackInterfaceModule.Server
GridServer = _GridInterfaceModule.Server
type LocationListBuilder = _LocationList.Builder
type LocationListReader = _LocationList.Reader
