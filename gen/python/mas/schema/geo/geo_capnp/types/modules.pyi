"""Module helper types for `geo.capnp`."""

from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
    _DynamicStructReader,
    _EnumModule,
    _EnumSchema,
    _StructModule,
    _StructSchema,
    _StructSchemaField,
)

from mas.schema.geo.geo_capnp.types import builders as builders
from mas.schema.geo.geo_capnp.types import common as common
from mas.schema.geo.geo_capnp.types import readers as readers
from mas.schema.geo.geo_capnp.types import schemas as schemas

class _CoordTypeEnumModule(_EnumModule):
    gk: int
    utm: int
    latlon: int

    class _CoordTypeSchema(_EnumSchema): ...

    @property
    @override
    def schema(self) -> schemas._CoordTypeEnumSchema: ...

class _EPSGStructModule(_StructModule):
    wgs84: int
    utm21S: int
    utm32N: int
    gk5: int
    gk4: int
    gk3: int
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _EPSGSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]): ...

        @property
        @override
        def fields(self) -> _EPSGStructModule._EPSGSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._EPSGSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        **kwargs: object,
    ) -> builders.EPSGBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.EPSGReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.EPSGReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.EPSGBuilder]: ...
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
    ) -> readers.EPSGReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.EPSGReader: ...

class _UTMCoordStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _UTMCoordSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["zone"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["latitudeBand"],
            ) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["r"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["h"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _UTMCoordStructModule._UTMCoordSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._UTMCoordSchema: ...
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
    ) -> builders.UTMCoordBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.UTMCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.UTMCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.UTMCoordBuilder]: ...
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
    ) -> readers.UTMCoordReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.UTMCoordReader: ...

class _LatLonCoordStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _LatLonCoordSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["lat"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["lon"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _LatLonCoordStructModule._LatLonCoordSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._LatLonCoordSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        lat: float | None = None,
        lon: float | None = None,
        **kwargs: object,
    ) -> builders.LatLonCoordBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.LatLonCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.LatLonCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.LatLonCoordBuilder]: ...
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
    ) -> readers.LatLonCoordReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.LatLonCoordReader: ...

class _GKCoordStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _GKCoordSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["meridianNo"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["r"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["h"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _GKCoordStructModule._GKCoordSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._GKCoordSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        meridianNo: int | None = None,
        r: float | None = None,
        h: float | None = None,
        **kwargs: object,
    ) -> builders.GKCoordBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.GKCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.GKCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.GKCoordBuilder]: ...
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
    ) -> readers.GKCoordReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.GKCoordReader: ...

class _Point2DStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _Point2DSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["x"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["y"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _Point2DStructModule._Point2DSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._Point2DSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        x: float | None = None,
        y: float | None = None,
        **kwargs: object,
    ) -> builders.Point2DBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.Point2DReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.Point2DReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.Point2DBuilder]: ...
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
    ) -> readers.Point2DReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.Point2DReader: ...

class _RowColStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _RowColSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["row"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["col"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _RowColStructModule._RowColSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._RowColSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        row: int | None = None,
        col: int | None = None,
        **kwargs: object,
    ) -> builders.RowColBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.RowColReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.RowColReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.RowColBuilder]: ...
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
    ) -> readers.RowColReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.RowColReader: ...

class _CoordStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _CoordSchema(_StructSchema):
        class _GkField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._GKCoordSchema: ...

        class _LatlonField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._LatLonCoordSchema: ...

        class _UtmField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._UTMCoordSchema: ...

        class _P2DField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._Point2DSchema: ...

        class _RowcolField(_StructSchemaField):
            @property
            @override
            def schema(self) -> schemas._RowColSchema: ...

        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(
                self,
                key: Literal["gk"],
            ) -> _CoordStructModule._CoordSchema._GkField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["latlon"],
            ) -> _CoordStructModule._CoordSchema._LatlonField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["utm"],
            ) -> _CoordStructModule._CoordSchema._UtmField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["p2D"],
            ) -> _CoordStructModule._CoordSchema._P2DField: ...
            @overload
            def __getitem__(
                self,
                key: Literal["rowcol"],
            ) -> _CoordStructModule._CoordSchema._RowcolField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _CoordStructModule._CoordSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._CoordSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        gk: builders.GKCoordBuilder | dict[str, Any] | None = None,
        latlon: builders.LatLonCoordBuilder | dict[str, Any] | None = None,
        utm: builders.UTMCoordBuilder | dict[str, Any] | None = None,
        p2D: builders.Point2DBuilder | dict[str, Any] | None = None,
        rowcol: builders.RowColBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> builders.CoordBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.CoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.CoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.CoordBuilder]: ...
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
    ) -> readers.CoordReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CoordReader: ...

class _RectBoundsStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    class _RectBoundsSchema(_StructSchema):
        class _Fields(dict[str, _StructSchemaField]):
            @overload
            def __getitem__(self, key: Literal["tl"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: Literal["br"]) -> _StructSchemaField: ...
            @overload
            def __getitem__(self, key: str) -> _StructSchemaField: ...

        @property
        @override
        def fields(self) -> _RectBoundsStructModule._RectBoundsSchema._Fields: ...

    @property
    @override
    def schema(self) -> schemas._RectBoundsSchema: ...
    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        tl: common.AnyPointer | None = None,
        br: common.AnyPointer | None = None,
        **kwargs: object,
    ) -> builders.RectBoundsBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.RectBoundsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[readers.RectBoundsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.RectBoundsBuilder]: ...
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
    ) -> readers.RectBoundsReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.RectBoundsReader: ...
