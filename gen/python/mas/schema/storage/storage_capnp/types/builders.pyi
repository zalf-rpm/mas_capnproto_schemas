"""Builder helper types for `storage.capnp`."""

from typing import Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.storage.storage_capnp.types import clients as clients
from mas.schema.storage.storage_capnp.types import common as common
from mas.schema.storage.storage_capnp.types import lists as lists
from mas.schema.storage.storage_capnp.types import modules as modules
from mas.schema.storage.storage_capnp.types import readers as readers

class ValueBuilder(_DynamicStructBuilder):
    @property
    def boolValue(self) -> bool: ...
    @boolValue.setter
    def boolValue(self, value: bool) -> None: ...
    @property
    def boolListValue(self) -> BoolListBuilder: ...
    @boolListValue.setter
    def boolListValue(
        self,
        value: BoolListBuilder | readers.BoolListReader | dict[str, Any],
    ) -> None: ...
    @property
    def int8Value(self) -> int: ...
    @int8Value.setter
    def int8Value(self, value: int) -> None: ...
    @property
    def int8ListValue(self) -> Int8ListBuilder: ...
    @int8ListValue.setter
    def int8ListValue(
        self,
        value: Int8ListBuilder | readers.Int8ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def int16Value(self) -> int: ...
    @int16Value.setter
    def int16Value(self, value: int) -> None: ...
    @property
    def int16ListValue(self) -> Int16ListBuilder: ...
    @int16ListValue.setter
    def int16ListValue(
        self,
        value: Int16ListBuilder | readers.Int16ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def int32Value(self) -> int: ...
    @int32Value.setter
    def int32Value(self, value: int) -> None: ...
    @property
    def int32ListValue(self) -> Int32ListBuilder: ...
    @int32ListValue.setter
    def int32ListValue(
        self,
        value: Int32ListBuilder | readers.Int32ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def int64Value(self) -> int: ...
    @int64Value.setter
    def int64Value(self, value: int) -> None: ...
    @property
    def int64ListValue(self) -> Int64ListBuilder: ...
    @int64ListValue.setter
    def int64ListValue(
        self,
        value: Int64ListBuilder | readers.Int64ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def uint8Value(self) -> int: ...
    @uint8Value.setter
    def uint8Value(self, value: int) -> None: ...
    @property
    def uint8ListValue(self) -> Uint8ListBuilder: ...
    @uint8ListValue.setter
    def uint8ListValue(
        self,
        value: Uint8ListBuilder | readers.Uint8ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def uint16Value(self) -> int: ...
    @uint16Value.setter
    def uint16Value(self, value: int) -> None: ...
    @property
    def uint16ListValue(self) -> Uint16ListBuilder: ...
    @uint16ListValue.setter
    def uint16ListValue(
        self,
        value: Uint16ListBuilder | readers.Uint16ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def uint32Value(self) -> int: ...
    @uint32Value.setter
    def uint32Value(self, value: int) -> None: ...
    @property
    def uint32ListValue(self) -> Uint32ListBuilder: ...
    @uint32ListValue.setter
    def uint32ListValue(
        self,
        value: Uint32ListBuilder | readers.Uint32ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def uint64Value(self) -> int: ...
    @uint64Value.setter
    def uint64Value(self, value: int) -> None: ...
    @property
    def uint64ListValue(self) -> Uint64ListBuilder: ...
    @uint64ListValue.setter
    def uint64ListValue(
        self,
        value: Uint64ListBuilder | readers.Uint64ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def float32Value(self) -> float: ...
    @float32Value.setter
    def float32Value(self, value: float) -> None: ...
    @property
    def float32ListValue(self) -> Float32ListBuilder: ...
    @float32ListValue.setter
    def float32ListValue(
        self,
        value: Float32ListBuilder | readers.Float32ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def float64Value(self) -> float: ...
    @float64Value.setter
    def float64Value(self, value: float) -> None: ...
    @property
    def float64ListValue(self) -> Float64ListBuilder: ...
    @float64ListValue.setter
    def float64ListValue(
        self,
        value: Float64ListBuilder | readers.Float64ListReader | dict[str, Any],
    ) -> None: ...
    @property
    def textValue(self) -> str: ...
    @textValue.setter
    def textValue(self, value: str) -> None: ...
    @property
    def textListValue(self) -> TextListBuilder: ...
    @textListValue.setter
    def textListValue(
        self,
        value: TextListBuilder | readers.TextListReader | dict[str, Any],
    ) -> None: ...
    @property
    def dataValue(self) -> bytes: ...
    @dataValue.setter
    def dataValue(self, value: bytes) -> None: ...
    @property
    def dataListValue(self) -> DataListBuilder: ...
    @dataListValue.setter
    def dataListValue(
        self,
        value: DataListBuilder | readers.DataListReader | dict[str, Any],
    ) -> None: ...
    @property
    def anyValue(self) -> _DynamicStructBuilder: ...
    @anyValue.setter
    def anyValue(self, value: common.AnyStruct | dict[str, Any]) -> None: ...
    @override
    def which(
        self,
    ) -> Literal[
        "boolValue",
        "boolListValue",
        "int8Value",
        "int8ListValue",
        "int16Value",
        "int16ListValue",
        "int32Value",
        "int32ListValue",
        "int64Value",
        "int64ListValue",
        "uint8Value",
        "uint8ListValue",
        "uint16Value",
        "uint16ListValue",
        "uint32Value",
        "uint32ListValue",
        "uint64Value",
        "uint64ListValue",
        "float32Value",
        "float32ListValue",
        "float64Value",
        "float64ListValue",
        "textValue",
        "textListValue",
        "dataValue",
        "dataListValue",
        "anyValue",
    ]: ...
    @override
    @overload
    def init(
        self,
        field: Literal["boolListValue"],
        size: int | None = None,
    ) -> BoolListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["int8ListValue"],
        size: int | None = None,
    ) -> Int8ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["int16ListValue"],
        size: int | None = None,
    ) -> Int16ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["int32ListValue"],
        size: int | None = None,
    ) -> Int32ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["int64ListValue"],
        size: int | None = None,
    ) -> Int64ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["uint8ListValue"],
        size: int | None = None,
    ) -> Uint8ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["uint16ListValue"],
        size: int | None = None,
    ) -> Uint16ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["uint32ListValue"],
        size: int | None = None,
    ) -> Uint32ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["uint64ListValue"],
        size: int | None = None,
    ) -> Uint64ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["float32ListValue"],
        size: int | None = None,
    ) -> Float32ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["float64ListValue"],
        size: int | None = None,
    ) -> Float64ListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["textListValue"],
        size: int | None = None,
    ) -> TextListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["dataListValue"],
        size: int | None = None,
    ) -> DataListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.ValueReader: ...

