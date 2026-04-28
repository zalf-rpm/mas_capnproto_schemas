"""Builder helper types for `common.capnp`."""

from typing import Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
    _DynamicStructBuilder,
)

from mas.schema.common.common_capnp.types import common as common
from mas.schema.common.common_capnp.types import enums as enums
from mas.schema.common.common_capnp.types import lists as lists
from mas.schema.common.common_capnp.types import readers as readers

class IdInformationBuilder(_DynamicStructBuilder):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> None: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str) -> None: ...
    @override
    def as_reader(self) -> readers.IdInformationReader: ...

class StructuredTextStructureBuilder(_DynamicStructBuilder):
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
    def as_reader(self) -> readers.StructuredTextStructureReader: ...

class StructuredTextBuilder(_DynamicStructBuilder):
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str) -> None: ...
    @property
    def structure(self) -> StructuredTextStructureBuilder: ...
    @structure.setter
    def structure(
        self,
        value: StructuredTextStructureBuilder
        | readers.StructuredTextStructureReader
        | dict[str, Any],
    ) -> None: ...
    @property
    def type(self) -> enums.StructuredTextTypeEnum: ...
    @type.setter
    def type(self, value: enums.StructuredTextTypeEnum) -> None: ...
    @override
    def init(
        self,
        field: Literal["structure"],
        size: int | None = None,
    ) -> StructuredTextStructureBuilder: ...
    @override
    def as_reader(self) -> readers.StructuredTextReader: ...

class PairBuilder(_DynamicStructBuilder):
    @property
    def fst(self) -> _DynamicObjectBuilder: ...
    @fst.setter
    def fst(self, value: common.AnyPointer) -> None: ...
    @property
    def snd(self) -> _DynamicObjectBuilder: ...
    @snd.setter
    def snd(self, value: common.AnyPointer) -> None: ...
    @override
    def as_reader(self) -> readers.PairReader: ...

class ValueBuilder(_DynamicStructBuilder):
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
    def p(self, value: common.AnyPointer) -> None: ...
    @property
    def cap(self) -> _DynamicObjectBuilder: ...
    @cap.setter
    def cap(self, value: common.Capability) -> None: ...
    @property
    def lf64(self) -> Float64ListBuilder: ...
    @lf64.setter
    def lf64(
        self,
        value: Float64ListBuilder | readers.Float64ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def lf32(self) -> Float32ListBuilder: ...
    @lf32.setter
    def lf32(
        self,
        value: Float32ListBuilder | readers.Float32ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def li64(self) -> Int64ListBuilder: ...
    @li64.setter
    def li64(
        self,
        value: Int64ListBuilder | readers.Int64ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def li32(self) -> Int32ListBuilder: ...
    @li32.setter
    def li32(
        self,
        value: Int32ListBuilder | readers.Int32ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def li16(self) -> Int16ListBuilder: ...
    @li16.setter
    def li16(
        self,
        value: Int16ListBuilder | readers.Int16ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def li8(self) -> Int8ListBuilder: ...
    @li8.setter
    def li8(
        self,
        value: Int8ListBuilder | readers.Int8ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def lui64(self) -> Uint64ListBuilder: ...
    @lui64.setter
    def lui64(
        self,
        value: Uint64ListBuilder | readers.Uint64ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def lui32(self) -> Uint32ListBuilder: ...
    @lui32.setter
    def lui32(
        self,
        value: Uint32ListBuilder | readers.Uint32ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def lui16(self) -> Uint16ListBuilder: ...
    @lui16.setter
    def lui16(
        self,
        value: Uint16ListBuilder | readers.Uint16ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def lui8(self) -> Uint8ListBuilder: ...
    @lui8.setter
    def lui8(
        self,
        value: Uint8ListBuilder | readers.Uint8ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def lb(self) -> BoolListBuilder: ...
    @lb.setter
    def lb(
        self,
        value: BoolListBuilder | readers.BoolListReader | dict[str, Any],
    ) -> None: ...
    @property
    def lt(self) -> TextListBuilder: ...
    @lt.setter
    def lt(
        self,
        value: TextListBuilder | readers.TextListReader | dict[str, Any],
    ) -> None: ...
    @property
    def ld(self) -> DataListBuilder: ...
    @ld.setter
    def ld(
        self,
        value: DataListBuilder | readers.DataListReader | dict[str, Any],
    ) -> None: ...
    @property
    def lcap(self) -> AnyPointerListBuilder: ...
    @lcap.setter
    def lcap(
        self,
        value: AnyPointerListBuilder | readers.AnyPointerListReader | dict[str, Any],
    ) -> None: ...
    @property
    def lpair(self) -> PairListBuilder: ...
    @lpair.setter
    def lpair(
        self,
        value: PairListBuilder | readers.PairListReader | dict[str, Any],
    ) -> None: ...
    @property
    def lv(self) -> ValueListBuilder: ...
    @lv.setter
    def lv(
        self,
        value: ValueListBuilder | readers.ValueListReader | dict[str, Any],
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
        "lv",
    ]: ...
    @override
    @overload
    def init(
        self,
        field: Literal["lf64"],
        size: int | None = None,
    ) -> Float64ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["lf32"],
        size: int | None = None,
    ) -> Float32ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["li64"],
        size: int | None = None,
    ) -> Int64ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["li32"],
        size: int | None = None,
    ) -> Int32ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["li16"],
        size: int | None = None,
    ) -> Int16ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["li8"],
        size: int | None = None,
    ) -> Int8ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["lui64"],
        size: int | None = None,
    ) -> Uint64ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["lui32"],
        size: int | None = None,
    ) -> Uint32ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["lui16"],
        size: int | None = None,
    ) -> Uint16ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["lui8"],
        size: int | None = None,
    ) -> Uint8ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["lb"],
        size: int | None = None,
    ) -> BoolListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["lt"],
        size: int | None = None,
    ) -> TextListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["ld"],
        size: int | None = None,
    ) -> DataListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["lcap"],
        size: int | None = None,
    ) -> AnyPointerListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["lpair"],
        size: int | None = None,
    ) -> PairListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["lv"],
        size: int | None = None,
    ) -> ValueListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.ValueReader: ...

type AnyPointerListBuilder = lists._AnyPointerList.Builder

type BoolListBuilder = lists._BoolList.Builder

type DataListBuilder = lists._DataList.Builder

type Float32ListBuilder = lists._Float32List.Builder

type Float64ListBuilder = lists._Float64List.Builder

type Int16ListBuilder = lists._Int16List.Builder

type Int32ListBuilder = lists._Int32List.Builder

type Int64ListBuilder = lists._Int64List.Builder

type Int8ListBuilder = lists._Int8List.Builder

type PairListBuilder = lists._PairList.Builder

type TextListBuilder = lists._TextList.Builder

type Uint16ListBuilder = lists._Uint16List.Builder

type Uint32ListBuilder = lists._Uint32List.Builder

type Uint64ListBuilder = lists._Uint64List.Builder

type Uint8ListBuilder = lists._Uint8List.Builder

type ValueListBuilder = lists._ValueList.Builder
