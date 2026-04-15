"""This is an automatically generated stub for `geo.capnp`."""

from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

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

class _CoordTypeEnumModule:
    gk: int
    utm: int
    latlon: int

class _EPSGStructModule(_StructModule):
    wgs84: int
    utm21S: int
    utm32N: int
    gk5: int
    gk4: int
    gk3: int
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        **kwargs: object,
    ) -> EPSGBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[EPSGReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[EPSGReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[EPSGBuilder]: ...
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
    ) -> EPSGReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> EPSGReader: ...

class EPSGReader(_DynamicStructReader):
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> EPSGBuilder: ...

class EPSGBuilder(_DynamicStructBuilder):
    @override
    def as_reader(self) -> EPSGReader: ...

EPSG: _EPSGStructModule

class _UTMCoordStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        zone: int | None = None,
        latitudeBand: str | None = None,
        r: float | None = None,
        h: float | None = None,
        **kwargs: object,
    ) -> UTMCoordBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[UTMCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[UTMCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[UTMCoordBuilder]: ...
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
    ) -> UTMCoordReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> UTMCoordReader: ...

class UTMCoordReader(_DynamicStructReader):
    @property
    def zone(self) -> int: ...
    @property
    def latitudeBand(self) -> str: ...
    @property
    def r(self) -> float: ...
    @property
    def h(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> UTMCoordBuilder: ...

class UTMCoordBuilder(_DynamicStructBuilder):
    @property
    def zone(self) -> int: ...
    @zone.setter
    def zone(self, value: int) -> None: ...
    @property
    def latitudeBand(self) -> str: ...
    @latitudeBand.setter
    def latitudeBand(self, value: str) -> None: ...
    @property
    def r(self) -> float: ...
    @r.setter
    def r(self, value: float) -> None: ...
    @property
    def h(self) -> float: ...
    @h.setter
    def h(self, value: float) -> None: ...
    @override
    def as_reader(self) -> UTMCoordReader: ...

UTMCoord: _UTMCoordStructModule

class _LatLonCoordStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        lat: float | None = None,
        lon: float | None = None,
        **kwargs: object,
    ) -> LatLonCoordBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[LatLonCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[LatLonCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[LatLonCoordBuilder]: ...
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
    ) -> LatLonCoordReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> LatLonCoordReader: ...

class LatLonCoordReader(_DynamicStructReader):
    @property
    def lat(self) -> float: ...
    @property
    def lon(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> LatLonCoordBuilder: ...

class LatLonCoordBuilder(_DynamicStructBuilder):
    @property
    def lat(self) -> float: ...
    @lat.setter
    def lat(self, value: float) -> None: ...
    @property
    def lon(self) -> float: ...
    @lon.setter
    def lon(self, value: float) -> None: ...
    @override
    def as_reader(self) -> LatLonCoordReader: ...

LatLonCoord: _LatLonCoordStructModule

class _GKCoordStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        meridianNo: int | None = None,
        r: float | None = None,
        h: float | None = None,
        **kwargs: object,
    ) -> GKCoordBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[GKCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[GKCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[GKCoordBuilder]: ...
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
    ) -> GKCoordReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> GKCoordReader: ...

class GKCoordReader(_DynamicStructReader):
    @property
    def meridianNo(self) -> int: ...
    @property
    def r(self) -> float: ...
    @property
    def h(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> GKCoordBuilder: ...

class GKCoordBuilder(_DynamicStructBuilder):
    @property
    def meridianNo(self) -> int: ...
    @meridianNo.setter
    def meridianNo(self, value: int) -> None: ...
    @property
    def r(self) -> float: ...
    @r.setter
    def r(self, value: float) -> None: ...
    @property
    def h(self) -> float: ...
    @h.setter
    def h(self, value: float) -> None: ...
    @override
    def as_reader(self) -> GKCoordReader: ...

GKCoord: _GKCoordStructModule

class _Point2DStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        x: float | None = None,
        y: float | None = None,
        **kwargs: object,
    ) -> Point2DBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[Point2DReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[Point2DReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[Point2DBuilder]: ...
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
    ) -> Point2DReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Point2DReader: ...

class Point2DReader(_DynamicStructReader):
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> Point2DBuilder: ...

class Point2DBuilder(_DynamicStructBuilder):
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...
    @override
    def as_reader(self) -> Point2DReader: ...

Point2D: _Point2DStructModule

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

RowCol: _RowColStructModule

class _CoordStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        gk: GKCoordBuilder | dict[str, Any] | None = None,
        latlon: LatLonCoordBuilder | dict[str, Any] | None = None,
        utm: UTMCoordBuilder | dict[str, Any] | None = None,
        p2D: Point2DBuilder | dict[str, Any] | None = None,
        rowcol: RowColBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> CoordBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[CoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[CoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[CoordBuilder]: ...
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
    ) -> CoordReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> CoordReader: ...

class CoordReader(_DynamicStructReader):
    @property
    def gk(self) -> GKCoordReader: ...
    @property
    def latlon(self) -> LatLonCoordReader: ...
    @property
    def utm(self) -> UTMCoordReader: ...
    @property
    def p2D(self) -> Point2DReader: ...
    @property
    def rowcol(self) -> RowColReader: ...
    @override
    def which(self) -> Literal["gk", "latlon", "utm", "p2D", "rowcol"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> CoordBuilder: ...

class CoordBuilder(_DynamicStructBuilder):
    @property
    def gk(self) -> GKCoordBuilder: ...
    @gk.setter
    def gk(self, value: GKCoordBuilder | GKCoordReader | dict[str, Any]) -> None: ...
    @property
    def latlon(self) -> LatLonCoordBuilder: ...
    @latlon.setter
    def latlon(
        self,
        value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any],
    ) -> None: ...
    @property
    def utm(self) -> UTMCoordBuilder: ...
    @utm.setter
    def utm(self, value: UTMCoordBuilder | UTMCoordReader | dict[str, Any]) -> None: ...
    @property
    def p2D(self) -> Point2DBuilder: ...
    @p2D.setter
    def p2D(self, value: Point2DBuilder | Point2DReader | dict[str, Any]) -> None: ...
    @property
    def rowcol(self) -> RowColBuilder: ...
    @rowcol.setter
    def rowcol(self, value: RowColBuilder | RowColReader | dict[str, Any]) -> None: ...
    @override
    def which(self) -> Literal["gk", "latlon", "utm", "p2D", "rowcol"]: ...
    @override
    @overload
    def init(self, field: Literal["gk"], size: int | None = None) -> GKCoordBuilder: ...
    @overload
    def init(
        self,
        field: Literal["latlon"],
        size: int | None = None,
    ) -> LatLonCoordBuilder: ...
    @overload
    def init(
        self,
        field: Literal["utm"],
        size: int | None = None,
    ) -> UTMCoordBuilder: ...
    @overload
    def init(
        self,
        field: Literal["p2D"],
        size: int | None = None,
    ) -> Point2DBuilder: ...
    @overload
    def init(
        self,
        field: Literal["rowcol"],
        size: int | None = None,
    ) -> RowColBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> CoordReader: ...

Coord: _CoordStructModule

class _RectBoundsStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        tl: AnyPointer | None = None,
        br: AnyPointer | None = None,
        **kwargs: object,
    ) -> RectBoundsBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[RectBoundsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[RectBoundsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[RectBoundsBuilder]: ...
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
    ) -> RectBoundsReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> RectBoundsReader: ...

class RectBoundsReader(_DynamicStructReader):
    @property
    def tl(self) -> _DynamicObjectReader: ...
    @property
    def br(self) -> _DynamicObjectReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> RectBoundsBuilder: ...

class RectBoundsBuilder(_DynamicStructBuilder):
    @property
    def tl(self) -> _DynamicObjectReader: ...
    @tl.setter
    def tl(self, value: AnyPointer) -> None: ...
    @property
    def br(self) -> _DynamicObjectReader: ...
    @br.setter
    def br(self, value: AnyPointer) -> None: ...
    @override
    def as_reader(self) -> RectBoundsReader: ...

RectBounds: _RectBoundsStructModule

# Top-level type aliases for use in type annotations
type CoordTypeEnum = int | Literal["gk", "utm", "latlon"]
