"""This is an automatically generated stub for `grid.capnp`."""

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
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> ValueBuilder: ...

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
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            f: float | None = None,
            i: int | None = None,
            ui: int | None = None,
            no: bool | None = None,
            **kwargs: Any,
        ) -> ValueBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[ValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ValueBuilder]: ...
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
        ) -> ValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> ValueReader: ...

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
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> ResolutionBuilder: ...

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
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            meter: int | None = None,
            degree: float | None = None,
            **kwargs: Any,
        ) -> ResolutionBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[ResolutionReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ResolutionReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ResolutionBuilder]: ...
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
        ) -> ResolutionReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> ResolutionReader: ...

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
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> RowColBuilder: ...

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
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            row: int | None = None,
            col: int | None = None,
            **kwargs: Any,
        ) -> RowColBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[RowColReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[RowColReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[RowColBuilder]: ...
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
        ) -> RowColReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> RowColReader: ...

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
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> AggregationPartBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def value(self) -> ValueBuilder: ...
            @value.setter
            def value(
                self, value: ValueBuilder | ValueReader | dict[str, Any]
            ) -> None: ...
            @property
            def rowCol(self) -> RowColBuilder: ...
            @rowCol.setter
            def rowCol(
                self, value: RowColBuilder | RowColReader | dict[str, Any]
            ) -> None: ...
            @property
            def areaFrac(self) -> float: ...
            @areaFrac.setter
            def areaFrac(self, value: float) -> None: ...
            @property
            def iValue(self) -> float: ...
            @iValue.setter
            def iValue(self, value: float) -> None: ...
            @overload
            def init(
                self, field: Literal["value"], size: int | None = None
            ) -> ValueBuilder: ...
            @overload
            def init(
                self, field: Literal["rowCol"], size: int | None = None
            ) -> RowColBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> AggregationPartReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            value: ValueBuilder | dict[str, Any] | None = None,
            rowCol: RowColBuilder | dict[str, Any] | None = None,
            areaFrac: float | None = None,
            iValue: float | None = None,
            **kwargs: Any,
        ) -> AggregationPartBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[AggregationPartReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[AggregationPartReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[AggregationPartBuilder]: ...
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
        ) -> AggregationPartReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AggregationPartReader: ...

    type AggregationPartReader = _AggregationPartModule.Reader
    type AggregationPartBuilder = _AggregationPartModule.Builder
    AggregationPart: _AggregationPartModule
    class _LocationModule(_StructModule):
        class Reader(_DynamicStructReader):
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
                allocate_seg_callable: Any = None,
            ) -> LocationBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def latLonCoord(self) -> LatLonCoordBuilder: ...
            @latLonCoord.setter
            def latLonCoord(
                self, value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]
            ) -> None: ...
            @property
            def rowCol(self) -> RowColBuilder: ...
            @rowCol.setter
            def rowCol(
                self, value: RowColBuilder | RowColReader | dict[str, Any]
            ) -> None: ...
            @property
            def value(self) -> ValueBuilder: ...
            @value.setter
            def value(
                self, value: ValueBuilder | ValueReader | dict[str, Any]
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["latLonCoord"], size: int | None = None
            ) -> LatLonCoordBuilder: ...
            @overload
            def init(
                self, field: Literal["rowCol"], size: int | None = None
            ) -> RowColBuilder: ...
            @overload
            def init(
                self, field: Literal["value"], size: int | None = None
            ) -> ValueBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> LocationReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            latLonCoord: LatLonCoordBuilder | dict[str, Any] | None = None,
            rowCol: RowColBuilder | dict[str, Any] | None = None,
            value: ValueBuilder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> LocationBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[LocationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[LocationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[LocationBuilder]: ...
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
        ) -> LocationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> LocationReader: ...

    type LocationReader = _LocationModule.Reader
    type LocationBuilder = _LocationModule.Builder
    Location: _LocationModule
    class _CallbackModule(_InterfaceModule):
        class SendcellsRequest(Protocol):
            maxCount: int
            def send(
                self,
            ) -> _GridModule._CallbackModule.CallbackClient.SendcellsResult: ...

        def _new_client(
            self, server: _DynamicCapabilityServer
        ) -> _GridModule._CallbackModule.CallbackClient: ...
        class Server(_DynamicCapabilityServer):
            class SendcellsResult(_DynamicStructBuilder):
                @property
                def locations(self) -> LocationListBuilder: ...
                @locations.setter
                def locations(
                    self,
                    value: LocationListBuilder | LocationListReader | Sequence[Any],
                ) -> None: ...
                @overload
                def init(
                    self, field: Literal["locations"], size: int | None = None
                ) -> LocationListBuilder: ...
                @overload
                def init(self, field: str, size: int | None = None) -> Any: ...

            class SendcellsResultTuple(NamedTuple):
                locations: LocationListBuilder | LocationListReader

            class SendcellsParams(Protocol):
                maxCount: int

            class SendcellsCallContext(Protocol):
                params: _GridModule._CallbackModule.Server.SendcellsParams
                @property
                def results(
                    self,
                ) -> _GridModule._CallbackModule.Server.SendcellsResult: ...

            def sendCells(
                self,
                maxCount: int,
                _context: _GridModule._CallbackModule.Server.SendcellsCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                Sequence[LocationBuilder | LocationReader]
                | _GridModule._CallbackModule.Server.SendcellsResultTuple
                | None
            ]: ...
            def sendCells_context(
                self, context: _GridModule._CallbackModule.Server.SendcellsCallContext
            ) -> Awaitable[None]: ...

        class CallbackClient(_DynamicCapabilityClient):
            class SendcellsResult(Awaitable[SendcellsResult], Protocol):
                locations: LocationListReader

            def sendCells(
                self, maxCount: int | None = None
            ) -> _GridModule._CallbackModule.CallbackClient.SendcellsResult: ...
            def sendCells_request(
                self, maxCount: int | None = None
            ) -> _GridModule._CallbackModule.SendcellsRequest: ...

    Callback: _CallbackModule
    type CallbackClient = _GridModule._CallbackModule.CallbackClient
    type CallbackServer = _GridModule._CallbackModule.Server
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
        resolution: ResolutionBuilder
        agg: AggregationEnum
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
        topLeft: RowColBuilder
        bottomRight: RowColBuilder
        @overload
        def init(self, name: Literal["topLeft"]) -> RowColBuilder: ...
        @overload
        def init(self, name: Literal["bottomRight"]) -> RowColBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _GridModule.GridClient.StreamcellsResult: ...

    class UnitRequest(Protocol):
        def send(self) -> _GridModule.GridClient.UnitResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _GridModule.GridClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class ClosestvalueatResult(_DynamicStructBuilder):
            @property
            def val(self) -> ValueBuilder: ...
            @val.setter
            def val(
                self, value: ValueBuilder | ValueReader | dict[str, Any]
            ) -> None: ...
            @property
            def tl(self) -> RowColBuilder: ...
            @tl.setter
            def tl(
                self, value: RowColBuilder | RowColReader | dict[str, Any]
            ) -> None: ...
            @property
            def br(self) -> RowColBuilder: ...
            @br.setter
            def br(
                self, value: RowColBuilder | RowColReader | dict[str, Any]
            ) -> None: ...
            @property
            def aggParts(self) -> AggregationPartListBuilder: ...
            @aggParts.setter
            def aggParts(
                self,
                value: AggregationPartListBuilder
                | AggregationPartListReader
                | Sequence[Any],
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["val"], size: int | None = None
            ) -> ValueBuilder: ...
            @overload
            def init(
                self, field: Literal["tl"], size: int | None = None
            ) -> RowColBuilder: ...
            @overload
            def init(
                self, field: Literal["br"], size: int | None = None
            ) -> RowColBuilder: ...
            @overload
            def init(
                self, field: Literal["aggParts"], size: int | None = None
            ) -> AggregationPartListBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...

        class ResolutionResult(_DynamicStructBuilder):
            @property
            def res(self) -> ResolutionBuilder: ...
            @res.setter
            def res(
                self, value: ResolutionBuilder | ResolutionReader | dict[str, Any]
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["res"], size: int | None = None
            ) -> ResolutionBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...

        class DimensionResult(_DynamicStructBuilder):
            @property
            def rows(self) -> int: ...
            @rows.setter
            def rows(self, value: int) -> None: ...
            @property
            def cols(self) -> int: ...
            @cols.setter
            def cols(self, value: int) -> None: ...

        class NodatavalueResult(_DynamicStructBuilder):
            @property
            def nodata(self) -> ValueBuilder: ...
            @nodata.setter
            def nodata(
                self, value: ValueBuilder | ValueReader | dict[str, Any]
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["nodata"], size: int | None = None
            ) -> ValueBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...

        class ValueatResult(_DynamicStructBuilder):
            @property
            def val(self) -> ValueBuilder: ...
            @val.setter
            def val(
                self, value: ValueBuilder | ValueReader | dict[str, Any]
            ) -> None: ...
            @property
            def aggParts(self) -> AggregationPartListBuilder: ...
            @aggParts.setter
            def aggParts(
                self,
                value: AggregationPartListBuilder
                | AggregationPartListReader
                | Sequence[Any],
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["val"], size: int | None = None
            ) -> ValueBuilder: ...
            @overload
            def init(
                self, field: Literal["aggParts"], size: int | None = None
            ) -> AggregationPartListBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...

        class LatlonboundsResult(_DynamicStructBuilder):
            @property
            def tl(self) -> LatLonCoordBuilder: ...
            @tl.setter
            def tl(
                self, value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]
            ) -> None: ...
            @property
            def tr(self) -> LatLonCoordBuilder: ...
            @tr.setter
            def tr(
                self, value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]
            ) -> None: ...
            @property
            def br(self) -> LatLonCoordBuilder: ...
            @br.setter
            def br(
                self, value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]
            ) -> None: ...
            @property
            def bl(self) -> LatLonCoordBuilder: ...
            @bl.setter
            def bl(
                self, value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["tl"], size: int | None = None
            ) -> LatLonCoordBuilder: ...
            @overload
            def init(
                self, field: Literal["tr"], size: int | None = None
            ) -> LatLonCoordBuilder: ...
            @overload
            def init(
                self, field: Literal["br"], size: int | None = None
            ) -> LatLonCoordBuilder: ...
            @overload
            def init(
                self, field: Literal["bl"], size: int | None = None
            ) -> LatLonCoordBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...

        class StreamcellsResult(_DynamicStructBuilder):
            @property
            def callback(
                self,
            ) -> (
                _GridModule._CallbackModule.Server
                | _GridModule._CallbackModule.CallbackClient
            ): ...
            @callback.setter
            def callback(
                self,
                value: _GridModule._CallbackModule.Server
                | _GridModule._CallbackModule.CallbackClient,
            ) -> None: ...

        class UnitResult(_DynamicStructBuilder):
            @property
            def unit(self) -> str: ...
            @unit.setter
            def unit(self, value: str) -> None: ...

        class ClosestvalueatResultTuple(NamedTuple):
            val: ValueBuilder | ValueReader
            tl: RowColBuilder | RowColReader
            br: RowColBuilder | RowColReader
            aggParts: AggregationPartListBuilder | AggregationPartListReader

        class ResolutionResultTuple(NamedTuple):
            res: ResolutionBuilder | ResolutionReader

        class DimensionResultTuple(NamedTuple):
            rows: int
            cols: int

        class NodatavalueResultTuple(NamedTuple):
            nodata: ValueBuilder | ValueReader

        class ValueatResultTuple(NamedTuple):
            val: ValueBuilder | ValueReader
            aggParts: AggregationPartListBuilder | AggregationPartListReader

        class LatlonboundsResultTuple(NamedTuple):
            tl: LatLonCoordBuilder | LatLonCoordReader
            tr: LatLonCoordBuilder | LatLonCoordReader
            br: LatLonCoordBuilder | LatLonCoordReader
            bl: LatLonCoordBuilder | LatLonCoordReader

        class StreamcellsResultTuple(NamedTuple):
            callback: (
                _GridModule._CallbackModule.Server
                | _GridModule._CallbackModule.CallbackClient
            )

        class UnitResultTuple(NamedTuple):
            unit: str

        class ClosestvalueatParams(Protocol):
            latlonCoord: LatLonCoordReader
            ignoreNoData: bool
            resolution: ResolutionReader
            agg: AggregationEnum
            returnRowCols: bool
            includeAggParts: bool

        class ClosestvalueatCallContext(Protocol):
            params: _GridModule.Server.ClosestvalueatParams
            @property
            def results(self) -> _GridModule.Server.ClosestvalueatResult: ...

        class ResolutionParams(Protocol): ...

        class ResolutionCallContext(Protocol):
            params: _GridModule.Server.ResolutionParams
            @property
            def results(self) -> _GridModule.Server.ResolutionResult: ...

        class DimensionParams(Protocol): ...

        class DimensionCallContext(Protocol):
            params: _GridModule.Server.DimensionParams
            @property
            def results(self) -> _GridModule.Server.DimensionResult: ...

        class NodatavalueParams(Protocol): ...

        class NodatavalueCallContext(Protocol):
            params: _GridModule.Server.NodatavalueParams
            @property
            def results(self) -> _GridModule.Server.NodatavalueResult: ...

        class ValueatParams(Protocol):
            row: int
            col: int
            resolution: ResolutionReader
            agg: AggregationEnum
            includeAggParts: bool

        class ValueatCallContext(Protocol):
            params: _GridModule.Server.ValueatParams
            @property
            def results(self) -> _GridModule.Server.ValueatResult: ...

        class LatlonboundsParams(Protocol):
            useCellCenter: bool

        class LatlonboundsCallContext(Protocol):
            params: _GridModule.Server.LatlonboundsParams
            @property
            def results(self) -> _GridModule.Server.LatlonboundsResult: ...

        class StreamcellsParams(Protocol):
            topLeft: RowColReader
            bottomRight: RowColReader

        class StreamcellsCallContext(Protocol):
            params: _GridModule.Server.StreamcellsParams
            @property
            def results(self) -> _GridModule.Server.StreamcellsResult: ...

        class UnitParams(Protocol): ...

        class UnitCallContext(Protocol):
            params: _GridModule.Server.UnitParams
            @property
            def results(self) -> _GridModule.Server.UnitResult: ...

        def closestValueAt(
            self,
            latlonCoord: LatLonCoordReader,
            ignoreNoData: bool,
            resolution: ResolutionReader,
            agg: AggregationEnum,
            returnRowCols: bool,
            includeAggParts: bool,
            _context: _GridModule.Server.ClosestvalueatCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_GridModule.Server.ClosestvalueatResultTuple | None]: ...
        def closestValueAt_context(
            self, context: _GridModule.Server.ClosestvalueatCallContext
        ) -> Awaitable[None]: ...
        def resolution(
            self,
            _context: _GridModule.Server.ResolutionCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _GridModule._ResolutionModule.Builder
            | _GridModule.Server.ResolutionResultTuple
            | None
        ]: ...
        def resolution_context(
            self, context: _GridModule.Server.ResolutionCallContext
        ) -> Awaitable[None]: ...
        def dimension(
            self,
            _context: _GridModule.Server.DimensionCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_GridModule.Server.DimensionResultTuple | None]: ...
        def dimension_context(
            self, context: _GridModule.Server.DimensionCallContext
        ) -> Awaitable[None]: ...
        def noDataValue(
            self,
            _context: _GridModule.Server.NodatavalueCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _GridModule._ValueModule.Builder
            | _GridModule.Server.NodatavalueResultTuple
            | None
        ]: ...
        def noDataValue_context(
            self, context: _GridModule.Server.NodatavalueCallContext
        ) -> Awaitable[None]: ...
        def valueAt(
            self,
            row: int,
            col: int,
            resolution: ResolutionReader,
            agg: AggregationEnum,
            includeAggParts: bool,
            _context: _GridModule.Server.ValueatCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_GridModule.Server.ValueatResultTuple | None]: ...
        def valueAt_context(
            self, context: _GridModule.Server.ValueatCallContext
        ) -> Awaitable[None]: ...
        def latLonBounds(
            self,
            useCellCenter: bool,
            _context: _GridModule.Server.LatlonboundsCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_GridModule.Server.LatlonboundsResultTuple | None]: ...
        def latLonBounds_context(
            self, context: _GridModule.Server.LatlonboundsCallContext
        ) -> Awaitable[None]: ...
        def streamCells(
            self,
            topLeft: RowColReader,
            bottomRight: RowColReader,
            _context: _GridModule.Server.StreamcellsCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _GridModule._CallbackModule.Server
            | _GridModule.Server.StreamcellsResultTuple
            | None
        ]: ...
        def streamCells_context(
            self, context: _GridModule.Server.StreamcellsCallContext
        ) -> Awaitable[None]: ...
        def unit(
            self, _context: _GridModule.Server.UnitCallContext, **kwargs: dict[str, Any]
        ) -> Awaitable[str | _GridModule.Server.UnitResultTuple | None]: ...
        def unit_context(
            self, context: _GridModule.Server.UnitCallContext
        ) -> Awaitable[None]: ...

    class GridClient(
        _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
    ):
        class ClosestvalueatResult(Awaitable[ClosestvalueatResult], Protocol):
            val: ValueReader
            tl: RowColReader
            br: RowColReader
            aggParts: AggregationPartListReader

        class ResolutionResult(Awaitable[ResolutionResult], Protocol):
            res: ResolutionReader

        class DimensionResult(Awaitable[DimensionResult], Protocol):
            rows: int
            cols: int

        class NodatavalueResult(Awaitable[NodatavalueResult], Protocol):
            nodata: ValueReader

        class ValueatResult(Awaitable[ValueatResult], Protocol):
            val: ValueReader
            aggParts: AggregationPartListReader

        class LatlonboundsResult(Awaitable[LatlonboundsResult], Protocol):
            tl: LatLonCoordReader
            tr: LatLonCoordReader
            br: LatLonCoordReader
            bl: LatLonCoordReader

        class StreamcellsResult(Awaitable[StreamcellsResult], Protocol):
            callback: _GridModule._CallbackModule.CallbackClient

        class UnitResult(Awaitable[UnitResult], Protocol):
            unit: str

        def closestValueAt(
            self,
            latlonCoord: LatLonCoordBuilder
            | LatLonCoordReader
            | dict[str, Any]
            | None = None,
            ignoreNoData: bool | None = None,
            resolution: ResolutionBuilder
            | ResolutionReader
            | dict[str, Any]
            | None = None,
            agg: AggregationEnum | None = None,
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
            resolution: ResolutionBuilder
            | ResolutionReader
            | dict[str, Any]
            | None = None,
            agg: AggregationEnum | None = None,
            includeAggParts: bool | None = None,
        ) -> _GridModule.GridClient.ValueatResult: ...
        def latLonBounds(
            self, useCellCenter: bool | None = None
        ) -> _GridModule.GridClient.LatlonboundsResult: ...
        def streamCells(
            self,
            topLeft: RowColBuilder | RowColReader | dict[str, Any] | None = None,
            bottomRight: RowColBuilder | RowColReader | dict[str, Any] | None = None,
        ) -> _GridModule.GridClient.StreamcellsResult: ...
        def unit(self) -> _GridModule.GridClient.UnitResult: ...
        def closestValueAt_request(
            self,
            latlonCoord: LatLonCoordBuilder | None = None,
            ignoreNoData: bool | None = None,
            resolution: ResolutionBuilder | None = None,
            agg: AggregationEnum | None = None,
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
            resolution: ResolutionBuilder | None = None,
            agg: AggregationEnum | None = None,
            includeAggParts: bool | None = None,
        ) -> _GridModule.ValueatRequest: ...
        def latLonBounds_request(
            self, useCellCenter: bool | None = None
        ) -> _GridModule.LatlonboundsRequest: ...
        def streamCells_request(
            self,
            topLeft: RowColBuilder | None = None,
            bottomRight: RowColBuilder | None = None,
        ) -> _GridModule.StreamcellsRequest: ...
        def unit_request(self) -> _GridModule.UnitRequest: ...

