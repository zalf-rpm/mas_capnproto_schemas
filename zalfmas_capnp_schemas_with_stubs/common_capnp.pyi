"""This is an automatically generated stub for `common.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
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

# Type alias for Capability parameters
type Capability = (
    _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class _IdInformationModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def id(self) -> str: ...
        @property
        def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @property
        def description(self) -> str: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> IdInformationBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def id(self) -> str: ...
        @id.setter
        def id(self, value: str) -> None: ...
        @property
        def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @name.setter
        def name(self, value: str) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str) -> None: ...
        @override
        def as_reader(self) -> IdInformationReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        id: str | None = None,
        name: str | None = None,
        description: str | None = None,
        **kwargs: Any,
    ) -> IdInformationBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[IdInformationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[IdInformationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[IdInformationBuilder]: ...
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
    ) -> IdInformationReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> IdInformationReader: ...

IdInformation: _IdInformationModule

class _IdentifiableModule(_InterfaceModule):
    class InfoRequest(Protocol):
        def send(self) -> _IdentifiableModule.IdentifiableClient.InfoResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _IdentifiableModule.IdentifiableClient: ...
    class Server(_DynamicCapabilityServer):
        class InfoResult(Awaitable[InfoResult], Protocol):
            id: str
            name: str
            description: str

        class InfoResultTuple(NamedTuple):
            id: str
            name: str
            description: str

        class InfoParams(Protocol): ...

        class InfoCallContext(Protocol):
            params: _IdentifiableModule.Server.InfoParams
            @property
            def results(self) -> IdInformationBuilder: ...

        def info(
            self,
            _context: _IdentifiableModule.Server.InfoCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_IdentifiableModule.Server.InfoResultTuple | None]: ...
        def info_context(
            self, context: _IdentifiableModule.Server.InfoCallContext
        ) -> Awaitable[None]: ...

    class IdentifiableClient(_DynamicCapabilityClient):
        class InfoResult(Awaitable[InfoResult], Protocol):
            id: str
            name: str
            description: str

        def info(self) -> _IdentifiableModule.IdentifiableClient.InfoResult: ...
        def info_request(self) -> _IdentifiableModule.InfoRequest: ...

Identifiable: _IdentifiableModule

class _StructuredTextModule(_StructModule):
    class _TypeModule:
        unstructured: int
        json: int
        xml: int
        toml: int
        sturdyRef: int

    Type: _TypeModule
    class _StructureModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def none(self) -> None: ...
            @property
            def json(self) -> None: ...
            @property
            def xml(self) -> None: ...
            @property
            def toml(self) -> None: ...
            @override
            def which(self) -> Literal["none", "json", "xml", "toml"]: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> StructureBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def none(self) -> None: ...
            @none.setter
            def none(self, value: None) -> None: ...
            @property
            def json(self) -> None: ...
            @json.setter
            def json(self, value: None) -> None: ...
            @property
            def xml(self) -> None: ...
            @xml.setter
            def xml(self, value: None) -> None: ...
            @property
            def toml(self) -> None: ...
            @toml.setter
            def toml(self, value: None) -> None: ...
            @override
            def which(self) -> Literal["none", "json", "xml", "toml"]: ...
            @override
            def as_reader(self) -> StructureReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            none: None | None = None,
            json: None | None = None,
            xml: None | None = None,
            toml: None | None = None,
            **kwargs: Any,
        ) -> StructureBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[StructureReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[StructureReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[StructureBuilder]: ...
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
        ) -> StructureReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> StructureReader: ...

    type StructureReader = _StructureModule.Reader
    type StructureBuilder = _StructureModule.Builder
    Structure: _StructureModule
    class Reader(_DynamicStructReader):
        @property
        def value(self) -> str: ...
        @property
        def structure(self) -> StructureReader: ...
        @property
        def type(self) -> StructuredTextTypeEnum: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> StructuredTextBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def value(self) -> str: ...
        @value.setter
        def value(self, value: str) -> None: ...
        @property
        def structure(self) -> StructureBuilder: ...
        @structure.setter
        def structure(
            self, value: StructureBuilder | StructureReader | dict[str, Any]
        ) -> None: ...
        @property
        def type(self) -> StructuredTextTypeEnum: ...
        @type.setter
        def type(self, value: StructuredTextTypeEnum) -> None: ...
        def init(
            self, field: Literal["structure"], size: int | None = None
        ) -> StructureBuilder: ...
        @override
        def as_reader(self) -> StructuredTextReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        value: str | None = None,
        structure: StructureBuilder | dict[str, Any] | None = None,
        type: StructuredTextTypeEnum | None = None,
        **kwargs: Any,
    ) -> StructuredTextBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[StructuredTextReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[StructuredTextReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[StructuredTextBuilder]: ...
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
    ) -> StructuredTextReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> StructuredTextReader: ...

StructuredText: _StructuredTextModule

class _Float64List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> float: ...
        def __iter__(self) -> Iterator[float]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> float: ...
        def __setitem__(self, key: int, value: float) -> None: ...
        def __iter__(self) -> Iterator[float]: ...

class _Float32List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> float: ...
        def __iter__(self) -> Iterator[float]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> float: ...
        def __setitem__(self, key: int, value: float) -> None: ...
        def __iter__(self) -> Iterator[float]: ...

class _Int64List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Int32List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Int16List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Int8List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Uint64List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Uint32List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Uint16List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _Uint8List:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __iter__(self) -> Iterator[int]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> int: ...
        def __setitem__(self, key: int, value: int) -> None: ...
        def __iter__(self) -> Iterator[int]: ...

class _BoolList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> bool: ...
        def __iter__(self) -> Iterator[bool]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> bool: ...
        def __setitem__(self, key: int, value: bool) -> None: ...
        def __iter__(self) -> Iterator[bool]: ...

class _TextList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> str: ...
        def __iter__(self) -> Iterator[str]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> str: ...
        def __setitem__(self, key: int, value: str) -> None: ...
        def __iter__(self) -> Iterator[str]: ...

class _DataList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> bytes: ...
        def __iter__(self) -> Iterator[bytes]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> bytes: ...
        def __setitem__(self, key: int, value: bytes) -> None: ...
        def __iter__(self) -> Iterator[bytes]: ...

class _AnyPointerList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> _DynamicObjectReader: ...
        def __iter__(self) -> Iterator[_DynamicObjectReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> _DynamicObjectBuilder: ...
        def __setitem__(self, key: int, value: AnyPointer) -> None: ...
        def __iter__(self) -> Iterator[_DynamicObjectBuilder]: ...

class _PairModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def fst(self) -> _DynamicObjectReader: ...
        @property
        def snd(self) -> _DynamicObjectReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> PairBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def fst(self) -> _DynamicObjectReader: ...
        @fst.setter
        def fst(self, value: AnyPointer) -> None: ...
        @property
        def snd(self) -> _DynamicObjectReader: ...
        @snd.setter
        def snd(self, value: AnyPointer) -> None: ...
        @override
        def as_reader(self) -> PairReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        fst: AnyPointer | None = None,
        snd: AnyPointer | None = None,
        **kwargs: Any,
    ) -> PairBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[PairReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[PairReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[PairBuilder]: ...
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
    ) -> PairReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> PairReader: ...

Pair: _PairModule

class _PairList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> PairReader: ...
        def __iter__(self) -> Iterator[PairReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> PairBuilder: ...
        def __setitem__(
            self, key: int, value: PairReader | PairBuilder | dict[str, Any]
        ) -> None: ...
        def __iter__(self) -> Iterator[PairBuilder]: ...
        def init(self, index: int, size: int | None = None) -> PairBuilder: ...

class _ValueModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def f64(self) -> float: ...
        @property
        def f32(self) -> float: ...
        @property
        def i64(self) -> int: ...
        @property
        def i32(self) -> int: ...
        @property
        def i16(self) -> int: ...
        @property
        def i8(self) -> int: ...
        @property
        def ui64(self) -> int: ...
        @property
        def ui32(self) -> int: ...
        @property
        def ui16(self) -> int: ...
        @property
        def ui8(self) -> int: ...
        @property
        def b(self) -> bool: ...
        @property
        def t(self) -> str: ...
        @property
        def d(self) -> bytes: ...
        @property
        def p(self) -> _DynamicObjectReader: ...
        @property
        def cap(self) -> _DynamicObjectReader: ...
        @property
        def lf64(self) -> Float64ListReader: ...
        @property
        def lf32(self) -> Float32ListReader: ...
        @property
        def li64(self) -> Int64ListReader: ...
        @property
        def li32(self) -> Int32ListReader: ...
        @property
        def li16(self) -> Int16ListReader: ...
        @property
        def li8(self) -> Int8ListReader: ...
        @property
        def lui64(self) -> Uint64ListReader: ...
        @property
        def lui32(self) -> Uint32ListReader: ...
        @property
        def lui16(self) -> Uint16ListReader: ...
        @property
        def lui8(self) -> Uint8ListReader: ...
        @property
        def lb(self) -> BoolListReader: ...
        @property
        def lt(self) -> TextListReader: ...
        @property
        def ld(self) -> DataListReader: ...
        @property
        def lcap(self) -> AnyPointerListReader: ...
        @property
        def lpair(self) -> PairListReader: ...
        @override
        def which(
            self,
        ) -> Literal[
            "f64",
            "f32",
            "i64",
            "i32",
            "i16",
            "i8",
            "ui64",
            "ui32",
            "ui16",
            "ui8",
            "b",
            "t",
            "d",
            "p",
            "cap",
            "lf64",
            "lf32",
            "li64",
            "li32",
            "li16",
            "li8",
            "lui64",
            "lui32",
            "lui16",
            "lui8",
            "lb",
            "lt",
            "ld",
            "lcap",
            "lpair",
        ]: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> ValueBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def f64(self) -> float: ...
        @f64.setter
        def f64(self, value: float) -> None: ...
        @property
        def f32(self) -> float: ...
        @f32.setter
        def f32(self, value: float) -> None: ...
        @property
        def i64(self) -> int: ...
        @i64.setter
        def i64(self, value: int) -> None: ...
        @property
        def i32(self) -> int: ...
        @i32.setter
        def i32(self, value: int) -> None: ...
        @property
        def i16(self) -> int: ...
        @i16.setter
        def i16(self, value: int) -> None: ...
        @property
        def i8(self) -> int: ...
        @i8.setter
        def i8(self, value: int) -> None: ...
        @property
        def ui64(self) -> int: ...
        @ui64.setter
        def ui64(self, value: int) -> None: ...
        @property
        def ui32(self) -> int: ...
        @ui32.setter
        def ui32(self, value: int) -> None: ...
        @property
        def ui16(self) -> int: ...
        @ui16.setter
        def ui16(self, value: int) -> None: ...
        @property
        def ui8(self) -> int: ...
        @ui8.setter
        def ui8(self, value: int) -> None: ...
        @property
        def b(self) -> bool: ...
        @b.setter
        def b(self, value: bool) -> None: ...
        @property
        def t(self) -> str: ...
        @t.setter
        def t(self, value: str) -> None: ...
        @property
        def d(self) -> bytes: ...
        @d.setter
        def d(self, value: bytes) -> None: ...
        @property
        def p(self) -> _DynamicObjectBuilder: ...
        @p.setter
        def p(self, value: AnyPointer) -> None: ...
        @property
        def cap(self) -> _DynamicObjectReader: ...
        @cap.setter
        def cap(self, value: Capability) -> None: ...
        @property
        def lf64(self) -> Float64ListBuilder: ...
        @lf64.setter
        def lf64(
            self, value: Float64ListBuilder | Float64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def lf32(self) -> Float32ListBuilder: ...
        @lf32.setter
        def lf32(
            self, value: Float32ListBuilder | Float32ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def li64(self) -> Int64ListBuilder: ...
        @li64.setter
        def li64(
            self, value: Int64ListBuilder | Int64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def li32(self) -> Int32ListBuilder: ...
        @li32.setter
        def li32(
            self, value: Int32ListBuilder | Int32ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def li16(self) -> Int16ListBuilder: ...
        @li16.setter
        def li16(
            self, value: Int16ListBuilder | Int16ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def li8(self) -> Int8ListBuilder: ...
        @li8.setter
        def li8(
            self, value: Int8ListBuilder | Int8ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def lui64(self) -> Uint64ListBuilder: ...
        @lui64.setter
        def lui64(
            self, value: Uint64ListBuilder | Uint64ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def lui32(self) -> Uint32ListBuilder: ...
        @lui32.setter
        def lui32(
            self, value: Uint32ListBuilder | Uint32ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def lui16(self) -> Uint16ListBuilder: ...
        @lui16.setter
        def lui16(
            self, value: Uint16ListBuilder | Uint16ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def lui8(self) -> Uint8ListBuilder: ...
        @lui8.setter
        def lui8(
            self, value: Uint8ListBuilder | Uint8ListReader | dict[str, Any]
        ) -> None: ...
        @property
        def lb(self) -> BoolListBuilder: ...
        @lb.setter
        def lb(
            self, value: BoolListBuilder | BoolListReader | dict[str, Any]
        ) -> None: ...
        @property
        def lt(self) -> TextListBuilder: ...
        @lt.setter
        def lt(
            self, value: TextListBuilder | TextListReader | dict[str, Any]
        ) -> None: ...
        @property
        def ld(self) -> DataListBuilder: ...
        @ld.setter
        def ld(
            self, value: DataListBuilder | DataListReader | dict[str, Any]
        ) -> None: ...
        @property
        def lcap(self) -> AnyPointerListBuilder: ...
        @lcap.setter
        def lcap(
            self, value: AnyPointerListBuilder | AnyPointerListReader | dict[str, Any]
        ) -> None: ...
        @property
        def lpair(self) -> PairListBuilder: ...
        @lpair.setter
        def lpair(
            self, value: PairListBuilder | PairListReader | dict[str, Any]
        ) -> None: ...
        @override
        def which(
            self,
        ) -> Literal[
            "f64",
            "f32",
            "i64",
            "i32",
            "i16",
            "i8",
            "ui64",
            "ui32",
            "ui16",
            "ui8",
            "b",
            "t",
            "d",
            "p",
            "cap",
            "lf64",
            "lf32",
            "li64",
            "li32",
            "li16",
            "li8",
            "lui64",
            "lui32",
            "lui16",
            "lui8",
            "lb",
            "lt",
            "ld",
            "lcap",
            "lpair",
        ]: ...
        @overload
        def init(
            self, field: Literal["lf64"], size: int | None = None
        ) -> Float64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["lf32"], size: int | None = None
        ) -> Float32ListBuilder: ...
        @overload
        def init(
            self, field: Literal["li64"], size: int | None = None
        ) -> Int64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["li32"], size: int | None = None
        ) -> Int32ListBuilder: ...
        @overload
        def init(
            self, field: Literal["li16"], size: int | None = None
        ) -> Int16ListBuilder: ...
        @overload
        def init(
            self, field: Literal["li8"], size: int | None = None
        ) -> Int8ListBuilder: ...
        @overload
        def init(
            self, field: Literal["lui64"], size: int | None = None
        ) -> Uint64ListBuilder: ...
        @overload
        def init(
            self, field: Literal["lui32"], size: int | None = None
        ) -> Uint32ListBuilder: ...
        @overload
        def init(
            self, field: Literal["lui16"], size: int | None = None
        ) -> Uint16ListBuilder: ...
        @overload
        def init(
            self, field: Literal["lui8"], size: int | None = None
        ) -> Uint8ListBuilder: ...
        @overload
        def init(
            self, field: Literal["lb"], size: int | None = None
        ) -> BoolListBuilder: ...
        @overload
        def init(
            self, field: Literal["lt"], size: int | None = None
        ) -> TextListBuilder: ...
        @overload
        def init(
            self, field: Literal["ld"], size: int | None = None
        ) -> DataListBuilder: ...
        @overload
        def init(
            self, field: Literal["lcap"], size: int | None = None
        ) -> AnyPointerListBuilder: ...
        @overload
        def init(
            self, field: Literal["lpair"], size: int | None = None
        ) -> PairListBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> ValueReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        f64: float | None = None,
        f32: float | None = None,
        i64: int | None = None,
        i32: int | None = None,
        i16: int | None = None,
        i8: int | None = None,
        ui64: int | None = None,
        ui32: int | None = None,
        ui16: int | None = None,
        ui8: int | None = None,
        b: bool | None = None,
        t: str | None = None,
        d: bytes | None = None,
        p: AnyPointer | None = None,
        cap: Capability | None = None,
        lf64: Float64ListBuilder | dict[str, Any] | None = None,
        lf32: Float32ListBuilder | dict[str, Any] | None = None,
        li64: Int64ListBuilder | dict[str, Any] | None = None,
        li32: Int32ListBuilder | dict[str, Any] | None = None,
        li16: Int16ListBuilder | dict[str, Any] | None = None,
        li8: Int8ListBuilder | dict[str, Any] | None = None,
        lui64: Uint64ListBuilder | dict[str, Any] | None = None,
        lui32: Uint32ListBuilder | dict[str, Any] | None = None,
        lui16: Uint16ListBuilder | dict[str, Any] | None = None,
        lui8: Uint8ListBuilder | dict[str, Any] | None = None,
        lb: BoolListBuilder | dict[str, Any] | None = None,
        lt: TextListBuilder | dict[str, Any] | None = None,
        ld: DataListBuilder | dict[str, Any] | None = None,
        lcap: AnyPointerListBuilder | dict[str, Any] | None = None,
        lpair: PairListBuilder | dict[str, Any] | None = None,
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

Value: _ValueModule

class _HolderModule(_InterfaceModule):
    class ValueRequest(Protocol):
        def send(self) -> _HolderModule.HolderClient.ValueResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _HolderModule.HolderClient: ...
    class Server(_DynamicCapabilityServer):
        class ValueResult(_DynamicStructBuilder):
            @property
            def value(self) -> AnyPointer: ...
            @value.setter
            def value(self, value: AnyPointer) -> None: ...

        class ValueResultTuple(NamedTuple):
            value: AnyPointer

        class ValueParams(Protocol): ...

        class ValueCallContext(Protocol):
            params: _HolderModule.Server.ValueParams
            @property
            def results(self) -> _HolderModule.Server.ValueResult: ...

        def value(
            self,
            _context: _HolderModule.Server.ValueCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[AnyPointer | _HolderModule.Server.ValueResultTuple | None]: ...
        def value_context(
            self, context: _HolderModule.Server.ValueCallContext
        ) -> Awaitable[None]: ...

    class HolderClient(_DynamicCapabilityClient):
        class ValueResult(Awaitable[ValueResult], Protocol):
            value: _DynamicObjectReader

        def value(self) -> _HolderModule.HolderClient.ValueResult: ...
        def value_request(self) -> _HolderModule.ValueRequest: ...

Holder: _HolderModule

class _IdentifiableHolderModule(_IdentifiableModule, _HolderModule):
    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _IdentifiableHolderModule.IdentifiableHolderClient: ...
    class Server(_IdentifiableModule.Server, _HolderModule.Server): ...
    class IdentifiableHolderClient(
        _IdentifiableModule.IdentifiableClient, _HolderModule.HolderClient
    ): ...

IdentifiableHolder: _IdentifiableHolderModule

# Top-level type aliases for use in type annotations
type AnyPointerListBuilder = _AnyPointerList.Builder
type AnyPointerListReader = _AnyPointerList.Reader
type BoolListBuilder = _BoolList.Builder
type BoolListReader = _BoolList.Reader
type DataListBuilder = _DataList.Builder
type DataListReader = _DataList.Reader
type Float32ListBuilder = _Float32List.Builder
type Float32ListReader = _Float32List.Reader
type Float64ListBuilder = _Float64List.Builder
type Float64ListReader = _Float64List.Reader
type HolderClient = _HolderModule.HolderClient
type HolderServer = _HolderModule.Server
type IdInformationBuilder = _IdInformationModule.Builder
type IdInformationReader = _IdInformationModule.Reader
type IdentifiableClient = _IdentifiableModule.IdentifiableClient
type IdentifiableHolderClient = _IdentifiableHolderModule.IdentifiableHolderClient
type IdentifiableHolderServer = _IdentifiableHolderModule.Server
type IdentifiableServer = _IdentifiableModule.Server
type InfoResult = _IdentifiableModule.IdentifiableClient.InfoResult
type Int16ListBuilder = _Int16List.Builder
type Int16ListReader = _Int16List.Reader
type Int32ListBuilder = _Int32List.Builder
type Int32ListReader = _Int32List.Reader
type Int64ListBuilder = _Int64List.Builder
type Int64ListReader = _Int64List.Reader
type Int8ListBuilder = _Int8List.Builder
type Int8ListReader = _Int8List.Reader
type PairBuilder = _PairModule.Builder
type PairListBuilder = _PairList.Builder
type PairListReader = _PairList.Reader
type PairReader = _PairModule.Reader
type StructureBuilder = _StructuredTextModule._StructureModule.Builder
type StructureReader = _StructuredTextModule._StructureModule.Reader
type StructuredTextBuilder = _StructuredTextModule.Builder
type StructuredTextReader = _StructuredTextModule.Reader
type StructuredTextTypeEnum = (
    int | Literal["unstructured", "json", "xml", "toml", "sturdyRef"]
)
type TextListBuilder = _TextList.Builder
type TextListReader = _TextList.Reader
type Uint16ListBuilder = _Uint16List.Builder
type Uint16ListReader = _Uint16List.Reader
type Uint32ListBuilder = _Uint32List.Builder
type Uint32ListReader = _Uint32List.Reader
type Uint64ListBuilder = _Uint64List.Builder
type Uint64ListReader = _Uint64List.Reader
type Uint8ListBuilder = _Uint8List.Builder
type Uint8ListReader = _Uint8List.Reader
type ValueBuilder = _ValueModule.Builder
type ValueReader = _ValueModule.Reader
type ValueResult = _HolderModule.HolderClient.ValueResult
