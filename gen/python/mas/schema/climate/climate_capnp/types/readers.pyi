"""Reader helper types for `climate.capnp`."""

from collections.abc import Callable
from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicObjectReader,
    _DynamicStructReader,
)

from mas.schema.climate.climate_capnp.types import builders as builders
from mas.schema.climate.climate_capnp.types import clients as clients
from mas.schema.climate.climate_capnp.types import enums as enums
from mas.schema.climate.climate_capnp.types import lists as lists
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader

class EnsembleMemberReader(_DynamicStructReader):
    @property
    def r(self) -> int: ...
    @property
    def i(self) -> int: ...
    @property
    def p(self) -> int: ...
    @property
    def f(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.EnsembleMemberBuilder: ...

class ValueReader(_DynamicStructReader):
    @property
    def text(self) -> str: ...
    @property
    def float(self) -> float: ...
    @property
    def int(self) -> int: ...
    @property
    def bool(self) -> bool: ...
    @property
    def date(self) -> DateReader: ...
    @override
    def which(self) -> Literal["text", "float", "int", "bool", "date"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ValueBuilder: ...

class EntryReader(_DynamicStructReader):
    @property
    def gcm(self) -> enums.GCMEnum: ...
    @property
    def rcm(self) -> enums.RCMEnum: ...
    @property
    def historical(self) -> None: ...
    @property
    def rcp(self) -> enums.RCPEnum: ...
    @property
    def ssp(self) -> enums.SSPEnum: ...
    @property
    def ensMem(self) -> EnsembleMemberReader: ...
    @property
    def version(self) -> str: ...
    @property
    def start(self) -> DateReader: ...
    @property
    def end(self) -> DateReader: ...
    @property
    def co2(self) -> float: ...
    @property
    def picontrol(self) -> None: ...
    @property
    def description(self) -> str: ...
    @override
    def which(
        self,
    ) -> Literal[
        "gcm",
        "rcm",
        "historical",
        "rcp",
        "ssp",
        "ensMem",
        "version",
        "start",
        "end",
        "co2",
        "picontrol",
        "description",
    ]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.EntryBuilder: ...

class MetadataReader(_DynamicStructReader):
    @property
    def entries(self) -> EntryListReader: ...
    @property
    def info(self) -> clients.InformationClient: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.MetadataBuilder: ...

class KVReader(_DynamicStructReader):
    @property
    def key(self) -> str: ...
    @property
    def value(self) -> _DynamicObjectReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.KVBuilder: ...

class LocationReader(_DynamicStructReader):
    @property
    def id(self) -> IdInformationReader: ...
    @property
    def heightNN(self) -> float: ...
    @property
    def latlon(self) -> LatLonCoordReader: ...
    @property
    def timeSeries(self) -> clients.TimeSeriesClient: ...
    @property
    def customData(self) -> KVListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.LocationBuilder: ...

class MetaPlusDataReader(_DynamicStructReader):
    @property
    def meta(self) -> MetadataReader: ...
    @property
    def data(self) -> clients.DatasetClient: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.MetaPlusDataBuilder: ...

class TimeSeriesDataReader(_DynamicStructReader):
    @property
    def data(self) -> Float32ListListReader: ...
    @property
    def isTransposed(self) -> bool: ...
    @property
    def header(self) -> ElementEnumListReader: ...
    @property
    def startDate(self) -> DateReader: ...
    @property
    def endDate(self) -> DateReader: ...
    @property
    def resolution(self) -> enums.TimeSeriesResolutionEnum: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.TimeSeriesDataBuilder: ...

class CSVConfigReader(_DynamicStructReader):
    @property
    def sep(self) -> str: ...
    @property
    def headerMap(self) -> PairListReader: ...
    @property
    def skipLinesToHeader(self) -> int: ...
    @property
    def skipLinesFromHeaderToData(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.CSVConfigBuilder: ...

class AlteredReader(_DynamicStructReader):
    @property
    def element(self) -> enums.ElementEnum: ...
    @property
    def value(self) -> float: ...
    @property
    def type(self) -> enums.AlterTimeSeriesWrapperAlterTypeEnum: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.AlteredBuilder: ...

type AlteredListReader = lists._AlteredList.Reader

type DatasetClientListReader = lists._DatasetClientList.Reader

type ElementEnumListReader = lists._ElementEnumList.Reader

type EntryListReader = lists._EntryList.Reader

type Float32ListListReader = lists._Float32ListList.Reader

type Float32ListReader = lists._Float32List.Reader

type IdInformationListReader = lists._IdInformationList.Reader

type KVListReader = lists._KVList.Reader

type LocationListReader = lists._LocationList.Reader

type MetaPlusDataListReader = lists._MetaPlusDataList.Reader

type PairListReader = lists._PairList.Reader
