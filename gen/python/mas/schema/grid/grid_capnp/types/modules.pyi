"""Module helper types for `grid.capnp`."""

from collections.abc import Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
)

from . import _all as _all

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
        ) -> _all.ValueBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.ValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.ValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.ValueBuilder]: ...
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
        ) -> _all.ValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.ValueReader: ...

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
        ) -> _all.ResolutionBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.ResolutionReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.ResolutionReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.ResolutionBuilder]: ...
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
        ) -> _all.ResolutionReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.ResolutionReader: ...

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
        ) -> _all.RowColBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.RowColReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.RowColReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.RowColBuilder]: ...
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
        ) -> _all.RowColReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.RowColReader: ...

    RowCol: _RowColStructModule
    class _AggregationPartStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            value: _all.ValueBuilder | dict[str, Any] | None = None,
            rowCol: _all.RowColBuilder | dict[str, Any] | None = None,
            areaFrac: float | None = None,
            iValue: float | None = None,
            **kwargs: object,
        ) -> _all.AggregationPartBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.AggregationPartReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.AggregationPartReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.AggregationPartBuilder]: ...
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
        ) -> _all.AggregationPartReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.AggregationPartReader: ...

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
            rowCol: _all.RowColBuilder | dict[str, Any] | None = None,
            value: _all.ValueBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> _all.LocationBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.LocationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.LocationReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.LocationBuilder]: ...
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
        ) -> _all.LocationReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.LocationReader: ...

    Location: _LocationStructModule
    class _CallbackInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.CallbackClient: ...
        class Server(_DynamicCapabilityServer):
            def sendCells(
                self,
                maxCount: int,
                _context: _all.SendcellsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _all.LocationListBuilder
                | _all.LocationListReader
                | Sequence[Any]
                | _all.SendcellsResultTuple
                | None
            ]: ...
            def sendCells_context(
                self,
                context: _all.SendcellsCallContext,
            ) -> Awaitable[None]: ...

    Callback: _CallbackInterfaceModule
    type CallbackServer = _GridInterfaceModule._CallbackInterfaceModule.Server
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.GridClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def closestValueAt(
            self,
            latlonCoord: LatLonCoordReader,
            ignoreNoData: bool,
            resolution: _all.ResolutionReader,
            agg: _all.AggregationEnum,
            returnRowCols: bool,
            includeAggParts: bool,
            _context: _all.ClosestvalueatCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.ClosestvalueatResultTuple | None]: ...
        def closestValueAt_context(
            self,
            context: _all.ClosestvalueatCallContext,
        ) -> Awaitable[None]: ...
        def resolution(
            self,
            _context: _all.ResolutionCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.ResolutionBuilder
            | _all.ResolutionReader
            | dict[str, Any]
            | _all.ResolutionResultTuple
            | None
        ]: ...
        def resolution_context(
            self,
            context: _all.ResolutionCallContext,
        ) -> Awaitable[None]: ...
        def dimension(
            self,
            _context: _all.DimensionCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.DimensionResultTuple | None]: ...
        def dimension_context(
            self,
            context: _all.DimensionCallContext,
        ) -> Awaitable[None]: ...
        def noDataValue(
            self,
            _context: _all.NodatavalueCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.ValueBuilder
            | _all.ValueReader
            | dict[str, Any]
            | _all.NodatavalueResultTuple
            | None
        ]: ...
        def noDataValue_context(
            self,
            context: _all.NodatavalueCallContext,
        ) -> Awaitable[None]: ...
        def valueAt(
            self,
            row: int,
            col: int,
            resolution: _all.ResolutionReader,
            agg: _all.AggregationEnum,
            includeAggParts: bool,
            _context: _all.ValueatCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.ValueatResultTuple | None]: ...
        def valueAt_context(
            self,
            context: _all.ValueatCallContext,
        ) -> Awaitable[None]: ...
        def latLonBounds(
            self,
            useCellCenter: bool,
            _context: _all.LatlonboundsCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.LatlonboundsResultTuple | None]: ...
        def latLonBounds_context(
            self,
            context: _all.LatlonboundsCallContext,
        ) -> Awaitable[None]: ...
        def streamCells(
            self,
            topLeft: _all.RowColReader,
            bottomRight: _all.RowColReader,
            _context: _all.StreamcellsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _GridInterfaceModule._CallbackInterfaceModule.Server
            | _all.CallbackClient
            | _all.StreamcellsResultTuple
            | None
        ]: ...
        def streamCells_context(
            self,
            context: _all.StreamcellsCallContext,
        ) -> Awaitable[None]: ...
        def unit(
            self,
            _context: _all.UnitCallContext,
            **kwargs: object,
        ) -> Awaitable[str | _all.UnitResultTuple | None]: ...
        def unit_context(self, context: _all.UnitCallContext) -> Awaitable[None]: ...
