"""This is an automatically generated stub for `climate.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
from contextlib import contextmanager
from enum import Enum
from io import BufferedWriter
from typing import Any, BinaryIO, Literal, NamedTuple, Protocol, TypeAlias, overload

from .common_capnp import Identifiable, IdentifiableClient, IdInformation, Pair
from .date_capnp import Date
from .geo_capnp import LatLonCoord
from .persistence_capnp import Persistent, PersistentClient

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

EnsembleMemberBuilder: TypeAlias = EnsembleMember.Builder
EnsembleMemberReader: TypeAlias = EnsembleMember.Reader

class EnsembleMember:
    class Reader:
        @property
        def r(self) -> int: ...
        @property
        def i(self) -> int: ...
        @property
        def p(self) -> int: ...
        @property
        def f(self) -> int: ...
        def as_builder(self) -> EnsembleMember.Builder: ...

    class Builder:
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
        def from_dict(dictionary: dict[str, Any]) -> EnsembleMember.Builder: ...
        def copy(self) -> EnsembleMember.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> EnsembleMember.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[EnsembleMember.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> EnsembleMember.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        r: int | None = None,
        i: int | None = None,
        p: int | None = None,
        f: int | None = None,
    ) -> EnsembleMember.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> EnsembleMember.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> EnsembleMember.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

MetadataBuilder: TypeAlias = Metadata.Builder
MetadataReader: TypeAlias = Metadata.Reader

class Metadata:
    class Supported:
        class CategoriesRequest(Protocol):
            def send(self) -> Metadata.Supported.CategoriesResult: ...

        class CategoriesResult(Awaitable[CategoriesResult], Protocol):
            types: Any

        class SupportedvaluesRequest(Protocol):
            typeId: str
            def send(self) -> Metadata.Supported.SupportedvaluesResult: ...

        class SupportedvaluesResult(Awaitable[SupportedvaluesResult], Protocol):
            values: Any

        @classmethod
        def _new_client(
            cls, server: Metadata.Supported.Server
        ) -> Metadata.SupportedClient: ...
        class Server(Protocol):
            class CategoriesResultTuple(NamedTuple):
                pass

            class SupportedvaluesResultTuple(NamedTuple):
                pass

            class CategoriesCallContext(Protocol):
                params: Metadata.Supported.CategoriesRequest
                results: Metadata.Supported.CategoriesResult

            class SupportedvaluesCallContext(Protocol):
                params: Metadata.Supported.SupportedvaluesRequest
                results: Metadata.Supported.SupportedvaluesResult

            def categories(
                self,
                _context: Metadata.Supported.Server.CategoriesCallContext,
                **kwargs: Any,
            ) -> Awaitable[Metadata.Supported.Server.CategoriesResultTuple | None]: ...
            def categories_context(
                self, context: Metadata.Supported.Server.CategoriesCallContext
            ) -> Awaitable[None]: ...
            def supportedValues(
                self,
                typeId: str,
                _context: Metadata.Supported.Server.SupportedvaluesCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Metadata.Supported.Server.SupportedvaluesResultTuple | None
            ]: ...
            def supportedValues_context(
                self, context: Metadata.Supported.Server.SupportedvaluesCallContext
            ) -> Awaitable[None]: ...

    class SupportedClient(Protocol):
        def categories(self) -> Metadata.Supported.CategoriesResult: ...
        def supportedValues(
            self, typeId: str | None = None
        ) -> Metadata.Supported.SupportedvaluesResult: ...
        def categories_request(self) -> Metadata.Supported.CategoriesRequest: ...
        def supportedValues_request(
            self, typeId: str | None = None
        ) -> Metadata.Supported.SupportedvaluesRequest: ...

    ValueBuilder: TypeAlias = Value.Builder
    ValueReader: TypeAlias = Value.Reader
    class Value:
        class Reader:
            @property
            def text(self) -> str: ...
            @property
            def float(self) -> float: ...
            @property
            def int(self) -> int: ...
            @property
            def bool(self) -> bool: ...
            @property
            def date(self) -> Date.Reader: ...
            def which(self) -> Literal["text", "float", "int", "bool", "date"]: ...
            def as_builder(self) -> Metadata.Value.Builder: ...

        class Builder:
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
            def date(self) -> Date.Builder: ...
            @date.setter
            def date(
                self, value: Date.Builder | Date.Reader | dict[str, Any]
            ) -> None: ...
            def which(self) -> Literal["text", "float", "int", "bool", "date"]: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Metadata.Value.Builder: ...
            def init(self, name: Literal["date"]) -> Date.Builder: ...
            def copy(self) -> Metadata.Value.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Metadata.Value.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def which(self) -> Literal["text", "float", "int", "bool", "date"]: ...
        def init(self, name: Literal["date"]) -> Date: ...
        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Metadata.Value.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Metadata.Value.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            text: str | None = None,
            float: float | None = None,
            int: int | None = None,
            bool: bool | None = None,
            date: Date.Builder | dict[str, Any] | None = None,
        ) -> Metadata.Value.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Metadata.Value.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Metadata.Value.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    EntryBuilder: TypeAlias = Entry.Builder
    EntryReader: TypeAlias = Entry.Reader
    class Entry:
        class Reader:
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
            def ensMem(self) -> EnsembleMember.Reader: ...
            @property
            def version(self) -> str: ...
            @property
            def start(self) -> Date.Reader: ...
            @property
            def end(self) -> Date.Reader: ...
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
            def as_builder(self) -> Metadata.Entry.Builder: ...

        class Builder:
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
                | Literal[
                    "rcp19", "rcp26", "rcp34", "rcp45", "rcp60", "rcp70", "rcp85"
                ],
            ) -> None: ...
            @property
            def ssp(self) -> SSP: ...
            @ssp.setter
            def ssp(
                self, value: SSP | Literal["ssp1", "ssp2", "ssp3", "ssp4", "ssp5"]
            ) -> None: ...
            @property
            def ensMem(self) -> EnsembleMember.Builder: ...
            @ensMem.setter
            def ensMem(
                self,
                value: EnsembleMember.Builder | EnsembleMember.Reader | dict[str, Any],
            ) -> None: ...
            @property
            def version(self) -> str: ...
            @version.setter
            def version(self, value: str) -> None: ...
            @property
            def start(self) -> Date.Builder: ...
            @start.setter
            def start(
                self, value: Date.Builder | Date.Reader | dict[str, Any]
            ) -> None: ...
            @property
            def end(self) -> Date.Builder: ...
            @end.setter
            def end(
                self, value: Date.Builder | Date.Reader | dict[str, Any]
            ) -> None: ...
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
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Metadata.Entry.Builder: ...
            @overload
            def init(self: Any, name: Literal["ensMem"]) -> EnsembleMember.Builder: ...
            @overload
            def init(self: Any, name: Literal["start"]) -> Date.Builder: ...
            @overload
            def init(self: Any, name: Literal["end"]) -> Date.Builder: ...
            def init(self: Any, name: str, size: int = ...) -> Any: ...
            def copy(self) -> Metadata.Entry.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Metadata.Entry.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

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
        ) -> Iterator[Metadata.Entry.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Metadata.Entry.Reader: ...
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
            ensMem: EnsembleMember.Builder | dict[str, Any] | None = None,
            version: str | None = None,
            start: Date.Builder | dict[str, Any] | None = None,
            end: Date.Builder | dict[str, Any] | None = None,
            co2: float | None = None,
            picontrol: None | None = None,
            description: str | None = None,
        ) -> Metadata.Entry.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Metadata.Entry.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Metadata.Entry.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Information:
        class ForoneRequest(Protocol):
            entry: Metadata.Entry.Builder
            @overload
            def init(self, name: Literal["entry"]) -> Metadata.Entry.Builder: ...
            @overload
            def init(self, name: str, size: int = ...) -> Any: ...
            def send(self) -> Metadata.Information.ForoneResult: ...

        class ForoneResult(Awaitable[ForoneResult], Protocol):
            id: str
            name: str
            description: str

        class ForallRequest(Protocol):
            def send(self) -> Metadata.Information.ForallResult: ...

        class ForallResult(Awaitable[ForallResult], Protocol):
            all: Any

        @classmethod
        def _new_client(
            cls, server: Metadata.Information.Server
        ) -> Metadata.InformationClient: ...
        class Server(Protocol):
            class ForoneResultTuple(NamedTuple):
                id: str
                name: str
                description: str

            class ForallResultTuple(NamedTuple):
                pass

            class ForoneCallContext(Protocol):
                params: Metadata.Information.ForoneRequest
                results: Metadata.Information.ForoneResult

            class ForallCallContext(Protocol):
                params: Metadata.Information.ForallRequest
                results: Metadata.Information.ForallResult

            def forOne(
                self,
                entry: Metadata.Entry.Reader,
                _context: Metadata.Information.Server.ForoneCallContext,
                **kwargs: Any,
            ) -> Awaitable[Metadata.Information.Server.ForoneResultTuple | None]: ...
            def forOne_context(
                self, context: Metadata.Information.Server.ForoneCallContext
            ) -> Awaitable[None]: ...
            def forAll(
                self,
                _context: Metadata.Information.Server.ForallCallContext,
                **kwargs: Any,
            ) -> Awaitable[Metadata.Information.Server.ForallResultTuple | None]: ...
            def forAll_context(
                self, context: Metadata.Information.Server.ForallCallContext
            ) -> Awaitable[None]: ...

    class InformationClient(Protocol):
        def forOne(
            self, entry: Metadata.Entry | dict[str, Any] | None = None
        ) -> Metadata.Information.ForoneResult: ...
        def forAll(self) -> Metadata.Information.ForallResult: ...
        def forOne_request(
            self, entry: Metadata.Entry.Builder | None = None
        ) -> Metadata.Information.ForoneRequest: ...
        def forAll_request(self) -> Metadata.Information.ForallRequest: ...

    class Reader:
        @property
        def entries(self) -> Sequence[Metadata.Entry.Reader]: ...
        @property
        def info(self) -> Metadata.InformationClient: ...
        def as_builder(self) -> Metadata.Builder: ...

    class Builder:
        @property
        def entries(self) -> Sequence[Metadata.Entry.Builder]: ...
        @entries.setter
        def entries(
            self,
            value: Sequence[Metadata.Entry.Builder | Metadata.Entry.Reader]
            | Sequence[dict[str, Any]],
        ) -> None: ...
        @property
        def info(self) -> Metadata.InformationClient: ...
        @info.setter
        def info(
            self, value: Metadata.InformationClient | Metadata.Information.Server
        ) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Metadata.Builder: ...
        def init(
            self, name: Literal["entries"], size: int = ...
        ) -> Sequence[Metadata.Entry.Builder]: ...
        def copy(self) -> Metadata.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Metadata.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[Metadata.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Metadata.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        entries: Sequence[Metadata.Entry.Builder]
        | Sequence[dict[str, Any]]
        | None = None,
        info: Metadata.InformationClient | Metadata.Information.Server | None = None,
    ) -> Metadata.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Metadata.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Metadata.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

class Dataset:
    class GetLocationsCallback:
        class NextlocationsRequest(Protocol):
            maxCount: int
            def send(self) -> Dataset.GetLocationsCallback.NextlocationsResult: ...

        class NextlocationsResult(Awaitable[NextlocationsResult], Protocol):
            locations: Sequence[Location.Builder | Location.Reader]

        @classmethod
        def _new_client(
            cls, server: Dataset.GetLocationsCallback.Server
        ) -> Dataset.GetLocationsCallbackClient: ...
        class Server(Protocol):
            class NextlocationsResultTuple(NamedTuple):
                locations: Sequence[Location]

            class NextlocationsCallContext(Protocol):
                params: Dataset.GetLocationsCallback.NextlocationsRequest
                results: Dataset.GetLocationsCallback.NextlocationsResult

            def nextLocations(
                self,
                maxCount: int,
                _context: Dataset.GetLocationsCallback.Server.NextlocationsCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                Dataset.GetLocationsCallback.Server.NextlocationsResultTuple | None
            ]: ...
            def nextLocations_context(
                self,
                context: Dataset.GetLocationsCallback.Server.NextlocationsCallContext,
            ) -> Awaitable[None]: ...

    class GetLocationsCallbackClient(Protocol):
        def nextLocations(
            self, maxCount: int | None = None
        ) -> Dataset.GetLocationsCallback.NextlocationsResult: ...
        def nextLocations_request(
            self, maxCount: int | None = None
        ) -> Dataset.GetLocationsCallback.NextlocationsRequest: ...

    class MetadataRequest(Protocol):
        def send(self) -> Dataset.MetadataResult: ...

    class MetadataResult(Awaitable[MetadataResult], Protocol):
        entries: Sequence[Metadata.Entry.Builder | Metadata.Entry.Reader]
        info: Metadata.InformationClient

    class ClosesttimeseriesatRequest(Protocol):
        latlon: LatLonCoord.Builder
        @overload
        def init(self, name: Literal["latlon"]) -> LatLonCoord.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Dataset.ClosesttimeseriesatResult: ...

    class ClosesttimeseriesatResult(Awaitable[ClosesttimeseriesatResult], Protocol):
        timeSeries: TimeSeriesClient

    class TimeseriesatRequest(Protocol):
        locationId: str
        def send(self) -> Dataset.TimeseriesatResult: ...

    class TimeseriesatResult(Awaitable[TimeseriesatResult], Protocol):
        timeSeries: TimeSeriesClient

    class LocationsRequest(Protocol):
        def send(self) -> Dataset.LocationsResult: ...

    class LocationsResult(Awaitable[LocationsResult], Protocol):
        locations: Sequence[Location.Builder | Location.Reader]

    class StreamlocationsRequest(Protocol):
        startAfterLocationId: str
        def send(self) -> Dataset.StreamlocationsResult: ...

    class StreamlocationsResult(Awaitable[StreamlocationsResult], Protocol):
        locationsCallback: Dataset.GetLocationsCallbackClient

    @classmethod
    def _new_client(
        cls, server: Dataset.Server | Identifiable.Server | Persistent.Server
    ) -> DatasetClient: ...
    class Server(Identifiable.Server, Persistent.Server):
        class MetadataResultTuple(NamedTuple):
            entries: Sequence[Metadata.Entry]
            info: Metadata.Information.Server

        class ClosesttimeseriesatResultTuple(NamedTuple):
            timeSeries: TimeSeries.Server

        class TimeseriesatResultTuple(NamedTuple):
            timeSeries: TimeSeries.Server

        class LocationsResultTuple(NamedTuple):
            locations: Sequence[Location]

        class StreamlocationsResultTuple(NamedTuple):
            locationsCallback: Dataset.GetLocationsCallback.Server

        class MetadataCallContext(Protocol):
            params: Dataset.MetadataRequest
            results: Dataset.MetadataResult

        class ClosesttimeseriesatCallContext(Protocol):
            params: Dataset.ClosesttimeseriesatRequest
            results: Dataset.ClosesttimeseriesatResult

        class TimeseriesatCallContext(Protocol):
            params: Dataset.TimeseriesatRequest
            results: Dataset.TimeseriesatResult

        class LocationsCallContext(Protocol):
            params: Dataset.LocationsRequest
            results: Dataset.LocationsResult

        class StreamlocationsCallContext(Protocol):
            params: Dataset.StreamlocationsRequest
            results: Dataset.StreamlocationsResult

        def metadata(
            self, _context: Dataset.Server.MetadataCallContext, **kwargs: Any
        ) -> Awaitable[Dataset.Server.MetadataResultTuple | None]: ...
        def metadata_context(
            self, context: Dataset.Server.MetadataCallContext
        ) -> Awaitable[None]: ...
        def closestTimeSeriesAt(
            self,
            latlon: LatLonCoord.Reader,
            _context: Dataset.Server.ClosesttimeseriesatCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            TimeSeries.Server | Dataset.Server.ClosesttimeseriesatResultTuple | None
        ]: ...
        def closestTimeSeriesAt_context(
            self, context: Dataset.Server.ClosesttimeseriesatCallContext
        ) -> Awaitable[None]: ...
        def timeSeriesAt(
            self,
            locationId: str,
            _context: Dataset.Server.TimeseriesatCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            TimeSeries.Server | Dataset.Server.TimeseriesatResultTuple | None
        ]: ...
        def timeSeriesAt_context(
            self, context: Dataset.Server.TimeseriesatCallContext
        ) -> Awaitable[None]: ...
        def locations(
            self, _context: Dataset.Server.LocationsCallContext, **kwargs: Any
        ) -> Awaitable[Dataset.Server.LocationsResultTuple | None]: ...
        def locations_context(
            self, context: Dataset.Server.LocationsCallContext
        ) -> Awaitable[None]: ...
        def streamLocations(
            self,
            startAfterLocationId: str,
            _context: Dataset.Server.StreamlocationsCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            Dataset.GetLocationsCallback.Server
            | Dataset.Server.StreamlocationsResultTuple
            | None
        ]: ...
        def streamLocations_context(
            self, context: Dataset.Server.StreamlocationsCallContext
        ) -> Awaitable[None]: ...

class TimeSeries:
    class Resolution(Enum):
        daily = "daily"
        hourly = "hourly"

    class ResolutionRequest(Protocol):
        def send(self) -> TimeSeries.ResolutionResult: ...

    class ResolutionResult(Awaitable[ResolutionResult], Protocol):
        resolution: TimeSeries.Resolution

    class RangeRequest(Protocol):
        def send(self) -> TimeSeries.RangeResult: ...

    class RangeResult(Awaitable[RangeResult], Protocol):
        startDate: Date.Builder | Date.Reader
        endDate: Date.Builder | Date.Reader

    class HeaderRequest(Protocol):
        def send(self) -> TimeSeries.HeaderResult: ...

    class HeaderResult(Awaitable[HeaderResult], Protocol):
        header: Any

    class DataRequest(Protocol):
        def send(self) -> TimeSeries.DataResult: ...

    class DataResult(Awaitable[DataResult], Protocol):
        data: Sequence[Sequence[float]]

    class DatatRequest(Protocol):
        def send(self) -> TimeSeries.DatatResult: ...

    class DatatResult(Awaitable[DatatResult], Protocol):
        data: Sequence[Sequence[float]]

    class SubrangeRequest(Protocol):
        start: Date.Builder
        end: Date.Builder
        @overload
        def init(self, name: Literal["start"]) -> Date.Builder: ...
        @overload
        def init(self, name: Literal["end"]) -> Date.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> TimeSeries.SubrangeResult: ...

    class SubrangeResult(Awaitable[SubrangeResult], Protocol):
        timeSeries: TimeSeriesClient

    class SubheaderRequest(Protocol):
        def send(self) -> TimeSeries.SubheaderResult: ...

    class SubheaderResult(Awaitable[SubheaderResult], Protocol):
        timeSeries: TimeSeriesClient

    class MetadataRequest(Protocol):
        def send(self) -> TimeSeries.MetadataResult: ...

    class MetadataResult(Awaitable[MetadataResult], Protocol):
        entries: Sequence[Metadata.Entry.Builder | Metadata.Entry.Reader]
        info: Metadata.InformationClient

    class LocationRequest(Protocol):
        def send(self) -> TimeSeries.LocationResult: ...

    class LocationResult(Awaitable[LocationResult], Protocol):
        id: IdInformation.Builder | IdInformation.Reader
        heightNN: float
        latlon: LatLonCoord.Builder | LatLonCoord.Reader
        timeSeries: TimeSeriesClient
        customData: Sequence[Location.KV.Builder | Location.KV.Reader]

    @classmethod
    def _new_client(
        cls, server: TimeSeries.Server | Identifiable.Server | Persistent.Server
    ) -> TimeSeriesClient: ...
    class Server(Identifiable.Server, Persistent.Server):
        class ResolutionResultTuple(NamedTuple):
            resolution: TimeSeries.Resolution

        class RangeResultTuple(NamedTuple):
            startDate: Date.Builder | Date.Reader
            endDate: Date.Builder | Date.Reader

        class HeaderResultTuple(NamedTuple):
            pass

        class DataResultTuple(NamedTuple):
            data: Sequence[Sequence[float]]

        class DatatResultTuple(NamedTuple):
            data: Sequence[Sequence[float]]

        class SubrangeResultTuple(NamedTuple):
            timeSeries: TimeSeries.Server

        class SubheaderResultTuple(NamedTuple):
            timeSeries: TimeSeries.Server

        class MetadataResultTuple(NamedTuple):
            entries: Sequence[Metadata.Entry]
            info: Metadata.Information.Server

        class LocationResultTuple(NamedTuple):
            id: IdInformation.Builder | IdInformation.Reader
            heightNN: float
            latlon: LatLonCoord.Builder | LatLonCoord.Reader
            timeSeries: TimeSeries.Server
            customData: Sequence[Location.KV]

        class ResolutionCallContext(Protocol):
            params: TimeSeries.ResolutionRequest
            results: TimeSeries.ResolutionResult

        class RangeCallContext(Protocol):
            params: TimeSeries.RangeRequest
            results: TimeSeries.RangeResult

        class HeaderCallContext(Protocol):
            params: TimeSeries.HeaderRequest
            results: TimeSeries.HeaderResult

        class DataCallContext(Protocol):
            params: TimeSeries.DataRequest
            results: TimeSeries.DataResult

        class DatatCallContext(Protocol):
            params: TimeSeries.DatatRequest
            results: TimeSeries.DatatResult

        class SubrangeCallContext(Protocol):
            params: TimeSeries.SubrangeRequest
            results: TimeSeries.SubrangeResult

        class SubheaderCallContext(Protocol):
            params: TimeSeries.SubheaderRequest
            results: TimeSeries.SubheaderResult

        class MetadataCallContext(Protocol):
            params: TimeSeries.MetadataRequest
            results: TimeSeries.MetadataResult

        class LocationCallContext(Protocol):
            params: TimeSeries.LocationRequest
            results: TimeSeries.LocationResult

        def resolution(
            self, _context: TimeSeries.Server.ResolutionCallContext, **kwargs: Any
        ) -> Awaitable[TimeSeries.Server.ResolutionResultTuple | None]: ...
        def resolution_context(
            self, context: TimeSeries.Server.ResolutionCallContext
        ) -> Awaitable[None]: ...
        def range(
            self, _context: TimeSeries.Server.RangeCallContext, **kwargs: Any
        ) -> Awaitable[TimeSeries.Server.RangeResultTuple | None]: ...
        def range_context(
            self, context: TimeSeries.Server.RangeCallContext
        ) -> Awaitable[None]: ...
        def header(
            self, _context: TimeSeries.Server.HeaderCallContext, **kwargs: Any
        ) -> Awaitable[TimeSeries.Server.HeaderResultTuple | None]: ...
        def header_context(
            self, context: TimeSeries.Server.HeaderCallContext
        ) -> Awaitable[None]: ...
        def data(
            self, _context: TimeSeries.Server.DataCallContext, **kwargs: Any
        ) -> Awaitable[TimeSeries.Server.DataResultTuple | None]: ...
        def data_context(
            self, context: TimeSeries.Server.DataCallContext
        ) -> Awaitable[None]: ...
        def dataT(
            self, _context: TimeSeries.Server.DatatCallContext, **kwargs: Any
        ) -> Awaitable[TimeSeries.Server.DatatResultTuple | None]: ...
        def dataT_context(
            self, context: TimeSeries.Server.DatatCallContext
        ) -> Awaitable[None]: ...
        def subrange(
            self,
            start: Date.Reader,
            end: Date.Reader,
            _context: TimeSeries.Server.SubrangeCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            TimeSeries.Server | TimeSeries.Server.SubrangeResultTuple | None
        ]: ...
        def subrange_context(
            self, context: TimeSeries.Server.SubrangeCallContext
        ) -> Awaitable[None]: ...
        def subheader(
            self, _context: TimeSeries.Server.SubheaderCallContext, **kwargs: Any
        ) -> Awaitable[
            TimeSeries.Server | TimeSeries.Server.SubheaderResultTuple | None
        ]: ...
        def subheader_context(
            self, context: TimeSeries.Server.SubheaderCallContext
        ) -> Awaitable[None]: ...
        def metadata(
            self, _context: TimeSeries.Server.MetadataCallContext, **kwargs: Any
        ) -> Awaitable[TimeSeries.Server.MetadataResultTuple | None]: ...
        def metadata_context(
            self, context: TimeSeries.Server.MetadataCallContext
        ) -> Awaitable[None]: ...
        def location(
            self, _context: TimeSeries.Server.LocationCallContext, **kwargs: Any
        ) -> Awaitable[TimeSeries.Server.LocationResultTuple | None]: ...
        def location_context(
            self, context: TimeSeries.Server.LocationCallContext
        ) -> Awaitable[None]: ...

class TimeSeriesClient(IdentifiableClient, PersistentClient):
    def resolution(self) -> TimeSeries.ResolutionResult: ...
    def range(self) -> TimeSeries.RangeResult: ...
    def header(self) -> TimeSeries.HeaderResult: ...
    def data(self) -> TimeSeries.DataResult: ...
    def dataT(self) -> TimeSeries.DatatResult: ...
    def subrange(
        self,
        start: Date | dict[str, Any] | None = None,
        end: Date | dict[str, Any] | None = None,
    ) -> TimeSeries.SubrangeResult: ...
    def subheader(self) -> TimeSeries.SubheaderResult: ...
    def metadata(self) -> TimeSeries.MetadataResult: ...
    def location(self) -> TimeSeries.LocationResult: ...
    def resolution_request(self) -> TimeSeries.ResolutionRequest: ...
    def range_request(self) -> TimeSeries.RangeRequest: ...
    def header_request(self) -> TimeSeries.HeaderRequest: ...
    def data_request(self) -> TimeSeries.DataRequest: ...
    def dataT_request(self) -> TimeSeries.DatatRequest: ...
    def subrange_request(
        self, start: Date.Builder | None = None, end: Date.Builder | None = None
    ) -> TimeSeries.SubrangeRequest: ...
    def subheader_request(self) -> TimeSeries.SubheaderRequest: ...
    def metadata_request(self) -> TimeSeries.MetadataRequest: ...
    def location_request(self) -> TimeSeries.LocationRequest: ...

LocationBuilder: TypeAlias = Location.Builder
LocationReader: TypeAlias = Location.Reader

class Location:
    KVBuilder: TypeAlias = KV.Builder
    KVReader: TypeAlias = KV.Reader
    class KV:
        class Reader:
            @property
            def key(self) -> str: ...
            @property
            def value(self) -> Any: ...
            def as_builder(self) -> Location.KV.Builder: ...

        class Builder:
            @property
            def key(self) -> str: ...
            @key.setter
            def key(self, value: str) -> None: ...
            @property
            def value(self) -> Any: ...
            @value.setter
            def value(self, value: Any) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Location.KV.Builder: ...
            def copy(self) -> Location.KV.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Location.KV.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Location.KV.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Location.KV.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            key: str | None = None,
            value: Any | None = None,
        ) -> Location.KV.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Location.KV.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Location.KV.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Reader:
        @property
        def id(self) -> IdInformation.Reader: ...
        @property
        def heightNN(self) -> float: ...
        @property
        def latlon(self) -> LatLonCoord.Reader: ...
        @property
        def timeSeries(self) -> TimeSeriesClient: ...
        @property
        def customData(self) -> Sequence[Location.KV.Reader]: ...
        def as_builder(self) -> Location.Builder: ...

    class Builder:
        @property
        def id(self) -> IdInformation.Builder: ...
        @id.setter
        def id(
            self, value: IdInformation.Builder | IdInformation.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def heightNN(self) -> float: ...
        @heightNN.setter
        def heightNN(self, value: float) -> None: ...
        @property
        def latlon(self) -> LatLonCoord.Builder: ...
        @latlon.setter
        def latlon(
            self, value: LatLonCoord.Builder | LatLonCoord.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def timeSeries(self) -> TimeSeriesClient: ...
        @timeSeries.setter
        def timeSeries(self, value: TimeSeriesClient | TimeSeries.Server) -> None: ...
        @property
        def customData(self) -> Sequence[Location.KV.Builder]: ...
        @customData.setter
        def customData(
            self,
            value: Sequence[Location.KV.Builder | Location.KV.Reader]
            | Sequence[dict[str, Any]],
        ) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Location.Builder: ...
        @overload
        def init(self: Any, name: Literal["id"]) -> IdInformation.Builder: ...
        @overload
        def init(self: Any, name: Literal["latlon"]) -> LatLonCoord.Builder: ...
        @overload
        def init(
            self: Any, name: Literal["customData"], size: int = ...
        ) -> Sequence[Location.KV.Builder]: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        def copy(self) -> Location.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Location.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

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
    ) -> Iterator[Location.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Location.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        id: IdInformation.Builder | dict[str, Any] | None = None,
        heightNN: float | None = None,
        latlon: LatLonCoord.Builder | dict[str, Any] | None = None,
        timeSeries: TimeSeriesClient | TimeSeries.Server | None = None,
        customData: Sequence[Location.KV.Builder]
        | Sequence[dict[str, Any]]
        | None = None,
    ) -> Location.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Location.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Location.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

class DatasetClient(IdentifiableClient, PersistentClient):
    def metadata(self) -> Dataset.MetadataResult: ...
    def closestTimeSeriesAt(
        self, latlon: LatLonCoord | dict[str, Any] | None = None
    ) -> Dataset.ClosesttimeseriesatResult: ...
    def timeSeriesAt(
        self, locationId: str | None = None
    ) -> Dataset.TimeseriesatResult: ...
    def locations(self) -> Dataset.LocationsResult: ...
    def streamLocations(
        self, startAfterLocationId: str | None = None
    ) -> Dataset.StreamlocationsResult: ...
    def metadata_request(self) -> Dataset.MetadataRequest: ...
    def closestTimeSeriesAt_request(
        self, latlon: LatLonCoord.Builder | None = None
    ) -> Dataset.ClosesttimeseriesatRequest: ...
    def timeSeriesAt_request(
        self, locationId: str | None = None
    ) -> Dataset.TimeseriesatRequest: ...
    def locations_request(self) -> Dataset.LocationsRequest: ...
    def streamLocations_request(
        self, startAfterLocationId: str | None = None
    ) -> Dataset.StreamlocationsRequest: ...

MetaPlusDataBuilder: TypeAlias = MetaPlusData.Builder
MetaPlusDataReader: TypeAlias = MetaPlusData.Reader

class MetaPlusData:
    class Reader:
        @property
        def meta(self) -> Metadata.Reader: ...
        @property
        def data(self) -> DatasetClient: ...
        def as_builder(self) -> MetaPlusData.Builder: ...

    class Builder:
        @property
        def meta(self) -> Metadata.Builder: ...
        @meta.setter
        def meta(
            self, value: Metadata.Builder | Metadata.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def data(self) -> DatasetClient: ...
        @data.setter
        def data(self, value: DatasetClient | Dataset.Server) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> MetaPlusData.Builder: ...
        def init(self, name: Literal["meta"]) -> Metadata.Builder: ...
        def copy(self) -> MetaPlusData.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> MetaPlusData.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    def init(self, name: Literal["meta"]) -> Metadata: ...
    @staticmethod
    @contextmanager
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[MetaPlusData.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> MetaPlusData.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        meta: Metadata.Builder | dict[str, Any] | None = None,
        data: DatasetClient | Dataset.Server | None = None,
    ) -> MetaPlusData.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> MetaPlusData.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> MetaPlusData.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

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

TimeSeriesDataBuilder: TypeAlias = TimeSeriesData.Builder
TimeSeriesDataReader: TypeAlias = TimeSeriesData.Reader

class TimeSeriesData:
    class Reader:
        @property
        def data(self) -> Sequence[Sequence[float]]: ...
        @property
        def isTransposed(self) -> bool: ...
        @property
        def header(self) -> Sequence[Element]: ...
        @property
        def startDate(self) -> Date.Reader: ...
        @property
        def endDate(self) -> Date.Reader: ...
        @property
        def resolution(self) -> TimeSeries.Resolution: ...
        def as_builder(self) -> TimeSeriesData.Builder: ...

    class Builder:
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
        def startDate(self) -> Date.Builder: ...
        @startDate.setter
        def startDate(
            self, value: Date.Builder | Date.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def endDate(self) -> Date.Builder: ...
        @endDate.setter
        def endDate(
            self, value: Date.Builder | Date.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def resolution(self) -> TimeSeries.Resolution: ...
        @resolution.setter
        def resolution(
            self, value: TimeSeries.Resolution | Literal["daily", "hourly"]
        ) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> TimeSeriesData.Builder: ...
        @overload
        def init(self: Any, name: Literal["startDate"]) -> Date.Builder: ...
        @overload
        def init(self: Any, name: Literal["endDate"]) -> Date.Builder: ...
        @overload
        def init(
            self: Any, name: Literal["data"], size: int = ...
        ) -> Sequence[float]: ...
        @overload
        def init(
            self: Any, name: Literal["header"], size: int = ...
        ) -> Sequence[Element]: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        def copy(self) -> TimeSeriesData.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> TimeSeriesData.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

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
    ) -> Iterator[TimeSeriesData.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> TimeSeriesData.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        data: Sequence[Sequence[float]] | None = None,
        isTransposed: bool | None = None,
        header: Sequence[Element] | None = None,
        startDate: Date.Builder | dict[str, Any] | None = None,
        endDate: Date.Builder | dict[str, Any] | None = None,
        resolution: TimeSeries.Resolution | Literal["daily", "hourly"] | None = None,
    ) -> TimeSeriesData.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> TimeSeriesData.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> TimeSeriesData.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

class Service:
    class GetavailabledatasetsRequest(Protocol):
        def send(self) -> Service.GetavailabledatasetsResult: ...

    class GetavailabledatasetsResult(Awaitable[GetavailabledatasetsResult], Protocol):
        datasets: Sequence[MetaPlusData.Builder | MetaPlusData.Reader]

    class GetdatasetsforRequest(Protocol):
        template: Metadata.Builder
        @overload
        def init(self, name: Literal["template"]) -> Metadata.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> Service.GetdatasetsforResult: ...

    class GetdatasetsforResult(Awaitable[GetdatasetsforResult], Protocol):
        datasets: Sequence[Dataset]

    @classmethod
    def _new_client(
        cls, server: Service.Server | Identifiable.Server | Persistent.Server
    ) -> ServiceClient: ...
    class Server(Identifiable.Server, Persistent.Server):
        class GetavailabledatasetsResultTuple(NamedTuple):
            datasets: Sequence[MetaPlusData]

        class GetdatasetsforResultTuple(NamedTuple):
            datasets: Sequence[Dataset]

        class GetavailabledatasetsCallContext(Protocol):
            params: Service.GetavailabledatasetsRequest
            results: Service.GetavailabledatasetsResult

        class GetdatasetsforCallContext(Protocol):
            params: Service.GetdatasetsforRequest
            results: Service.GetdatasetsforResult

        def getAvailableDatasets(
            self,
            _context: Service.Server.GetavailabledatasetsCallContext,
            **kwargs: Any,
        ) -> Awaitable[Service.Server.GetavailabledatasetsResultTuple | None]: ...
        def getAvailableDatasets_context(
            self, context: Service.Server.GetavailabledatasetsCallContext
        ) -> Awaitable[None]: ...
        def getDatasetsFor(
            self,
            template: Metadata.Reader,
            _context: Service.Server.GetdatasetsforCallContext,
            **kwargs: Any,
        ) -> Awaitable[Service.Server.GetdatasetsforResultTuple | None]: ...
        def getDatasetsFor_context(
            self, context: Service.Server.GetdatasetsforCallContext
        ) -> Awaitable[None]: ...

class ServiceClient(IdentifiableClient, PersistentClient):
    def getAvailableDatasets(self) -> Service.GetavailabledatasetsResult: ...
    def getDatasetsFor(
        self, template: Metadata | dict[str, Any] | None = None
    ) -> Service.GetdatasetsforResult: ...
    def getAvailableDatasets_request(self) -> Service.GetavailabledatasetsRequest: ...
    def getDatasetsFor_request(
        self, template: Metadata.Builder | None = None
    ) -> Service.GetdatasetsforRequest: ...

class CSVTimeSeriesFactory:
    CSVConfigBuilder: TypeAlias = CSVConfig.Builder
    CSVConfigReader: TypeAlias = CSVConfig.Reader
    class CSVConfig:
        class Reader:
            @property
            def sep(self) -> str: ...
            @property
            def headerMap(self) -> Sequence[Pair.Reader]: ...
            @property
            def skipLinesToHeader(self) -> int: ...
            @property
            def skipLinesFromHeaderToData(self) -> int: ...
            def as_builder(self) -> CSVTimeSeriesFactory.CSVConfig.Builder: ...

        class Builder:
            @property
            def sep(self) -> str: ...
            @sep.setter
            def sep(self, value: str) -> None: ...
            @property
            def headerMap(self) -> Sequence[Pair.Builder]: ...
            @headerMap.setter
            def headerMap(
                self,
                value: Sequence[Pair.Builder | Pair.Reader] | Sequence[dict[str, Any]],
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
            def from_dict(
                dictionary: dict[str, Any],
            ) -> CSVTimeSeriesFactory.CSVConfig.Builder: ...
            def init(
                self, name: Literal["headerMap"], size: int = ...
            ) -> Sequence[Pair.Builder]: ...
            def copy(self) -> CSVTimeSeriesFactory.CSVConfig.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> CSVTimeSeriesFactory.CSVConfig.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[CSVTimeSeriesFactory.CSVConfig.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> CSVTimeSeriesFactory.CSVConfig.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            sep: str | None = None,
            headerMap: Sequence[Pair.Builder] | Sequence[dict[str, Any]] | None = None,
            skipLinesToHeader: int | None = None,
            skipLinesFromHeaderToData: int | None = None,
        ) -> CSVTimeSeriesFactory.CSVConfig.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> CSVTimeSeriesFactory.CSVConfig.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> CSVTimeSeriesFactory.CSVConfig.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class CreateRequest(Protocol):
        csvData: str
        config: CSVTimeSeriesFactory.CSVConfig.Builder
        @overload
        def init(
            self, name: Literal["config"]
        ) -> CSVTimeSeriesFactory.CSVConfig.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> CSVTimeSeriesFactory.CreateResult: ...

    class CreateResult(Awaitable[CreateResult], Protocol):
        timeseries: TimeSeriesClient
        error: str

    @classmethod
    def _new_client(
        cls, server: CSVTimeSeriesFactory.Server | Identifiable.Server
    ) -> CSVTimeSeriesFactoryClient: ...
    class Server(Identifiable.Server):
        class CreateResultTuple(NamedTuple):
            timeseries: TimeSeries.Server
            error: str

        class CreateCallContext(Protocol):
            params: CSVTimeSeriesFactory.CreateRequest
            results: CSVTimeSeriesFactory.CreateResult

        def create(
            self,
            csvData: str,
            config: CSVTimeSeriesFactory.CSVConfig.Reader,
            _context: CSVTimeSeriesFactory.Server.CreateCallContext,
            **kwargs: Any,
        ) -> Awaitable[CSVTimeSeriesFactory.Server.CreateResultTuple | None]: ...
        def create_context(
            self, context: CSVTimeSeriesFactory.Server.CreateCallContext
        ) -> Awaitable[None]: ...

class CSVTimeSeriesFactoryClient(IdentifiableClient):
    def create(
        self,
        csvData: str | None = None,
        config: CSVTimeSeriesFactory.CSVConfig | dict[str, Any] | None = None,
    ) -> CSVTimeSeriesFactory.CreateResult: ...
    def create_request(
        self,
        csvData: str | None = None,
        config: CSVTimeSeriesFactory.CSVConfig.Builder | None = None,
    ) -> CSVTimeSeriesFactory.CreateRequest: ...

class AlterTimeSeriesWrapper:
    AlteredBuilder: TypeAlias = Altered.Builder
    AlteredReader: TypeAlias = Altered.Reader
    class Altered:
        class AlterType(Enum):
            add = "add"
            mul = "mul"

        class Reader:
            @property
            def element(self) -> Element: ...
            @property
            def value(self) -> float: ...
            @property
            def type(self) -> AlterTimeSeriesWrapper.Altered.AlterType: ...
            def as_builder(self) -> AlterTimeSeriesWrapper.Altered.Builder: ...

        class Builder:
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
            def from_dict(
                dictionary: dict[str, Any],
            ) -> AlterTimeSeriesWrapper.Altered.Builder: ...
            def copy(self) -> AlterTimeSeriesWrapper.Altered.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> AlterTimeSeriesWrapper.Altered.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @staticmethod
        @contextmanager
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[AlterTimeSeriesWrapper.Altered.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AlterTimeSeriesWrapper.Altered.Reader: ...
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
        ) -> AlterTimeSeriesWrapper.Altered.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AlterTimeSeriesWrapper.Altered.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AlterTimeSeriesWrapper.Altered.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class WrappedtimeseriesRequest(Protocol):
        def send(self) -> AlterTimeSeriesWrapper.WrappedtimeseriesResult: ...

    class WrappedtimeseriesResult(Awaitable[WrappedtimeseriesResult], Protocol):
        timeSeries: TimeSeriesClient

    class AlteredelementsRequest(Protocol):
        def send(self) -> AlterTimeSeriesWrapper.AlteredelementsResult: ...

    class AlteredelementsResult(Awaitable[AlteredelementsResult], Protocol):
        list: Sequence[
            AlterTimeSeriesWrapper.Altered.Builder
            | AlterTimeSeriesWrapper.Altered.Reader
        ]

    class AlterRequest(Protocol):
        desc: AlterTimeSeriesWrapper.Altered.Builder
        asNewTimeSeries: bool
        @overload
        def init(
            self, name: Literal["desc"]
        ) -> AlterTimeSeriesWrapper.Altered.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> AlterTimeSeriesWrapper.AlterResult: ...

    class AlterResult(Awaitable[AlterResult], Protocol):
        timeSeries: TimeSeriesClient

    class RemoveRequest(Protocol):
        alteredElement: (
            Element
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
        )
        def send(self) -> None: ...

    class ReplacewrappedtimeseriesRequest(Protocol):
        timeSeries: TimeSeries | TimeSeries.Server
        def send(self) -> None: ...

    @classmethod
    def _new_client(
        cls,
        server: AlterTimeSeriesWrapper.Server
        | Identifiable.Server
        | Persistent.Server
        | TimeSeries.Server,
    ) -> AlterTimeSeriesWrapperClient: ...
    class Server(TimeSeries.Server):
        class WrappedtimeseriesResultTuple(NamedTuple):
            timeSeries: TimeSeries.Server

        class AlteredelementsResultTuple(NamedTuple):
            list: Sequence[AlterTimeSeriesWrapper.Altered]

        class AlterResultTuple(NamedTuple):
            timeSeries: TimeSeries.Server

        class WrappedtimeseriesCallContext(Protocol):
            params: AlterTimeSeriesWrapper.WrappedtimeseriesRequest
            results: AlterTimeSeriesWrapper.WrappedtimeseriesResult

        class AlteredelementsCallContext(Protocol):
            params: AlterTimeSeriesWrapper.AlteredelementsRequest
            results: AlterTimeSeriesWrapper.AlteredelementsResult

        class AlterCallContext(Protocol):
            params: AlterTimeSeriesWrapper.AlterRequest
            results: AlterTimeSeriesWrapper.AlterResult

        class RemoveCallContext(Protocol):
            params: AlterTimeSeriesWrapper.RemoveRequest

        class ReplacewrappedtimeseriesCallContext(Protocol):
            params: AlterTimeSeriesWrapper.ReplacewrappedtimeseriesRequest

        def wrappedTimeSeries(
            self,
            _context: AlterTimeSeriesWrapper.Server.WrappedtimeseriesCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            TimeSeries.Server
            | AlterTimeSeriesWrapper.Server.WrappedtimeseriesResultTuple
            | None
        ]: ...
        def wrappedTimeSeries_context(
            self, context: AlterTimeSeriesWrapper.Server.WrappedtimeseriesCallContext
        ) -> Awaitable[None]: ...
        def alteredElements(
            self,
            _context: AlterTimeSeriesWrapper.Server.AlteredelementsCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            AlterTimeSeriesWrapper.Server.AlteredelementsResultTuple | None
        ]: ...
        def alteredElements_context(
            self, context: AlterTimeSeriesWrapper.Server.AlteredelementsCallContext
        ) -> Awaitable[None]: ...
        def alter(
            self,
            desc: AlterTimeSeriesWrapper.Altered.Reader,
            asNewTimeSeries: bool,
            _context: AlterTimeSeriesWrapper.Server.AlterCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            TimeSeries.Server | AlterTimeSeriesWrapper.Server.AlterResultTuple | None
        ]: ...
        def alter_context(
            self, context: AlterTimeSeriesWrapper.Server.AlterCallContext
        ) -> Awaitable[None]: ...
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
            _context: AlterTimeSeriesWrapper.Server.RemoveCallContext,
            **kwargs: Any,
        ) -> Awaitable[None]: ...
        def remove_context(
            self, context: AlterTimeSeriesWrapper.Server.RemoveCallContext
        ) -> Awaitable[None]: ...
        def replaceWrappedTimeSeries(
            self,
            timeSeries: TimeSeries,
            _context: AlterTimeSeriesWrapper.Server.ReplacewrappedtimeseriesCallContext,
            **kwargs: Any,
        ) -> Awaitable[None]: ...
        def replaceWrappedTimeSeries_context(
            self,
            context: AlterTimeSeriesWrapper.Server.ReplacewrappedtimeseriesCallContext,
        ) -> Awaitable[None]: ...

class AlterTimeSeriesWrapperClient(TimeSeriesClient):
    def wrappedTimeSeries(self) -> AlterTimeSeriesWrapper.WrappedtimeseriesResult: ...
    def alteredElements(self) -> AlterTimeSeriesWrapper.AlteredelementsResult: ...
    def alter(
        self,
        desc: AlterTimeSeriesWrapper.Altered | dict[str, Any] | None = None,
        asNewTimeSeries: bool | None = None,
    ) -> AlterTimeSeriesWrapper.AlterResult: ...
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
        ]
        | None = None,
    ) -> None: ...
    def replaceWrappedTimeSeries(
        self, timeSeries: TimeSeries | TimeSeries.Server | None = None
    ) -> None: ...
    def wrappedTimeSeries_request(
        self,
    ) -> AlterTimeSeriesWrapper.WrappedtimeseriesRequest: ...
    def alteredElements_request(
        self,
    ) -> AlterTimeSeriesWrapper.AlteredelementsRequest: ...
    def alter_request(
        self,
        desc: AlterTimeSeriesWrapper.Altered.Builder | None = None,
        asNewTimeSeries: bool | None = None,
    ) -> AlterTimeSeriesWrapper.AlterRequest: ...
    def remove_request(
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
        ]
        | None = None,
    ) -> AlterTimeSeriesWrapper.RemoveRequest: ...
    def replaceWrappedTimeSeries_request(
        self, timeSeries: TimeSeries | TimeSeries.Server | None = None
    ) -> AlterTimeSeriesWrapper.ReplacewrappedtimeseriesRequest: ...

class AlterTimeSeriesWrapperFactory:
    class WrapRequest(Protocol):
        timeSeries: TimeSeries | TimeSeries.Server
        def send(self) -> AlterTimeSeriesWrapperFactory.WrapResult: ...

    class WrapResult(Awaitable[WrapResult], Protocol):
        wrapper: AlterTimeSeriesWrapperClient

    @classmethod
    def _new_client(
        cls, server: AlterTimeSeriesWrapperFactory.Server | Identifiable.Server
    ) -> AlterTimeSeriesWrapperFactoryClient: ...
    class Server(Identifiable.Server):
        class WrapResultTuple(NamedTuple):
            wrapper: AlterTimeSeriesWrapper.Server

        class WrapCallContext(Protocol):
            params: AlterTimeSeriesWrapperFactory.WrapRequest
            results: AlterTimeSeriesWrapperFactory.WrapResult

        def wrap(
            self,
            timeSeries: TimeSeries,
            _context: AlterTimeSeriesWrapperFactory.Server.WrapCallContext,
            **kwargs: Any,
        ) -> Awaitable[
            AlterTimeSeriesWrapper.Server
            | AlterTimeSeriesWrapperFactory.Server.WrapResultTuple
            | None
        ]: ...
        def wrap_context(
            self, context: AlterTimeSeriesWrapperFactory.Server.WrapCallContext
        ) -> Awaitable[None]: ...

class AlterTimeSeriesWrapperFactoryClient(IdentifiableClient):
    def wrap(
        self, timeSeries: TimeSeries | TimeSeries.Server | None = None
    ) -> AlterTimeSeriesWrapperFactory.WrapResult: ...
    def wrap_request(
        self, timeSeries: TimeSeries | TimeSeries.Server | None = None
    ) -> AlterTimeSeriesWrapperFactory.WrapRequest: ...
