"""Module helper types for `geo.capnp`."""

from collections.abc import Callable, Iterator, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _AsyncIoStream,
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

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        **kwargs: object,
    ) -> builders.EPSGBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.EPSGBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.EPSGReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.EPSGReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.EPSGBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.EPSGBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.EPSGReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.EPSGReader: ...
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
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.EPSGReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.EPSGReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.EPSGReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.EPSGReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.EPSGReader]: ...

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

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        zone: int | None = None,
        latitudeBand: str | None = None,
        r: float | None = None,
        h: float | None = None,
        **kwargs: object,
    ) -> builders.UTMCoordBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.UTMCoordBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.UTMCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.UTMCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.UTMCoordBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.UTMCoordBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.UTMCoordReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.UTMCoordReader: ...
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
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.UTMCoordReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.UTMCoordReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.UTMCoordReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.UTMCoordReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.UTMCoordReader]: ...

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

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        lat: float | None = None,
        lon: float | None = None,
        **kwargs: object,
    ) -> builders.LatLonCoordBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.LatLonCoordBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.LatLonCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.LatLonCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.LatLonCoordBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.LatLonCoordBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.LatLonCoordReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.LatLonCoordReader: ...
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
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.LatLonCoordReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.LatLonCoordReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.LatLonCoordReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.LatLonCoordReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.LatLonCoordReader]: ...

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

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        meridianNo: int | None = None,
        r: float | None = None,
        h: float | None = None,
        **kwargs: object,
    ) -> builders.GKCoordBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.GKCoordBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.GKCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.GKCoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.GKCoordBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.GKCoordBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.GKCoordReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.GKCoordReader: ...
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
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.GKCoordReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.GKCoordReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.GKCoordReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.GKCoordReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.GKCoordReader]: ...

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

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        x: float | None = None,
        y: float | None = None,
        **kwargs: object,
    ) -> builders.Point2DBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.Point2DBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.Point2DReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.Point2DReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.Point2DBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.Point2DBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.Point2DReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.Point2DReader: ...
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
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.Point2DReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.Point2DReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.Point2DReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.Point2DReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.Point2DReader]: ...

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

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        row: int | None = None,
        col: int | None = None,
        **kwargs: object,
    ) -> builders.RowColBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.RowColBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.RowColReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.RowColReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.RowColBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.RowColBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.RowColReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.RowColReader: ...
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
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.RowColReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.RowColReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.RowColReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.RowColReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.RowColReader]: ...

class _CoordStructModule(_StructModule):
    Union: type[common._CoordModuleWhich]
    class Reader(_DynamicStructReader):
        @property
        @override
        def which(self) -> common._CoordWhich: ...

    class Builder(_DynamicStructBuilder):
        @property
        @override
        def which(self) -> common._CoordWhich: ...

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

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        gk: builders.GKCoordBuilder
        | readers.GKCoordReader
        | dict[str, Any]
        | None = None,
        latlon: builders.LatLonCoordBuilder
        | readers.LatLonCoordReader
        | dict[str, Any]
        | None = None,
        utm: builders.UTMCoordBuilder
        | readers.UTMCoordReader
        | dict[str, Any]
        | None = None,
        p2D: builders.Point2DBuilder
        | readers.Point2DReader
        | dict[str, Any]
        | None = None,
        rowcol: builders.RowColBuilder
        | readers.RowColReader
        | dict[str, Any]
        | None = None,
        **kwargs: object,
    ) -> builders.CoordBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.CoordBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.CoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.CoordReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.CoordBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.CoordBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CoordReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CoordReader: ...
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
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.CoordReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.CoordReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.CoordReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.CoordReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.CoordReader]: ...

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

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        tl: common.AnyPointer | None = None,
        br: common.AnyPointer | None = None,
        **kwargs: object,
    ) -> builders.RectBoundsBuilder: ...
    @override
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: object,
    ) -> builders.RectBoundsBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[readers.RectBoundsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> AbstractContextManager[readers.RectBoundsReader]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.RectBoundsBuilder]: ...
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> AbstractContextManager[builders.RectBoundsBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.RectBoundsReader: ...
    @override
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.RectBoundsReader: ...
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
    @override
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> readers.RectBoundsReader | None: ...
    @override
    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.RectBoundsReader]: ...
    @override
    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[readers.RectBoundsReader]: ...
    @override
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.RectBoundsReader]: ...
    @override
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[readers.RectBoundsReader]: ...
