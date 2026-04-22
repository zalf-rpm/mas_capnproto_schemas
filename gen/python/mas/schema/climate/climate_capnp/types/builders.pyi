"""Builder helper types for `climate.capnp`."""

from typing import Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
    _DynamicStructBuilder,
)

from mas.schema.climate.climate_capnp.types import clients as clients
from mas.schema.climate.climate_capnp.types import common as common
from mas.schema.climate.climate_capnp.types import enums as enums
from mas.schema.climate.climate_capnp.types import lists as lists
from mas.schema.climate.climate_capnp.types import modules as modules
from mas.schema.climate.climate_capnp.types import readers as readers
from mas.schema.common.common_capnp.types.builders import (
    IdInformationBuilder,
)
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader

class EnsembleMemberBuilder(_DynamicStructBuilder):
    @property
    def r(self) -> int: ...
    @r.setter
    def r(self, value: int) -> None: ...
    @property
    def i(self) -> int: ...
    @i.setter
    def i(self, value: int) -> None: ...
    @property
    def p(self) -> int: ...
    @p.setter
    def p(self, value: int) -> None: ...
    @property
    def f(self) -> int: ...
    @f.setter
    def f(self, value: int) -> None: ...
    @override
    def as_reader(self) -> readers.EnsembleMemberReader: ...

class ValueBuilder(_DynamicStructBuilder):
    @property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str) -> None: ...
    @property
    def float(self) -> float: ...
    @float.setter
    def float(self, value: float) -> None: ...
    @property
    def int(self) -> int: ...
    @int.setter
    def int(self, value: int) -> None: ...
    @property
    def bool(self) -> bool: ...
    @bool.setter
    def bool(self, value: bool) -> None: ...
    @property
    def date(self) -> DateBuilder: ...
    @date.setter
    def date(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
    @override
    def which(self) -> Literal["text", "float", "int", "bool", "date"]: ...
    @override
    def init(self, field: Literal["date"], size: int | None = None) -> DateBuilder: ...
    @override
    def as_reader(self) -> readers.ValueReader: ...

class EntryBuilder(_DynamicStructBuilder):
    @property
    def gcm(self) -> enums.GCMEnum: ...
    @gcm.setter
    def gcm(self, value: enums.GCMEnum) -> None: ...
    @property
    def rcm(self) -> enums.RCMEnum: ...
    @rcm.setter
    def rcm(self, value: enums.RCMEnum) -> None: ...
    @property
    def historical(self) -> None: ...
    @historical.setter
    def historical(self, value: None) -> None: ...
    @property
    def rcp(self) -> enums.RCPEnum: ...
    @rcp.setter
    def rcp(self, value: enums.RCPEnum) -> None: ...
    @property
    def ssp(self) -> enums.SSPEnum: ...
    @ssp.setter
    def ssp(self, value: enums.SSPEnum) -> None: ...
    @property
    def ensMem(self) -> EnsembleMemberBuilder: ...
    @ensMem.setter
    def ensMem(
        self,
        value: EnsembleMemberBuilder | readers.EnsembleMemberReader | dict[str, Any],
    ) -> None: ...
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str) -> None: ...
    @property
    def start(self) -> DateBuilder: ...
    @start.setter
    def start(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
    @property
    def end(self) -> DateBuilder: ...
    @end.setter
    def end(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
    @property
    def co2(self) -> float: ...
    @co2.setter
    def co2(self, value: float) -> None: ...
    @property
    def picontrol(self) -> None: ...
    @picontrol.setter
    def picontrol(self, value: None) -> None: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str) -> None: ...
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
    @overload
    def init(
        self,
        field: Literal["ensMem"],
        size: int | None = None,
    ) -> EnsembleMemberBuilder: ...
    @overload
    def init(self, field: Literal["start"], size: int | None = None) -> DateBuilder: ...
    @overload
    def init(self, field: Literal["end"], size: int | None = None) -> DateBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.EntryReader: ...

class MetadataBuilder(_DynamicStructBuilder):
    @property
    def entries(self) -> EntryListBuilder: ...
    @entries.setter
    def entries(
        self,
        value: EntryListBuilder | readers.EntryListReader | dict[str, Any],
    ) -> None: ...
    @property
    def info(self) -> clients.InformationClient: ...
    @info.setter
    def info(
        self,
        value: clients.InformationClient
        | modules._MetadataStructModule._InformationInterfaceModule.Server,
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["entries"],
        size: int | None = None,
    ) -> EntryListBuilder: ...
    @override
    def as_reader(self) -> readers.MetadataReader: ...

class KVBuilder(_DynamicStructBuilder):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str) -> None: ...
    @property
    def value(self) -> _DynamicObjectBuilder: ...
    @value.setter
    def value(self, value: common.AnyPointer) -> None: ...
    @override
    def as_reader(self) -> readers.KVReader: ...

