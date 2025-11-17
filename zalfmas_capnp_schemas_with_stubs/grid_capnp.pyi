"""This is an automatically generated stub for `grid.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

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
from .geo_capnp import _LatLonCoordModule
from .persistence_capnp import Persistent, PersistentClient, _PersistentModule

class _AggregationModule:
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

class _GridModule(_IdentifiableModule, _PersistentModule):
    class _ValueModule(_StructModule):
        class Reader(_DynamicStructReader):
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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> ValueBuilder: ...

        class Builder(_DynamicStructBuilder):
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

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, f: float | None = None, i: int | None = None, ui: int | None = None, no: bool | None = None, **kwargs: Any) -> ValueBuilder: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> AbstractContextManager[ValueReader]: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ..., *, builder: Literal[False]) -> AbstractContextManager[ValueReader]: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ..., *, builder: Literal[True]) -> AbstractContextManager[ValueBuilder]: ...
        def from_bytes_packed(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> _DynamicStructReader: ...
        @override
        def read(self, file: IO[str] | IO[bytes], traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> ValueReader: ...
        @override
        def read_packed(self, file: IO[str] | IO[bytes], traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> ValueReader: ...

    type ValueReader = _ValueModule.Reader
    type ValueBuilder = _ValueModule.Builder
    Value: _ValueModule
    class _ResolutionModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def meter(self) -> int: ...
            @property
            def degree(self) -> float: ...
            @override
            def which(self) -> Literal["meter", "degree"]: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> ResolutionBuilder: ...

        class Builder(_DynamicStructBuilder):
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

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, meter: int | None = None, degree: float | None = None, **kwargs: Any) -> ResolutionBuilder: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> AbstractContextManager[ResolutionReader]: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ..., *, builder: Literal[False]) -> AbstractContextManager[ResolutionReader]: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ..., *, builder: Literal[True]) -> AbstractContextManager[ResolutionBuilder]: ...
        def from_bytes_packed(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> _DynamicStructReader: ...
        @override
        def read(self, file: IO[str] | IO[bytes], traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> ResolutionReader: ...
        @override
        def read_packed(self, file: IO[str] | IO[bytes], traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> ResolutionReader: ...

    type ResolutionReader = _ResolutionModule.Reader
    type ResolutionBuilder = _ResolutionModule.Builder
    Resolution: _ResolutionModule
    class _RowColModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def row(self) -> int: ...
            @property
            def col(self) -> int: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> RowColBuilder: ...

        class Builder(_DynamicStructBuilder):
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

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, row: int | None = None, col: int | None = None, **kwargs: Any) -> RowColBuilder: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> AbstractContextManager[RowColReader]: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ..., *, builder: Literal[False]) -> AbstractContextManager[RowColReader]: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ..., *, builder: Literal[True]) -> AbstractContextManager[RowColBuilder]: ...
        def from_bytes_packed(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> _DynamicStructReader: ...
        @override
        def read(self, file: IO[str] | IO[bytes], traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> RowColReader: ...
        @override
        def read_packed(self, file: IO[str] | IO[bytes], traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> RowColReader: ...

    type RowColReader = _RowColModule.Reader
    type RowColBuilder = _RowColModule.Builder
    RowCol: _RowColModule
    class _AggregationPartModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def value(self) -> ValueReader: ...
            @property
            def rowCol(self) -> RowColReader: ...
            @property
            def areaFrac(self) -> float: ...
            @property
            def iValue(self) -> float: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> AggregationPartBuilder: ...

        class Builder(_DynamicStructBuilder):
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
            @overload
            def init(self, field: Literal["value"], size: int | None = None) -> ValueBuilder: ...
            @overload
            def init(self, field: Literal["rowCol"], size: int | None = None) -> RowColBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> AggregationPartReader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, value: ValueBuilder | dict[str, Any] | None = None, rowCol: RowColBuilder | dict[str, Any] | None = None, areaFrac: float | None = None, iValue: float | None = None, **kwargs: Any) -> AggregationPartBuilder: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> AbstractContextManager[AggregationPartReader]: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ..., *, builder: Literal[False]) -> AbstractContextManager[AggregationPartReader]: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ..., *, builder: Literal[True]) -> AbstractContextManager[AggregationPartBuilder]: ...
        def from_bytes_packed(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> _DynamicStructReader: ...
        @override
        def read(self, file: IO[str] | IO[bytes], traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> AggregationPartReader: ...
        @override
        def read_packed(self, file: IO[str] | IO[bytes], traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> AggregationPartReader: ...

    type AggregationPartReader = _AggregationPartModule.Reader
    type AggregationPartBuilder = _AggregationPartModule.Builder
    AggregationPart: _AggregationPartModule
    class _LocationModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def latLonCoord(self) -> _LatLonCoordModule.Reader: ...
            @property
            def rowCol(self) -> RowColReader: ...
            @property
            def value(self) -> ValueReader: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> LocationBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def latLonCoord(self) -> _LatLonCoordModule.Builder: ...
            @latLonCoord.setter
            def latLonCoord(self, value: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader | dict[str, Any]) -> None: ...
            @property
            def rowCol(self) -> RowColBuilder: ...
            @rowCol.setter
            def rowCol(self, value: RowColBuilder | RowColReader | dict[str, Any]) -> None: ...
            @property
            def value(self) -> ValueBuilder: ...
            @value.setter
            def value(self, value: ValueBuilder | ValueReader | dict[str, Any]) -> None: ...
            @overload
            def init(self, field: Literal["latLonCoord"], size: int | None = None) -> _LatLonCoordModule.Builder: ...
            @overload
            def init(self, field: Literal["rowCol"], size: int | None = None) -> RowColBuilder: ...
            @overload
            def init(self, field: Literal["value"], size: int | None = None) -> ValueBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> LocationReader: ...

        @override
        def new_message(
            self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, latLonCoord: _LatLonCoordModule.Builder | dict[str, Any] | None = None, rowCol: RowColBuilder | dict[str, Any] | None = None, value: ValueBuilder | dict[str, Any] | None = None, **kwargs: Any
        ) -> LocationBuilder: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> AbstractContextManager[LocationReader]: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ..., *, builder: Literal[False]) -> AbstractContextManager[LocationReader]: ...
        @overload
        def from_bytes(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ..., *, builder: Literal[True]) -> AbstractContextManager[LocationBuilder]: ...
        def from_bytes_packed(self, buf: bytes, traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> _DynamicStructReader: ...
        @override
        def read(self, file: IO[str] | IO[bytes], traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> LocationReader: ...
        @override
        def read_packed(self, file: IO[str] | IO[bytes], traversal_limit_in_words: int | None = ..., nesting_limit: int | None = ...) -> LocationReader: ...

    type LocationReader = _LocationModule.Reader
    type LocationBuilder = _LocationModule.Builder
    Location: _LocationModule
    class _CallbackModule(_InterfaceModule):
        class SendcellsRequest(Protocol):
            maxCount: int
            def send(self) -> _GridModule._CallbackModule.CallbackClient.SendcellsResult: ...

        @classmethod
        def _new_client(cls, server: _DynamicCapabilityServer) -> _GridModule._CallbackModule.CallbackClient: ...
        class Server(_DynamicCapabilityServer):
            class SendcellsResult(Awaitable[SendcellsResult], Protocol):
                locations: Sequence[_GridModule._LocationModule.Builder | _GridModule._LocationModule.Reader]

            class SendcellsResultTuple(NamedTuple):
                locations: Sequence[_GridModule._LocationModule]

            class SendcellsCallContext(Protocol):
                params: _GridModule._CallbackModule.SendcellsRequest
                results: _GridModule._CallbackModule.Server.SendcellsResult

            def sendCells(self, maxCount: int, _context: _GridModule._CallbackModule.Server.SendcellsCallContext, **kwargs: Any) -> Awaitable[_GridModule._CallbackModule.Server.SendcellsResultTuple | None]: ...
            def sendCells_context(self, context: _GridModule._CallbackModule.Server.SendcellsCallContext) -> Awaitable[None]: ...

        class CallbackClient(_DynamicCapabilityClient):
            class SendcellsResult(Awaitable[SendcellsResult], Protocol):
                locations: Sequence[_GridModule._LocationModule.Builder | _GridModule._LocationModule.Reader]

            def sendCells(self, maxCount: int | None = None) -> _GridModule._CallbackModule.CallbackClient.SendcellsResult: ...
            def sendCells_request(self, maxCount: int | None = None) -> _GridModule._CallbackModule.SendcellsRequest: ...

    Callback: _CallbackModule
    type CallbackClient = _GridModule._CallbackModule.CallbackClient
    class ClosestvalueatRequest(Protocol):
        latlonCoord: _LatLonCoordModule.Builder
        ignoreNoData: bool
        resolution: _GridModule._ResolutionModule.Builder
        agg: int | Literal["none", "wAvg", "wMedian", "min", "max", "sum", "iAvg", "iMedian", "avg", "median", "wSum", "iSum", "wMin", "iMin", "wMax", "iMax"]
        returnRowCols: bool
        includeAggParts: bool
        @overload
        def init(self, name: Literal["latlonCoord"]) -> _LatLonCoordModule.Builder: ...
        @overload
        def init(self, name: Literal["resolution"]) -> ResolutionBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _GridModule.GridClient.ClosestvalueatResult: ...

    class ResolutionRequest(Protocol):
        def send(self) -> _GridModule.GridClient.ResolutionResult: ...

    class DimensionRequest(Protocol):
        def send(self) -> _GridModule.GridClient.DimensionResult: ...

    class NodatavalueRequest(Protocol):
        def send(self) -> _GridModule.GridClient.NodatavalueResult: ...

    class ValueatRequest(Protocol):
        row: int
        col: int
        resolution: _GridModule._ResolutionModule.Builder
        agg: int | Literal["none", "wAvg", "wMedian", "min", "max", "sum", "iAvg", "iMedian", "avg", "median", "wSum", "iSum", "wMin", "iMin", "wMax", "iMax"]
        includeAggParts: bool
        @overload
        def init(self, name: Literal["resolution"]) -> ResolutionBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _GridModule.GridClient.ValueatResult: ...

    class LatlonboundsRequest(Protocol):
        useCellCenter: bool
        def send(self) -> _GridModule.GridClient.LatlonboundsResult: ...

    class StreamcellsRequest(Protocol):
        topLeft: _GridModule._RowColModule.Builder
        bottomRight: _GridModule._RowColModule.Builder
        @overload
        def init(self, name: Literal["topLeft"]) -> RowColBuilder: ...
        @overload
        def init(self, name: Literal["bottomRight"]) -> RowColBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _GridModule.GridClient.StreamcellsResult: ...

    class UnitRequest(Protocol):
        def send(self) -> _GridModule.GridClient.UnitResult: ...

    @classmethod
    def _new_client(cls, server: _DynamicCapabilityServer) -> _GridModule.GridClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class ClosestvalueatResult(Awaitable[ClosestvalueatResult], Protocol):
            val: _GridModule._ValueModule.Builder | _GridModule._ValueModule.Reader
            tl: _GridModule._RowColModule.Builder | _GridModule._RowColModule.Reader
            br: _GridModule._RowColModule.Builder | _GridModule._RowColModule.Reader
            aggParts: Sequence[_GridModule._AggregationPartModule.Builder | _GridModule._AggregationPartModule.Reader]

        class ResolutionResult(Awaitable[ResolutionResult], Protocol):
            res: _GridModule._ResolutionModule.Builder | _GridModule._ResolutionModule.Reader

        class DimensionResult(Awaitable[DimensionResult], Protocol):
            rows: int
            cols: int

        class NodatavalueResult(Awaitable[NodatavalueResult], Protocol):
            nodata: _GridModule._ValueModule.Builder | _GridModule._ValueModule.Reader

        class ValueatResult(Awaitable[ValueatResult], Protocol):
            val: _GridModule._ValueModule.Builder | _GridModule._ValueModule.Reader
            aggParts: Sequence[_GridModule._AggregationPartModule.Builder | _GridModule._AggregationPartModule.Reader]

        class LatlonboundsResult(Awaitable[LatlonboundsResult], Protocol):
            tl: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader
            tr: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader
            br: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader
            bl: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader

        class StreamcellsResult(Awaitable[StreamcellsResult], Protocol):
            callback: _GridModule._CallbackModule.CallbackClient

        class UnitResult(Awaitable[UnitResult], Protocol):
            unit: str

        class ClosestvalueatResultTuple(NamedTuple):
            val: _GridModule._ValueModule.Builder | _GridModule._ValueModule.Reader
            tl: _GridModule._RowColModule.Builder | _GridModule._RowColModule.Reader
            br: _GridModule._RowColModule.Builder | _GridModule._RowColModule.Reader
            aggParts: Sequence[_GridModule._AggregationPartModule]

        class ResolutionResultTuple(NamedTuple):
            res: _GridModule._ResolutionModule.Builder | _GridModule._ResolutionModule.Reader

        class DimensionResultTuple(NamedTuple):
            rows: int
            cols: int

        class NodatavalueResultTuple(NamedTuple):
            nodata: _GridModule._ValueModule.Builder | _GridModule._ValueModule.Reader

        class ValueatResultTuple(NamedTuple):
            val: _GridModule._ValueModule.Builder | _GridModule._ValueModule.Reader
            aggParts: Sequence[_GridModule._AggregationPartModule]

        class LatlonboundsResultTuple(NamedTuple):
            tl: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader
            tr: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader
            br: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader
            bl: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader

        class StreamcellsResultTuple(NamedTuple):
            callback: _GridModule._CallbackModule.Server

        class UnitResultTuple(NamedTuple):
            unit: str

        class ClosestvalueatCallContext(Protocol):
            params: _GridModule.ClosestvalueatRequest
            results: _GridModule.Server.ClosestvalueatResult

        class ResolutionCallContext(Protocol):
            params: _GridModule.ResolutionRequest
            results: _GridModule.Server.ResolutionResult

        class DimensionCallContext(Protocol):
            params: _GridModule.DimensionRequest
            results: _GridModule.Server.DimensionResult

        class NodatavalueCallContext(Protocol):
            params: _GridModule.NodatavalueRequest
            results: _GridModule.Server.NodatavalueResult

        class ValueatCallContext(Protocol):
            params: _GridModule.ValueatRequest
            results: _GridModule.Server.ValueatResult

        class LatlonboundsCallContext(Protocol):
            params: _GridModule.LatlonboundsRequest
            results: _GridModule.Server.LatlonboundsResult

        class StreamcellsCallContext(Protocol):
            params: _GridModule.StreamcellsRequest
            results: _GridModule.Server.StreamcellsResult

        class UnitCallContext(Protocol):
            params: _GridModule.UnitRequest
            results: _GridModule.Server.UnitResult

        def closestValueAt(
            self,
            latlonCoord: _LatLonCoordModule.Reader,
            ignoreNoData: bool,
            resolution: _GridModule._ResolutionModule.Reader,
            agg: int | Literal["none", "wAvg", "wMedian", "min", "max", "sum", "iAvg", "iMedian", "avg", "median", "wSum", "iSum", "wMin", "iMin", "wMax", "iMax"],
            returnRowCols: bool,
            includeAggParts: bool,
            _context: _GridModule.Server.ClosestvalueatCallContext,
            **kwargs: Any,
        ) -> Awaitable[_GridModule.Server.ClosestvalueatResultTuple | None]: ...
        def closestValueAt_context(self, context: _GridModule.Server.ClosestvalueatCallContext) -> Awaitable[None]: ...
        def resolution(self, _context: _GridModule.Server.ResolutionCallContext, **kwargs: Any) -> Awaitable[_GridModule.Server.ResolutionResultTuple | None]: ...
        def resolution_context(self, context: _GridModule.Server.ResolutionCallContext) -> Awaitable[None]: ...
        def dimension(self, _context: _GridModule.Server.DimensionCallContext, **kwargs: Any) -> Awaitable[_GridModule.Server.DimensionResultTuple | None]: ...
        def dimension_context(self, context: _GridModule.Server.DimensionCallContext) -> Awaitable[None]: ...
        def noDataValue(self, _context: _GridModule.Server.NodatavalueCallContext, **kwargs: Any) -> Awaitable[_GridModule.Server.NodatavalueResultTuple | None]: ...
        def noDataValue_context(self, context: _GridModule.Server.NodatavalueCallContext) -> Awaitable[None]: ...
        def valueAt(
            self,
            row: int,
            col: int,
            resolution: _GridModule._ResolutionModule.Reader,
            agg: int | Literal["none", "wAvg", "wMedian", "min", "max", "sum", "iAvg", "iMedian", "avg", "median", "wSum", "iSum", "wMin", "iMin", "wMax", "iMax"],
            includeAggParts: bool,
            _context: _GridModule.Server.ValueatCallContext,
            **kwargs: Any,
        ) -> Awaitable[_GridModule.Server.ValueatResultTuple | None]: ...
        def valueAt_context(self, context: _GridModule.Server.ValueatCallContext) -> Awaitable[None]: ...
        def latLonBounds(self, useCellCenter: bool, _context: _GridModule.Server.LatlonboundsCallContext, **kwargs: Any) -> Awaitable[_GridModule.Server.LatlonboundsResultTuple | None]: ...
        def latLonBounds_context(self, context: _GridModule.Server.LatlonboundsCallContext) -> Awaitable[None]: ...
        def streamCells(self, topLeft: _GridModule._RowColModule.Reader, bottomRight: _GridModule._RowColModule.Reader, _context: _GridModule.Server.StreamcellsCallContext, **kwargs: Any) -> Awaitable[_GridModule._CallbackModule.Server | _GridModule.Server.StreamcellsResultTuple | None]: ...
        def streamCells_context(self, context: _GridModule.Server.StreamcellsCallContext) -> Awaitable[None]: ...
        def unit(self, _context: _GridModule.Server.UnitCallContext, **kwargs: Any) -> Awaitable[str | _GridModule.Server.UnitResultTuple | None]: ...
        def unit_context(self, context: _GridModule.Server.UnitCallContext) -> Awaitable[None]: ...

    class GridClient(_IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient):
        class ClosestvalueatResult(Awaitable[ClosestvalueatResult], Protocol):
            val: _GridModule._ValueModule.Builder | _GridModule._ValueModule.Reader
            tl: _GridModule._RowColModule.Builder | _GridModule._RowColModule.Reader
            br: _GridModule._RowColModule.Builder | _GridModule._RowColModule.Reader
            aggParts: Sequence[_GridModule._AggregationPartModule.Builder | _GridModule._AggregationPartModule.Reader]

        class ResolutionResult(Awaitable[ResolutionResult], Protocol):
            res: _GridModule._ResolutionModule.Builder | _GridModule._ResolutionModule.Reader

        class DimensionResult(Awaitable[DimensionResult], Protocol):
            rows: int
            cols: int

        class NodatavalueResult(Awaitable[NodatavalueResult], Protocol):
            nodata: _GridModule._ValueModule.Builder | _GridModule._ValueModule.Reader

        class ValueatResult(Awaitable[ValueatResult], Protocol):
            val: _GridModule._ValueModule.Builder | _GridModule._ValueModule.Reader
            aggParts: Sequence[_GridModule._AggregationPartModule.Builder | _GridModule._AggregationPartModule.Reader]

        class LatlonboundsResult(Awaitable[LatlonboundsResult], Protocol):
            tl: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader
            tr: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader
            br: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader
            bl: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader

        class StreamcellsResult(Awaitable[StreamcellsResult], Protocol):
            callback: _GridModule._CallbackModule.CallbackClient

        class UnitResult(Awaitable[UnitResult], Protocol):
            unit: str

        def closestValueAt(
            self,
            latlonCoord: _LatLonCoordModule | dict[str, Any] | None = None,
            ignoreNoData: bool | None = None,
            resolution: ResolutionBuilder | ResolutionReader | dict[str, Any] | None = None,
            agg: int | Literal["none", "wAvg", "wMedian", "min", "max", "sum", "iAvg", "iMedian", "avg", "median", "wSum", "iSum", "wMin", "iMin", "wMax", "iMax"] | None = None,
            returnRowCols: bool | None = None,
            includeAggParts: bool | None = None,
        ) -> _GridModule.GridClient.ClosestvalueatResult: ...
        def resolution(self) -> _GridModule.GridClient.ResolutionResult: ...
        def dimension(self) -> _GridModule.GridClient.DimensionResult: ...
        def noDataValue(self) -> _GridModule.GridClient.NodatavalueResult: ...
        def valueAt(
            self,
            row: int | None = None,
            col: int | None = None,
            resolution: ResolutionBuilder | ResolutionReader | dict[str, Any] | None = None,
            agg: int | Literal["none", "wAvg", "wMedian", "min", "max", "sum", "iAvg", "iMedian", "avg", "median", "wSum", "iSum", "wMin", "iMin", "wMax", "iMax"] | None = None,
            includeAggParts: bool | None = None,
        ) -> _GridModule.GridClient.ValueatResult: ...
        def latLonBounds(self, useCellCenter: bool | None = None) -> _GridModule.GridClient.LatlonboundsResult: ...
        def streamCells(self, topLeft: RowColBuilder | RowColReader | dict[str, Any] | None = None, bottomRight: RowColBuilder | RowColReader | dict[str, Any] | None = None) -> _GridModule.GridClient.StreamcellsResult: ...
        def unit(self) -> _GridModule.GridClient.UnitResult: ...
        def closestValueAt_request(
            self,
            latlonCoord: _LatLonCoordModule.Builder | None = None,
            ignoreNoData: bool | None = None,
            resolution: _GridModule._ResolutionModule.Builder | None = None,
            agg: int | Literal["none", "wAvg", "wMedian", "min", "max", "sum", "iAvg", "iMedian", "avg", "median", "wSum", "iSum", "wMin", "iMin", "wMax", "iMax"] | None = None,
            returnRowCols: bool | None = None,
            includeAggParts: bool | None = None,
        ) -> _GridModule.ClosestvalueatRequest: ...
        def resolution_request(self) -> _GridModule.ResolutionRequest: ...
        def dimension_request(self) -> _GridModule.DimensionRequest: ...
        def noDataValue_request(self) -> _GridModule.NodatavalueRequest: ...
        def valueAt_request(
            self,
            row: int | None = None,
            col: int | None = None,
            resolution: _GridModule._ResolutionModule.Builder | None = None,
            agg: int | Literal["none", "wAvg", "wMedian", "min", "max", "sum", "iAvg", "iMedian", "avg", "median", "wSum", "iSum", "wMin", "iMin", "wMax", "iMax"] | None = None,
            includeAggParts: bool | None = None,
        ) -> _GridModule.ValueatRequest: ...
        def latLonBounds_request(self, useCellCenter: bool | None = None) -> _GridModule.LatlonboundsRequest: ...
        def streamCells_request(self, topLeft: _GridModule._RowColModule.Builder | None = None, bottomRight: _GridModule._RowColModule.Builder | None = None) -> _GridModule.StreamcellsRequest: ...
        def unit_request(self) -> _GridModule.UnitRequest: ...

Grid: _GridModule

# Top-level type aliases for use in type annotations
type Aggregation = int | Literal["none", "wAvg", "wMedian", "min", "max", "sum", "iAvg", "iMedian", "avg", "median", "wSum", "iSum", "wMin", "iMin", "wMax", "iMax"]
type AggregationPartBuilder = _GridModule._AggregationPartModule.Builder
type AggregationPartReader = _GridModule._AggregationPartModule.Reader
type CallbackClient = _GridModule._CallbackModule.CallbackClient
type ClosestvalueatResult = _GridModule.GridClient.ClosestvalueatResult
type DimensionResult = _GridModule.GridClient.DimensionResult
type GridClient = _GridModule.GridClient
type LatlonboundsResult = _GridModule.GridClient.LatlonboundsResult
type LocationBuilder = _GridModule._LocationModule.Builder
type LocationReader = _GridModule._LocationModule.Reader
type NodatavalueResult = _GridModule.GridClient.NodatavalueResult
type ResolutionBuilder = _GridModule._ResolutionModule.Builder
type ResolutionReader = _GridModule._ResolutionModule.Reader
type ResolutionResult = _GridModule.GridClient.ResolutionResult
type RowColBuilder = _GridModule._RowColModule.Builder
type RowColReader = _GridModule._RowColModule.Reader
type SendcellsResult = _GridModule._CallbackModule.CallbackClient.SendcellsResult
type StreamcellsResult = _GridModule.GridClient.StreamcellsResult
type UnitResult = _GridModule.GridClient.UnitResult
type ValueBuilder = _GridModule._ValueModule.Builder
type ValueReader = _GridModule._ValueModule.Reader
type ValueatResult = _GridModule.GridClient.ValueatResult
