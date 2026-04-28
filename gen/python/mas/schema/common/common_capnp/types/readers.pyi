"""Reader helper types for `common.capnp`."""

from collections.abc import Callable
from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicObjectReader,
    _DynamicStructReader,
)

from mas.schema.common.common_capnp.types import builders as builders
from mas.schema.common.common_capnp.types import enums as enums
from mas.schema.common.common_capnp.types import lists as lists

class IdInformationReader(_DynamicStructReader):
    @property
    def id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def description(self) -> str: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.IdInformationBuilder: ...

class StructuredTextStructureReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.StructuredTextStructureBuilder: ...

class StructuredTextReader(_DynamicStructReader):
    @property
    def value(self) -> str: ...
    @property
    def structure(self) -> StructuredTextStructureReader: ...
    @property
    def type(self) -> enums.StructuredTextTypeEnum: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.StructuredTextBuilder: ...

class PairReader(_DynamicStructReader):
    @property
    def fst(self) -> _DynamicObjectReader: ...
    @property
    def snd(self) -> _DynamicObjectReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.PairBuilder: ...

class ValueReader(_DynamicStructReader):
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
    @property
    def lv(self) -> ValueListReader: ...
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
        "lv",
    ]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ValueBuilder: ...

type AnyPointerListReader = lists._AnyPointerList.Reader

type BoolListReader = lists._BoolList.Reader

type DataListReader = lists._DataList.Reader

type Float32ListReader = lists._Float32List.Reader

type Float64ListReader = lists._Float64List.Reader

type Int16ListReader = lists._Int16List.Reader

type Int32ListReader = lists._Int32List.Reader

type Int64ListReader = lists._Int64List.Reader

type Int8ListReader = lists._Int8List.Reader

type PairListReader = lists._PairList.Reader

type TextListReader = lists._TextList.Reader

type Uint16ListReader = lists._Uint16List.Reader

type Uint32ListReader = lists._Uint32List.Reader

type Uint64ListReader = lists._Uint64List.Reader

type Uint8ListReader = lists._Uint8List.Reader

type ValueListReader = lists._ValueList.Reader
