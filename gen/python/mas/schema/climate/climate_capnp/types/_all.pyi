"""This is an automatically generated stub for `climate.capnp`."""

from collections.abc import Awaitable, Callable, Iterator, Sequence
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

from mas.schema.common.common_capnp.types.builders import (
    IdInformationBuilder,
    PairBuilder,
)
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader, PairReader
from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient
from mas.schema.persistence.persistence_capnp.types.modules import (
    _PersistentInterfaceModule,
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

class _GCMEnumModule:
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

class _RCMEnumModule:
    clmcomCclm4817: int
    gericsRemo2015: int
    knmiRacmo22E: int
    smhiRca4: int
    clmcomBtuCclm4817: int
    mpiCscRemo2009: int
    uhohWrf361H: int

class _SSPEnumModule:
    ssp1: int
    ssp2: int
    ssp3: int
    ssp4: int
    ssp5: int

class _RCPEnumModule:
    rcp19: int
    rcp26: int
    rcp34: int
    rcp45: int
    rcp60: int
    rcp70: int
    rcp85: int

class _EnsembleMemberStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        r: int | None = None,
        i: int | None = None,
        p: int | None = None,
        f: int | None = None,
        **kwargs: object,
    ) -> EnsembleMemberBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[EnsembleMemberReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[EnsembleMemberReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[EnsembleMemberBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> EnsembleMemberReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> EnsembleMemberReader: ...

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
    ) -> EnsembleMemberBuilder: ...

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
    def as_reader(self) -> EnsembleMemberReader: ...

EnsembleMember: _EnsembleMemberStructModule

class CategoriesRequest(Protocol):
    def send(self) -> CategoriesResult: ...

class _IdInformationList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdInformationReader: ...
        @override
        def __iter__(self) -> Iterator[IdInformationReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdInformationBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: IdInformationReader | IdInformationBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[IdInformationBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> IdInformationBuilder: ...

class CategoriesResult(Awaitable[CategoriesResult], Protocol):
    types: IdInformationListReader

class CategoriesServerResult(_DynamicStructBuilder):
    @property
    def types(self) -> IdInformationListBuilder: ...
    @types.setter
    def types(
        self,
        value: IdInformationListBuilder | IdInformationListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["types"],
        size: int | None = None,
    ) -> IdInformationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class CategoriesParams(Protocol): ...

class CategoriesCallContext(Protocol):
    params: CategoriesParams
    @property
    def results(self) -> CategoriesServerResult: ...

class CategoriesResultTuple(NamedTuple):
    types: IdInformationListBuilder | IdInformationListReader | Sequence[Any]

class SupportedvaluesRequest(Protocol):
    typeId: str
    def send(self) -> SupportedvaluesResult: ...

class SupportedvaluesResult(Awaitable[SupportedvaluesResult], Protocol):
    values: IdInformationListReader

class SupportedvaluesServerResult(_DynamicStructBuilder):
    @property
    def values(self) -> IdInformationListBuilder: ...
    @values.setter
    def values(
        self,
        value: IdInformationListBuilder | IdInformationListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["values"],
        size: int | None = None,
    ) -> IdInformationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class SupportedvaluesParams(Protocol):
    typeId: str

class SupportedvaluesCallContext(Protocol):
    params: SupportedvaluesParams
    @property
    def results(self) -> SupportedvaluesServerResult: ...

class SupportedvaluesResultTuple(NamedTuple):
    values: IdInformationListBuilder | IdInformationListReader | Sequence[Any]

class SupportedClient(_DynamicCapabilityClient):
    def categories(self) -> CategoriesResult: ...
    def supportedValues(self, typeId: str | None = None) -> SupportedvaluesResult: ...
    def categories_request(self) -> CategoriesRequest: ...
    def supportedValues_request(
        self,
        typeId: str | None = None,
    ) -> SupportedvaluesRequest: ...

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
    ) -> ValueBuilder: ...

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
    def as_reader(self) -> ValueReader: ...

class EntryReader(_DynamicStructReader):
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
    ) -> EntryBuilder: ...

class EntryBuilder(_DynamicStructBuilder):
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
    def as_reader(self) -> EntryReader: ...

class ForoneRequest(Protocol):
    entry: EntryBuilder
    @overload
    def init(self, name: Literal["entry"]) -> EntryBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> ForoneResult: ...

class ForoneResult(Awaitable[ForoneResult], Protocol):
    id: str
    name: str
    description: str

class ForoneParams(Protocol):
    entry: EntryReader

class ForoneCallContext(Protocol):
    params: ForoneParams
    @property
    def results(self) -> IdInformationBuilder: ...

class ForoneResultTuple(NamedTuple):
    id: str
    name: str
    description: str

class ForallRequest(Protocol):
    def send(self) -> ForallResult: ...

class _PairList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> PairReader: ...
        @override
        def __iter__(self) -> Iterator[PairReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> PairBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: PairReader | PairBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[PairBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> PairBuilder: ...

class ForallResult(Awaitable[ForallResult], Protocol):
    all: PairListReader

class ForallServerResult(_DynamicStructBuilder):
    @property
    def all(self) -> PairListBuilder: ...
    @all.setter
    def all(self, value: PairListBuilder | PairListReader | Sequence[Any]) -> None: ...
    @overload
    def init(
        self,
        field: Literal["all"],
        size: int | None = None,
    ) -> PairListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ForallParams(Protocol): ...

class ForallCallContext(Protocol):
    params: ForallParams
    @property
    def results(self) -> ForallServerResult: ...

class ForallResultTuple(NamedTuple):
    all: PairListBuilder | PairListReader | Sequence[Any]

class InformationClient(_DynamicCapabilityClient):
    def forOne(
        self,
        entry: EntryBuilder | EntryReader | dict[str, Any] | None = None,
    ) -> ForoneResult: ...
    def forAll(self) -> ForallResult: ...
    def forOne_request(self, entry: EntryBuilder | None = None) -> ForoneRequest: ...
    def forAll_request(self) -> ForallRequest: ...

class _EntryList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> EntryReader: ...
        @override
        def __iter__(self) -> Iterator[EntryReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> EntryBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: EntryReader | EntryBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[EntryBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> EntryBuilder: ...

class _MetadataStructModule(_StructModule):
    class _SupportedInterfaceModule(_InterfaceModule):
        @override
        def _new_client(self, server: _DynamicCapabilityServer) -> SupportedClient: ...
        class Server(_DynamicCapabilityServer):
            def categories(
                self,
                _context: CategoriesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                IdInformationListBuilder
                | IdInformationListReader
                | Sequence[Any]
                | CategoriesResultTuple
                | None
            ]: ...
            def categories_context(
                self,
                context: CategoriesCallContext,
            ) -> Awaitable[None]: ...
            def supportedValues(
                self,
                typeId: str,
                _context: SupportedvaluesCallContext,
                **kwargs: object,
            ) -> Awaitable[
                IdInformationListBuilder
                | IdInformationListReader
                | Sequence[Any]
                | SupportedvaluesResultTuple
                | None
            ]: ...
            def supportedValues_context(
                self,
                context: SupportedvaluesCallContext,
            ) -> Awaitable[None]: ...

    Supported: _SupportedInterfaceModule
    type SupportedServer = _MetadataStructModule._SupportedInterfaceModule.Server
    class _ValueStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            text: str | None = None,
            float: float | None = None,
            int: int | None = None,
            bool: bool | None = None,
            date: DateBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> ValueBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[ValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ValueReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ValueBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> ValueReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> ValueReader: ...

    Value: _ValueStructModule
    class _EntryStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            gcm: GCMEnum | None = None,
            rcm: RCMEnum | None = None,
            historical: None | None = None,
            rcp: RCPEnum | None = None,
            ssp: SSPEnum | None = None,
            ensMem: EnsembleMemberBuilder | dict[str, Any] | None = None,
            version: str | None = None,
            start: DateBuilder | dict[str, Any] | None = None,
            end: DateBuilder | dict[str, Any] | None = None,
            co2: float | None = None,
            picontrol: None | None = None,
            description: str | None = None,
            **kwargs: object,
        ) -> EntryBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[EntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[EntryBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> EntryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> EntryReader: ...

    Entry: _EntryStructModule
    class _InformationInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> InformationClient: ...
        class Server(_DynamicCapabilityServer):
            def forOne(
                self,
                entry: EntryReader,
                _context: ForoneCallContext,
                **kwargs: object,
            ) -> Awaitable[ForoneResultTuple | None]: ...
            def forOne_context(self, context: ForoneCallContext) -> Awaitable[None]: ...
            def forAll(
                self,
                _context: ForallCallContext,
                **kwargs: object,
            ) -> Awaitable[
                PairListBuilder
                | PairListReader
                | Sequence[Any]
                | ForallResultTuple
                | None
            ]: ...
            def forAll_context(self, context: ForallCallContext) -> Awaitable[None]: ...

    Information: _InformationInterfaceModule
    type InformationServer = _MetadataStructModule._InformationInterfaceModule.Server
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        entries: EntryListBuilder | dict[str, Any] | None = None,
        info: InformationClient
        | _MetadataStructModule._InformationInterfaceModule.Server
        | None = None,
        **kwargs: object,
    ) -> MetadataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[MetadataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[MetadataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[MetadataBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> MetadataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> MetadataReader: ...

class MetadataReader(_DynamicStructReader):
    @property
    def entries(self) -> EntryListReader: ...
    @property
    def info(self) -> InformationClient: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> MetadataBuilder: ...

class MetadataBuilder(_DynamicStructBuilder):
    @property
    def entries(self) -> EntryListBuilder: ...
    @entries.setter
    def entries(
        self,
        value: EntryListBuilder | EntryListReader | dict[str, Any],
    ) -> None: ...
    @property
    def info(self) -> InformationClient: ...
    @info.setter
    def info(
        self,
        value: InformationClient
        | _MetadataStructModule._InformationInterfaceModule.Server,
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["entries"],
        size: int | None = None,
    ) -> EntryListBuilder: ...
    @override
    def as_reader(self) -> MetadataReader: ...

Metadata: _MetadataStructModule

class _DatasetInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _GetLocationsCallbackInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> GetLocationsCallbackClient: ...
        class Server(_DynamicCapabilityServer):
            def nextLocations(
                self,
                maxCount: int,
                _context: NextlocationsCallContext,
                **kwargs: object,
            ) -> Awaitable[
                LocationListBuilder
                | LocationListReader
                | Sequence[Any]
                | NextlocationsResultTuple
                | None
            ]: ...
            def nextLocations_context(
                self,
                context: NextlocationsCallContext,
            ) -> Awaitable[None]: ...

    GetLocationsCallback: _GetLocationsCallbackInterfaceModule
    type GetLocationsCallbackServer = (
        _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
    )
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> DatasetClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def metadata(
            self,
            _context: DatasetMetadataCallContext,
            **kwargs: object,
        ) -> Awaitable[DatasetMetadataResultTuple | None]: ...
        def metadata_context(
            self,
            context: DatasetMetadataCallContext,
        ) -> Awaitable[None]: ...
        def closestTimeSeriesAt(
            self,
            latlon: LatLonCoordReader,
            _context: ClosesttimeseriesatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | TimeSeriesClient
            | ClosesttimeseriesatResultTuple
            | None
        ]: ...
        def closestTimeSeriesAt_context(
            self,
            context: ClosesttimeseriesatCallContext,
        ) -> Awaitable[None]: ...
        def timeSeriesAt(
            self,
            locationId: str,
            _context: TimeseriesatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | TimeSeriesClient
            | TimeseriesatResultTuple
            | None
        ]: ...
        def timeSeriesAt_context(
            self,
            context: TimeseriesatCallContext,
        ) -> Awaitable[None]: ...
        def locations(
            self,
            _context: LocationsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            LocationListBuilder
            | LocationListReader
            | Sequence[Any]
            | LocationsResultTuple
            | None
        ]: ...
        def locations_context(
            self,
            context: LocationsCallContext,
        ) -> Awaitable[None]: ...
        def streamLocations(
            self,
            startAfterLocationId: str,
            _context: StreamlocationsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
            | GetLocationsCallbackClient
            | StreamlocationsResultTuple
            | None
        ]: ...
        def streamLocations_context(
            self,
            context: StreamlocationsCallContext,
        ) -> Awaitable[None]: ...

class NextlocationsRequest(Protocol):
    maxCount: int
    def send(self) -> NextlocationsResult: ...

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
    ) -> KVBuilder: ...

class KVBuilder(_DynamicStructBuilder):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str) -> None: ...
    @property
    def value(self) -> _DynamicObjectBuilder: ...
    @value.setter
    def value(self, value: AnyPointer) -> None: ...
    @override
    def as_reader(self) -> KVReader: ...

class _TimeSeriesInterfaceModule(
    _IdentifiableInterfaceModule,
    _PersistentInterfaceModule,
):
    class _ResolutionEnumModule:
        daily: int
        hourly: int

    Resolution: _ResolutionEnumModule
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> TimeSeriesClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def resolution(
            self,
            _context: ResolutionCallContext,
            **kwargs: object,
        ) -> Awaitable[TimeSeriesResolutionEnum | ResolutionResultTuple | None]: ...
        def resolution_context(
            self,
            context: ResolutionCallContext,
        ) -> Awaitable[None]: ...
        def range(
            self,
            _context: RangeCallContext,
            **kwargs: object,
        ) -> Awaitable[RangeResultTuple | None]: ...
        def range_context(self, context: RangeCallContext) -> Awaitable[None]: ...
        def header(
            self,
            _context: HeaderCallContext,
            **kwargs: object,
        ) -> Awaitable[
            ElementEnumListBuilder
            | ElementEnumListReader
            | Sequence[Any]
            | HeaderResultTuple
            | None
        ]: ...
        def header_context(self, context: HeaderCallContext) -> Awaitable[None]: ...
        def data(
            self,
            _context: DataCallContext,
            **kwargs: object,
        ) -> Awaitable[
            Float32ListListBuilder
            | Float32ListListReader
            | Sequence[Any]
            | DataResultTuple
            | None
        ]: ...
        def data_context(self, context: DataCallContext) -> Awaitable[None]: ...
        def dataT(
            self,
            _context: DatatCallContext,
            **kwargs: object,
        ) -> Awaitable[
            Float32ListListBuilder
            | Float32ListListReader
            | Sequence[Any]
            | DatatResultTuple
            | None
        ]: ...
        def dataT_context(self, context: DatatCallContext) -> Awaitable[None]: ...
        def subrange(
            self,
            start: DateReader,
            end: DateReader,
            _context: SubrangeCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | TimeSeriesClient
            | SubrangeResultTuple
            | None
        ]: ...
        def subrange_context(self, context: SubrangeCallContext) -> Awaitable[None]: ...
        def subheader(
            self,
            elements: ElementEnumListReader,
            _context: SubheaderCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | TimeSeriesClient
            | SubheaderResultTuple
            | None
        ]: ...
        def subheader_context(
            self,
            context: SubheaderCallContext,
        ) -> Awaitable[None]: ...
        def metadata(
            self,
            _context: TimeSeriesMetadataCallContext,
            **kwargs: object,
        ) -> Awaitable[TimeSeriesMetadataResultTuple | None]: ...
        def metadata_context(
            self,
            context: TimeSeriesMetadataCallContext,
        ) -> Awaitable[None]: ...
        def location(
            self,
            _context: LocationCallContext,
            **kwargs: object,
        ) -> Awaitable[LocationResultTuple | None]: ...
        def location_context(self, context: LocationCallContext) -> Awaitable[None]: ...

class ResolutionRequest(Protocol):
    def send(self) -> ResolutionResult: ...

class ResolutionResult(Awaitable[ResolutionResult], Protocol):
    resolution: TimeSeriesResolutionEnum

class ResolutionServerResult(_DynamicStructBuilder):
    @property
    def resolution(self) -> TimeSeriesResolutionEnum: ...
    @resolution.setter
    def resolution(self, value: TimeSeriesResolutionEnum) -> None: ...

class ResolutionParams(Protocol): ...

class ResolutionCallContext(Protocol):
    params: ResolutionParams
    @property
    def results(self) -> ResolutionServerResult: ...

class ResolutionResultTuple(NamedTuple):
    resolution: TimeSeriesResolutionEnum

class RangeRequest(Protocol):
    def send(self) -> RangeResult: ...

class RangeResult(Awaitable[RangeResult], Protocol):
    startDate: DateReader
    endDate: DateReader

class RangeServerResult(_DynamicStructBuilder):
    @property
    def startDate(self) -> DateBuilder: ...
    @startDate.setter
    def startDate(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
    @property
    def endDate(self) -> DateBuilder: ...
    @endDate.setter
    def endDate(self, value: DateBuilder | DateReader | dict[str, Any]) -> None: ...
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
    def init(self, field: str, size: int | None = None) -> Any: ...

class RangeParams(Protocol): ...

class RangeCallContext(Protocol):
    params: RangeParams
    @property
    def results(self) -> RangeServerResult: ...

class RangeResultTuple(NamedTuple):
    startDate: DateBuilder | DateReader | dict[str, Any]
    endDate: DateBuilder | DateReader | dict[str, Any]

class HeaderRequest(Protocol):
    def send(self) -> HeaderResult: ...

class _ElementEnumModule:
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

class _ElementEnumList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> ElementEnum: ...
        @override
        def __iter__(self) -> Iterator[ElementEnum]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> ElementEnum: ...
        @override
        def __setitem__(self, key: int, value: ElementEnum) -> None: ...
        @override
        def __iter__(self) -> Iterator[ElementEnum]: ...

class HeaderResult(Awaitable[HeaderResult], Protocol):
    header: ElementEnumListReader

class HeaderServerResult(_DynamicStructBuilder):
    @property
    def header(self) -> ElementEnumListBuilder: ...
    @header.setter
    def header(
        self,
        value: ElementEnumListBuilder | ElementEnumListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["header"],
        size: int | None = None,
    ) -> ElementEnumListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class HeaderParams(Protocol): ...

class HeaderCallContext(Protocol):
    params: HeaderParams
    @property
    def results(self) -> HeaderServerResult: ...

class HeaderResultTuple(NamedTuple):
    header: ElementEnumListBuilder | ElementEnumListReader | Sequence[Any]

class DataRequest(Protocol):
    def send(self) -> DataResult: ...

class _Float32List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> float: ...
        @override
        def __iter__(self) -> Iterator[float]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> float: ...
        @override
        def __setitem__(self, key: int, value: float) -> None: ...
        @override
        def __iter__(self) -> Iterator[float]: ...

class _Float32ListList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> Float32ListReader: ...
        @override
        def __iter__(self) -> Iterator[Float32ListReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> Float32ListBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: Float32ListReader | Float32ListBuilder | Sequence[Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[Float32ListBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> Float32ListBuilder: ...

class DataResult(Awaitable[DataResult], Protocol):
    data: Float32ListListReader

class DataServerResult(_DynamicStructBuilder):
    @property
    def data(self) -> Float32ListListBuilder: ...
    @data.setter
    def data(
        self,
        value: Float32ListListBuilder | Float32ListListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["data"],
        size: int | None = None,
    ) -> Float32ListListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class DataParams(Protocol): ...

class DataCallContext(Protocol):
    params: DataParams
    @property
    def results(self) -> DataServerResult: ...

class DataResultTuple(NamedTuple):
    data: Float32ListListBuilder | Float32ListListReader | Sequence[Any]

class DatatRequest(Protocol):
    def send(self) -> DatatResult: ...

class DatatResult(Awaitable[DatatResult], Protocol):
    data: Float32ListListReader

class DatatServerResult(_DynamicStructBuilder):
    @property
    def data(self) -> Float32ListListBuilder: ...
    @data.setter
    def data(
        self,
        value: Float32ListListBuilder | Float32ListListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["data"],
        size: int | None = None,
    ) -> Float32ListListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class DatatParams(Protocol): ...

class DatatCallContext(Protocol):
    params: DatatParams
    @property
    def results(self) -> DatatServerResult: ...

class DatatResultTuple(NamedTuple):
    data: Float32ListListBuilder | Float32ListListReader | Sequence[Any]

class SubrangeRequest(Protocol):
    start: DateBuilder
    end: DateBuilder
    @overload
    def init(self, name: Literal["start"]) -> DateBuilder: ...
    @overload
    def init(self, name: Literal["end"]) -> DateBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> SubrangeResult: ...

class SubrangeResult(Awaitable[SubrangeResult], Protocol):
    timeSeries: TimeSeriesClient

class SubrangeServerResult(_DynamicStructBuilder):
    @property
    def timeSeries(self) -> _TimeSeriesInterfaceModule.Server | TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: _TimeSeriesInterfaceModule.Server | TimeSeriesClient,
    ) -> None: ...

class SubrangeParams(Protocol):
    start: DateReader
    end: DateReader

class SubrangeCallContext(Protocol):
    params: SubrangeParams
    @property
    def results(self) -> SubrangeServerResult: ...

class SubrangeResultTuple(NamedTuple):
    timeSeries: _TimeSeriesInterfaceModule.Server | TimeSeriesClient

class SubheaderRequest(Protocol):
    elements: ElementEnumListBuilder | ElementEnumListReader | Sequence[Any]
    @overload
    def init(
        self,
        name: Literal["elements"],
        size: int = ...,
    ) -> ElementEnumListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> SubheaderResult: ...

class SubheaderResult(Awaitable[SubheaderResult], Protocol):
    timeSeries: TimeSeriesClient

class SubheaderServerResult(_DynamicStructBuilder):
    @property
    def timeSeries(self) -> _TimeSeriesInterfaceModule.Server | TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: _TimeSeriesInterfaceModule.Server | TimeSeriesClient,
    ) -> None: ...

class SubheaderParams(Protocol):
    elements: ElementEnumListReader

class SubheaderCallContext(Protocol):
    params: SubheaderParams
    @property
    def results(self) -> SubheaderServerResult: ...

class SubheaderResultTuple(NamedTuple):
    timeSeries: _TimeSeriesInterfaceModule.Server | TimeSeriesClient

class TimeSeriesMetadataRequest(Protocol):
    def send(self) -> TimeSeriesMetadataResult: ...

class TimeSeriesMetadataResult(Awaitable[TimeSeriesMetadataResult], Protocol):
    entries: EntryListReader
    info: InformationClient

class TimeSeriesMetadataParams(Protocol): ...

class TimeSeriesMetadataCallContext(Protocol):
    params: TimeSeriesMetadataParams
    @property
    def results(self) -> MetadataBuilder: ...

class TimeSeriesMetadataResultTuple(NamedTuple):
    entries: EntryListBuilder | EntryListReader | Sequence[Any]
    info: _MetadataStructModule._InformationInterfaceModule.Server | InformationClient

class LocationRequest(Protocol):
    def send(self) -> LocationResult: ...

class _KVList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> KVReader: ...
        @override
        def __iter__(self) -> Iterator[KVReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> KVBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: KVReader | KVBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[KVBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> KVBuilder: ...

class LocationResult(Awaitable[LocationResult], Protocol):
    id: IdInformationReader
    heightNN: float
    latlon: LatLonCoordReader
    timeSeries: TimeSeriesClient
    customData: KVListReader

class LocationParams(Protocol): ...

class LocationCallContext(Protocol):
    params: LocationParams
    @property
    def results(self) -> LocationBuilder: ...

class LocationResultTuple(NamedTuple):
    id: IdInformationBuilder | IdInformationReader | dict[str, Any]
    heightNN: float
    latlon: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any]
    timeSeries: _TimeSeriesInterfaceModule.Server | TimeSeriesClient
    customData: KVListBuilder | KVListReader | Sequence[Any]

class TimeSeriesClient(IdentifiableClient, PersistentClient):
    def resolution(self) -> ResolutionResult: ...
    def range(self) -> RangeResult: ...
    def header(self) -> HeaderResult: ...
    def data(self) -> DataResult: ...
    def dataT(self) -> DatatResult: ...
    def subrange(
        self,
        start: DateBuilder | DateReader | dict[str, Any] | None = None,
        end: DateBuilder | DateReader | dict[str, Any] | None = None,
    ) -> SubrangeResult: ...
    def subheader(
        self,
        elements: ElementEnumListBuilder
        | ElementEnumListReader
        | Sequence[Any]
        | None = None,
    ) -> SubheaderResult: ...
    def metadata(self) -> TimeSeriesMetadataResult: ...
    def location(self) -> LocationResult: ...
    def resolution_request(self) -> ResolutionRequest: ...
    def range_request(self) -> RangeRequest: ...
    def header_request(self) -> HeaderRequest: ...
    def data_request(self) -> DataRequest: ...
    def dataT_request(self) -> DatatRequest: ...
    def subrange_request(
        self,
        start: DateBuilder | None = None,
        end: DateBuilder | None = None,
    ) -> SubrangeRequest: ...
    def subheader_request(
        self,
        elements: ElementEnumListBuilder
        | ElementEnumListReader
        | Sequence[Any]
        | None = None,
    ) -> SubheaderRequest: ...
    def metadata_request(self) -> TimeSeriesMetadataRequest: ...
    def location_request(self) -> LocationRequest: ...

TimeSeries: _TimeSeriesInterfaceModule

class _LocationStructModule(_StructModule):
    class _KVStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            key: str | None = None,
            value: AnyPointer | None = None,
            **kwargs: object,
        ) -> KVBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[KVReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[KVReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[KVBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> KVReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> KVReader: ...

    KV: _KVStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        id: IdInformationBuilder | dict[str, Any] | None = None,
        heightNN: float | None = None,
        latlon: LatLonCoordBuilder | dict[str, Any] | None = None,
        timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server | None = None,
        customData: KVListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> LocationBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[LocationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[LocationReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[LocationBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> LocationReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> LocationReader: ...

class LocationReader(_DynamicStructReader):
    @property
    def id(self) -> IdInformationReader: ...
    @property
    def heightNN(self) -> float: ...
    @property
    def latlon(self) -> LatLonCoordReader: ...
    @property
    def timeSeries(self) -> TimeSeriesClient: ...
    @property
    def customData(self) -> KVListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> LocationBuilder: ...

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
    def timeSeries(self) -> TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: TimeSeriesClient | _TimeSeriesInterfaceModule.Server,
    ) -> None: ...
    @property
    def customData(self) -> KVListBuilder: ...
    @customData.setter
    def customData(
        self,
        value: KVListBuilder | KVListReader | dict[str, Any],
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
    def as_reader(self) -> LocationReader: ...

Location: _LocationStructModule

class _LocationList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> LocationReader: ...
        @override
        def __iter__(self) -> Iterator[LocationReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> LocationBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: LocationReader | LocationBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[LocationBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> LocationBuilder: ...

class NextlocationsResult(Awaitable[NextlocationsResult], Protocol):
    locations: LocationListReader

class NextlocationsServerResult(_DynamicStructBuilder):
    @property
    def locations(self) -> LocationListBuilder: ...
    @locations.setter
    def locations(
        self,
        value: LocationListBuilder | LocationListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["locations"],
        size: int | None = None,
    ) -> LocationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class NextlocationsParams(Protocol):
    maxCount: int

class NextlocationsCallContext(Protocol):
    params: NextlocationsParams
    @property
    def results(self) -> NextlocationsServerResult: ...

class NextlocationsResultTuple(NamedTuple):
    locations: LocationListBuilder | LocationListReader | Sequence[Any]

class GetLocationsCallbackClient(_DynamicCapabilityClient):
    def nextLocations(self, maxCount: int | None = None) -> NextlocationsResult: ...
    def nextLocations_request(
        self,
        maxCount: int | None = None,
    ) -> NextlocationsRequest: ...

class DatasetMetadataRequest(Protocol):
    def send(self) -> DatasetMetadataResult: ...

class DatasetMetadataResult(Awaitable[DatasetMetadataResult], Protocol):
    entries: EntryListReader
    info: InformationClient

class DatasetMetadataParams(Protocol): ...

class DatasetMetadataCallContext(Protocol):
    params: DatasetMetadataParams
    @property
    def results(self) -> MetadataBuilder: ...

class DatasetMetadataResultTuple(NamedTuple):
    entries: EntryListBuilder | EntryListReader | Sequence[Any]
    info: _MetadataStructModule._InformationInterfaceModule.Server | InformationClient

class ClosesttimeseriesatRequest(Protocol):
    latlon: LatLonCoordBuilder
    @overload
    def init(self, name: Literal["latlon"]) -> LatLonCoordBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> ClosesttimeseriesatResult: ...

class ClosesttimeseriesatResult(Awaitable[ClosesttimeseriesatResult], Protocol):
    timeSeries: TimeSeriesClient

class ClosesttimeseriesatServerResult(_DynamicStructBuilder):
    @property
    def timeSeries(self) -> _TimeSeriesInterfaceModule.Server | TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: _TimeSeriesInterfaceModule.Server | TimeSeriesClient,
    ) -> None: ...

class ClosesttimeseriesatParams(Protocol):
    latlon: LatLonCoordReader

class ClosesttimeseriesatCallContext(Protocol):
    params: ClosesttimeseriesatParams
    @property
    def results(self) -> ClosesttimeseriesatServerResult: ...

class ClosesttimeseriesatResultTuple(NamedTuple):
    timeSeries: _TimeSeriesInterfaceModule.Server | TimeSeriesClient

class TimeseriesatRequest(Protocol):
    locationId: str
    def send(self) -> TimeseriesatResult: ...

class TimeseriesatResult(Awaitable[TimeseriesatResult], Protocol):
    timeSeries: TimeSeriesClient

class TimeseriesatServerResult(_DynamicStructBuilder):
    @property
    def timeSeries(self) -> _TimeSeriesInterfaceModule.Server | TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: _TimeSeriesInterfaceModule.Server | TimeSeriesClient,
    ) -> None: ...

class TimeseriesatParams(Protocol):
    locationId: str

class TimeseriesatCallContext(Protocol):
    params: TimeseriesatParams
    @property
    def results(self) -> TimeseriesatServerResult: ...

class TimeseriesatResultTuple(NamedTuple):
    timeSeries: _TimeSeriesInterfaceModule.Server | TimeSeriesClient

class LocationsRequest(Protocol):
    def send(self) -> LocationsResult: ...

class LocationsResult(Awaitable[LocationsResult], Protocol):
    locations: LocationListReader

class LocationsServerResult(_DynamicStructBuilder):
    @property
    def locations(self) -> LocationListBuilder: ...
    @locations.setter
    def locations(
        self,
        value: LocationListBuilder | LocationListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["locations"],
        size: int | None = None,
    ) -> LocationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class LocationsParams(Protocol): ...

class LocationsCallContext(Protocol):
    params: LocationsParams
    @property
    def results(self) -> LocationsServerResult: ...

class LocationsResultTuple(NamedTuple):
    locations: LocationListBuilder | LocationListReader | Sequence[Any]

class StreamlocationsRequest(Protocol):
    startAfterLocationId: str
    def send(self) -> StreamlocationsResult: ...

class StreamlocationsResult(Awaitable[StreamlocationsResult], Protocol):
    locationsCallback: GetLocationsCallbackClient

class StreamlocationsServerResult(_DynamicStructBuilder):
    @property
    def locationsCallback(
        self,
    ) -> (
        _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
        | GetLocationsCallbackClient
    ): ...
    @locationsCallback.setter
    def locationsCallback(
        self,
        value: _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
        | GetLocationsCallbackClient,
    ) -> None: ...

class StreamlocationsParams(Protocol):
    startAfterLocationId: str

class StreamlocationsCallContext(Protocol):
    params: StreamlocationsParams
    @property
    def results(self) -> StreamlocationsServerResult: ...

class StreamlocationsResultTuple(NamedTuple):
    locationsCallback: (
        _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
        | GetLocationsCallbackClient
    )

class DatasetClient(IdentifiableClient, PersistentClient):
    def metadata(self) -> DatasetMetadataResult: ...
    def closestTimeSeriesAt(
        self,
        latlon: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any] | None = None,
    ) -> ClosesttimeseriesatResult: ...
    def timeSeriesAt(self, locationId: str | None = None) -> TimeseriesatResult: ...
    def locations(self) -> LocationsResult: ...
    def streamLocations(
        self,
        startAfterLocationId: str | None = None,
    ) -> StreamlocationsResult: ...
    def metadata_request(self) -> DatasetMetadataRequest: ...
    def closestTimeSeriesAt_request(
        self,
        latlon: LatLonCoordBuilder | None = None,
    ) -> ClosesttimeseriesatRequest: ...
    def timeSeriesAt_request(
        self,
        locationId: str | None = None,
    ) -> TimeseriesatRequest: ...
    def locations_request(self) -> LocationsRequest: ...
    def streamLocations_request(
        self,
        startAfterLocationId: str | None = None,
    ) -> StreamlocationsRequest: ...

Dataset: _DatasetInterfaceModule

class _MetaPlusDataStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        meta: MetadataBuilder | dict[str, Any] | None = None,
        data: DatasetClient | _DatasetInterfaceModule.Server | None = None,
        **kwargs: object,
    ) -> MetaPlusDataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[MetaPlusDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[MetaPlusDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[MetaPlusDataBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> MetaPlusDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> MetaPlusDataReader: ...

class MetaPlusDataReader(_DynamicStructReader):
    @property
    def meta(self) -> MetadataReader: ...
    @property
    def data(self) -> DatasetClient: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> MetaPlusDataBuilder: ...

class MetaPlusDataBuilder(_DynamicStructBuilder):
    @property
    def meta(self) -> MetadataBuilder: ...
    @meta.setter
    def meta(
        self,
        value: MetadataBuilder | MetadataReader | dict[str, Any],
    ) -> None: ...
    @property
    def data(self) -> DatasetClient: ...
    @data.setter
    def data(self, value: DatasetClient | _DatasetInterfaceModule.Server) -> None: ...
    @override
    def init(
        self,
        field: Literal["meta"],
        size: int | None = None,
    ) -> MetadataBuilder: ...
    @override
    def as_reader(self) -> MetaPlusDataReader: ...

MetaPlusData: _MetaPlusDataStructModule

class _TimeSeriesDataStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        data: Float32ListListBuilder | dict[str, Any] | None = None,
        isTransposed: bool | None = None,
        header: ElementEnumListBuilder | dict[str, Any] | None = None,
        startDate: DateBuilder | dict[str, Any] | None = None,
        endDate: DateBuilder | dict[str, Any] | None = None,
        resolution: TimeSeriesResolutionEnum | None = None,
        **kwargs: object,
    ) -> TimeSeriesDataBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[TimeSeriesDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[TimeSeriesDataReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[TimeSeriesDataBuilder]: ...
    @override
    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader: ...
    @override
    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> TimeSeriesDataReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> TimeSeriesDataReader: ...

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
    def resolution(self) -> TimeSeriesResolutionEnum: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> TimeSeriesDataBuilder: ...

class TimeSeriesDataBuilder(_DynamicStructBuilder):
    @property
    def data(self) -> Float32ListListBuilder: ...
    @data.setter
    def data(
        self,
        value: Float32ListListBuilder | Float32ListListReader | dict[str, Any],
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
        value: ElementEnumListBuilder | ElementEnumListReader | dict[str, Any],
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
    def resolution(self) -> TimeSeriesResolutionEnum: ...
    @resolution.setter
    def resolution(self, value: TimeSeriesResolutionEnum) -> None: ...
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
    def as_reader(self) -> TimeSeriesDataReader: ...

TimeSeriesData: _TimeSeriesDataStructModule

class _ServiceInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> ServiceClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def getAvailableDatasets(
            self,
            _context: GetavailabledatasetsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            MetaPlusDataListBuilder
            | MetaPlusDataListReader
            | Sequence[Any]
            | GetavailabledatasetsResultTuple
            | None
        ]: ...
        def getAvailableDatasets_context(
            self,
            context: GetavailabledatasetsCallContext,
        ) -> Awaitable[None]: ...
        def getDatasetsFor(
            self,
            template: MetadataReader,
            _context: GetdatasetsforCallContext,
            **kwargs: object,
        ) -> Awaitable[
            DatasetClientListBuilder
            | DatasetClientListReader
            | Sequence[Any]
            | GetdatasetsforResultTuple
            | None
        ]: ...
        def getDatasetsFor_context(
            self,
            context: GetdatasetsforCallContext,
        ) -> Awaitable[None]: ...

class GetavailabledatasetsRequest(Protocol):
    def send(self) -> GetavailabledatasetsResult: ...

class _MetaPlusDataList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> MetaPlusDataReader: ...
        @override
        def __iter__(self) -> Iterator[MetaPlusDataReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> MetaPlusDataBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: MetaPlusDataReader | MetaPlusDataBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[MetaPlusDataBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> MetaPlusDataBuilder: ...

class GetavailabledatasetsResult(Awaitable[GetavailabledatasetsResult], Protocol):
    datasets: MetaPlusDataListReader

class GetavailabledatasetsServerResult(_DynamicStructBuilder):
    @property
    def datasets(self) -> MetaPlusDataListBuilder: ...
    @datasets.setter
    def datasets(
        self,
        value: MetaPlusDataListBuilder | MetaPlusDataListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["datasets"],
        size: int | None = None,
    ) -> MetaPlusDataListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class GetavailabledatasetsParams(Protocol): ...

class GetavailabledatasetsCallContext(Protocol):
    params: GetavailabledatasetsParams
    @property
    def results(self) -> GetavailabledatasetsServerResult: ...

class GetavailabledatasetsResultTuple(NamedTuple):
    datasets: MetaPlusDataListBuilder | MetaPlusDataListReader | Sequence[Any]

class GetdatasetsforRequest(Protocol):
    template: MetadataBuilder
    @overload
    def init(self, name: Literal["template"]) -> MetadataBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> GetdatasetsforResult: ...

class _DatasetClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> DatasetClient: ...
        @override
        def __iter__(self) -> Iterator[DatasetClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> DatasetClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: DatasetClient | _DatasetInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[DatasetClient]: ...

class GetdatasetsforResult(Awaitable[GetdatasetsforResult], Protocol):
    datasets: DatasetClientListReader

class GetdatasetsforServerResult(_DynamicStructBuilder):
    @property
    def datasets(self) -> DatasetClientListBuilder: ...
    @datasets.setter
    def datasets(
        self,
        value: DatasetClientListBuilder | DatasetClientListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["datasets"],
        size: int | None = None,
    ) -> DatasetClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class GetdatasetsforParams(Protocol):
    template: MetadataReader

class GetdatasetsforCallContext(Protocol):
    params: GetdatasetsforParams
    @property
    def results(self) -> GetdatasetsforServerResult: ...

class GetdatasetsforResultTuple(NamedTuple):
    datasets: DatasetClientListBuilder | DatasetClientListReader | Sequence[Any]

class ServiceClient(IdentifiableClient, PersistentClient):
    def getAvailableDatasets(self) -> GetavailabledatasetsResult: ...
    def getDatasetsFor(
        self,
        template: MetadataBuilder | MetadataReader | dict[str, Any] | None = None,
    ) -> GetdatasetsforResult: ...
    def getAvailableDatasets_request(self) -> GetavailabledatasetsRequest: ...
    def getDatasetsFor_request(
        self,
        template: MetadataBuilder | None = None,
    ) -> GetdatasetsforRequest: ...

Service: _ServiceInterfaceModule

class _CSVTimeSeriesFactoryInterfaceModule(_IdentifiableInterfaceModule):
    class _CSVConfigStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            sep: str | None = None,
            headerMap: PairListBuilder | dict[str, Any] | None = None,
            skipLinesToHeader: int | None = None,
            skipLinesFromHeaderToData: int | None = None,
            **kwargs: object,
        ) -> CSVConfigBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[CSVConfigReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[CSVConfigReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[CSVConfigBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> CSVConfigReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> CSVConfigReader: ...

    CSVConfig: _CSVConfigStructModule
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> CSVTimeSeriesFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def create(
            self,
            csvData: str,
            config: CSVConfigReader,
            _context: CreateCallContext,
            **kwargs: object,
        ) -> Awaitable[CreateResultTuple | None]: ...
        def create_context(self, context: CreateCallContext) -> Awaitable[None]: ...

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
    ) -> CSVConfigBuilder: ...

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
        value: PairListBuilder | PairListReader | dict[str, Any],
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
    def as_reader(self) -> CSVConfigReader: ...

class CreateRequest(Protocol):
    csvData: str
    config: CSVConfigBuilder
    @overload
    def init(self, name: Literal["config"]) -> CSVConfigBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> CreateResult: ...

class CreateResult(Awaitable[CreateResult], Protocol):
    timeseries: TimeSeriesClient
    error: str

class CreateServerResult(_DynamicStructBuilder):
    @property
    def timeseries(self) -> _TimeSeriesInterfaceModule.Server | TimeSeriesClient: ...
    @timeseries.setter
    def timeseries(
        self,
        value: _TimeSeriesInterfaceModule.Server | TimeSeriesClient,
    ) -> None: ...
    @property
    def error(self) -> str: ...
    @error.setter
    def error(self, value: str) -> None: ...

class CreateParams(Protocol):
    csvData: str
    config: CSVConfigReader

class CreateCallContext(Protocol):
    params: CreateParams
    @property
    def results(self) -> CreateServerResult: ...

class CreateResultTuple(NamedTuple):
    timeseries: _TimeSeriesInterfaceModule.Server | TimeSeriesClient
    error: str

class CSVTimeSeriesFactoryClient(IdentifiableClient):
    def create(
        self,
        csvData: str | None = None,
        config: CSVConfigBuilder | CSVConfigReader | dict[str, Any] | None = None,
    ) -> CreateResult: ...
    def create_request(
        self,
        csvData: str | None = None,
        config: CSVConfigBuilder | None = None,
    ) -> CreateRequest: ...

CSVTimeSeriesFactory: _CSVTimeSeriesFactoryInterfaceModule

class _AlterTimeSeriesWrapperInterfaceModule(_TimeSeriesInterfaceModule):
    class _AlterTypeEnumModule:
        add: int
        mul: int

    AlterType: _AlterTypeEnumModule
    class _AlteredStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            element: ElementEnum | None = None,
            value: float | None = None,
            type: AlterTimeSeriesWrapperAlterTypeEnum | None = None,
            **kwargs: object,
        ) -> AlteredBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[AlteredReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[AlteredReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[AlteredBuilder]: ...
        @override
        def from_bytes_packed(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _DynamicStructReader: ...
        @override
        def read(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AlteredReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AlteredReader: ...

    Altered: _AlteredStructModule
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> AlterTimeSeriesWrapperClient: ...
    class Server(_TimeSeriesInterfaceModule.Server):
        def wrappedTimeSeries(
            self,
            _context: WrappedtimeseriesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | TimeSeriesClient
            | WrappedtimeseriesResultTuple
            | None
        ]: ...
        def wrappedTimeSeries_context(
            self,
            context: WrappedtimeseriesCallContext,
        ) -> Awaitable[None]: ...
        def alteredElements(
            self,
            _context: AlteredelementsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            AlteredListBuilder
            | AlteredListReader
            | Sequence[Any]
            | AlteredelementsResultTuple
            | None
        ]: ...
        def alteredElements_context(
            self,
            context: AlteredelementsCallContext,
        ) -> Awaitable[None]: ...
        def alter(
            self,
            desc: AlteredReader,
            asNewTimeSeries: bool,
            _context: AlterCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _TimeSeriesInterfaceModule.Server
            | TimeSeriesClient
            | AlterResultTuple
            | None
        ]: ...
        def alter_context(self, context: AlterCallContext) -> Awaitable[None]: ...
        def remove(
            self,
            alteredElement: ElementEnum,
            _context: RemoveCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def remove_context(self, context: RemoveCallContext) -> Awaitable[None]: ...
        def replaceWrappedTimeSeries(
            self,
            timeSeries: TimeSeriesClient,
            _context: ReplacewrappedtimeseriesCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def replaceWrappedTimeSeries_context(
            self,
            context: ReplacewrappedtimeseriesCallContext,
        ) -> Awaitable[None]: ...

class AlteredReader(_DynamicStructReader):
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
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> AlteredBuilder: ...

class AlteredBuilder(_DynamicStructBuilder):
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

class WrappedtimeseriesRequest(Protocol):
    def send(self) -> WrappedtimeseriesResult: ...

class WrappedtimeseriesResult(Awaitable[WrappedtimeseriesResult], Protocol):
    timeSeries: TimeSeriesClient

class WrappedtimeseriesServerResult(_DynamicStructBuilder):
    @property
    def timeSeries(self) -> _TimeSeriesInterfaceModule.Server | TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: _TimeSeriesInterfaceModule.Server | TimeSeriesClient,
    ) -> None: ...

class WrappedtimeseriesParams(Protocol): ...

class WrappedtimeseriesCallContext(Protocol):
    params: WrappedtimeseriesParams
    @property
    def results(self) -> WrappedtimeseriesServerResult: ...

class WrappedtimeseriesResultTuple(NamedTuple):
    timeSeries: _TimeSeriesInterfaceModule.Server | TimeSeriesClient

class AlteredelementsRequest(Protocol):
    def send(self) -> AlteredelementsResult: ...

class _AlteredList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> AlteredReader: ...
        @override
        def __iter__(self) -> Iterator[AlteredReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> AlteredBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: AlteredReader | AlteredBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[AlteredBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> AlteredBuilder: ...

class AlteredelementsResult(Awaitable[AlteredelementsResult], Protocol):
    list: AlteredListReader

class AlteredelementsServerResult(_DynamicStructBuilder):
    @property
    def list(self) -> AlteredListBuilder: ...
    @list.setter
    def list(
        self,
        value: AlteredListBuilder | AlteredListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["list"],
        size: int | None = None,
    ) -> AlteredListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class AlteredelementsParams(Protocol): ...

class AlteredelementsCallContext(Protocol):
    params: AlteredelementsParams
    @property
    def results(self) -> AlteredelementsServerResult: ...

class AlteredelementsResultTuple(NamedTuple):
    list: AlteredListBuilder | AlteredListReader | Sequence[Any]

class AlterRequest(Protocol):
    desc: AlteredBuilder
    asNewTimeSeries: bool
    @overload
    def init(self, name: Literal["desc"]) -> AlteredBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> AlterResult: ...

class AlterResult(Awaitable[AlterResult], Protocol):
    timeSeries: TimeSeriesClient

class AlterServerResult(_DynamicStructBuilder):
    @property
    def timeSeries(self) -> _TimeSeriesInterfaceModule.Server | TimeSeriesClient: ...
    @timeSeries.setter
    def timeSeries(
        self,
        value: _TimeSeriesInterfaceModule.Server | TimeSeriesClient,
    ) -> None: ...

class AlterParams(Protocol):
    desc: AlteredReader
    asNewTimeSeries: bool

class AlterCallContext(Protocol):
    params: AlterParams
    @property
    def results(self) -> AlterServerResult: ...

class AlterResultTuple(NamedTuple):
    timeSeries: _TimeSeriesInterfaceModule.Server | TimeSeriesClient

class RemoveRequest(Protocol):
    alteredElement: ElementEnum
    def send(self) -> RemoveResult: ...

class RemoveResult(Awaitable[None], Protocol): ...

class RemoveParams(Protocol):
    alteredElement: ElementEnum

class RemoveCallContext(Protocol):
    params: RemoveParams

class ReplacewrappedtimeseriesRequest(Protocol):
    timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server
    def send(self) -> ReplacewrappedtimeseriesResult: ...

class ReplacewrappedtimeseriesResult(Awaitable[None], Protocol): ...

class ReplacewrappedtimeseriesParams(Protocol):
    timeSeries: TimeSeriesClient

class ReplacewrappedtimeseriesCallContext(Protocol):
    params: ReplacewrappedtimeseriesParams

class AlterTimeSeriesWrapperClient(TimeSeriesClient):
    def wrappedTimeSeries(self) -> WrappedtimeseriesResult: ...
    def alteredElements(self) -> AlteredelementsResult: ...
    def alter(
        self,
        desc: AlteredBuilder | AlteredReader | dict[str, Any] | None = None,
        asNewTimeSeries: bool | None = None,
    ) -> AlterResult: ...
    def remove(self, alteredElement: ElementEnum | None = None) -> RemoveResult: ...
    def replaceWrappedTimeSeries(
        self,
        timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server | None = None,
    ) -> ReplacewrappedtimeseriesResult: ...
    def wrappedTimeSeries_request(self) -> WrappedtimeseriesRequest: ...
    def alteredElements_request(self) -> AlteredelementsRequest: ...
    def alter_request(
        self,
        desc: AlteredBuilder | None = None,
        asNewTimeSeries: bool | None = None,
    ) -> AlterRequest: ...
    def remove_request(
        self,
        alteredElement: ElementEnum | None = None,
    ) -> RemoveRequest: ...
    def replaceWrappedTimeSeries_request(
        self,
        timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server | None = None,
    ) -> ReplacewrappedtimeseriesRequest: ...

AlterTimeSeriesWrapper: _AlterTimeSeriesWrapperInterfaceModule

class _AlterTimeSeriesWrapperFactoryInterfaceModule(_IdentifiableInterfaceModule):
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> AlterTimeSeriesWrapperFactoryClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def wrap(
            self,
            timeSeries: TimeSeriesClient,
            _context: WrapCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _AlterTimeSeriesWrapperInterfaceModule.Server
            | AlterTimeSeriesWrapperClient
            | WrapResultTuple
            | None
        ]: ...
        def wrap_context(self, context: WrapCallContext) -> Awaitable[None]: ...

class WrapRequest(Protocol):
    timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server
    def send(self) -> WrapResult: ...

class WrapResult(Awaitable[WrapResult], Protocol):
    wrapper: AlterTimeSeriesWrapperClient

class WrapServerResult(_DynamicStructBuilder):
    @property
    def wrapper(
        self,
    ) -> (
        _AlterTimeSeriesWrapperInterfaceModule.Server | AlterTimeSeriesWrapperClient
    ): ...
    @wrapper.setter
    def wrapper(
        self,
        value: _AlterTimeSeriesWrapperInterfaceModule.Server
        | AlterTimeSeriesWrapperClient,
    ) -> None: ...

class WrapParams(Protocol):
    timeSeries: TimeSeriesClient

class WrapCallContext(Protocol):
    params: WrapParams
    @property
    def results(self) -> WrapServerResult: ...

class WrapResultTuple(NamedTuple):
    wrapper: (
        _AlterTimeSeriesWrapperInterfaceModule.Server | AlterTimeSeriesWrapperClient
    )

class AlterTimeSeriesWrapperFactoryClient(IdentifiableClient):
    def wrap(
        self,
        timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server | None = None,
    ) -> WrapResult: ...
    def wrap_request(
        self,
        timeSeries: TimeSeriesClient | _TimeSeriesInterfaceModule.Server | None = None,
    ) -> WrapRequest: ...

AlterTimeSeriesWrapperFactory: _AlterTimeSeriesWrapperFactoryInterfaceModule

# Top-level type aliases for use in type annotations
type AlterTimeSeriesWrapperAlterTypeEnum = int | Literal["add", "mul"]
AlterTimeSeriesWrapperFactoryServer = (
    _AlterTimeSeriesWrapperFactoryInterfaceModule.Server
)
AlterTimeSeriesWrapperServer = _AlterTimeSeriesWrapperInterfaceModule.Server
type AlteredListBuilder = _AlteredList.Builder
type AlteredListReader = _AlteredList.Reader
CSVTimeSeriesFactoryServer = _CSVTimeSeriesFactoryInterfaceModule.Server
type DatasetClientListBuilder = _DatasetClientList.Builder
type DatasetClientListReader = _DatasetClientList.Reader
DatasetServer = _DatasetInterfaceModule.Server
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
type ElementEnumListBuilder = _ElementEnumList.Builder
type ElementEnumListReader = _ElementEnumList.Reader
type EntryListBuilder = _EntryList.Builder
type EntryListReader = _EntryList.Reader
type Float32ListBuilder = _Float32List.Builder
type Float32ListListBuilder = _Float32ListList.Builder
type Float32ListListReader = _Float32ListList.Reader
type Float32ListReader = _Float32List.Reader
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
GetLocationsCallbackServer = (
    _DatasetInterfaceModule._GetLocationsCallbackInterfaceModule.Server
)
type IdInformationListBuilder = _IdInformationList.Builder
type IdInformationListReader = _IdInformationList.Reader
InformationServer = _MetadataStructModule._InformationInterfaceModule.Server
type KVListBuilder = _KVList.Builder
type KVListReader = _KVList.Reader
type LocationListBuilder = _LocationList.Builder
type LocationListReader = _LocationList.Reader
type MetaPlusDataListBuilder = _MetaPlusDataList.Builder
type MetaPlusDataListReader = _MetaPlusDataList.Reader
type PairListBuilder = _PairList.Builder
type PairListReader = _PairList.Reader
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
type SSPEnum = int | Literal["ssp1", "ssp2", "ssp3", "ssp4", "ssp5"]
ServiceServer = _ServiceInterfaceModule.Server
SupportedServer = _MetadataStructModule._SupportedInterfaceModule.Server
type TimeSeriesResolutionEnum = int | Literal["daily", "hourly"]
TimeSeriesServer = _TimeSeriesInterfaceModule.Server