class LocationBuilder(_DynamicStructBuilder):
    @property
    def id(self) -> IdInformationBuilder: ...
    @id.setter
    def id(
        self,
        value: IdInformationBuilder | IdInformationReader | dict[str, Any],
    ) -> None: ...
    @property
    def heightNN(self) -> float: ...
    @heightNN.setter
    def heightNN(self, value: float) -> None: ...
    @property
    def latlon(self) -> LatLonCoordBuilder: ...
    @latlon.setter
    def latlon(
        self,
        value: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any],
    ) -> None: ...
    @property
    def timeSeries(self) -> clients.TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: clients.TimeSeriesClient | modules._TimeSeriesInterfaceModule.Server,
    ) -> None: ...
    @property
    def customData(self) -> KVListBuilder: ...
    @customData.setter
    def customData(
        self,
        value: KVListBuilder | readers.KVListReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["id"],
        size: int | None = None,
    ) -> IdInformationBuilder: ...
    @overload
    def init(
        self,
        field: Literal["latlon"],
        size: int | None = None,
    ) -> LatLonCoordBuilder: ...
    @overload
    def init(
        self,
        field: Literal["customData"],
        size: int | None = None,
    ) -> KVListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.LocationReader: ...

class MetaPlusDataBuilder(_DynamicStructBuilder):
    @property
    def meta(self) -> MetadataBuilder: ...
    @meta.setter
    def meta(
        self,
        value: MetadataBuilder | readers.MetadataReader | dict[str, Any],
    ) -> None: ...
    @property
    def data(self) -> clients.DatasetClient: ...
    @data.setter
    def data(
        self,
        value: clients.DatasetClient | modules._DatasetInterfaceModule.Server,
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["meta"],
        size: int | None = None,
    ) -> MetadataBuilder: ...
    @override
    def as_reader(self) -> readers.MetaPlusDataReader: ...

class TimeSeriesDataBuilder(_DynamicStructBuilder):
    @property
    def data(self) -> Float32ListListBuilder: ...
    @data.setter
    def data(
        self,
        value: Float32ListListBuilder | readers.Float32ListListReader | dict[str, Any],
    ) -> None: ...
    @property
    def isTransposed(self) -> bool: ...
    @isTransposed.setter
    def isTransposed(self, value: bool) -> None: ...
    @property
    def header(self) -> ElementEnumListBuilder: ...
    @header.setter
    def header(
        self,
        value: ElementEnumListBuilder | readers.ElementEnumListReader | dict[str, Any],
    ) -> None: ...
    @property
    def startDate(self) -> DateBuilder: ...
    @startDate.setter
    def startDate(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
    @property
    def endDate(self) -> DateBuilder: ...
    @endDate.setter
    def endDate(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
    @property
    def resolution(self) -> enums.TimeSeriesResolutionEnum: ...
    @resolution.setter
    def resolution(self, value: enums.TimeSeriesResolutionEnum) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["startDate"],
        size: int | None = None,
    ) -> DateBuilder: ...
    @overload
    def init(
        self,
        field: Literal["endDate"],
        size: int | None = None,
    ) -> DateBuilder: ...
    @overload
    def init(
        self,
        field: Literal["data"],
        size: int | None = None,
    ) -> Float32ListListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["header"],
        size: int | None = None,
    ) -> ElementEnumListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.TimeSeriesDataReader: ...

class CSVConfigBuilder(_DynamicStructBuilder):
    @property
    def sep(self) -> str: ...
    @sep.setter
    def sep(self, value: str) -> None: ...
    @property
    def headerMap(self) -> PairListBuilder: ...
    @headerMap.setter
    def headerMap(
        self,
        value: PairListBuilder | readers.PairListReader | dict[str, Any],
    ) -> None: ...
    @property
    def skipLinesToHeader(self) -> int: ...
    @skipLinesToHeader.setter
    def skipLinesToHeader(self, value: int) -> None: ...
    @property
    def skipLinesFromHeaderToData(self) -> int: ...
    @skipLinesFromHeaderToData.setter
    def skipLinesFromHeaderToData(self, value: int) -> None: ...
    @override
    def init(
        self,
        field: Literal["headerMap"],
        size: int | None = None,
    ) -> PairListBuilder: ...
    @override
    def as_reader(self) -> readers.CSVConfigReader: ...

class AlteredBuilder(_DynamicStructBuilder):
    @property
    def element(self) -> enums.ElementEnum: ...
    @element.setter
    def element(self, value: enums.ElementEnum) -> None: ...
    @property
    def value(self) -> float: ...
    @value.setter
    def value(self, value: float) -> None: ...
    @property
    def type(self) -> enums.AlterTimeSeriesWrapperAlterTypeEnum: ...
    @type.setter
    def type(self, value: enums.AlterTimeSeriesWrapperAlterTypeEnum) -> None: ...
    @override
    def as_reader(self) -> readers.AlteredReader: ...

type AlteredListBuilder = lists._AlteredList.Builder

type DatasetClientListBuilder = lists._DatasetClientList.Builder

type ElementEnumListBuilder = lists._ElementEnumList.Builder

type EntryListBuilder = lists._EntryList.Builder

type Float32ListBuilder = lists._Float32List.Builder

type Float32ListListBuilder = lists._Float32ListList.Builder

type IdInformationListBuilder = lists._IdInformationList.Builder

type KVListBuilder = lists._KVList.Builder

type LocationListBuilder = lists._LocationList.Builder

type MetaPlusDataListBuilder = lists._MetaPlusDataList.Builder

type PairListBuilder = lists._PairList.Builder