class _LocationList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> LocationReader: ...
        def __iter__(self) -> Iterator[LocationReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> LocationBuilder: ...
        def __setitem__(
            self, key: int, value: LocationReader | LocationBuilder | dict[str, Any]
        ) -> None: ...
        def __iter__(self) -> Iterator[LocationBuilder]: ...
        def init(self, index: int, size: int | None = None) -> LocationBuilder: ...

class _AggregationPartList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> AggregationPartReader: ...
        def __iter__(self) -> Iterator[AggregationPartReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> AggregationPartBuilder: ...
        def __setitem__(
            self,
            key: int,
            value: AggregationPartReader | AggregationPartBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[AggregationPartBuilder]: ...
        def init(
            self, index: int, size: int | None = None
        ) -> AggregationPartBuilder: ...

Grid: _GridModule

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
type AggregationPartBuilder = _GridModule._AggregationPartModule.Builder
type AggregationPartListBuilder = _AggregationPartList.Builder
type AggregationPartListReader = _AggregationPartList.Reader
type AggregationPartReader = _GridModule._AggregationPartModule.Reader
type CallbackClient = _GridModule._CallbackModule.CallbackClient
type CallbackServer = _GridModule._CallbackModule.Server
type ClosestvalueatResult = _GridModule.GridClient.ClosestvalueatResult
type DimensionResult = _GridModule.GridClient.DimensionResult
type GridClient = _GridModule.GridClient
type GridServer = _GridModule.Server
type LatlonboundsResult = _GridModule.GridClient.LatlonboundsResult
type LocationBuilder = _GridModule._LocationModule.Builder
type LocationListBuilder = _LocationList.Builder
type LocationListReader = _LocationList.Reader
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