class KeyAndEntryBuilder(_DynamicStructBuilder):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str) -> None: ...
    @property
    def entry(self) -> clients.EntryClient: ...
    @entry.setter
    def entry(
        self,
        value: clients.EntryClient
        | modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule.Server,
    ) -> None: ...
    @override
    def as_reader(self) -> readers.KeyAndEntryReader: ...

class InfoAndContainerBuilder(_DynamicStructBuilder):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> None: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def container(self) -> clients.ContainerClient: ...
    @container.setter
    def container(
        self,
        value: clients.ContainerClient
        | modules._StoreInterfaceModule._ContainerInterfaceModule.Server,
    ) -> None: ...
    @override
    def as_reader(self) -> readers.InfoAndContainerReader: ...

class ImportExportDataBuilder(_DynamicStructBuilder):
    @property
    def info(self) -> IdInformationBuilder: ...
    @info.setter
    def info(
        self,
        value: IdInformationBuilder | IdInformationReader | dict[str, Any],
    ) -> None: ...
    @property
    def entries(self) -> PairListBuilder: ...
    @entries.setter
    def entries(
        self,
        value: PairListBuilder | readers.PairListReader | dict[str, Any],
    ) -> None: ...
    @property
    def isAnyValue(self) -> BoolListBuilder: ...
    @isAnyValue.setter
    def isAnyValue(
        self,
        value: BoolListBuilder | readers.BoolListReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["info"],
        size: int | None = None,
    ) -> IdInformationBuilder: ...
    @overload
    def init(
        self,
        field: Literal["entries"],
        size: int | None = None,
    ) -> PairListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["isAnyValue"],
        size: int | None = None,
    ) -> BoolListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.ImportExportDataReader: ...

type BoolListBuilder = lists._BoolList.Builder

type DataListBuilder = lists._DataList.Builder

type Float32ListBuilder = lists._Float32List.Builder

type Float64ListBuilder = lists._Float64List.Builder

type InfoAndContainerListBuilder = lists._InfoAndContainerList.Builder

type Int16ListBuilder = lists._Int16List.Builder

type Int32ListBuilder = lists._Int32List.Builder

type Int64ListBuilder = lists._Int64List.Builder

type Int8ListBuilder = lists._Int8List.Builder

type KeyAndEntryListBuilder = lists._KeyAndEntryList.Builder

type PairListBuilder = lists._PairList.Builder

type TextListBuilder = lists._TextList.Builder

type Uint16ListBuilder = lists._Uint16List.Builder

type Uint32ListBuilder = lists._Uint32List.Builder

type Uint64ListBuilder = lists._Uint64List.Builder

type Uint8ListBuilder = lists._Uint8List.Builder
