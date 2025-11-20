"""This is an automatically generated stub for `climate.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, MutableSequence, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _StructModule,
)

from .common_capnp import (
    _IdentifiableModule,
    _IdInformationModule,
    _PairModule,
)
from .date_capnp import _DateModule
from .geo_capnp import _LatLonCoordModule
from .persistence_capnp import _PersistentModule

class _GCMModule:
    cccmaCanEsm2: int
    ichecEcEarth: int
    ipslIpslCm5AMr: int
    mirocMiroc5: int
    mpiMMpiEsmLr: int
    gfdlEsm4: int
    ipslCm6aLr: int
    mpiEsm12Hr: int
    mriEsm20: int
    ukesm10Ll: int
    gswp3W5E5: int
    mohcHadGem2Es: int

class _RCMModule:
    clmcomCclm4817: int
    gericsRemo2015: int
    knmiRacmo22E: int
    smhiRca4: int
    clmcomBtuCclm4817: int
    mpiCscRemo2009: int
    uhohWrf361H: int

class _SSPModule:
    ssp1: int
    ssp2: int
    ssp3: int
    ssp4: int
    ssp5: int

class _RCPModule:
    rcp19: int
    rcp26: int
    rcp34: int
    rcp45: int
    rcp60: int
    rcp70: int
    rcp85: int

class _EnsembleMemberModule(_StructModule):
    class Reader(_DynamicStructReader):
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
            allocate_seg_callable: Any = None,
        ) -> EnsembleMemberBuilder: ...

    class Builder(_DynamicStructBuilder):
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
        def as_reader(self) -> EnsembleMemberReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        r: int | None = None,
        i: int | None = None,
        p: int | None = None,
        f: int | None = None,
        **kwargs: Any,
    ) -> EnsembleMemberBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[EnsembleMemberReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[EnsembleMemberReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[EnsembleMemberBuilder]: ...
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
    ) -> EnsembleMemberReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> EnsembleMemberReader: ...

EnsembleMember: _EnsembleMemberModule

class _MetadataModule(_StructModule):
    class _SupportedModule(_InterfaceModule):
        class CategoriesRequest(Protocol):
            def send(
                self,
            ) -> _MetadataModule._SupportedModule.SupportedClient.CategoriesResult: ...

        class SupportedvaluesRequest(Protocol):
            typeId: str
            def send(
                self,
            ) -> (
                _MetadataModule._SupportedModule.SupportedClient.SupportedvaluesResult
            ): ...

        def _new_client(
            self, server: _DynamicCapabilityServer
        ) -> _MetadataModule._SupportedModule.SupportedClient: ...
        class Server(_DynamicCapabilityServer):
            class CategoriesResult(Awaitable[CategoriesResult], Protocol):
                types: Any

            class SupportedvaluesResult(Awaitable[SupportedvaluesResult], Protocol):
                values: Any

            class CategoriesResultTuple(NamedTuple):
                pass

            class SupportedvaluesResultTuple(NamedTuple):
                pass

            class CategoriesParams(Protocol): ...

            class CategoriesCallContext(Protocol):
                params: _MetadataModule._SupportedModule.Server.CategoriesParams
                results: _MetadataModule._SupportedModule.Server.CategoriesResult

            class SupportedvaluesParams(Protocol):
                typeId: str

            class SupportedvaluesCallContext(Protocol):
                params: _MetadataModule._SupportedModule.Server.SupportedvaluesParams
                results: _MetadataModule._SupportedModule.Server.SupportedvaluesResult

            def categories(
                self,
                _context: _MetadataModule._SupportedModule.Server.CategoriesCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                _MetadataModule._SupportedModule.Server.CategoriesResultTuple | None
            ]: ...
            def categories_context(
                self,
                context: _MetadataModule._SupportedModule.Server.CategoriesCallContext,
            ) -> Awaitable[None]: ...
            def supportedValues(
                self,
                typeId: str,
                _context: _MetadataModule._SupportedModule.Server.SupportedvaluesCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                _MetadataModule._SupportedModule.Server.SupportedvaluesResultTuple
                | None
            ]: ...
            def supportedValues_context(
                self,
                context: _MetadataModule._SupportedModule.Server.SupportedvaluesCallContext,
            ) -> Awaitable[None]: ...

        class SupportedClient(_DynamicCapabilityClient):
            class CategoriesResult(Awaitable[CategoriesResult], Protocol):
                types: Any

            class SupportedvaluesResult(Awaitable[SupportedvaluesResult], Protocol):
                values: Any

            def categories(
                self,
            ) -> _MetadataModule._SupportedModule.SupportedClient.CategoriesResult: ...
            def supportedValues(
                self, typeId: str | None = None
            ) -> (
                _MetadataModule._SupportedModule.SupportedClient.SupportedvaluesResult
            ): ...
            def categories_request(
                self,
            ) -> _MetadataModule._SupportedModule.CategoriesRequest: ...
            def supportedValues_request(
                self, typeId: str | None = None
            ) -> _MetadataModule._SupportedModule.SupportedvaluesRequest: ...

    Supported: _SupportedModule
    type SupportedClient = _MetadataModule._SupportedModule.SupportedClient
    class _ValueModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def text(self) -> str: ...
            @property
            def float(self) -> float: ...
            @property
            def int(self) -> int: ...
            @property
            def bool(self) -> bool: ...
            @property
            def date(self) -> _DateModule.Reader: ...
            @override
            def which(self) -> Literal["text", "float", "int", "bool", "date"]: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> ValueBuilder: ...

        class Builder(_DynamicStructBuilder):
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
            def date(self) -> _DateModule.Builder: ...
            @date.setter
            def date(
                self, value: _DateModule.Builder | _DateModule.Reader | dict[str, Any]
            ) -> None: ...
            @override
            def which(self) -> Literal["text", "float", "int", "bool", "date"]: ...
            def init(
                self, field: Literal["date"], size: int | None = None
            ) -> _DateModule.Builder: ...
            @override
            def as_reader(self) -> ValueReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            text: str | None = None,
            float: float | None = None,
            int: int | None = None,
            bool: bool | None = None,
            date: _DateModule.Builder | dict[str, Any] | None = None,
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

    type ValueReader = _ValueModule.Reader
    type ValueBuilder = _ValueModule.Builder
    Value: _ValueModule
    class _EntryModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def gcm(self) -> GCMEnum: ...
            @property
            def rcm(self) -> RCMEnum: ...
            @property
            def historical(self) -> None: ...
            @property
            def rcp(self) -> RCPEnum: ...
            @property
            def ssp(self) -> SSPEnum: ...
            @property
            def ensMem(self) -> EnsembleMemberReader: ...
            @property
            def version(self) -> str: ...
            @property
            def start(self) -> _DateModule.Reader: ...
            @property
            def end(self) -> _DateModule.Reader: ...
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
                allocate_seg_callable: Any = None,
            ) -> EntryBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def gcm(self) -> GCMEnum: ...
            @gcm.setter
            def gcm(self, value: GCMEnum) -> None: ...
            @property
            def rcm(self) -> RCMEnum: ...
            @rcm.setter
            def rcm(self, value: RCMEnum) -> None: ...
            @property
            def historical(self) -> None: ...
            @historical.setter
            def historical(self, value: None) -> None: ...
            @property
            def rcp(self) -> RCPEnum: ...
            @rcp.setter
            def rcp(self, value: RCPEnum) -> None: ...
            @property
            def ssp(self) -> SSPEnum: ...
            @ssp.setter
            def ssp(self, value: SSPEnum) -> None: ...
            @property
            def ensMem(self) -> EnsembleMemberBuilder: ...
            @ensMem.setter
            def ensMem(
                self,
                value: EnsembleMemberBuilder | EnsembleMemberReader | dict[str, Any],
            ) -> None: ...
            @property
            def version(self) -> str: ...
            @version.setter
            def version(self, value: str) -> None: ...
            @property
            def start(self) -> _DateModule.Builder: ...
            @start.setter
            def start(
                self, value: _DateModule.Builder | _DateModule.Reader | dict[str, Any]
            ) -> None: ...
            @property
            def end(self) -> _DateModule.Builder: ...
            @end.setter
            def end(
                self, value: _DateModule.Builder | _DateModule.Reader | dict[str, Any]
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
            @overload
            def init(
                self, field: Literal["ensMem"], size: int | None = None
            ) -> EnsembleMemberBuilder: ...
            @overload
            def init(
                self, field: Literal["start"], size: int | None = None
            ) -> _DateModule.Builder: ...
            @overload
            def init(
                self, field: Literal["end"], size: int | None = None
            ) -> _DateModule.Builder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> EntryReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            gcm: GCMEnum | None = None,
            rcm: RCMEnum | None = None,
            historical: None | None = None,
            rcp: RCPEnum | None = None,
            ssp: SSPEnum | None = None,
            ensMem: EnsembleMemberBuilder | dict[str, Any] | None = None,
            version: str | None = None,
            start: _DateModule.Builder | dict[str, Any] | None = None,
            end: _DateModule.Builder | dict[str, Any] | None = None,
            co2: float | None = None,
            picontrol: None | None = None,
            description: str | None = None,
            **kwargs: Any,
        ) -> EntryBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[EntryBuilder]: ...
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
        ) -> EntryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> EntryReader: ...

    type EntryReader = _EntryModule.Reader
    type EntryBuilder = _EntryModule.Builder
    Entry: _EntryModule
    class _InformationModule(_InterfaceModule):
        class ForoneRequest(Protocol):
            entry: EntryBuilder
            @overload
            def init(self, name: Literal["entry"]) -> EntryBuilder: ...
            @overload
            def init(self, name: str, size: int = ...) -> Any: ...
            def send(
                self,
            ) -> _MetadataModule._InformationModule.InformationClient.ForoneResult: ...

        class ForallRequest(Protocol):
            def send(
                self,
            ) -> _MetadataModule._InformationModule.InformationClient.ForallResult: ...

        def _new_client(
            self, server: _DynamicCapabilityServer
        ) -> _MetadataModule._InformationModule.InformationClient: ...
        class Server(_DynamicCapabilityServer):
            class ForoneResult(Awaitable[ForoneResult], Protocol):
                id: str
                name: str
                description: str

            class ForallResult(Awaitable[ForallResult], Protocol):
                all: Any

            class ForoneResultTuple(NamedTuple):
                id: str
                name: str
                description: str

            class ForallResultTuple(NamedTuple):
                pass

            class ForoneParams(Protocol):
                entry: EntryReader

            class ForoneCallContext(Protocol):
                params: _MetadataModule._InformationModule.Server.ForoneParams
                results: _MetadataModule._InformationModule.Server.ForoneResult

            class ForallParams(Protocol): ...

            class ForallCallContext(Protocol):
                params: _MetadataModule._InformationModule.Server.ForallParams
                results: _MetadataModule._InformationModule.Server.ForallResult

            def forOne(
                self,
                entry: EntryReader,
                _context: _MetadataModule._InformationModule.Server.ForoneCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                _MetadataModule._InformationModule.Server.ForoneResultTuple | None
            ]: ...
            def forOne_context(
                self,
                context: _MetadataModule._InformationModule.Server.ForoneCallContext,
            ) -> Awaitable[None]: ...
            def forAll(
                self,
                _context: _MetadataModule._InformationModule.Server.ForallCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                _MetadataModule._InformationModule.Server.ForallResultTuple | None
            ]: ...
            def forAll_context(
                self,
                context: _MetadataModule._InformationModule.Server.ForallCallContext,
            ) -> Awaitable[None]: ...

        class InformationClient(_DynamicCapabilityClient):
            class ForoneResult(Awaitable[ForoneResult], Protocol):
                id: str
                name: str
                description: str

            class ForallResult(Awaitable[ForallResult], Protocol):
                all: Any

            def forOne(
                self, entry: EntryBuilder | EntryReader | dict[str, Any] | None = None
            ) -> _MetadataModule._InformationModule.InformationClient.ForoneResult: ...
            def forAll(
                self,
            ) -> _MetadataModule._InformationModule.InformationClient.ForallResult: ...
            def forOne_request(
                self, entry: EntryBuilder | None = None
            ) -> _MetadataModule._InformationModule.ForoneRequest: ...
            def forAll_request(
                self,
            ) -> _MetadataModule._InformationModule.ForallRequest: ...

    Information: _InformationModule
    type InformationClient = _MetadataModule._InformationModule.InformationClient
    class Reader(_DynamicStructReader):
        @property
        def entries(self) -> Sequence[EntryReader]: ...
        @property
        def info(self) -> _MetadataModule._InformationModule.InformationClient: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> MetadataBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def entries(self) -> MutableSequence[EntryBuilder]: ...
        @entries.setter
        def entries(
            self, value: Sequence[EntryBuilder | EntryReader] | Sequence[dict[str, Any]]
        ) -> None: ...
        @property
        def info(self) -> _MetadataModule._InformationModule.InformationClient: ...
        @info.setter
        def info(
            self,
            value: _MetadataModule._InformationModule.InformationClient
            | _MetadataModule._InformationModule.Server,
        ) -> None: ...
        def init(
            self, field: Literal["entries"], size: int | None = None
        ) -> MutableSequence[EntryBuilder]: ...
        @override
        def as_reader(self) -> MetadataReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        entries: Sequence[EntryBuilder] | Sequence[dict[str, Any]] | None = None,
        info: _MetadataModule._InformationModule.InformationClient
        | _MetadataModule._InformationModule.Server
        | None = None,
        **kwargs: Any,
    ) -> MetadataBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[MetadataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[MetadataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[MetadataBuilder]: ...
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
    ) -> MetadataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> MetadataReader: ...

Metadata: _MetadataModule

class _DatasetModule(_IdentifiableModule, _PersistentModule):
    class _GetLocationsCallbackModule(_InterfaceModule):
        class NextlocationsRequest(Protocol):
            maxCount: int
            def send(
                self,
            ) -> _DatasetModule._GetLocationsCallbackModule.GetLocationsCallbackClient.NextlocationsResult: ...

        def _new_client(
            self, server: _DynamicCapabilityServer
        ) -> _DatasetModule._GetLocationsCallbackModule.GetLocationsCallbackClient: ...
        class Server(_DynamicCapabilityServer):
            class NextlocationsResult(Awaitable[NextlocationsResult], Protocol):
                locations: Sequence[LocationBuilder | LocationReader]

            class NextlocationsResultTuple(NamedTuple):
                locations: Sequence[LocationBuilder | LocationReader]

            class NextlocationsParams(Protocol):
                maxCount: int

            class NextlocationsCallContext(Protocol):
                params: _DatasetModule._GetLocationsCallbackModule.Server.NextlocationsParams
                results: _DatasetModule._GetLocationsCallbackModule.Server.NextlocationsResult

            def nextLocations(
                self,
                maxCount: int,
                _context: _DatasetModule._GetLocationsCallbackModule.Server.NextlocationsCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                _DatasetModule._GetLocationsCallbackModule.Server.NextlocationsResultTuple
                | None
            ]: ...
            def nextLocations_context(
                self,
                context: _DatasetModule._GetLocationsCallbackModule.Server.NextlocationsCallContext,
            ) -> Awaitable[None]: ...

        class GetLocationsCallbackClient(_DynamicCapabilityClient):
            class NextlocationsResult(Awaitable[NextlocationsResult], Protocol):
                locations: Sequence[LocationReader]

            def nextLocations(
                self, maxCount: int | None = None
            ) -> _DatasetModule._GetLocationsCallbackModule.GetLocationsCallbackClient.NextlocationsResult: ...
            def nextLocations_request(
                self, maxCount: int | None = None
            ) -> _DatasetModule._GetLocationsCallbackModule.NextlocationsRequest: ...

    GetLocationsCallback: _GetLocationsCallbackModule
    type GetLocationsCallbackClient = (
        _DatasetModule._GetLocationsCallbackModule.GetLocationsCallbackClient
    )
    class MetadataRequest(Protocol):
        def send(self) -> _DatasetModule.DatasetClient.MetadataResult: ...

    class ClosesttimeseriesatRequest(Protocol):
        latlon: _LatLonCoordModule.Builder
        @overload
        def init(self, name: Literal["latlon"]) -> _LatLonCoordModule.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _DatasetModule.DatasetClient.ClosesttimeseriesatResult: ...

    class TimeseriesatRequest(Protocol):
        locationId: str
        def send(self) -> _DatasetModule.DatasetClient.TimeseriesatResult: ...

    class LocationsRequest(Protocol):
        def send(self) -> _DatasetModule.DatasetClient.LocationsResult: ...

    class StreamlocationsRequest(Protocol):
        startAfterLocationId: str
        def send(self) -> _DatasetModule.DatasetClient.StreamlocationsResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _DatasetModule.DatasetClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class MetadataResult(Awaitable[MetadataResult], Protocol):
            entries: Sequence[EntryBuilder | EntryReader]
            info: _MetadataModule._InformationModule.InformationClient

        class ClosesttimeseriesatResult(Awaitable[ClosesttimeseriesatResult], Protocol):
            timeSeries: _TimeSeriesModule.TimeSeriesClient

        class TimeseriesatResult(Awaitable[TimeseriesatResult], Protocol):
            timeSeries: _TimeSeriesModule.TimeSeriesClient

        class LocationsResult(Awaitable[LocationsResult], Protocol):
            locations: Sequence[LocationBuilder | LocationReader]

        class StreamlocationsResult(Awaitable[StreamlocationsResult], Protocol):
            locationsCallback: (
                _DatasetModule._GetLocationsCallbackModule.GetLocationsCallbackClient
            )

        class MetadataResultTuple(NamedTuple):
            entries: Sequence[EntryBuilder | EntryReader]
            info: _MetadataModule._InformationModule.Server

        class ClosesttimeseriesatResultTuple(NamedTuple):
            timeSeries: _TimeSeriesModule.Server

        class TimeseriesatResultTuple(NamedTuple):
            timeSeries: _TimeSeriesModule.Server

        class LocationsResultTuple(NamedTuple):
            locations: Sequence[LocationBuilder | LocationReader]

        class StreamlocationsResultTuple(NamedTuple):
            locationsCallback: _DatasetModule._GetLocationsCallbackModule.Server

        class MetadataParams(Protocol): ...

        class MetadataCallContext(Protocol):
            params: _DatasetModule.Server.MetadataParams
            results: _DatasetModule.Server.MetadataResult

        class ClosesttimeseriesatParams(Protocol):
            latlon: _LatLonCoordModule.Reader

        class ClosesttimeseriesatCallContext(Protocol):
            params: _DatasetModule.Server.ClosesttimeseriesatParams
            results: _DatasetModule.Server.ClosesttimeseriesatResult

        class TimeseriesatParams(Protocol):
            locationId: str

        class TimeseriesatCallContext(Protocol):
            params: _DatasetModule.Server.TimeseriesatParams
            results: _DatasetModule.Server.TimeseriesatResult

        class LocationsParams(Protocol): ...

        class LocationsCallContext(Protocol):
            params: _DatasetModule.Server.LocationsParams
            results: _DatasetModule.Server.LocationsResult

        class StreamlocationsParams(Protocol):
            startAfterLocationId: str

        class StreamlocationsCallContext(Protocol):
            params: _DatasetModule.Server.StreamlocationsParams
            results: _DatasetModule.Server.StreamlocationsResult

        def metadata(
            self,
            _context: _DatasetModule.Server.MetadataCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_DatasetModule.Server.MetadataResultTuple | None]: ...
        def metadata_context(
            self, context: _DatasetModule.Server.MetadataCallContext
        ) -> Awaitable[None]: ...
        def closestTimeSeriesAt(
            self,
            latlon: _LatLonCoordModule.Reader,
            _context: _DatasetModule.Server.ClosesttimeseriesatCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _TimeSeriesModule.Server
            | _DatasetModule.Server.ClosesttimeseriesatResultTuple
            | None
        ]: ...
        def closestTimeSeriesAt_context(
            self, context: _DatasetModule.Server.ClosesttimeseriesatCallContext
        ) -> Awaitable[None]: ...
        def timeSeriesAt(
            self,
            locationId: str,
            _context: _DatasetModule.Server.TimeseriesatCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _TimeSeriesModule.Server
            | _DatasetModule.Server.TimeseriesatResultTuple
            | None
        ]: ...
        def timeSeriesAt_context(
            self, context: _DatasetModule.Server.TimeseriesatCallContext
        ) -> Awaitable[None]: ...
        def locations(
            self,
            _context: _DatasetModule.Server.LocationsCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_DatasetModule.Server.LocationsResultTuple | None]: ...
        def locations_context(
            self, context: _DatasetModule.Server.LocationsCallContext
        ) -> Awaitable[None]: ...
        def streamLocations(
            self,
            startAfterLocationId: str,
            _context: _DatasetModule.Server.StreamlocationsCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _DatasetModule._GetLocationsCallbackModule.Server
            | _DatasetModule.Server.StreamlocationsResultTuple
            | None
        ]: ...
        def streamLocations_context(
            self, context: _DatasetModule.Server.StreamlocationsCallContext
        ) -> Awaitable[None]: ...

    class DatasetClient(
        _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
    ):
        class MetadataResult(Awaitable[MetadataResult], Protocol):
            entries: Sequence[EntryReader]
            info: _MetadataModule._InformationModule.InformationClient

        class ClosesttimeseriesatResult(Awaitable[ClosesttimeseriesatResult], Protocol):
            timeSeries: _TimeSeriesModule.TimeSeriesClient

        class TimeseriesatResult(Awaitable[TimeseriesatResult], Protocol):
            timeSeries: _TimeSeriesModule.TimeSeriesClient

        class LocationsResult(Awaitable[LocationsResult], Protocol):
            locations: Sequence[LocationReader]

        class StreamlocationsResult(Awaitable[StreamlocationsResult], Protocol):
            locationsCallback: (
                _DatasetModule._GetLocationsCallbackModule.GetLocationsCallbackClient
            )

        def metadata(self) -> _DatasetModule.DatasetClient.MetadataResult: ...
        def closestTimeSeriesAt(
            self, latlon: _LatLonCoordModule | dict[str, Any] | None = None
        ) -> _DatasetModule.DatasetClient.ClosesttimeseriesatResult: ...
        def timeSeriesAt(
            self, locationId: str | None = None
        ) -> _DatasetModule.DatasetClient.TimeseriesatResult: ...
        def locations(self) -> _DatasetModule.DatasetClient.LocationsResult: ...
        def streamLocations(
            self, startAfterLocationId: str | None = None
        ) -> _DatasetModule.DatasetClient.StreamlocationsResult: ...
        def metadata_request(self) -> _DatasetModule.MetadataRequest: ...
        def closestTimeSeriesAt_request(
            self, latlon: _LatLonCoordModule.Builder | None = None
        ) -> _DatasetModule.ClosesttimeseriesatRequest: ...
        def timeSeriesAt_request(
            self, locationId: str | None = None
        ) -> _DatasetModule.TimeseriesatRequest: ...
        def locations_request(self) -> _DatasetModule.LocationsRequest: ...
        def streamLocations_request(
            self, startAfterLocationId: str | None = None
        ) -> _DatasetModule.StreamlocationsRequest: ...

class _TimeSeriesModule(_IdentifiableModule, _PersistentModule):
    class _ResolutionModule:
        daily: int
        hourly: int

    Resolution: _ResolutionModule
    class ResolutionRequest(Protocol):
        def send(self) -> _TimeSeriesModule.TimeSeriesClient.ResolutionResult: ...

    class RangeRequest(Protocol):
        def send(self) -> _TimeSeriesModule.TimeSeriesClient.RangeResult: ...

    class HeaderRequest(Protocol):
        def send(self) -> _TimeSeriesModule.TimeSeriesClient.HeaderResult: ...

    class DataRequest(Protocol):
        def send(self) -> _TimeSeriesModule.TimeSeriesClient.DataResult: ...

    class DatatRequest(Protocol):
        def send(self) -> _TimeSeriesModule.TimeSeriesClient.DatatResult: ...

    class SubrangeRequest(Protocol):
        start: _DateModule.Builder
        end: _DateModule.Builder
        @overload
        def init(self, name: Literal["start"]) -> _DateModule.Builder: ...
        @overload
        def init(self, name: Literal["end"]) -> _DateModule.Builder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _TimeSeriesModule.TimeSeriesClient.SubrangeResult: ...

    class SubheaderRequest(Protocol):
        def send(self) -> _TimeSeriesModule.TimeSeriesClient.SubheaderResult: ...

    class MetadataRequest(Protocol):
        def send(self) -> _TimeSeriesModule.TimeSeriesClient.MetadataResult: ...

    class LocationRequest(Protocol):
        def send(self) -> _TimeSeriesModule.TimeSeriesClient.LocationResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _TimeSeriesModule.TimeSeriesClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class ResolutionResult(Awaitable[ResolutionResult], Protocol):
            resolution: TimeSeriesResolutionEnum

        class RangeResult(Awaitable[RangeResult], Protocol):
            startDate: _DateModule.Builder | _DateModule.Reader
            endDate: _DateModule.Builder | _DateModule.Reader

        class HeaderResult(Awaitable[HeaderResult], Protocol):
            header: Any

        class DataResult(Awaitable[DataResult], Protocol):
            data: Sequence[Sequence[float]]

        class DatatResult(Awaitable[DatatResult], Protocol):
            data: Sequence[Sequence[float]]

        class SubrangeResult(Awaitable[SubrangeResult], Protocol):
            timeSeries: _TimeSeriesModule.TimeSeriesClient

        class SubheaderResult(Awaitable[SubheaderResult], Protocol):
            timeSeries: _TimeSeriesModule.TimeSeriesClient

        class MetadataResult(Awaitable[MetadataResult], Protocol):
            entries: Sequence[EntryBuilder | EntryReader]
            info: _MetadataModule._InformationModule.InformationClient

        class LocationResult(Awaitable[LocationResult], Protocol):
            id: _IdInformationModule.Builder | _IdInformationModule.Reader
            heightNN: float
            latlon: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader
            timeSeries: _TimeSeriesModule.TimeSeriesClient
            customData: Sequence[KVBuilder | KVReader]

        class ResolutionResultTuple(NamedTuple):
            resolution: TimeSeriesResolutionEnum

        class RangeResultTuple(NamedTuple):
            startDate: _DateModule.Builder | _DateModule.Reader
            endDate: _DateModule.Builder | _DateModule.Reader

        class HeaderResultTuple(NamedTuple):
            pass

        class DataResultTuple(NamedTuple):
            data: Sequence[Sequence[float]]

        class DatatResultTuple(NamedTuple):
            data: Sequence[Sequence[float]]

        class SubrangeResultTuple(NamedTuple):
            timeSeries: _TimeSeriesModule.Server

        class SubheaderResultTuple(NamedTuple):
            timeSeries: _TimeSeriesModule.Server

        class MetadataResultTuple(NamedTuple):
            entries: Sequence[EntryBuilder | EntryReader]
            info: _MetadataModule._InformationModule.Server

        class LocationResultTuple(NamedTuple):
            id: _IdInformationModule.Builder | _IdInformationModule.Reader
            heightNN: float
            latlon: _LatLonCoordModule.Builder | _LatLonCoordModule.Reader
            timeSeries: _TimeSeriesModule.Server
            customData: Sequence[KVBuilder | KVReader]

        class ResolutionParams(Protocol): ...

        class ResolutionCallContext(Protocol):
            params: _TimeSeriesModule.Server.ResolutionParams
            results: _TimeSeriesModule.Server.ResolutionResult

        class RangeParams(Protocol): ...

        class RangeCallContext(Protocol):
            params: _TimeSeriesModule.Server.RangeParams
            results: _TimeSeriesModule.Server.RangeResult

        class HeaderParams(Protocol): ...

        class HeaderCallContext(Protocol):
            params: _TimeSeriesModule.Server.HeaderParams
            results: _TimeSeriesModule.Server.HeaderResult

        class DataParams(Protocol): ...

        class DataCallContext(Protocol):
            params: _TimeSeriesModule.Server.DataParams
            results: _TimeSeriesModule.Server.DataResult

        class DatatParams(Protocol): ...

        class DatatCallContext(Protocol):
            params: _TimeSeriesModule.Server.DatatParams
            results: _TimeSeriesModule.Server.DatatResult

        class SubrangeParams(Protocol):
            start: _DateModule.Reader
            end: _DateModule.Reader

        class SubrangeCallContext(Protocol):
            params: _TimeSeriesModule.Server.SubrangeParams
            results: _TimeSeriesModule.Server.SubrangeResult

        class SubheaderParams(Protocol): ...

        class SubheaderCallContext(Protocol):
            params: _TimeSeriesModule.Server.SubheaderParams
            results: _TimeSeriesModule.Server.SubheaderResult

        class MetadataParams(Protocol): ...

        class MetadataCallContext(Protocol):
            params: _TimeSeriesModule.Server.MetadataParams
            results: _TimeSeriesModule.Server.MetadataResult

        class LocationParams(Protocol): ...

        class LocationCallContext(Protocol):
            params: _TimeSeriesModule.Server.LocationParams
            results: _TimeSeriesModule.Server.LocationResult

        def resolution(
            self,
            _context: _TimeSeriesModule.Server.ResolutionCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            TimeSeriesResolutionEnum
            | _TimeSeriesModule.Server.ResolutionResultTuple
            | None
        ]: ...
        def resolution_context(
            self, context: _TimeSeriesModule.Server.ResolutionCallContext
        ) -> Awaitable[None]: ...
        def range(
            self,
            _context: _TimeSeriesModule.Server.RangeCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_TimeSeriesModule.Server.RangeResultTuple | None]: ...
        def range_context(
            self, context: _TimeSeriesModule.Server.RangeCallContext
        ) -> Awaitable[None]: ...
        def header(
            self,
            _context: _TimeSeriesModule.Server.HeaderCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_TimeSeriesModule.Server.HeaderResultTuple | None]: ...
        def header_context(
            self, context: _TimeSeriesModule.Server.HeaderCallContext
        ) -> Awaitable[None]: ...
        def data(
            self,
            _context: _TimeSeriesModule.Server.DataCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_TimeSeriesModule.Server.DataResultTuple | None]: ...
        def data_context(
            self, context: _TimeSeriesModule.Server.DataCallContext
        ) -> Awaitable[None]: ...
        def dataT(
            self,
            _context: _TimeSeriesModule.Server.DatatCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_TimeSeriesModule.Server.DatatResultTuple | None]: ...
        def dataT_context(
            self, context: _TimeSeriesModule.Server.DatatCallContext
        ) -> Awaitable[None]: ...
        def subrange(
            self,
            start: _DateModule.Reader,
            end: _DateModule.Reader,
            _context: _TimeSeriesModule.Server.SubrangeCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _TimeSeriesModule.Server
            | _TimeSeriesModule.Server.SubrangeResultTuple
            | None
        ]: ...
        def subrange_context(
            self, context: _TimeSeriesModule.Server.SubrangeCallContext
        ) -> Awaitable[None]: ...
        def subheader(
            self,
            _context: _TimeSeriesModule.Server.SubheaderCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _TimeSeriesModule.Server
            | _TimeSeriesModule.Server.SubheaderResultTuple
            | None
        ]: ...
        def subheader_context(
            self, context: _TimeSeriesModule.Server.SubheaderCallContext
        ) -> Awaitable[None]: ...
        def metadata(
            self,
            _context: _TimeSeriesModule.Server.MetadataCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_TimeSeriesModule.Server.MetadataResultTuple | None]: ...
        def metadata_context(
            self, context: _TimeSeriesModule.Server.MetadataCallContext
        ) -> Awaitable[None]: ...
        def location(
            self,
            _context: _TimeSeriesModule.Server.LocationCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_TimeSeriesModule.Server.LocationResultTuple | None]: ...
        def location_context(
            self, context: _TimeSeriesModule.Server.LocationCallContext
        ) -> Awaitable[None]: ...

    class TimeSeriesClient(
        _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
    ):
        class ResolutionResult(Awaitable[ResolutionResult], Protocol):
            resolution: TimeSeriesResolutionEnum

        class RangeResult(Awaitable[RangeResult], Protocol):
            startDate: _DateModule.Reader
            endDate: _DateModule.Reader

        class HeaderResult(Awaitable[HeaderResult], Protocol):
            header: Any

        class DataResult(Awaitable[DataResult], Protocol):
            data: Sequence[Sequence[float]]

        class DatatResult(Awaitable[DatatResult], Protocol):
            data: Sequence[Sequence[float]]

        class SubrangeResult(Awaitable[SubrangeResult], Protocol):
            timeSeries: _TimeSeriesModule.TimeSeriesClient

        class SubheaderResult(Awaitable[SubheaderResult], Protocol):
            timeSeries: _TimeSeriesModule.TimeSeriesClient

        class MetadataResult(Awaitable[MetadataResult], Protocol):
            entries: Sequence[EntryReader]
            info: _MetadataModule._InformationModule.InformationClient

        class LocationResult(Awaitable[LocationResult], Protocol):
            id: _IdInformationModule.Reader
            heightNN: float
            latlon: _LatLonCoordModule.Reader
            timeSeries: _TimeSeriesModule.TimeSeriesClient
            customData: Sequence[KVReader]

        def resolution(self) -> _TimeSeriesModule.TimeSeriesClient.ResolutionResult: ...
        def range(self) -> _TimeSeriesModule.TimeSeriesClient.RangeResult: ...
        def header(self) -> _TimeSeriesModule.TimeSeriesClient.HeaderResult: ...
        def data(self) -> _TimeSeriesModule.TimeSeriesClient.DataResult: ...
        def dataT(self) -> _TimeSeriesModule.TimeSeriesClient.DatatResult: ...
        def subrange(
            self,
            start: _DateModule | dict[str, Any] | None = None,
            end: _DateModule | dict[str, Any] | None = None,
        ) -> _TimeSeriesModule.TimeSeriesClient.SubrangeResult: ...
        def subheader(self) -> _TimeSeriesModule.TimeSeriesClient.SubheaderResult: ...
        def metadata(self) -> _TimeSeriesModule.TimeSeriesClient.MetadataResult: ...
        def location(self) -> _TimeSeriesModule.TimeSeriesClient.LocationResult: ...
        def resolution_request(self) -> _TimeSeriesModule.ResolutionRequest: ...
        def range_request(self) -> _TimeSeriesModule.RangeRequest: ...
        def header_request(self) -> _TimeSeriesModule.HeaderRequest: ...
        def data_request(self) -> _TimeSeriesModule.DataRequest: ...
        def dataT_request(self) -> _TimeSeriesModule.DatatRequest: ...
        def subrange_request(
            self,
            start: _DateModule.Builder | None = None,
            end: _DateModule.Builder | None = None,
        ) -> _TimeSeriesModule.SubrangeRequest: ...
        def subheader_request(self) -> _TimeSeriesModule.SubheaderRequest: ...
        def metadata_request(self) -> _TimeSeriesModule.MetadataRequest: ...
        def location_request(self) -> _TimeSeriesModule.LocationRequest: ...

TimeSeries: _TimeSeriesModule

class _LocationModule(_StructModule):
    class _KVModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def key(self) -> str: ...
            @property
            def value(self) -> Any: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> KVBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def key(self) -> str: ...
            @key.setter
            def key(self, value: str) -> None: ...
            @property
            def value(self) -> Any: ...
            @value.setter
            def value(self, value: Any) -> None: ...
            @override
            def as_reader(self) -> KVReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            key: str | None = None,
            value: Any | None = None,
            **kwargs: Any,
        ) -> KVBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[KVReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[KVReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[KVBuilder]: ...
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
        ) -> KVReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> KVReader: ...

    type KVReader = _KVModule.Reader
    type KVBuilder = _KVModule.Builder
    KV: _KVModule
    class Reader(_DynamicStructReader):
        @property
        def id(self) -> _IdInformationModule.Reader: ...
        @property
        def heightNN(self) -> float: ...
        @property
        def latlon(self) -> _LatLonCoordModule.Reader: ...
        @property
        def timeSeries(self) -> _TimeSeriesModule.TimeSeriesClient: ...
        @property
        def customData(self) -> Sequence[KVReader]: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> LocationBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def id(self) -> _IdInformationModule.Builder: ...
        @id.setter
        def id(
            self,
            value: _IdInformationModule.Builder
            | _IdInformationModule.Reader
            | dict[str, Any],
        ) -> None: ...
        @property
        def heightNN(self) -> float: ...
        @heightNN.setter
        def heightNN(self, value: float) -> None: ...
        @property
        def latlon(self) -> _LatLonCoordModule.Builder: ...
        @latlon.setter
        def latlon(
            self,
            value: _LatLonCoordModule.Builder
            | _LatLonCoordModule.Reader
            | dict[str, Any],
        ) -> None: ...
        @property
        def timeSeries(self) -> _TimeSeriesModule.TimeSeriesClient: ...
        @timeSeries.setter
        def timeSeries(
            self, value: _TimeSeriesModule.TimeSeriesClient | _TimeSeriesModule.Server
        ) -> None: ...
        @property
        def customData(self) -> MutableSequence[KVBuilder]: ...
        @customData.setter
        def customData(
            self, value: Sequence[KVBuilder | KVReader] | Sequence[dict[str, Any]]
        ) -> None: ...
        @overload
        def init(
            self, field: Literal["id"], size: int | None = None
        ) -> _IdInformationModule.Builder: ...
        @overload
        def init(
            self, field: Literal["latlon"], size: int | None = None
        ) -> _LatLonCoordModule.Builder: ...
        @overload
        def init(
            self, field: Literal["customData"], size: int | None = None
        ) -> MutableSequence[KVBuilder]: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> LocationReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        id: _IdInformationModule.Builder | dict[str, Any] | None = None,
        heightNN: float | None = None,
        latlon: _LatLonCoordModule.Builder | dict[str, Any] | None = None,
        timeSeries: _TimeSeriesModule.TimeSeriesClient
        | _TimeSeriesModule.Server
        | None = None,
        customData: Sequence[KVBuilder] | Sequence[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> LocationBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[LocationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[LocationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[LocationBuilder]: ...
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
    ) -> LocationReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> LocationReader: ...

Location: _LocationModule
Dataset: _DatasetModule

class _MetaPlusDataModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def meta(self) -> MetadataReader: ...
        @property
        def data(self) -> _DatasetModule.DatasetClient: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> MetaPlusDataBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def meta(self) -> MetadataBuilder: ...
        @meta.setter
        def meta(
            self, value: MetadataBuilder | MetadataReader | dict[str, Any]
        ) -> None: ...
        @property
        def data(self) -> _DatasetModule.DatasetClient: ...
        @data.setter
        def data(
            self, value: _DatasetModule.DatasetClient | _DatasetModule.Server
        ) -> None: ...
        def init(
            self, field: Literal["meta"], size: int | None = None
        ) -> MetadataBuilder: ...
        @override
        def as_reader(self) -> MetaPlusDataReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        meta: MetadataBuilder | dict[str, Any] | None = None,
        data: _DatasetModule.DatasetClient | _DatasetModule.Server | None = None,
        **kwargs: Any,
    ) -> MetaPlusDataBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[MetaPlusDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[MetaPlusDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[MetaPlusDataBuilder]: ...
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
    ) -> MetaPlusDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> MetaPlusDataReader: ...

MetaPlusData: _MetaPlusDataModule

class _ElementModule:
    tmin: int
    tavg: int
    tmax: int
    precip: int
    globrad: int
    wind: int
    sunhours: int
    cloudamount: int
    relhumid: int
    airpress: int
    vaporpress: int
    co2: int
    o3: int
    et0: int
    dewpointTemp: int
    specificHumidity: int
    snowfallFlux: int
    surfaceDownwellingLongwaveRadiation: int
    potET: int

class _TimeSeriesDataModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def data(self) -> Sequence[Sequence[float]]: ...
        @property
        def isTransposed(self) -> bool: ...
        @property
        def header(self) -> Sequence[ElementEnum]: ...
        @property
        def startDate(self) -> _DateModule.Reader: ...
        @property
        def endDate(self) -> _DateModule.Reader: ...
        @property
        def resolution(self) -> TimeSeriesResolutionEnum: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> TimeSeriesDataBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def data(self) -> MutableSequence[MutableSequence[float]]: ...
        @data.setter
        def data(self, value: Sequence[Sequence[float]]) -> None: ...
        @property
        def isTransposed(self) -> bool: ...
        @isTransposed.setter
        def isTransposed(self, value: bool) -> None: ...
        @property
        def header(self) -> MutableSequence[ElementEnum]: ...
        @header.setter
        def header(self, value: Sequence[ElementEnum]) -> None: ...
        @property
        def startDate(self) -> _DateModule.Builder: ...
        @startDate.setter
        def startDate(
            self, value: _DateModule.Builder | _DateModule.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def endDate(self) -> _DateModule.Builder: ...
        @endDate.setter
        def endDate(
            self, value: _DateModule.Builder | _DateModule.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def resolution(self) -> TimeSeriesResolutionEnum: ...
        @resolution.setter
        def resolution(self, value: TimeSeriesResolutionEnum) -> None: ...
        @overload
        def init(
            self, field: Literal["startDate"], size: int | None = None
        ) -> _DateModule.Builder: ...
        @overload
        def init(
            self, field: Literal["endDate"], size: int | None = None
        ) -> _DateModule.Builder: ...
        @overload
        def init(
            self, field: Literal["data"], size: int | None = None
        ) -> MutableSequence[float]: ...
        @overload
        def init(
            self, field: Literal["header"], size: int | None = None
        ) -> MutableSequence[ElementEnum]: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> TimeSeriesDataReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        data: Sequence[Sequence[float]] | None = None,
        isTransposed: bool | None = None,
        header: Sequence[ElementEnum] | None = None,
        startDate: _DateModule.Builder | dict[str, Any] | None = None,
        endDate: _DateModule.Builder | dict[str, Any] | None = None,
        resolution: TimeSeriesResolutionEnum | None = None,
        **kwargs: Any,
    ) -> TimeSeriesDataBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[TimeSeriesDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[TimeSeriesDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[TimeSeriesDataBuilder]: ...
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
    ) -> TimeSeriesDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> TimeSeriesDataReader: ...

TimeSeriesData: _TimeSeriesDataModule

class _ServiceModule(_IdentifiableModule, _PersistentModule):
    class GetavailabledatasetsRequest(Protocol):
        def send(self) -> _ServiceModule.ServiceClient.GetavailabledatasetsResult: ...

    class GetdatasetsforRequest(Protocol):
        template: MetadataBuilder
        @overload
        def init(self, name: Literal["template"]) -> MetadataBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _ServiceModule.ServiceClient.GetdatasetsforResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _ServiceModule.ServiceClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class GetavailabledatasetsResult(
            Awaitable[GetavailabledatasetsResult], Protocol
        ):
            datasets: Sequence[MetaPlusDataBuilder | MetaPlusDataReader]

        class GetdatasetsforResult(Awaitable[GetdatasetsforResult], Protocol):
            datasets: Sequence[_DatasetModule]

        class GetavailabledatasetsResultTuple(NamedTuple):
            datasets: Sequence[MetaPlusDataBuilder | MetaPlusDataReader]

        class GetdatasetsforResultTuple(NamedTuple):
            datasets: Sequence[_DatasetModule]

        class GetavailabledatasetsParams(Protocol): ...

        class GetavailabledatasetsCallContext(Protocol):
            params: _ServiceModule.Server.GetavailabledatasetsParams
            results: _ServiceModule.Server.GetavailabledatasetsResult

        class GetdatasetsforParams(Protocol):
            template: MetadataReader

        class GetdatasetsforCallContext(Protocol):
            params: _ServiceModule.Server.GetdatasetsforParams
            results: _ServiceModule.Server.GetdatasetsforResult

        def getAvailableDatasets(
            self,
            _context: _ServiceModule.Server.GetavailabledatasetsCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _ServiceModule.Server.GetavailabledatasetsResultTuple | None
        ]: ...
        def getAvailableDatasets_context(
            self, context: _ServiceModule.Server.GetavailabledatasetsCallContext
        ) -> Awaitable[None]: ...
        def getDatasetsFor(
            self,
            template: MetadataReader,
            _context: _ServiceModule.Server.GetdatasetsforCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_ServiceModule.Server.GetdatasetsforResultTuple | None]: ...
        def getDatasetsFor_context(
            self, context: _ServiceModule.Server.GetdatasetsforCallContext
        ) -> Awaitable[None]: ...

    class ServiceClient(
        _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
    ):
        class GetavailabledatasetsResult(
            Awaitable[GetavailabledatasetsResult], Protocol
        ):
            datasets: Sequence[MetaPlusDataReader]

        class GetdatasetsforResult(Awaitable[GetdatasetsforResult], Protocol):
            datasets: Sequence[_DatasetModule]

        def getAvailableDatasets(
            self,
        ) -> _ServiceModule.ServiceClient.GetavailabledatasetsResult: ...
        def getDatasetsFor(
            self,
            template: MetadataBuilder | MetadataReader | dict[str, Any] | None = None,
        ) -> _ServiceModule.ServiceClient.GetdatasetsforResult: ...
        def getAvailableDatasets_request(
            self,
        ) -> _ServiceModule.GetavailabledatasetsRequest: ...
        def getDatasetsFor_request(
            self, template: MetadataBuilder | None = None
        ) -> _ServiceModule.GetdatasetsforRequest: ...

Service: _ServiceModule

class _CSVTimeSeriesFactoryModule(_IdentifiableModule):
    class _CSVConfigModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def sep(self) -> str: ...
            @property
            def headerMap(self) -> Sequence[_PairModule.Reader]: ...
            @property
            def skipLinesToHeader(self) -> int: ...
            @property
            def skipLinesFromHeaderToData(self) -> int: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> CSVConfigBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def sep(self) -> str: ...
            @sep.setter
            def sep(self, value: str) -> None: ...
            @property
            def headerMap(self) -> MutableSequence[_PairModule.Builder]: ...
            @headerMap.setter
            def headerMap(
                self,
                value: Sequence[_PairModule.Builder | _PairModule.Reader]
                | Sequence[dict[str, Any]],
            ) -> None: ...
            @property
            def skipLinesToHeader(self) -> int: ...
            @skipLinesToHeader.setter
            def skipLinesToHeader(self, value: int) -> None: ...
            @property
            def skipLinesFromHeaderToData(self) -> int: ...
            @skipLinesFromHeaderToData.setter
            def skipLinesFromHeaderToData(self, value: int) -> None: ...
            def init(
                self, field: Literal["headerMap"], size: int | None = None
            ) -> MutableSequence[_PairModule.Builder]: ...
            @override
            def as_reader(self) -> CSVConfigReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            sep: str | None = None,
            headerMap: Sequence[_PairModule.Builder]
            | Sequence[dict[str, Any]]
            | None = None,
            skipLinesToHeader: int | None = None,
            skipLinesFromHeaderToData: int | None = None,
            **kwargs: Any,
        ) -> CSVConfigBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[CSVConfigReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[CSVConfigReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[CSVConfigBuilder]: ...
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
        ) -> CSVConfigReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> CSVConfigReader: ...

    type CSVConfigReader = _CSVConfigModule.Reader
    type CSVConfigBuilder = _CSVConfigModule.Builder
    CSVConfig: _CSVConfigModule
    class CreateRequest(Protocol):
        csvData: str
        config: CSVConfigBuilder
        @overload
        def init(self, name: Literal["config"]) -> CSVConfigBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(
            self,
        ) -> _CSVTimeSeriesFactoryModule.CSVTimeSeriesFactoryClient.CreateResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _CSVTimeSeriesFactoryModule.CSVTimeSeriesFactoryClient: ...
    class Server(_IdentifiableModule.Server):
        class CreateResult(Awaitable[CreateResult], Protocol):
            timeseries: _TimeSeriesModule.TimeSeriesClient
            error: str

        class CreateResultTuple(NamedTuple):
            timeseries: _TimeSeriesModule.Server
            error: str

        class CreateParams(Protocol):
            csvData: str
            config: CSVConfigReader

        class CreateCallContext(Protocol):
            params: _CSVTimeSeriesFactoryModule.Server.CreateParams
            results: _CSVTimeSeriesFactoryModule.Server.CreateResult

        def create(
            self,
            csvData: str,
            config: CSVConfigReader,
            _context: _CSVTimeSeriesFactoryModule.Server.CreateCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_CSVTimeSeriesFactoryModule.Server.CreateResultTuple | None]: ...
        def create_context(
            self, context: _CSVTimeSeriesFactoryModule.Server.CreateCallContext
        ) -> Awaitable[None]: ...

    class CSVTimeSeriesFactoryClient(_IdentifiableModule.IdentifiableClient):
        class CreateResult(Awaitable[CreateResult], Protocol):
            timeseries: _TimeSeriesModule.TimeSeriesClient
            error: str

        def create(
            self,
            csvData: str | None = None,
            config: CSVConfigBuilder | CSVConfigReader | dict[str, Any] | None = None,
        ) -> _CSVTimeSeriesFactoryModule.CSVTimeSeriesFactoryClient.CreateResult: ...
        def create_request(
            self, csvData: str | None = None, config: CSVConfigBuilder | None = None
        ) -> _CSVTimeSeriesFactoryModule.CreateRequest: ...

CSVTimeSeriesFactory: _CSVTimeSeriesFactoryModule

class _AlterTimeSeriesWrapperModule(_TimeSeriesModule):
    class _AlterTypeModule:
        add: int
        mul: int

    AlterType: _AlterTypeModule
    class _AlteredModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def element(self) -> ElementEnum: ...
            @property
            def value(self) -> float: ...
            @property
            def type(self) -> AlterTimeSeriesWrapperAlterTypeEnum: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> AlteredBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def element(self) -> ElementEnum: ...
            @element.setter
            def element(self, value: ElementEnum) -> None: ...
            @property
            def value(self) -> float: ...
            @value.setter
            def value(self, value: float) -> None: ...
            @property
            def type(self) -> AlterTimeSeriesWrapperAlterTypeEnum: ...
            @type.setter
            def type(self, value: AlterTimeSeriesWrapperAlterTypeEnum) -> None: ...
            @override
            def as_reader(self) -> AlteredReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            element: ElementEnum | None = None,
            value: float | None = None,
            type: AlterTimeSeriesWrapperAlterTypeEnum | None = None,
            **kwargs: Any,
        ) -> AlteredBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[AlteredReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[AlteredReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[AlteredBuilder]: ...
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
        ) -> AlteredReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AlteredReader: ...

    type AlteredReader = _AlteredModule.Reader
    type AlteredBuilder = _AlteredModule.Builder
    Altered: _AlteredModule
    class WrappedtimeseriesRequest(Protocol):
        def send(
            self,
        ) -> _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.WrappedtimeseriesResult: ...

    class AlteredelementsRequest(Protocol):
        def send(
            self,
        ) -> _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.AlteredelementsResult: ...

    class AlterRequest(Protocol):
        desc: AlteredBuilder
        asNewTimeSeries: bool
        @overload
        def init(self, name: Literal["desc"]) -> AlteredBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(
            self,
        ) -> _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.AlterResult: ...

    class RemoveRequest(Protocol):
        alteredElement: ElementEnum
        def send(
            self,
        ) -> (
            _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.RemoveResult
        ): ...

    class ReplacewrappedtimeseriesRequest(Protocol):
        timeSeries: TimeSeriesClient | _TimeSeriesModule.Server
        def send(
            self,
        ) -> _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.ReplacewrappedtimeseriesResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient: ...
    class Server(_TimeSeriesModule.Server):
        class WrappedtimeseriesResult(Awaitable[WrappedtimeseriesResult], Protocol):
            timeSeries: _TimeSeriesModule.TimeSeriesClient

        class AlteredelementsResult(Awaitable[AlteredelementsResult], Protocol):
            list: Sequence[AlteredBuilder | AlteredReader]

        class AlterResult(Awaitable[AlterResult], Protocol):
            timeSeries: _TimeSeriesModule.TimeSeriesClient

        class RemoveResult(Awaitable[None], Protocol): ...
        class ReplacewrappedtimeseriesResult(Awaitable[None], Protocol): ...

        class WrappedtimeseriesResultTuple(NamedTuple):
            timeSeries: _TimeSeriesModule.Server

        class AlteredelementsResultTuple(NamedTuple):
            list: Sequence[AlteredBuilder | AlteredReader]

        class AlterResultTuple(NamedTuple):
            timeSeries: _TimeSeriesModule.Server

        class WrappedtimeseriesParams(Protocol): ...

        class WrappedtimeseriesCallContext(Protocol):
            params: _AlterTimeSeriesWrapperModule.Server.WrappedtimeseriesParams
            results: _AlterTimeSeriesWrapperModule.Server.WrappedtimeseriesResult

        class AlteredelementsParams(Protocol): ...

        class AlteredelementsCallContext(Protocol):
            params: _AlterTimeSeriesWrapperModule.Server.AlteredelementsParams
            results: _AlterTimeSeriesWrapperModule.Server.AlteredelementsResult

        class AlterParams(Protocol):
            desc: AlteredReader
            asNewTimeSeries: bool

        class AlterCallContext(Protocol):
            params: _AlterTimeSeriesWrapperModule.Server.AlterParams
            results: _AlterTimeSeriesWrapperModule.Server.AlterResult

        class RemoveParams(Protocol):
            alteredElement: ElementEnum

        class RemoveCallContext(Protocol):
            params: _AlterTimeSeriesWrapperModule.Server.RemoveParams

        class ReplacewrappedtimeseriesParams(Protocol):
            timeSeries: TimeSeriesClient

        class ReplacewrappedtimeseriesCallContext(Protocol):
            params: _AlterTimeSeriesWrapperModule.Server.ReplacewrappedtimeseriesParams

        def wrappedTimeSeries(
            self,
            _context: _AlterTimeSeriesWrapperModule.Server.WrappedtimeseriesCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _TimeSeriesModule.Server
            | _AlterTimeSeriesWrapperModule.Server.WrappedtimeseriesResultTuple
            | None
        ]: ...
        def wrappedTimeSeries_context(
            self,
            context: _AlterTimeSeriesWrapperModule.Server.WrappedtimeseriesCallContext,
        ) -> Awaitable[None]: ...
        def alteredElements(
            self,
            _context: _AlterTimeSeriesWrapperModule.Server.AlteredelementsCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _AlterTimeSeriesWrapperModule.Server.AlteredelementsResultTuple | None
        ]: ...
        def alteredElements_context(
            self,
            context: _AlterTimeSeriesWrapperModule.Server.AlteredelementsCallContext,
        ) -> Awaitable[None]: ...
        def alter(
            self,
            desc: AlteredReader,
            asNewTimeSeries: bool,
            _context: _AlterTimeSeriesWrapperModule.Server.AlterCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _TimeSeriesModule.Server
            | _AlterTimeSeriesWrapperModule.Server.AlterResultTuple
            | None
        ]: ...
        def alter_context(
            self, context: _AlterTimeSeriesWrapperModule.Server.AlterCallContext
        ) -> Awaitable[None]: ...
        def remove(
            self,
            alteredElement: ElementEnum,
            _context: _AlterTimeSeriesWrapperModule.Server.RemoveCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[None]: ...
        def remove_context(
            self, context: _AlterTimeSeriesWrapperModule.Server.RemoveCallContext
        ) -> Awaitable[None]: ...
        def replaceWrappedTimeSeries(
            self,
            timeSeries: TimeSeriesClient,
            _context: _AlterTimeSeriesWrapperModule.Server.ReplacewrappedtimeseriesCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[None]: ...
        def replaceWrappedTimeSeries_context(
            self,
            context: _AlterTimeSeriesWrapperModule.Server.ReplacewrappedtimeseriesCallContext,
        ) -> Awaitable[None]: ...

    class AlterTimeSeriesWrapperClient(_TimeSeriesModule.TimeSeriesClient):
        class WrappedtimeseriesResult(Awaitable[WrappedtimeseriesResult], Protocol):
            timeSeries: _TimeSeriesModule.TimeSeriesClient

        class AlteredelementsResult(Awaitable[AlteredelementsResult], Protocol):
            list: Sequence[AlteredReader]

        class AlterResult(Awaitable[AlterResult], Protocol):
            timeSeries: _TimeSeriesModule.TimeSeriesClient

        class RemoveResult(Awaitable[None], Protocol): ...
        class ReplacewrappedtimeseriesResult(Awaitable[None], Protocol): ...

        def wrappedTimeSeries(
            self,
        ) -> _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.WrappedtimeseriesResult: ...
        def alteredElements(
            self,
        ) -> _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.AlteredelementsResult: ...
        def alter(
            self,
            desc: AlteredBuilder | AlteredReader | dict[str, Any] | None = None,
            asNewTimeSeries: bool | None = None,
        ) -> _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.AlterResult: ...
        def remove(
            self, alteredElement: ElementEnum | None = None
        ) -> (
            _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.RemoveResult
        ): ...
        def replaceWrappedTimeSeries(
            self, timeSeries: TimeSeriesClient | _TimeSeriesModule.Server | None = None
        ) -> _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.ReplacewrappedtimeseriesResult: ...
        def wrappedTimeSeries_request(
            self,
        ) -> _AlterTimeSeriesWrapperModule.WrappedtimeseriesRequest: ...
        def alteredElements_request(
            self,
        ) -> _AlterTimeSeriesWrapperModule.AlteredelementsRequest: ...
        def alter_request(
            self,
            desc: AlteredBuilder | None = None,
            asNewTimeSeries: bool | None = None,
        ) -> _AlterTimeSeriesWrapperModule.AlterRequest: ...
        def remove_request(
            self, alteredElement: ElementEnum | None = None
        ) -> _AlterTimeSeriesWrapperModule.RemoveRequest: ...
        def replaceWrappedTimeSeries_request(
            self, timeSeries: TimeSeriesClient | _TimeSeriesModule.Server | None = None
        ) -> _AlterTimeSeriesWrapperModule.ReplacewrappedtimeseriesRequest: ...

AlterTimeSeriesWrapper: _AlterTimeSeriesWrapperModule

class _AlterTimeSeriesWrapperFactoryModule(_IdentifiableModule):
    class WrapRequest(Protocol):
        timeSeries: TimeSeriesClient | _TimeSeriesModule.Server
        def send(
            self,
        ) -> _AlterTimeSeriesWrapperFactoryModule.AlterTimeSeriesWrapperFactoryClient.WrapResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _AlterTimeSeriesWrapperFactoryModule.AlterTimeSeriesWrapperFactoryClient: ...
    class Server(_IdentifiableModule.Server):
        class WrapResult(Awaitable[WrapResult], Protocol):
            wrapper: _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient

        class WrapResultTuple(NamedTuple):
            wrapper: _AlterTimeSeriesWrapperModule.Server

        class WrapParams(Protocol):
            timeSeries: TimeSeriesClient

        class WrapCallContext(Protocol):
            params: _AlterTimeSeriesWrapperFactoryModule.Server.WrapParams
            results: _AlterTimeSeriesWrapperFactoryModule.Server.WrapResult

        def wrap(
            self,
            timeSeries: TimeSeriesClient,
            _context: _AlterTimeSeriesWrapperFactoryModule.Server.WrapCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _AlterTimeSeriesWrapperModule.Server
            | _AlterTimeSeriesWrapperFactoryModule.Server.WrapResultTuple
            | None
        ]: ...
        def wrap_context(
            self, context: _AlterTimeSeriesWrapperFactoryModule.Server.WrapCallContext
        ) -> Awaitable[None]: ...

    class AlterTimeSeriesWrapperFactoryClient(_IdentifiableModule.IdentifiableClient):
        class WrapResult(Awaitable[WrapResult], Protocol):
            wrapper: _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient

        def wrap(
            self, timeSeries: TimeSeriesClient | _TimeSeriesModule.Server | None = None
        ) -> _AlterTimeSeriesWrapperFactoryModule.AlterTimeSeriesWrapperFactoryClient.WrapResult: ...
        def wrap_request(
            self, timeSeries: TimeSeriesClient | _TimeSeriesModule.Server | None = None
        ) -> _AlterTimeSeriesWrapperFactoryModule.WrapRequest: ...

AlterTimeSeriesWrapperFactory: _AlterTimeSeriesWrapperFactoryModule

# Top-level type aliases for use in type annotations
type AlterResult = (
    _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.AlterResult
)
type AlterTimeSeriesWrapperAlterTypeEnum = int | Literal["add", "mul"]
type AlterTimeSeriesWrapperClient = (
    _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient
)
type AlterTimeSeriesWrapperFactoryClient = (
    _AlterTimeSeriesWrapperFactoryModule.AlterTimeSeriesWrapperFactoryClient
)
type AlteredBuilder = _AlterTimeSeriesWrapperModule._AlteredModule.Builder
type AlteredReader = _AlterTimeSeriesWrapperModule._AlteredModule.Reader
type AlteredelementsResult = (
    _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.AlteredelementsResult
)
type CSVConfigBuilder = _CSVTimeSeriesFactoryModule._CSVConfigModule.Builder
type CSVConfigReader = _CSVTimeSeriesFactoryModule._CSVConfigModule.Reader
type CSVTimeSeriesFactoryClient = _CSVTimeSeriesFactoryModule.CSVTimeSeriesFactoryClient
type CategoriesResult = (
    _MetadataModule._SupportedModule.SupportedClient.CategoriesResult
)
type ClosesttimeseriesatResult = _DatasetModule.DatasetClient.ClosesttimeseriesatResult
type CreateResult = _CSVTimeSeriesFactoryModule.CSVTimeSeriesFactoryClient.CreateResult
type DataResult = _TimeSeriesModule.TimeSeriesClient.DataResult
type DatasetClient = _DatasetModule.DatasetClient
type DatatResult = _TimeSeriesModule.TimeSeriesClient.DatatResult
type ElementEnum = (
    int
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
type EnsembleMemberBuilder = _EnsembleMemberModule.Builder
type EnsembleMemberReader = _EnsembleMemberModule.Reader
type EntryBuilder = _MetadataModule._EntryModule.Builder
type EntryReader = _MetadataModule._EntryModule.Reader
type ForallResult = _MetadataModule._InformationModule.InformationClient.ForallResult
type ForoneResult = _MetadataModule._InformationModule.InformationClient.ForoneResult
type GCMEnum = (
    int
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
)
type GetLocationsCallbackClient = (
    _DatasetModule._GetLocationsCallbackModule.GetLocationsCallbackClient
)
type GetavailabledatasetsResult = (
    _ServiceModule.ServiceClient.GetavailabledatasetsResult
)
type GetdatasetsforResult = _ServiceModule.ServiceClient.GetdatasetsforResult
type HeaderResult = _TimeSeriesModule.TimeSeriesClient.HeaderResult
type InformationClient = _MetadataModule._InformationModule.InformationClient
type KVBuilder = _LocationModule._KVModule.Builder
type KVReader = _LocationModule._KVModule.Reader
type LocationBuilder = _LocationModule.Builder
type LocationReader = _LocationModule.Reader
type LocationResult = _TimeSeriesModule.TimeSeriesClient.LocationResult
type LocationsResult = _DatasetModule.DatasetClient.LocationsResult
type MetaPlusDataBuilder = _MetaPlusDataModule.Builder
type MetaPlusDataReader = _MetaPlusDataModule.Reader
type MetadataBuilder = _MetadataModule.Builder
type MetadataReader = _MetadataModule.Reader
type MetadataResult = _DatasetModule.DatasetClient.MetadataResult
type NextlocationsResult = _DatasetModule._GetLocationsCallbackModule.GetLocationsCallbackClient.NextlocationsResult
type RCMEnum = (
    int
    | Literal[
        "clmcomCclm4817",
        "gericsRemo2015",
        "knmiRacmo22E",
        "smhiRca4",
        "clmcomBtuCclm4817",
        "mpiCscRemo2009",
        "uhohWrf361H",
    ]
)
type RCPEnum = (
    int | Literal["rcp19", "rcp26", "rcp34", "rcp45", "rcp60", "rcp70", "rcp85"]
)
type RangeResult = _TimeSeriesModule.TimeSeriesClient.RangeResult
type RemoveResult = (
    _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.RemoveResult
)
type ReplacewrappedtimeseriesResult = _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.ReplacewrappedtimeseriesResult
type ResolutionResult = _TimeSeriesModule.TimeSeriesClient.ResolutionResult
type SSPEnum = int | Literal["ssp1", "ssp2", "ssp3", "ssp4", "ssp5"]
type ServiceClient = _ServiceModule.ServiceClient
type StreamlocationsResult = _DatasetModule.DatasetClient.StreamlocationsResult
type SubheaderResult = _TimeSeriesModule.TimeSeriesClient.SubheaderResult
type SubrangeResult = _TimeSeriesModule.TimeSeriesClient.SubrangeResult
type SupportedClient = _MetadataModule._SupportedModule.SupportedClient
type SupportedvaluesResult = (
    _MetadataModule._SupportedModule.SupportedClient.SupportedvaluesResult
)
type TimeSeriesClient = _TimeSeriesModule.TimeSeriesClient
type TimeSeriesDataBuilder = _TimeSeriesDataModule.Builder
type TimeSeriesDataReader = _TimeSeriesDataModule.Reader
type TimeSeriesResolutionEnum = int | Literal["daily", "hourly"]
type TimeseriesatResult = _DatasetModule.DatasetClient.TimeseriesatResult
type ValueBuilder = _MetadataModule._ValueModule.Builder
type ValueReader = _MetadataModule._ValueModule.Reader
type WrapResult = (
    _AlterTimeSeriesWrapperFactoryModule.AlterTimeSeriesWrapperFactoryClient.WrapResult
)
type WrappedtimeseriesResult = (
    _AlterTimeSeriesWrapperModule.AlterTimeSeriesWrapperClient.WrappedtimeseriesResult
)
