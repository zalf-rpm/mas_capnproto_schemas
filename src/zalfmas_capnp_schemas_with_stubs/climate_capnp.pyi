"""This is an automatically generated stub for `climate.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
from contextlib import contextmanager
from enum import Enum
from io import BufferedWriter
from typing import Any, BinaryIO, Literal, Protocol, overload

from capnp import _DynamicListBuilder

from .common_capnp import (
    Identifiable,
    IdInformation,
    IdInformationBuilder,
    IdInformationReader,
    Pair,
    PairBuilder,
    PairReader,
)
from .date_capnp import Date, DateBuilder, DateReader
from .geo_capnp import LatLonCoord, LatLonCoordBuilder, LatLonCoordReader
from .persistence_capnp import Persistent

class GCM(Enum):
    cccmaCanEsm2 = "cccmaCanEsm2"
    ichecEcEarth = "ichecEcEarth"
    ipslIpslCm5AMr = "ipslIpslCm5AMr"
    mirocMiroc5 = "mirocMiroc5"
    mpiMMpiEsmLr = "mpiMMpiEsmLr"
    gfdlEsm4 = "gfdlEsm4"
    ipslCm6aLr = "ipslCm6aLr"
    mpiEsm12Hr = "mpiEsm12Hr"
    mriEsm20 = "mriEsm20"
    ukesm10Ll = "ukesm10Ll"
    gswp3W5E5 = "gswp3W5E5"
    mohcHadGem2Es = "mohcHadGem2Es"

class RCM(Enum):
    clmcomCclm4817 = "clmcomCclm4817"
    gericsRemo2015 = "gericsRemo2015"
    knmiRacmo22E = "knmiRacmo22E"
    smhiRca4 = "smhiRca4"
    clmcomBtuCclm4817 = "clmcomBtuCclm4817"
    mpiCscRemo2009 = "mpiCscRemo2009"
    uhohWrf361H = "uhohWrf361H"

class SSP(Enum):
    ssp1 = "ssp1"
    ssp2 = "ssp2"
    ssp3 = "ssp3"
    ssp4 = "ssp4"
    ssp5 = "ssp5"

class RCP(Enum):
    rcp19 = "rcp19"
    rcp26 = "rcp26"
    rcp34 = "rcp34"
    rcp45 = "rcp45"
    rcp60 = "rcp60"
    rcp70 = "rcp70"
    rcp85 = "rcp85"

class EnsembleMember:
    @property
    def r(self) -> int: ...
    @property
    def i(self) -> int: ...
    @property
    def p(self) -> int: ...
    @property
    def f(self) -> int: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[EnsembleMemberReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> EnsembleMemberReader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        r: int | None = None,
        i: int | None = None,
        p: int | None = None,
        f: int | None = None,
    ) -> EnsembleMemberBuilder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> EnsembleMemberReader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> EnsembleMemberReader: ...
    def to_dict(self) -> dict: ...

class EnsembleMemberReader(EnsembleMember):
    def as_builder(self) -> EnsembleMemberBuilder: ...

class EnsembleMemberBuilder(EnsembleMember):
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
    @staticmethod
    def from_dict(dictionary: dict) -> EnsembleMemberBuilder: ...
    def copy(self) -> EnsembleMemberBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> EnsembleMemberReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class Metadata:
    class Supported(Protocol):
        class CategoriesResult(Awaitable[CategoriesResult], Protocol):
            types: Any

        def categories(self) -> CategoriesResult: ...
        class CategoriesRequest(Protocol):
            def send(self) -> Metadata.Supported.CategoriesResult: ...

        def categories_request(self) -> CategoriesRequest: ...
        class SupportedvaluesResult(Awaitable[SupportedvaluesResult], Protocol):
            values: Any

        def supportedValues(self, typeId: str) -> SupportedvaluesResult: ...
        class SupportedvaluesRequest(Protocol):
            typeId: str
            def send(self) -> Metadata.Supported.SupportedvaluesResult: ...

        def supportedValues_request(self) -> SupportedvaluesRequest: ...
        class Server:
            def categories(self, **kwargs) -> Awaitable[Any]: ...
            def supportedValues(self, typeId: str, **kwargs) -> Awaitable[Any]: ...

    class Value:
        @property
        def text(self) -> str: ...
        @property
        def float(self) -> float: ...
        @property
        def int(self) -> int: ...
        @property
        def bool(self) -> bool: ...
        @property
        def date(self) -> Date: ...
        def which(self) -> Literal["text", "float", "int", "bool", "date"]: ...
        def init(self, name: Literal["date"]) -> Date: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Metadata.ValueReader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Metadata.ValueReader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            text: str | None = None,
            float: float | None = None,
            int: int | None = None,
            bool: bool | None = None,
            date: DateBuilder | None = None,
        ) -> Metadata.ValueBuilder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Metadata.ValueReader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Metadata.ValueReader: ...
        def to_dict(self) -> dict: ...

    class ValueReader(Metadata.Value):
        @property
        def date(self) -> DateReader: ...
        def as_builder(self) -> Metadata.ValueBuilder: ...

    class ValueBuilder(Metadata.Value):
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
        def date(self, value: Date | DateBuilder | DateReader) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict) -> Metadata.ValueBuilder: ...
        def init(self: Any, name: Literal["date"]) -> DateBuilder: ...
        def copy(self) -> Metadata.ValueBuilder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Metadata.ValueReader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    class Entry:
        @property
        def gcm(self) -> GCM: ...
        @property
        def rcm(self) -> RCM: ...
        @property
        def historical(self) -> None: ...
        @property
        def rcp(self) -> RCP: ...
        @property
        def ssp(self) -> SSP: ...
        @property
        def ensMem(self) -> EnsembleMember: ...
        @property
        def version(self) -> str: ...
        @property
        def start(self) -> Date: ...
        @property
        def end(self) -> Date: ...
        @property
        def co2(self) -> float: ...
        @property
        def picontrol(self) -> None: ...
        @property
        def description(self) -> str: ...
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
        @overload
        def init(self, name: Literal["ensMem"]) -> EnsembleMember: ...
        @overload
        def init(self, name: Literal["start"]) -> Date: ...
        @overload
        def init(self, name: Literal["end"]) -> Date: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Metadata.EntryReader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Metadata.EntryReader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            gcm: GCM
            | Literal[
                "cccmaCanEsm2",
                "ichecEcEarth",
                "ipslIpslCm5AMr",
                "mirocMiroc5",
                "mpiMMpiEsmLr",
                "gfdlEsm4",
                "ipslCm6aLr",
                "mpiEsm12Hr",
                "mriEsm20",
                "ukesm10Ll",
                "gswp3W5E5",
                "mohcHadGem2Es",
            ]
            | None = None,
            rcm: RCM
            | Literal[
                "clmcomCclm4817",
                "gericsRemo2015",
                "knmiRacmo22E",
                "smhiRca4",
                "clmcomBtuCclm4817",
                "mpiCscRemo2009",
                "uhohWrf361H",
            ]
            | None = None,
            historical: None | None = None,
            rcp: RCP
            | Literal["rcp19", "rcp26", "rcp34", "rcp45", "rcp60", "rcp70", "rcp85"]
            | None = None,
            ssp: SSP | Literal["ssp1", "ssp2", "ssp3", "ssp4", "ssp5"] | None = None,
            ensMem: EnsembleMemberBuilder | None = None,
            version: str | None = None,
            start: DateBuilder | None = None,
            end: DateBuilder | None = None,
            co2: float | None = None,
            picontrol: None | None = None,
            description: str | None = None,
        ) -> Metadata.EntryBuilder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Metadata.EntryReader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Metadata.EntryReader: ...
        def to_dict(self) -> dict: ...

    class EntryReader(Metadata.Entry):
        @property
        def ensMem(self) -> EnsembleMemberReader: ...
        @property
        def start(self) -> DateReader: ...
        @property
        def end(self) -> DateReader: ...
        def as_builder(self) -> Metadata.EntryBuilder: ...

    class EntryBuilder(Metadata.Entry):
        @property
        def gcm(self) -> GCM: ...
        @gcm.setter
        def gcm(
            self,
            value: GCM
            | Literal[
                "cccmaCanEsm2",
                "ichecEcEarth",
                "ipslIpslCm5AMr",
                "mirocMiroc5",
                "mpiMMpiEsmLr",
                "gfdlEsm4",
                "ipslCm6aLr",
                "mpiEsm12Hr",
                "mriEsm20",
                "ukesm10Ll",
                "gswp3W5E5",
                "mohcHadGem2Es",
            ],
        ) -> None: ...
        @property
        def rcm(self) -> RCM: ...
        @rcm.setter
        def rcm(
            self,
            value: RCM
            | Literal[
                "clmcomCclm4817",
                "gericsRemo2015",
                "knmiRacmo22E",
                "smhiRca4",
                "clmcomBtuCclm4817",
                "mpiCscRemo2009",
                "uhohWrf361H",
            ],
        ) -> None: ...
        @property
        def historical(self) -> None: ...
        @historical.setter
        def historical(self, value: None) -> None: ...
        @property
        def rcp(self) -> RCP: ...
        @rcp.setter
        def rcp(
            self,
            value: RCP
            | Literal["rcp19", "rcp26", "rcp34", "rcp45", "rcp60", "rcp70", "rcp85"],
        ) -> None: ...
        @property
        def ssp(self) -> SSP: ...
        @ssp.setter
        def ssp(
            self, value: SSP | Literal["ssp1", "ssp2", "ssp3", "ssp4", "ssp5"]
        ) -> None: ...
        @property
        def ensMem(self) -> EnsembleMemberBuilder: ...
        @ensMem.setter
        def ensMem(
            self, value: EnsembleMember | EnsembleMemberBuilder | EnsembleMemberReader
        ) -> None: ...
        @property
        def version(self) -> str: ...
        @version.setter
        def version(self, value: str) -> None: ...
        @property
        def start(self) -> DateBuilder: ...
        @start.setter
        def start(self, value: Date | DateBuilder | DateReader) -> None: ...
        @property
        def end(self) -> DateBuilder: ...
        @end.setter
        def end(self, value: Date | DateBuilder | DateReader) -> None: ...
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
        @staticmethod
        def from_dict(dictionary: dict) -> Metadata.EntryBuilder: ...
        @overload
        def init(self: Any, name: Literal["ensMem"]) -> EnsembleMemberBuilder: ...
        @overload
        def init(self: Any, name: Literal["start"]) -> DateBuilder: ...
        @overload
        def init(self: Any, name: Literal["end"]) -> DateBuilder: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        def copy(self) -> Metadata.EntryBuilder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Metadata.EntryReader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    class Information(Protocol):
        class ForoneResult(Awaitable[ForoneResult], Protocol):
            id: str
            name: str
            description: str

        def forOne(self, entry: Metadata.Entry | dict[str, Any]) -> ForoneResult: ...
        class ForoneRequest(Protocol):
            entry: Metadata.EntryBuilder
            def send(self) -> Metadata.Information.ForoneResult: ...

        def forOne_request(self) -> ForoneRequest: ...
        class ForallResult(Awaitable[ForallResult], Protocol):
            all: Any

        def forAll(self) -> ForallResult: ...
        class ForallRequest(Protocol):
            def send(self) -> Metadata.Information.ForallResult: ...

        def forAll_request(self) -> ForallRequest: ...
        class Server:
            def forOne(
                self, entry: Metadata.EntryReader, **kwargs
            ) -> Awaitable[IdInformation]: ...
            def forAll(self, **kwargs) -> Awaitable[Any]: ...

    @property
    def entries(self) -> Sequence[Metadata.Entry]: ...
    @property
    def info(self) -> Metadata.Information: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[MetadataReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> MetadataReader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        entries: Sequence[Metadata.EntryBuilder] | None = None,
        info: Metadata.Information | Metadata.Information.Server | None = None,
    ) -> MetadataBuilder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> MetadataReader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> MetadataReader: ...
    def to_dict(self) -> dict: ...

class MetadataReader(Metadata):
    @property
    def entries(self) -> Sequence[Metadata.EntryReader]: ...
    def as_builder(self) -> MetadataBuilder: ...

class MetadataBuilder(Metadata):
    @property
    def entries(self) -> Sequence[Metadata.EntryBuilder]: ...
    @entries.setter
    def entries(
        self,
        value: Sequence[Metadata.Entry | Metadata.EntryBuilder | Metadata.EntryReader],
    ) -> None: ...
    @property
    def info(self) -> Metadata.Information: ...
    @info.setter
    def info(
        self, value: Metadata.Information | Metadata.Information.Server
    ) -> None: ...
    @staticmethod
    def from_dict(dictionary: dict) -> MetadataBuilder: ...
    def init(
        self: Any, name: Literal["entries"], size: int = ...
    ) -> _DynamicListBuilder[Metadata.EntryBuilder]: ...
    def copy(self) -> MetadataBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> MetadataReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class Dataset(Identifiable, Persistent, Protocol):
    class GetLocationsCallback(Protocol):
        class NextlocationsResult(Awaitable[NextlocationsResult], Protocol):
            locations: Sequence[Location]

        def nextLocations(self, maxCount: int) -> NextlocationsResult: ...
        class NextlocationsRequest(Protocol):
            maxCount: int
            def send(self) -> Dataset.GetLocationsCallback.NextlocationsResult: ...

        def nextLocations_request(self) -> NextlocationsRequest: ...
        class Server:
            def nextLocations(
                self, maxCount: int, **kwargs
            ) -> Awaitable[Sequence[Location]]: ...

    class MetadataResult(Awaitable[MetadataResult], Protocol):
        entries: Sequence[Metadata.Entry]
        info: Metadata.Information

    def metadata(self) -> MetadataResult: ...
    class MetadataRequest(Protocol):
        def send(self) -> Dataset.MetadataResult: ...

    def metadata_request(self) -> MetadataRequest: ...
    class ClosesttimeseriesatResult(Awaitable[ClosesttimeseriesatResult], Protocol):
        timeSeries: TimeSeries

    def closestTimeSeriesAt(
        self, latlon: LatLonCoord | dict[str, Any]
    ) -> ClosesttimeseriesatResult: ...
    class ClosesttimeseriesatRequest(Protocol):
        latlon: LatLonCoordBuilder
        def send(self) -> Dataset.ClosesttimeseriesatResult: ...

    def closestTimeSeriesAt_request(self) -> ClosesttimeseriesatRequest: ...
    class TimeseriesatResult(Awaitable[TimeseriesatResult], Protocol):
        timeSeries: TimeSeries

    def timeSeriesAt(self, locationId: str) -> TimeseriesatResult: ...
    class TimeseriesatRequest(Protocol):
        locationId: str
        def send(self) -> Dataset.TimeseriesatResult: ...

    def timeSeriesAt_request(self) -> TimeseriesatRequest: ...
    class LocationsResult(Awaitable[LocationsResult], Protocol):
        locations: Sequence[Location]

    def locations(self) -> LocationsResult: ...
    class LocationsRequest(Protocol):
        def send(self) -> Dataset.LocationsResult: ...

    def locations_request(self) -> LocationsRequest: ...
    class StreamlocationsResult(Awaitable[StreamlocationsResult], Protocol):
        locationsCallback: Dataset.GetLocationsCallback

    def streamLocations(self, startAfterLocationId: str) -> StreamlocationsResult: ...
    class StreamlocationsRequest(Protocol):
        startAfterLocationId: str
        def send(self) -> Dataset.StreamlocationsResult: ...

    def streamLocations_request(self) -> StreamlocationsRequest: ...
    class Server(Identifiable.Server, Persistent.Server):
        def metadata(self, **kwargs) -> Awaitable[Metadata]: ...
        def closestTimeSeriesAt(
            self, latlon: LatLonCoordReader, **kwargs
        ) -> Awaitable[TimeSeries | TimeSeries.Server]: ...
        def timeSeriesAt(
            self, locationId: str, **kwargs
        ) -> Awaitable[TimeSeries | TimeSeries.Server]: ...
        def locations(self, **kwargs) -> Awaitable[Sequence[Location]]: ...
        def streamLocations(
            self, startAfterLocationId: str, **kwargs
        ) -> Awaitable[
            Dataset.GetLocationsCallback | Dataset.GetLocationsCallback.Server
        ]: ...

class TimeSeries(Identifiable, Persistent, Protocol):
    class Resolution(Enum):
        daily = "daily"
        hourly = "hourly"

    class ResolutionResult(Awaitable[ResolutionResult], Protocol):
        resolution: TimeSeries.Resolution

    def resolution(self) -> ResolutionResult: ...
    class ResolutionRequest(Protocol):
        def send(self) -> TimeSeries.ResolutionResult: ...

    def resolution_request(self) -> ResolutionRequest: ...
    class RangeResult(Awaitable[RangeResult], Protocol):
        startDate: Date
        endDate: Date

    def range(self) -> RangeResult: ...
    class RangeRequest(Protocol):
        def send(self) -> TimeSeries.RangeResult: ...

    def range_request(self) -> RangeRequest: ...
    class HeaderResult(Awaitable[HeaderResult], Protocol):
        header: Any

    def header(self) -> HeaderResult: ...
    class HeaderRequest(Protocol):
        def send(self) -> TimeSeries.HeaderResult: ...

    def header_request(self) -> HeaderRequest: ...
    class DataResult(Awaitable[DataResult], Protocol):
        data: Sequence[Sequence[float]]

    def data(self) -> DataResult: ...
    class DataRequest(Protocol):
        def send(self) -> TimeSeries.DataResult: ...

    def data_request(self) -> DataRequest: ...
    class DatatResult(Awaitable[DatatResult], Protocol):
        data: Sequence[Sequence[float]]

    def dataT(self) -> DatatResult: ...
    class DatatRequest(Protocol):
        def send(self) -> TimeSeries.DatatResult: ...

    def dataT_request(self) -> DatatRequest: ...
    class SubrangeResult(Awaitable[SubrangeResult], Protocol):
        timeSeries: TimeSeries

    def subrange(
        self, start: Date | dict[str, Any], end: Date | dict[str, Any]
    ) -> SubrangeResult: ...
    class SubrangeRequest(Protocol):
        start: DateBuilder
        end: DateBuilder
        def send(self) -> TimeSeries.SubrangeResult: ...

    def subrange_request(self) -> SubrangeRequest: ...
    class SubheaderResult(Awaitable[SubheaderResult], Protocol):
        timeSeries: TimeSeries

    def subheader(self, elements: Any) -> SubheaderResult: ...
    class SubheaderRequest(Protocol):
        elements: Any
        def send(self) -> TimeSeries.SubheaderResult: ...

    def subheader_request(self) -> SubheaderRequest: ...
    class MetadataResult(Awaitable[MetadataResult], Protocol):
        entries: Sequence[Metadata.Entry]
        info: Metadata.Information

    def metadata(self) -> MetadataResult: ...
    class MetadataRequest(Protocol):
        def send(self) -> TimeSeries.MetadataResult: ...

    def metadata_request(self) -> MetadataRequest: ...
    class LocationResult(Awaitable[LocationResult], Protocol):
        id: IdInformation
        heightNN: float
        latlon: LatLonCoord
        timeSeries: TimeSeries
        customData: Sequence[Location.KV]

    def location(self) -> LocationResult: ...
    class LocationRequest(Protocol):
        def send(self) -> TimeSeries.LocationResult: ...

    def location_request(self) -> LocationRequest: ...
    class Server(Identifiable.Server, Persistent.Server):
        def resolution(self, **kwargs) -> Awaitable[TimeSeries.Resolution]: ...
        def range(self, **kwargs) -> Awaitable[TimeSeries.RangeResult]: ...
        def header(self, **kwargs) -> Awaitable[Any]: ...
        def data(self, **kwargs) -> Awaitable[Sequence[Sequence[float]]]: ...
        def dataT(self, **kwargs) -> Awaitable[Sequence[Sequence[float]]]: ...
        def subrange(
            self, start: DateReader, end: DateReader, **kwargs
        ) -> Awaitable[TimeSeries | TimeSeries.Server]: ...
        def subheader(
            self, elements: Any, **kwargs
        ) -> Awaitable[TimeSeries | TimeSeries.Server]: ...
        def metadata(self, **kwargs) -> Awaitable[Metadata]: ...
        def location(self, **kwargs) -> Awaitable[Location]: ...

class Location:
    class KV:
        @property
        def key(self) -> str: ...
        @property
        def value(self) -> Any: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Location.KVReader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Location.KVReader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            key: str | None = None,
            value: Any | None = None,
        ) -> Location.KVBuilder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Location.KVReader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Location.KVReader: ...
        def to_dict(self) -> dict: ...

    class KVReader(Location.KV):
        def as_builder(self) -> Location.KVBuilder: ...

    class KVBuilder(Location.KV):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str) -> None: ...
        @property
        def value(self) -> Any: ...
        @value.setter
        def value(self, value: Any) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict) -> Location.KVBuilder: ...
        def copy(self) -> Location.KVBuilder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Location.KVReader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @property
    def id(self) -> IdInformation: ...
    @property
    def heightNN(self) -> float: ...
    @property
    def latlon(self) -> LatLonCoord: ...
    @property
    def timeSeries(self) -> TimeSeries: ...
    @property
    def customData(self) -> Sequence[Location.KV]: ...
    @overload
    def init(self, name: Literal["id"]) -> IdInformation: ...
    @overload
    def init(self, name: Literal["latlon"]) -> LatLonCoord: ...
    def init(self: Any, name: str, size: int = ...) -> Any: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[LocationReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> LocationReader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        id: IdInformationBuilder | None = None,
        heightNN: float | None = None,
        latlon: LatLonCoordBuilder | None = None,
        timeSeries: TimeSeries | TimeSeries.Server | None = None,
        customData: Sequence[Location.KVBuilder] | None = None,
    ) -> LocationBuilder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> LocationReader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> LocationReader: ...
    def to_dict(self) -> dict: ...

class LocationReader(Location):
    @property
    def id(self) -> IdInformationReader: ...
    @property
    def latlon(self) -> LatLonCoordReader: ...
    @property
    def customData(self) -> Sequence[Location.KVReader]: ...
    def as_builder(self) -> LocationBuilder: ...

class LocationBuilder(Location):
    @property
    def id(self) -> IdInformationBuilder: ...
    @id.setter
    def id(
        self, value: IdInformation | IdInformationBuilder | IdInformationReader
    ) -> None: ...
    @property
    def heightNN(self) -> float: ...
    @heightNN.setter
    def heightNN(self, value: float) -> None: ...
    @property
    def latlon(self) -> LatLonCoordBuilder: ...
    @latlon.setter
    def latlon(
        self, value: LatLonCoord | LatLonCoordBuilder | LatLonCoordReader
    ) -> None: ...
    @property
    def timeSeries(self) -> TimeSeries: ...
    @timeSeries.setter
    def timeSeries(self, value: TimeSeries | TimeSeries.Server) -> None: ...
    @property
    def customData(self) -> Sequence[Location.KVBuilder]: ...
    @customData.setter
    def customData(
        self, value: Sequence[Location.KV | Location.KVBuilder | Location.KVReader]
    ) -> None: ...
    @staticmethod
    def from_dict(dictionary: dict) -> LocationBuilder: ...
    @overload
    def init(self: Any, name: Literal["id"]) -> IdInformationBuilder: ...
    @overload
    def init(self: Any, name: Literal["latlon"]) -> LatLonCoordBuilder: ...
    @overload
    def init(
        self: Any, name: Literal["customData"], size: int = ...
    ) -> _DynamicListBuilder[Location.KVBuilder]: ...
    def init(self: Any, name: str, size: int = ...) -> Any: ...
    def copy(self) -> LocationBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> LocationReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class MetaPlusData:
    @property
    def meta(self) -> Metadata: ...
    @property
    def data(self) -> Dataset: ...
    def init(self, name: Literal["meta"]) -> Metadata: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[MetaPlusDataReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> MetaPlusDataReader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        meta: MetadataBuilder | None = None,
        data: Dataset | Dataset.Server | None = None,
    ) -> MetaPlusDataBuilder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> MetaPlusDataReader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> MetaPlusDataReader: ...
    def to_dict(self) -> dict: ...

class MetaPlusDataReader(MetaPlusData):
    @property
    def meta(self) -> MetadataReader: ...
    def as_builder(self) -> MetaPlusDataBuilder: ...

class MetaPlusDataBuilder(MetaPlusData):
    @property
    def meta(self) -> MetadataBuilder: ...
    @meta.setter
    def meta(self, value: Metadata | MetadataBuilder | MetadataReader) -> None: ...
    @property
    def data(self) -> Dataset: ...
    @data.setter
    def data(self, value: Dataset | Dataset.Server) -> None: ...
    @staticmethod
    def from_dict(dictionary: dict) -> MetaPlusDataBuilder: ...
    def init(self: Any, name: Literal["meta"]) -> MetadataBuilder: ...
    def copy(self) -> MetaPlusDataBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> MetaPlusDataReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class Element(Enum):
    tmin = "tmin"
    tavg = "tavg"
    tmax = "tmax"
    precip = "precip"
    globrad = "globrad"
    wind = "wind"
    sunhours = "sunhours"
    cloudamount = "cloudamount"
    relhumid = "relhumid"
    airpress = "airpress"
    vaporpress = "vaporpress"
    co2 = "co2"
    o3 = "o3"
    et0 = "et0"
    dewpointTemp = "dewpointTemp"
    specificHumidity = "specificHumidity"
    snowfallFlux = "snowfallFlux"
    surfaceDownwellingLongwaveRadiation = "surfaceDownwellingLongwaveRadiation"
    potET = "potET"

class TimeSeriesData:
    @property
    def data(self) -> Sequence[Sequence[float]]: ...
    @property
    def isTransposed(self) -> bool: ...
    @property
    def header(self) -> Sequence[Element]: ...
    @property
    def startDate(self) -> Date: ...
    @property
    def endDate(self) -> Date: ...
    @property
    def resolution(self) -> TimeSeries.Resolution: ...
    @overload
    def init(self, name: Literal["startDate"]) -> Date: ...
    @overload
    def init(self, name: Literal["endDate"]) -> Date: ...
    def init(self: Any, name: str, size: int = ...) -> Any: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[TimeSeriesDataReader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> TimeSeriesDataReader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        data: Sequence[Sequence[float]] | None = None,
        isTransposed: bool | None = None,
        header: Sequence[Element] | None = None,
        startDate: DateBuilder | None = None,
        endDate: DateBuilder | None = None,
        resolution: TimeSeries.Resolution | Literal["daily", "hourly"] | None = None,
    ) -> TimeSeriesDataBuilder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> TimeSeriesDataReader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> TimeSeriesDataReader: ...
    def to_dict(self) -> dict: ...

class TimeSeriesDataReader(TimeSeriesData):
    @property
    def startDate(self) -> DateReader: ...
    @property
    def endDate(self) -> DateReader: ...
    def as_builder(self) -> TimeSeriesDataBuilder: ...

class TimeSeriesDataBuilder(TimeSeriesData):
    @property
    def data(self) -> Sequence[Sequence[float]]: ...
    @data.setter
    def data(self, value: Sequence[Sequence[float]]) -> None: ...
    @property
    def isTransposed(self) -> bool: ...
    @isTransposed.setter
    def isTransposed(self, value: bool) -> None: ...
    @property
    def header(self) -> Sequence[Element]: ...
    @header.setter
    def header(self, value: Sequence[Element]) -> None: ...
    @property
    def startDate(self) -> DateBuilder: ...
    @startDate.setter
    def startDate(self, value: Date | DateBuilder | DateReader) -> None: ...
    @property
    def endDate(self) -> DateBuilder: ...
    @endDate.setter
    def endDate(self, value: Date | DateBuilder | DateReader) -> None: ...
    @property
    def resolution(self) -> TimeSeries.Resolution: ...
    @resolution.setter
    def resolution(
        self, value: TimeSeries.Resolution | Literal["daily", "hourly"]
    ) -> None: ...
    @staticmethod
    def from_dict(dictionary: dict) -> TimeSeriesDataBuilder: ...
    @overload
    def init(self: Any, name: Literal["startDate"]) -> DateBuilder: ...
    @overload
    def init(self: Any, name: Literal["endDate"]) -> DateBuilder: ...
    @overload
    def init(
        self: Any, name: Literal["data"], size: int = ...
    ) -> _DynamicListBuilder[float]: ...
    @overload
    def init(
        self: Any, name: Literal["header"], size: int = ...
    ) -> _DynamicListBuilder[Element]: ...
    def init(self: Any, name: str, size: int = ...) -> Any: ...
    def copy(self) -> TimeSeriesDataBuilder: ...
    def to_bytes(self) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def to_segments(self) -> list[bytes]: ...
    def as_reader(self) -> TimeSeriesDataReader: ...
    @staticmethod
    def write(file: BufferedWriter) -> None: ...
    @staticmethod
    def write_packed(file: BufferedWriter) -> None: ...

class Service(Identifiable, Persistent, Protocol):
    class GetavailabledatasetsResult(Awaitable[GetavailabledatasetsResult], Protocol):
        datasets: Sequence[MetaPlusData]

    def getAvailableDatasets(self) -> GetavailabledatasetsResult: ...
    class GetavailabledatasetsRequest(Protocol):
        def send(self) -> Service.GetavailabledatasetsResult: ...

    def getAvailableDatasets_request(self) -> GetavailabledatasetsRequest: ...
    class GetdatasetsforResult(Awaitable[GetdatasetsforResult], Protocol):
        datasets: Sequence[Dataset]

    def getDatasetsFor(
        self, template: Metadata | dict[str, Any]
    ) -> GetdatasetsforResult: ...
    class GetdatasetsforRequest(Protocol):
        template: MetadataBuilder
        def send(self) -> Service.GetdatasetsforResult: ...

    def getDatasetsFor_request(self) -> GetdatasetsforRequest: ...
    class Server(Identifiable.Server, Persistent.Server):
        def getAvailableDatasets(
            self, **kwargs
        ) -> Awaitable[Sequence[MetaPlusData]]: ...
        def getDatasetsFor(
            self, template: MetadataReader, **kwargs
        ) -> Awaitable[Sequence[Dataset]]: ...

class CSVTimeSeriesFactory(Identifiable, Protocol):
    class CSVConfig:
        @property
        def sep(self) -> str: ...
        @property
        def headerMap(self) -> Sequence[Pair]: ...
        @property
        def skipLinesToHeader(self) -> int: ...
        @property
        def skipLinesFromHeaderToData(self) -> int: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[CSVTimeSeriesFactory.CSVConfigReader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> CSVTimeSeriesFactory.CSVConfigReader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            sep: str | None = None,
            headerMap: Sequence[PairBuilder] | None = None,
            skipLinesToHeader: int | None = None,
            skipLinesFromHeaderToData: int | None = None,
        ) -> CSVTimeSeriesFactory.CSVConfigBuilder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> CSVTimeSeriesFactory.CSVConfigReader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> CSVTimeSeriesFactory.CSVConfigReader: ...
        def to_dict(self) -> dict: ...

    class CSVConfigReader(CSVTimeSeriesFactory.CSVConfig):
        @property
        def headerMap(self) -> Sequence[PairReader]: ...
        def as_builder(self) -> CSVTimeSeriesFactory.CSVConfigBuilder: ...

    class CSVConfigBuilder(CSVTimeSeriesFactory.CSVConfig):
        @property
        def sep(self) -> str: ...
        @sep.setter
        def sep(self, value: str) -> None: ...
        @property
        def headerMap(self) -> Sequence[PairBuilder]: ...
        @headerMap.setter
        def headerMap(
            self, value: Sequence[Pair | PairBuilder | PairReader]
        ) -> None: ...
        @property
        def skipLinesToHeader(self) -> int: ...
        @skipLinesToHeader.setter
        def skipLinesToHeader(self, value: int) -> None: ...
        @property
        def skipLinesFromHeaderToData(self) -> int: ...
        @skipLinesFromHeaderToData.setter
        def skipLinesFromHeaderToData(self, value: int) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict) -> CSVTimeSeriesFactory.CSVConfigBuilder: ...
        def init(
            self: Any, name: Literal["headerMap"], size: int = ...
        ) -> _DynamicListBuilder[PairBuilder]: ...
        def copy(self) -> CSVTimeSeriesFactory.CSVConfigBuilder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> CSVTimeSeriesFactory.CSVConfigReader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    class CreateResult(Awaitable[CreateResult], Protocol):
        timeseries: TimeSeries
        error: str

    def create(
        self, csvData: str, config: CSVTimeSeriesFactory.CSVConfig | dict[str, Any]
    ) -> CreateResult: ...
    class CreateRequest(Protocol):
        csvData: str
        config: CSVTimeSeriesFactory.CSVConfigBuilder
        def send(self) -> CSVTimeSeriesFactory.CreateResult: ...

    def create_request(self) -> CreateRequest: ...
    class Server(Identifiable.Server):
        def create(
            self, csvData: str, config: CSVTimeSeriesFactory.CSVConfigReader, **kwargs
        ) -> Awaitable[CSVTimeSeriesFactory.CreateResult]: ...

class AlterTimeSeriesWrapper(TimeSeries, Protocol):
    class Altered:
        class AlterType(Enum):
            add = "add"
            mul = "mul"

        @property
        def element(self) -> Element: ...
        @property
        def value(self) -> float: ...
        @property
        def type(self) -> AlterTimeSeriesWrapper.Altered.AlterType: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[AlterTimeSeriesWrapper.AlteredReader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AlterTimeSeriesWrapper.AlteredReader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            element: Element
            | Literal[
                "tmin",
                "tavg",
                "tmax",
                "precip",
                "globrad",
                "wind",
                "sunhours",
                "cloudamount",
                "relhumid",
                "airpress",
                "vaporpress",
                "co2",
                "o3",
                "et0",
                "dewpointTemp",
                "specificHumidity",
                "snowfallFlux",
                "surfaceDownwellingLongwaveRadiation",
                "potET",
            ]
            | None = None,
            value: float | None = None,
            type: AlterTimeSeriesWrapper.Altered.AlterType
            | Literal["add", "mul"]
            | None = None,
        ) -> AlterTimeSeriesWrapper.AlteredBuilder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AlterTimeSeriesWrapper.AlteredReader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AlterTimeSeriesWrapper.AlteredReader: ...
        def to_dict(self) -> dict: ...

    class AlteredReader(AlterTimeSeriesWrapper.Altered):
        def as_builder(self) -> AlterTimeSeriesWrapper.AlteredBuilder: ...

    class AlteredBuilder(AlterTimeSeriesWrapper.Altered):
        @property
        def element(self) -> Element: ...
        @element.setter
        def element(
            self,
            value: Element
            | Literal[
                "tmin",
                "tavg",
                "tmax",
                "precip",
                "globrad",
                "wind",
                "sunhours",
                "cloudamount",
                "relhumid",
                "airpress",
                "vaporpress",
                "co2",
                "o3",
                "et0",
                "dewpointTemp",
                "specificHumidity",
                "snowfallFlux",
                "surfaceDownwellingLongwaveRadiation",
                "potET",
            ],
        ) -> None: ...
        @property
        def value(self) -> float: ...
        @value.setter
        def value(self, value: float) -> None: ...
        @property
        def type(self) -> AlterTimeSeriesWrapper.Altered.AlterType: ...
        @type.setter
        def type(
            self,
            value: AlterTimeSeriesWrapper.Altered.AlterType | Literal["add", "mul"],
        ) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict) -> AlterTimeSeriesWrapper.AlteredBuilder: ...
        def copy(self) -> AlterTimeSeriesWrapper.AlteredBuilder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> AlterTimeSeriesWrapper.AlteredReader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    class WrappedtimeseriesResult(Awaitable[WrappedtimeseriesResult], Protocol):
        timeSeries: TimeSeries

    def wrappedTimeSeries(self) -> WrappedtimeseriesResult: ...
    class WrappedtimeseriesRequest(Protocol):
        def send(self) -> AlterTimeSeriesWrapper.WrappedtimeseriesResult: ...

    def wrappedTimeSeries_request(self) -> WrappedtimeseriesRequest: ...
    class AlteredelementsResult(Awaitable[AlteredelementsResult], Protocol):
        list: Sequence[AlterTimeSeriesWrapper.Altered]

    def alteredElements(self) -> AlteredelementsResult: ...
    class AlteredelementsRequest(Protocol):
        def send(self) -> AlterTimeSeriesWrapper.AlteredelementsResult: ...

    def alteredElements_request(self) -> AlteredelementsRequest: ...
    class AlterResult(Awaitable[AlterResult], Protocol):
        timeSeries: TimeSeries

    def alter(
        self,
        desc: AlterTimeSeriesWrapper.Altered | dict[str, Any],
        asNewTimeSeries: bool,
    ) -> AlterResult: ...
    class AlterRequest(Protocol):
        desc: AlterTimeSeriesWrapper.AlteredBuilder
        asNewTimeSeries: bool
        def send(self) -> AlterTimeSeriesWrapper.AlterResult: ...

    def alter_request(self) -> AlterRequest: ...
    def remove(
        self,
        alteredElement: Element
        | Literal[
            "tmin",
            "tavg",
            "tmax",
            "precip",
            "globrad",
            "wind",
            "sunhours",
            "cloudamount",
            "relhumid",
            "airpress",
            "vaporpress",
            "co2",
            "o3",
            "et0",
            "dewpointTemp",
            "specificHumidity",
            "snowfallFlux",
            "surfaceDownwellingLongwaveRadiation",
            "potET",
        ],
    ) -> None: ...
    class RemoveRequest(Protocol):
        alteredElement: Element
        def send(self) -> Any: ...

    def remove_request(self) -> RemoveRequest: ...
    def replaceWrappedTimeSeries(self, timeSeries: TimeSeries) -> None: ...
    class ReplacewrappedtimeseriesRequest(Protocol):
        timeSeries: TimeSeries
        def send(self) -> Any: ...

    def replaceWrappedTimeSeries_request(self) -> ReplacewrappedtimeseriesRequest: ...
    class Server(TimeSeries.Server):
        def wrappedTimeSeries(
            self, **kwargs
        ) -> Awaitable[TimeSeries | TimeSeries.Server]: ...
        def alteredElements(
            self, **kwargs
        ) -> Awaitable[Sequence[AlterTimeSeriesWrapper.Altered]]: ...
        def alter(
            self,
            desc: AlterTimeSeriesWrapper.AlteredReader,
            asNewTimeSeries: bool,
            **kwargs,
        ) -> Awaitable[TimeSeries | TimeSeries.Server]: ...
        def remove(
            self,
            alteredElement: Element
            | Literal[
                "tmin",
                "tavg",
                "tmax",
                "precip",
                "globrad",
                "wind",
                "sunhours",
                "cloudamount",
                "relhumid",
                "airpress",
                "vaporpress",
                "co2",
                "o3",
                "et0",
                "dewpointTemp",
                "specificHumidity",
                "snowfallFlux",
                "surfaceDownwellingLongwaveRadiation",
                "potET",
            ],
            **kwargs,
        ) -> None: ...
        def replaceWrappedTimeSeries(
            self, timeSeries: TimeSeries, **kwargs
        ) -> None: ...

class AlterTimeSeriesWrapperFactory(Identifiable, Protocol):
    class WrapResult(Awaitable[WrapResult], Protocol):
        wrapper: AlterTimeSeriesWrapper

    def wrap(self, timeSeries: TimeSeries) -> WrapResult: ...
    class WrapRequest(Protocol):
        timeSeries: TimeSeries
        def send(self) -> AlterTimeSeriesWrapperFactory.WrapResult: ...

    def wrap_request(self) -> WrapRequest: ...
    class Server(Identifiable.Server):
        def wrap(
            self, timeSeries: TimeSeries, **kwargs
        ) -> Awaitable[AlterTimeSeriesWrapper | AlterTimeSeriesWrapper.Server]: ...
