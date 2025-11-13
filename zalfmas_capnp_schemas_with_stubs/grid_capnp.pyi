"""This is an automatically generated stub for `grid.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
from contextlib import contextmanager
from enum import Enum
from io import BufferedWriter
from typing import (
    Any,
    BinaryIO,
    Literal,
    NamedTuple,
    Protocol,
    Self,
    TypeAlias,
    overload,
)

from .common_capnp import Identifiable, IdentifiableClient
from .geo_capnp import LatLonCoord
from .persistence_capnp import Persistent, PersistentClient

class Aggregation(Enum):
    none = "none"
    wAvg = "wAvg"
    wMedian = "wMedian"
    min = "min"
    max = "max"
    sum = "sum"
    iAvg = "iAvg"
    iMedian = "iMedian"
    avg = "avg"
    median = "median"
    wSum = "wSum"
    iSum = "iSum"
    wMin = "wMin"
    iMin = "iMin"
    wMax = "wMax"
    iMax = "iMax"

class Grid:
    ValueBuilder: TypeAlias = Value.Builder
    ValueReader: TypeAlias = Value.Reader
    class Value:
        class Reader:
            @property
            def f(self) -> float: ...
            @property
            def i(self) -> int: ...
            @property
            def ui(self) -> int: ...
            @property
            def no(self) -> bool: ...
            def which(self) -> Literal["f", "i", "ui", "no"]: ...
            def as_builder(self) -> Grid.Value.Builder: ...

        class Builder:
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
            def which(self) -> Literal["f", "i", "ui", "no"]: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Grid.Value.Builder: ...
            def copy(self) -> Grid.Value.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Grid.Value.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def which(self) -> Literal["f", "i", "ui", "no"]: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Grid.Value.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.Value.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            f: float | None = None,
            i: int | None = None,
            ui: int | None = None,
            no: bool | None = None,
        ) -> Grid.Value.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.Value.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.Value.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    ResolutionBuilder: TypeAlias = Resolution.Builder
    ResolutionReader: TypeAlias = Resolution.Reader
    class Resolution:
        class Reader:
            @property
            def meter(self) -> int: ...
            @property
            def degree(self) -> float: ...
            def which(self) -> Literal["meter", "degree"]: ...
            def as_builder(self) -> Grid.Resolution.Builder: ...

        class Builder:
            @property
            def meter(self) -> int: ...
            @meter.setter
            def meter(self, value: int) -> None: ...
            @property
            def degree(self) -> float: ...
            @degree.setter
            def degree(self, value: float) -> None: ...
            def which(self) -> Literal["meter", "degree"]: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Grid.Resolution.Builder: ...
            def copy(self) -> Grid.Resolution.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Grid.Resolution.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def which(self) -> Literal["meter", "degree"]: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Grid.Resolution.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.Resolution.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            meter: int | None = None,
            degree: float | None = None,
        ) -> Grid.Resolution.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.Resolution.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.Resolution.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    RowColBuilder: TypeAlias = RowCol.Builder
    RowColReader: TypeAlias = RowCol.Reader
    class RowCol:
        class Reader:
            @property
            def row(self) -> int: ...
            @property
            def col(self) -> int: ...
            def as_builder(self) -> Grid.RowCol.Builder: ...

        class Builder:
            @property
            def row(self) -> int: ...
            @row.setter
            def row(self, value: int) -> None: ...
            @property
            def col(self) -> int: ...
            @col.setter
            def col(self, value: int) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Grid.RowCol.Builder: ...
            def copy(self) -> Grid.RowCol.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Grid.RowCol.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Grid.RowCol.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.RowCol.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            row: int | None = None,
            col: int | None = None,
        ) -> Grid.RowCol.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.RowCol.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.RowCol.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    AggregationPartBuilder: TypeAlias = AggregationPart.Builder
    AggregationPartReader: TypeAlias = AggregationPart.Reader
    class AggregationPart:
        class Reader:
            @property
            def value(self) -> Grid.Value.Reader: ...
            @property
            def rowCol(self) -> Grid.RowCol.Reader: ...
            @property
            def areaFrac(self) -> float: ...
            @property
            def iValue(self) -> float: ...
            def as_builder(self) -> Grid.AggregationPart.Builder: ...

        class Builder:
            @property
            def value(self) -> Grid.Value.Builder: ...
            @value.setter
            def value(
                self, value: Grid.Value.Builder | Grid.Value.Reader | dict[str, Any]
            ) -> None: ...
            @property
            def rowCol(self) -> Grid.RowCol.Builder: ...
            @rowCol.setter
            def rowCol(
                self, value: Grid.RowCol.Builder | Grid.RowCol.Reader | dict[str, Any]
            ) -> None: ...
            @property
            def areaFrac(self) -> float: ...
            @areaFrac.setter
            def areaFrac(self, value: float) -> None: ...
            @property
            def iValue(self) -> float: ...
            @iValue.setter
            def iValue(self, value: float) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Grid.AggregationPart.Builder: ...
            @overload
            def init(self: Any, name: Literal["value"]) -> Grid.Value.Builder: ...
            @overload
            def init(self: Any, name: Literal["rowCol"]) -> Grid.RowCol.Builder: ...
            def init(self: Any, name: str, size: int = ...) -> Any: ...
            def copy(self) -> Grid.AggregationPart.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Grid.AggregationPart.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @overload
        def init(self, name: Literal["value"]) -> Grid.Value: ...
        @overload
        def init(self, name: Literal["rowCol"]) -> Grid.RowCol: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Grid.AggregationPart.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.AggregationPart.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            value: Grid.Value.Builder | dict[str, Any] | None = None,
            rowCol: Grid.RowCol.Builder | dict[str, Any] | None = None,
            areaFrac: float | None = None,
            iValue: float | None = None,
        ) -> Grid.AggregationPart.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.AggregationPart.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.AggregationPart.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    LocationBuilder: TypeAlias = Location.Builder
    LocationReader: TypeAlias = Location.Reader
    class Location:
        class Reader:
            @property
            def latLonCoord(self) -> LatLonCoord.Reader: ...
            @property
            def rowCol(self) -> Grid.RowCol.Reader: ...
            @property
            def value(self) -> Grid.Value.Reader: ...
            def as_builder(self) -> Grid.Location.Builder: ...

        class Builder:
            @property
            def latLonCoord(self) -> LatLonCoord.Builder: ...
            @latLonCoord.setter
            def latLonCoord(
                self, value: LatLonCoord.Builder | LatLonCoord.Reader | dict[str, Any]
            ) -> None: ...
            @property
            def rowCol(self) -> Grid.RowCol.Builder: ...
            @rowCol.setter
            def rowCol(
                self, value: Grid.RowCol.Builder | Grid.RowCol.Reader | dict[str, Any]
            ) -> None: ...
            @property
            def value(self) -> Grid.Value.Builder: ...
            @value.setter
            def value(
                self, value: Grid.Value.Builder | Grid.Value.Reader | dict[str, Any]
            ) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Grid.Location.Builder: ...
            @overload
            def init(
                self: Any, name: Literal["latLonCoord"]
            ) -> LatLonCoord.Builder: ...
            @overload
            def init(self: Any, name: Literal["rowCol"]) -> Grid.RowCol.Builder: ...
            @overload
            def init(self: Any, name: Literal["value"]) -> Grid.Value.Builder: ...
            def init(self: Any, name: str, size: int = ...) -> Any: ...
            def copy(self) -> Grid.Location.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Grid.Location.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @overload
        def init(self, name: Literal["latLonCoord"]) -> LatLonCoord: ...
        @overload
        def init(self, name: Literal["rowCol"]) -> Grid.RowCol: ...
        @overload
        def init(self, name: Literal["value"]) -> Grid.Value: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Grid.Location.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.Location.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            latLonCoord: LatLonCoord.Builder | dict[str, Any] | None = None,
            rowCol: Grid.RowCol.Builder | dict[str, Any] | None = None,
            value: Grid.Value.Builder | dict[str, Any] | None = None,
        ) -> Grid.Location.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.Location.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Grid.Location.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Callback:
        class SendcellsRequest(Protocol):
            maxCount: int
            def send(self) -> Grid.Callback.SendcellsResult: ...

        class SendcellsResult(Awaitable[SendcellsResult], Protocol):
            locations: Sequence[Grid.Location.Builder | Grid.Location.Reader]

        @classmethod
        def _new_client(cls, server: Grid.Callback.Server) -> "Grid.CallbackClient": ...
        class Server(Protocol):
            class SendcellsResultTuple(NamedTuple):
                locations: Sequence[Grid.Location]

            class SendcellsCallContext(Protocol):
                results: Grid.Callback.SendcellsResult

            def sendCells(
                self,
                maxCount: int,
                _context: Grid.Callback.Server.SendcellsCallContext,
                **kwargs: Any,
            ) -> Awaitable[Grid.Callback.Server.SendcellsResultTuple | None]: ...
            def __enter__(self) -> Self: ...
            def __exit__(self, *args: Any) -> None: ...

    class CallbackClient(Protocol):
        def sendCells(
            self, maxCount: int | None = None
        ) -> Grid.Callback.SendcellsResult: ...
        def sendCells_request(
            self, maxCount: int | None = None
        ) -> Grid.Callback.SendcellsRequest: ...

    class ClosestvalueatRequest(Protocol):
        latlonCoord: LatLonCoord.Builder
        ignoreNoData: bool
        resolution: Grid.Resolution.Builder
        agg: (
            Aggregation
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
        returnRowCols: bool
        includeAggParts: bool
        @overload
        def init(self, name: Literal["latlonCoord"]) -> LatLonCoord.Builder: ...
        @overload
        def init(self, name: Literal["resolution"]) -> Grid.Resolution.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Grid.ClosestvalueatResult: ...

    class ClosestvalueatResult(Awaitable[ClosestvalueatResult], Protocol):
        val: Grid.Value.Builder | Grid.Value.Reader
        tl: Grid.RowCol.Builder | Grid.RowCol.Reader
        br: Grid.RowCol.Builder | Grid.RowCol.Reader
        aggParts: Sequence[Grid.AggregationPart.Builder | Grid.AggregationPart.Reader]

    class ResolutionRequest(Protocol):
        def send(self) -> Grid.ResolutionResult: ...

    class ResolutionResult(Awaitable[ResolutionResult], Protocol):
        res: Grid.Resolution.Builder | Grid.Resolution.Reader

    class DimensionRequest(Protocol):
        def send(self) -> Grid.DimensionResult: ...

    class DimensionResult(Awaitable[DimensionResult], Protocol):
        rows: int
        cols: int

    class NodatavalueRequest(Protocol):
        def send(self) -> Grid.NodatavalueResult: ...

    class NodatavalueResult(Awaitable[NodatavalueResult], Protocol):
        nodata: Grid.Value.Builder | Grid.Value.Reader

    class ValueatRequest(Protocol):
        row: int
        col: int
        resolution: Grid.Resolution.Builder
        agg: (
            Aggregation
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
        includeAggParts: bool
        @overload
        def init(self, name: Literal["resolution"]) -> Grid.Resolution.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Grid.ValueatResult: ...

    class ValueatResult(Awaitable[ValueatResult], Protocol):
        val: Grid.Value.Builder | Grid.Value.Reader
        aggParts: Sequence[Grid.AggregationPart.Builder | Grid.AggregationPart.Reader]

    class LatlonboundsRequest(Protocol):
        useCellCenter: bool
        def send(self) -> Grid.LatlonboundsResult: ...

    class LatlonboundsResult(Awaitable[LatlonboundsResult], Protocol):
        tl: LatLonCoord.Builder | LatLonCoord.Reader
        tr: LatLonCoord.Builder | LatLonCoord.Reader
        br: LatLonCoord.Builder | LatLonCoord.Reader
        bl: LatLonCoord.Builder | LatLonCoord.Reader

    class StreamcellsRequest(Protocol):
        topLeft: Grid.RowCol.Builder
        bottomRight: Grid.RowCol.Builder
        @overload
        def init(self, name: Literal["topLeft"]) -> Grid.RowCol.Builder: ...
        @overload
        def init(self, name: Literal["bottomRight"]) -> Grid.RowCol.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Grid.StreamcellsResult: ...

    class StreamcellsResult(Awaitable[StreamcellsResult], Protocol):
        callback: Grid.CallbackClient

    class UnitRequest(Protocol):
        def send(self) -> Grid.UnitResult: ...

    class UnitResult(Awaitable[UnitResult], Protocol):
        unit: str

    @classmethod
    def _new_client(
        cls, server: Grid.Server | Identifiable.Server | Persistent.Server
    ) -> "GridClient": ...
    class Server(Identifiable.Server, Persistent.Server):
        class ClosestvalueatResultTuple(NamedTuple):
            val: Grid.Value.Builder | Grid.Value.Reader
            tl: Grid.RowCol.Builder | Grid.RowCol.Reader
            br: Grid.RowCol.Builder | Grid.RowCol.Reader
            aggParts: Sequence[Grid.AggregationPart]

        class ResolutionResultTuple(NamedTuple):
            res: Grid.Resolution.Builder | Grid.Resolution.Reader

        class DimensionResultTuple(NamedTuple):
            rows: int
            cols: int

        class NodatavalueResultTuple(NamedTuple):
            nodata: Grid.Value.Builder | Grid.Value.Reader

        class ValueatResultTuple(NamedTuple):
            val: Grid.Value.Builder | Grid.Value.Reader
            aggParts: Sequence[Grid.AggregationPart]

        class LatlonboundsResultTuple(NamedTuple):
            tl: LatLonCoord.Builder | LatLonCoord.Reader
            tr: LatLonCoord.Builder | LatLonCoord.Reader
            br: LatLonCoord.Builder | LatLonCoord.Reader
            bl: LatLonCoord.Builder | LatLonCoord.Reader

        class StreamcellsResultTuple(NamedTuple):
            callback: Grid.Callback.Server

        class UnitResultTuple(NamedTuple):
            unit: str

        class ClosestvalueatCallContext(Protocol):
            results: Grid.ClosestvalueatResult

        class ResolutionCallContext(Protocol):
            results: Grid.ResolutionResult

        class DimensionCallContext(Protocol):
            results: Grid.DimensionResult

        class NodatavalueCallContext(Protocol):
            results: Grid.NodatavalueResult

        class ValueatCallContext(Protocol):
            results: Grid.ValueatResult

        class LatlonboundsCallContext(Protocol):
            results: Grid.LatlonboundsResult

        class StreamcellsCallContext(Protocol):
            results: Grid.StreamcellsResult

        class UnitCallContext(Protocol):
            results: Grid.UnitResult

        def closestValueAt(
            self,
            latlonCoord: LatLonCoord.Reader,
            ignoreNoData: bool,
            resolution: Grid.Resolution.Reader,
            agg: Aggregation
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
            ],
            returnRowCols: bool,
            includeAggParts: bool,
            _context: Grid.Server.ClosestvalueatCallContext,
            **kwargs: Any,
        ) -> Awaitable[Grid.Server.ClosestvalueatResultTuple | None]: ...
        def resolution(
            self, _context: Grid.Server.ResolutionCallContext, **kwargs: Any
        ) -> Awaitable[Grid.Server.ResolutionResultTuple | None]: ...
        def dimension(
            self, _context: Grid.Server.DimensionCallContext, **kwargs: Any
        ) -> Awaitable[Grid.Server.DimensionResultTuple | None]: ...
        def noDataValue(
            self, _context: Grid.Server.NodatavalueCallContext, **kwargs: Any
        ) -> Awaitable[Grid.Server.NodatavalueResultTuple | None]: ...
        def valueAt(
            self,
            row: int,
            col: int,
            resolution: Grid.Resolution.Reader,
            agg: Aggregation
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
            ],
            includeAggParts: bool,
            _context: Grid.Server.ValueatCallContext,
            **kwargs: Any,
        ) -> Awaitable[Grid.Server.ValueatResultTuple | None]: ...
        def latLonBounds(
            self,
            useCellCenter: bool,
            _context: Grid.Server.LatlonboundsCallContext,
            **kwargs: Any,
        ) -> Awaitable[Grid.Server.LatlonboundsResultTuple | None]: ...
        def streamCells(
            self,
            topLeft: Grid.RowCol.Reader,
            bottomRight: Grid.RowCol.Reader,
            _context: Grid.Server.StreamcellsCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            Grid.Callback.Server | Grid.Server.StreamcellsResultTuple | None
        ]: ...
        def unit(
            self, _context: Grid.Server.UnitCallContext, **kwargs: Any
        ) -> Awaitable[str | Grid.Server.UnitResultTuple | None]: ...
        def __enter__(self) -> Self: ...
        def __exit__(self, *args: Any) -> None: ...

class GridClient(IdentifiableClient, PersistentClient):
    def closestValueAt(
        self,
        latlonCoord: LatLonCoord | dict[str, Any] | None = None,
        ignoreNoData: bool | None = None,
        resolution: Grid.Resolution | dict[str, Any] | None = None,
        agg: Aggregation
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
        | None = None,
        returnRowCols: bool | None = None,
        includeAggParts: bool | None = None,
    ) -> Grid.ClosestvalueatResult: ...
    def resolution(self) -> Grid.ResolutionResult: ...
    def dimension(self) -> Grid.DimensionResult: ...
    def noDataValue(self) -> Grid.NodatavalueResult: ...
    def valueAt(
        self,
        row: int | None = None,
        col: int | None = None,
        resolution: Grid.Resolution | dict[str, Any] | None = None,
        agg: Aggregation
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
        | None = None,
        includeAggParts: bool | None = None,
    ) -> Grid.ValueatResult: ...
    def latLonBounds(
        self, useCellCenter: bool | None = None
    ) -> Grid.LatlonboundsResult: ...
    def streamCells(
        self,
        topLeft: Grid.RowCol | dict[str, Any] | None = None,
        bottomRight: Grid.RowCol | dict[str, Any] | None = None,
    ) -> Grid.StreamcellsResult: ...
    def unit(self) -> Grid.UnitResult: ...
    def closestValueAt_request(
        self,
        latlonCoord: LatLonCoord.Builder | None = None,
        ignoreNoData: bool | None = None,
        resolution: Grid.Resolution.Builder | None = None,
        agg: Aggregation
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
        | None = None,
        returnRowCols: bool | None = None,
        includeAggParts: bool | None = None,
    ) -> Grid.ClosestvalueatRequest: ...
    def resolution_request(self) -> Grid.ResolutionRequest: ...
    def dimension_request(self) -> Grid.DimensionRequest: ...
    def noDataValue_request(self) -> Grid.NodatavalueRequest: ...
    def valueAt_request(
        self,
        row: int | None = None,
        col: int | None = None,
        resolution: Grid.Resolution.Builder | None = None,
        agg: Aggregation
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
        | None = None,
        includeAggParts: bool | None = None,
    ) -> Grid.ValueatRequest: ...
    def latLonBounds_request(
        self, useCellCenter: bool | None = None
    ) -> Grid.LatlonboundsRequest: ...
    def streamCells_request(
        self,
        topLeft: Grid.RowCol.Builder | None = None,
        bottomRight: Grid.RowCol.Builder | None = None,
    ) -> Grid.StreamcellsRequest: ...
    def unit_request(self) -> Grid.UnitRequest: ...
