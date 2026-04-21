"""Reader helper types for `storage.capnp`."""

from collections.abc import Callable
from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicObjectReader,
    _DynamicStructReader,
)

from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.storage.storage_capnp.types import builders as builders
from mas.schema.storage.storage_capnp.types import clients as clients
from mas.schema.storage.storage_capnp.types import lists as lists

class ValueReader(_DynamicStructReader):
    @property
    def boolValue(self) -> bool: ...
    @property
    def boolListValue(self) -> BoolListReader: ...
    @property
    def int8Value(self) -> int: ...
    @property
    def int8ListValue(self) -> Int8ListReader: ...
    @property
    def int16Value(self) -> int: ...
    @property
    def int16ListValue(self) -> Int16ListReader: ...
    @property
    def int32Value(self) -> int: ...
    @property
    def int32ListValue(self) -> Int32ListReader: ...
    @property
    def int64Value(self) -> int: ...
    @property
    def int64ListValue(self) -> Int64ListReader: ...
    @property
    def uint8Value(self) -> int: ...
    @property
    def uint8ListValue(self) -> Uint8ListReader: ...
    @property
    def uint16Value(self) -> int: ...
    @property
    def uint16ListValue(self) -> Uint16ListReader: ...
    @property
    def uint32Value(self) -> int: ...
    @property
    def uint32ListValue(self) -> Uint32ListReader: ...
    @property
    def uint64Value(self) -> int: ...
    @property
    def uint64ListValue(self) -> Uint64ListReader: ...
    @property
    def float32Value(self) -> float: ...
    @property
    def float32ListValue(self) -> Float32ListReader: ...
    @property
    def float64Value(self) -> float: ...
    @property
    def float64ListValue(self) -> Float64ListReader: ...
    @property
    def textValue(self) -> str: ...
    @property
    def textListValue(self) -> TextListReader: ...
    @property
    def dataValue(self) -> bytes: ...
    @property
    def dataListValue(self) -> DataListReader: ...
    @property
    def anyValue(self) -> _DynamicObjectReader: ...
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
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ValueBuilder: ...

class KeyAndEntryReader(_DynamicStructReader):
    @property
    def key(self) -> str: ...
    @property
    def entry(self) -> clients.EntryClient: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.KeyAndEntryBuilder: ...

class InfoAndContainerReader(_DynamicStructReader):
    @property
    def id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def container(self) -> clients.ContainerClient: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.InfoAndContainerBuilder: ...

class ImportExportDataReader(_DynamicStructReader):
    @property
    def info(self) -> IdInformationReader: ...
    @property
    def entries(self) -> PairListReader: ...
    @property
    def isAnyValue(self) -> BoolListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ImportExportDataBuilder: ...

type BoolListReader = lists._BoolList.Reader

type DataListReader = lists._DataList.Reader

type Float32ListReader = lists._Float32List.Reader

type Float64ListReader = lists._Float64List.Reader

type InfoAndContainerListReader = lists._InfoAndContainerList.Reader

type Int16ListReader = lists._Int16List.Reader

type Int32ListReader = lists._Int32List.Reader

type Int64ListReader = lists._Int64List.Reader

type Int8ListReader = lists._Int8List.Reader

type KeyAndEntryListReader = lists._KeyAndEntryList.Reader

type PairListReader = lists._PairList.Reader

type TextListReader = lists._TextList.Reader

type Uint16ListReader = lists._Uint16List.Reader

type Uint32ListReader = lists._Uint32List.Reader

type Uint64ListReader = lists._Uint64List.Reader

type Uint8ListReader = lists._Uint8List.Reader
