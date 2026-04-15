"""This is an automatically generated stub for `fbp.capnp`."""

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
    StructuredTextBuilder,
    ValueBuilder,
)
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import (
    IdInformationReader,
    StructuredTextReader,
    ValueReader,
)
from mas.schema.persistence.persistence_capnp.types.builders import SturdyRefBuilder
from mas.schema.persistence.persistence_capnp.types.clients import (
    GatewayRegistrableClient,
    PersistentClient,
)
from mas.schema.persistence.persistence_capnp.types.modules import (
    _GatewayRegistrableInterfaceModule,
    _PersistentInterfaceModule,
)
from mas.schema.persistence.persistence_capnp.types.readers import SturdyRefReader
from mas.schema.service.service_capnp.types.clients import StoppableClient
from mas.schema.service.service_capnp.types.modules import _StoppableInterfaceModule

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

class KVReader(_DynamicStructReader):
    @property
    def key(self) -> str: ...
    @property
    def desc(self) -> str: ...
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
    def desc(self) -> str: ...
    @desc.setter
    def desc(self, value: str) -> None: ...
    @property
    def value(self) -> _DynamicObjectBuilder: ...
    @value.setter
    def value(self, value: AnyPointer) -> None: ...
    @override
    def as_reader(self) -> KVReader: ...

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

class _IPStructModule(_StructModule):
    class _KVStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            key: str | None = None,
            desc: str | None = None,
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
    class _TypeEnumModule:
        standard: int
        openBracket: int
        closeBracket: int

    Type: _TypeEnumModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        attributes: KVListBuilder | dict[str, Any] | None = None,
        content: AnyPointer | None = None,
        type: IPTypeEnum | None = None,
        **kwargs: object,
    ) -> IPBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[IPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[IPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[IPBuilder]: ...
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
    ) -> IPReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> IPReader: ...

class IPReader(_DynamicStructReader):
    @property
    def attributes(self) -> KVListReader: ...
    @property
    def content(self) -> _DynamicObjectReader: ...
    @property
    def type(self) -> IPTypeEnum: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> IPBuilder: ...

class IPBuilder(_DynamicStructBuilder):
    @property
    def attributes(self) -> KVListBuilder: ...
    @attributes.setter
    def attributes(
        self,
        value: KVListBuilder | KVListReader | dict[str, Any],
    ) -> None: ...
    @property
    def content(self) -> _DynamicObjectBuilder: ...
    @content.setter
    def content(self, value: AnyPointer) -> None: ...
    @property
    def type(self) -> IPTypeEnum: ...
    @type.setter
    def type(self, value: IPTypeEnum) -> None: ...
    @override
    def init(
        self,
        field: Literal["attributes"],
        size: int | None = None,
    ) -> KVListBuilder: ...
    @override
    def as_reader(self) -> IPReader: ...

IP: _IPStructModule

class _IIPStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        content: AnyPointer | None = None,
        **kwargs: object,
    ) -> IIPBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[IIPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[IIPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[IIPBuilder]: ...
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
    ) -> IIPReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> IIPReader: ...

class IIPReader(_DynamicStructReader):
    @property
    def content(self) -> _DynamicObjectReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> IIPBuilder: ...

class IIPBuilder(_DynamicStructBuilder):
    @property
    def content(self) -> _DynamicObjectBuilder: ...
    @content.setter
    def content(self, value: AnyPointer) -> None: ...
    @override
    def as_reader(self) -> IIPReader: ...

IIP: _IIPStructModule

class _ChannelInterfaceModule(_IdentifiableInterfaceModule, _PersistentInterfaceModule):
    class _CloseSemanticsEnumModule:
        fbp: int
        no: int

    CloseSemantics: _CloseSemanticsEnumModule
    class _MsgStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            value: AnyPointer | None = None,
            done: None | None = None,
            noMsg: None | None = None,
            **kwargs: object,
        ) -> MsgBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[MsgReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[MsgReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[MsgBuilder]: ...
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
        ) -> MsgReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> MsgReader: ...

    Msg: _MsgStructModule
    class _ReaderInterfaceModule(
        _IdentifiableInterfaceModule,
        _PersistentInterfaceModule,
    ):
        @override
        def _new_client(self, server: _DynamicCapabilityServer) -> ReaderClient: ...
        class Server(
            _IdentifiableInterfaceModule.Server,
            _PersistentInterfaceModule.Server,
        ):
            def read(
                self,
                _context: ReadCallContext,
                **kwargs: object,
            ) -> Awaitable[ReadResultTuple | None]: ...
            def read_context(self, context: ReadCallContext) -> Awaitable[None]: ...
            def close(
                self,
                _context: ReaderCloseCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def close_context(
                self,
                context: ReaderCloseCallContext,
            ) -> Awaitable[None]: ...
            def readIfMsg(
                self,
                _context: ReadifmsgCallContext,
                **kwargs: object,
            ) -> Awaitable[ReadifmsgResultTuple | None]: ...
            def readIfMsg_context(
                self,
                context: ReadifmsgCallContext,
            ) -> Awaitable[None]: ...

    Reader: _ReaderInterfaceModule
    type ReaderServer = _ChannelInterfaceModule._ReaderInterfaceModule.Server
    class _WriterInterfaceModule(
        _IdentifiableInterfaceModule,
        _PersistentInterfaceModule,
    ):
        @override
        def _new_client(self, server: _DynamicCapabilityServer) -> WriterClient: ...
        class Server(
            _IdentifiableInterfaceModule.Server,
            _PersistentInterfaceModule.Server,
        ):
            def write_context(self, context: WriteCallContext) -> Awaitable[None]: ...
            def close(
                self,
                _context: WriterCloseCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def close_context(
                self,
                context: WriterCloseCallContext,
            ) -> Awaitable[None]: ...
            def writeIfSpace_context(
                self,
                context: WriteifspaceCallContext,
            ) -> Awaitable[None]: ...

    Writer: _WriterInterfaceModule
    type WriterServer = _ChannelInterfaceModule._WriterInterfaceModule.Server
    class _StartupInfoStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            bufferSize: int | None = None,
            closeSemantics: ChannelCloseSemanticsEnum | None = None,
            channelSR: SturdyRefBuilder | dict[str, Any] | None = None,
            readerSRs: SturdyRefListBuilder | dict[str, Any] | None = None,
            writerSRs: SturdyRefListBuilder | dict[str, Any] | None = None,
            channel: ChannelClient | _ChannelInterfaceModule.Server | None = None,
            readers: ReaderClientListBuilder | dict[str, Any] | None = None,
            writers: WriterClientListBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> StartupInfoBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[StartupInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[StartupInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[StartupInfoBuilder]: ...
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
        ) -> StartupInfoReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> StartupInfoReader: ...

    StartupInfo: _StartupInfoStructModule
    class _StatsCallbackInterfaceModule(_InterfaceModule):
        class _StatsStructModule(_StructModule):
            class Reader(_DynamicStructReader): ...
            class Builder(_DynamicStructBuilder): ...

            @override
            def new_message(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Callable[[int], bytearray] | None = None,
                noOfWaitingWriters: int | None = None,
                noOfWaitingReaders: int | None = None,
                noOfIpsInQueue: int | None = None,
                totalNoOfIpsReceived: int | None = None,
                timestamp: str | None = None,
                updateIntervalInMs: int | None = None,
                **kwargs: object,
            ) -> StatsBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[StatsReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[StatsReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[StatsBuilder]: ...
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
            ) -> StatsReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> StatsReader: ...

        Stats: _StatsStructModule
        class _UnregisterInterfaceModule(_InterfaceModule):
            @override
            def _new_client(
                self,
                server: _DynamicCapabilityServer,
            ) -> UnregisterClient: ...
            class Server(_DynamicCapabilityServer):
                def unreg(
                    self,
                    _context: UnregCallContext,
                    **kwargs: object,
                ) -> Awaitable[bool | UnregResultTuple | None]: ...
                def unreg_context(
                    self,
                    context: UnregCallContext,
                ) -> Awaitable[None]: ...

        Unregister: _UnregisterInterfaceModule
        type UnregisterServer = _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> StatsCallbackClient: ...
        class Server(_DynamicCapabilityServer):
            def status(
                self,
                stats: StatsReader,
                _context: StatusCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def status_context(self, context: StatusCallContext) -> Awaitable[None]: ...

    StatsCallback: _StatsCallbackInterfaceModule
    type StatsCallbackServer = (
        _ChannelInterfaceModule._StatsCallbackInterfaceModule.Server
    )
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> ChannelClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def setBufferSize(
            self,
            size: int,
            _context: SetbuffersizeCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def setBufferSize_context(
            self,
            context: SetbuffersizeCallContext,
        ) -> Awaitable[None]: ...
        def reader(
            self,
            _context: ReaderCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _ChannelInterfaceModule._ReaderInterfaceModule.Server
            | ReaderClient
            | ReaderResultTuple
            | None
        ]: ...
        def reader_context(self, context: ReaderCallContext) -> Awaitable[None]: ...
        def writer(
            self,
            _context: WriterCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _ChannelInterfaceModule._WriterInterfaceModule.Server
            | WriterClient
            | WriterResultTuple
            | None
        ]: ...
        def writer_context(self, context: WriterCallContext) -> Awaitable[None]: ...
        def endpoints(
            self,
            _context: EndpointsCallContext,
            **kwargs: object,
        ) -> Awaitable[EndpointsResultTuple | None]: ...
        def endpoints_context(
            self,
            context: EndpointsCallContext,
        ) -> Awaitable[None]: ...
        def setAutoCloseSemantics(
            self,
            cs: ChannelCloseSemanticsEnum,
            _context: SetautoclosesemanticsCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def setAutoCloseSemantics_context(
            self,
            context: SetautoclosesemanticsCallContext,
        ) -> Awaitable[None]: ...
        def close(
            self,
            waitForEmptyBuffer: bool,
            _context: ChannelCloseCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def close_context(
            self,
            context: ChannelCloseCallContext,
        ) -> Awaitable[None]: ...
        def registerStatsCallback(
            self,
            callback: StatsCallbackClient,
            updateIntervalInMs: int,
            _context: RegisterstatscallbackCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server
            | UnregisterClient
            | RegisterstatscallbackResultTuple
            | None
        ]: ...
        def registerStatsCallback_context(
            self,
            context: RegisterstatscallbackCallContext,
        ) -> Awaitable[None]: ...

class MsgReader(_DynamicStructReader):
    @property
    def value(self) -> _DynamicObjectReader: ...
    @property
    def done(self) -> None: ...
    @property
    def noMsg(self) -> None: ...
    @override
    def which(self) -> Literal["value", "done", "noMsg"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> MsgBuilder: ...

class MsgBuilder(_DynamicStructBuilder):
    @property
    def value(self) -> _DynamicObjectReader: ...
    @value.setter
    def value(self, value: AnyPointer) -> None: ...
    @property
    def done(self) -> None: ...
    @done.setter
    def done(self, value: None) -> None: ...
    @property
    def noMsg(self) -> None: ...
    @noMsg.setter
    def noMsg(self, value: None) -> None: ...
    @override
    def which(self) -> Literal["value", "done", "noMsg"]: ...
    @override
    def as_reader(self) -> MsgReader: ...

class _SturdyRefList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> SturdyRefReader: ...
        @override
        def __iter__(self) -> Iterator[SturdyRefReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> SturdyRefBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: SturdyRefReader | SturdyRefBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[SturdyRefBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> SturdyRefBuilder: ...

class ReadRequest(Protocol):
    def send(self) -> ReadResult: ...

class ReadResult(Awaitable[ReadResult], Protocol):
    value: _DynamicObjectReader
    done: None
    noMsg: None
    def which(self) -> Literal["value", "done", "noMsg"]: ...

class ReadParams(Protocol): ...

class ReadCallContext(Protocol):
    params: ReadParams
    @property
    def results(self) -> MsgBuilder: ...

class ReadResultTuple(NamedTuple):
    value: AnyPointer
    done: None
    noMsg: None

class ReaderCloseRequest(Protocol):
    def send(self) -> ReaderCloseResult: ...

class ReaderCloseResult(Awaitable[None], Protocol): ...
class ReaderCloseParams(Protocol): ...

class ReaderCloseCallContext(Protocol):
    params: ReaderCloseParams

class ReadifmsgRequest(Protocol):
    def send(self) -> ReadifmsgResult: ...

class ReadifmsgResult(Awaitable[ReadifmsgResult], Protocol):
    value: _DynamicObjectReader
    done: None
    noMsg: None
    def which(self) -> Literal["value", "done", "noMsg"]: ...

class ReadifmsgParams(Protocol): ...

class ReadifmsgCallContext(Protocol):
    params: ReadifmsgParams
    @property
    def results(self) -> MsgBuilder: ...

class ReadifmsgResultTuple(NamedTuple):
    value: AnyPointer
    done: None
    noMsg: None

class ReaderClient(IdentifiableClient, PersistentClient):
    def read(self) -> ReadResult: ...
    def close(self) -> ReaderCloseResult: ...
    def readIfMsg(self) -> ReadifmsgResult: ...
    def read_request(self) -> ReadRequest: ...
    def close_request(self) -> ReaderCloseRequest: ...
    def readIfMsg_request(self) -> ReadifmsgRequest: ...

class _ReaderClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> ReaderClient: ...
        @override
        def __iter__(self) -> Iterator[ReaderClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> ReaderClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: ReaderClient | _ChannelInterfaceModule._ReaderInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[ReaderClient]: ...

class WriteRequest(Protocol):
    value: AnyPointer
    done: None
    noMsg: None
    def send(self) -> WriteResult: ...

class WriteResult(Awaitable[None], Protocol): ...

class WriteCallContext(Protocol):
    params: MsgReader

class WriterCloseRequest(Protocol):
    def send(self) -> WriterCloseResult: ...

class WriterCloseResult(Awaitable[None], Protocol): ...
class WriterCloseParams(Protocol): ...

class WriterCloseCallContext(Protocol):
    params: WriterCloseParams

class WriteifspaceRequest(Protocol):
    value: AnyPointer
    done: None
    noMsg: None
    def send(self) -> WriteifspaceResult: ...

class WriteifspaceResult(Awaitable[WriteifspaceResult], Protocol):
    success: bool

class WriteifspaceServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class WriteifspaceCallContext(Protocol):
    params: MsgReader
    @property
    def results(self) -> WriteifspaceServerResult: ...

class WriteifspaceResultTuple(NamedTuple):
    success: bool

class WriterClient(IdentifiableClient, PersistentClient):
    def write(
        self,
        value: AnyPointer | None = None,
        done: None = None,
        noMsg: None = None,
    ) -> WriteResult: ...
    def close(self) -> WriterCloseResult: ...
    def writeIfSpace(
        self,
        value: AnyPointer | None = None,
        done: None = None,
        noMsg: None = None,
    ) -> WriteifspaceResult: ...
    def write_request(
        self,
        value: AnyPointer | None = None,
        done: None = None,
        noMsg: None = None,
    ) -> WriteRequest: ...
    def close_request(self) -> WriterCloseRequest: ...
    def writeIfSpace_request(
        self,
        value: AnyPointer | None = None,
        done: None = None,
        noMsg: None = None,
    ) -> WriteifspaceRequest: ...

class _WriterClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> WriterClient: ...
        @override
        def __iter__(self) -> Iterator[WriterClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> WriterClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: WriterClient | _ChannelInterfaceModule._WriterInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[WriterClient]: ...

class StartupInfoReader(_DynamicStructReader):
    @property
    def bufferSize(self) -> int: ...
    @property
    def closeSemantics(self) -> ChannelCloseSemanticsEnum: ...
    @property
    def channelSR(self) -> SturdyRefReader: ...
    @property
    def readerSRs(self) -> SturdyRefListReader: ...
    @property
    def writerSRs(self) -> SturdyRefListReader: ...
    @property
    def channel(self) -> ChannelClient: ...
    @property
    def readers(self) -> ReaderClientListReader: ...
    @property
    def writers(self) -> WriterClientListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> StartupInfoBuilder: ...

class StartupInfoBuilder(_DynamicStructBuilder):
    @property
    def bufferSize(self) -> int: ...
    @bufferSize.setter
    def bufferSize(self, value: int) -> None: ...
    @property
    def closeSemantics(self) -> ChannelCloseSemanticsEnum: ...
    @closeSemantics.setter
    def closeSemantics(self, value: ChannelCloseSemanticsEnum) -> None: ...
    @property
    def channelSR(self) -> SturdyRefBuilder: ...
    @channelSR.setter
    def channelSR(
        self,
        value: SturdyRefBuilder | SturdyRefReader | dict[str, Any],
    ) -> None: ...
    @property
    def readerSRs(self) -> SturdyRefListBuilder: ...
    @readerSRs.setter
    def readerSRs(
        self,
        value: SturdyRefListBuilder | SturdyRefListReader | dict[str, Any],
    ) -> None: ...
    @property
    def writerSRs(self) -> SturdyRefListBuilder: ...
    @writerSRs.setter
    def writerSRs(
        self,
        value: SturdyRefListBuilder | SturdyRefListReader | dict[str, Any],
    ) -> None: ...
    @property
    def channel(self) -> ChannelClient: ...
    @channel.setter
    def channel(
        self,
        value: ChannelClient | _ChannelInterfaceModule.Server,
    ) -> None: ...
    @property
    def readers(self) -> ReaderClientListBuilder: ...
    @readers.setter
    def readers(
        self,
        value: ReaderClientListBuilder | ReaderClientListReader | dict[str, Any],
    ) -> None: ...
    @property
    def writers(self) -> WriterClientListBuilder: ...
    @writers.setter
    def writers(
        self,
        value: WriterClientListBuilder | WriterClientListReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["channelSR"],
        size: int | None = None,
    ) -> SturdyRefBuilder: ...
    @overload
    def init(
        self,
        field: Literal["readerSRs"],
        size: int | None = None,
    ) -> SturdyRefListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["writerSRs"],
        size: int | None = None,
    ) -> SturdyRefListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["readers"],
        size: int | None = None,
    ) -> ReaderClientListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["writers"],
        size: int | None = None,
    ) -> WriterClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> StartupInfoReader: ...

class StatsReader(_DynamicStructReader):
    @property
    def noOfWaitingWriters(self) -> int: ...
    @property
    def noOfWaitingReaders(self) -> int: ...
    @property
    def noOfIpsInQueue(self) -> int: ...
    @property
    def totalNoOfIpsReceived(self) -> int: ...
    @property
    def timestamp(self) -> str: ...
    @property
    def updateIntervalInMs(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> StatsBuilder: ...

class StatsBuilder(_DynamicStructBuilder):
    @property
    def noOfWaitingWriters(self) -> int: ...
    @noOfWaitingWriters.setter
    def noOfWaitingWriters(self, value: int) -> None: ...
    @property
    def noOfWaitingReaders(self) -> int: ...
    @noOfWaitingReaders.setter
    def noOfWaitingReaders(self, value: int) -> None: ...
    @property
    def noOfIpsInQueue(self) -> int: ...
    @noOfIpsInQueue.setter
    def noOfIpsInQueue(self, value: int) -> None: ...
    @property
    def totalNoOfIpsReceived(self) -> int: ...
    @totalNoOfIpsReceived.setter
    def totalNoOfIpsReceived(self, value: int) -> None: ...
    @property
    def timestamp(self) -> str: ...
    @timestamp.setter
    def timestamp(self, value: str) -> None: ...
    @property
    def updateIntervalInMs(self) -> int: ...
    @updateIntervalInMs.setter
    def updateIntervalInMs(self, value: int) -> None: ...
    @override
    def as_reader(self) -> StatsReader: ...

class UnregRequest(Protocol):
    def send(self) -> UnregResult: ...

class UnregResult(Awaitable[UnregResult], Protocol):
    success: bool

class UnregServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class UnregParams(Protocol): ...

class UnregCallContext(Protocol):
    params: UnregParams
    @property
    def results(self) -> UnregServerResult: ...

class UnregResultTuple(NamedTuple):
    success: bool

class UnregisterClient(_DynamicCapabilityClient):
    def unreg(self) -> UnregResult: ...
    def unreg_request(self) -> UnregRequest: ...

class StatusRequest(Protocol):
    stats: StatsBuilder
    @overload
    def init(self, name: Literal["stats"]) -> StatsBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> StatusResult: ...

class StatusResult(Awaitable[None], Protocol): ...

class StatusParams(Protocol):
    stats: StatsReader

class StatusCallContext(Protocol):
    params: StatusParams

class StatsCallbackClient(_DynamicCapabilityClient):
    def status(
        self,
        stats: StatsBuilder | StatsReader | dict[str, Any] | None = None,
    ) -> StatusResult: ...
    def status_request(self, stats: StatsBuilder | None = None) -> StatusRequest: ...

class SetbuffersizeRequest(Protocol):
    size: int
    def send(self) -> SetbuffersizeResult: ...

class SetbuffersizeResult(Awaitable[None], Protocol): ...

class SetbuffersizeParams(Protocol):
    size: int

class SetbuffersizeCallContext(Protocol):
    params: SetbuffersizeParams

class ReaderRequest(Protocol):
    def send(self) -> ReaderResult: ...

class ReaderResult(Awaitable[ReaderResult], Protocol):
    r: ReaderClient

class ReaderServerResult(_DynamicStructBuilder):
    @property
    def r(
        self,
    ) -> _ChannelInterfaceModule._ReaderInterfaceModule.Server | ReaderClient: ...
    @r.setter
    def r(
        self,
        value: _ChannelInterfaceModule._ReaderInterfaceModule.Server | ReaderClient,
    ) -> None: ...

class ReaderParams(Protocol): ...

class ReaderCallContext(Protocol):
    params: ReaderParams
    @property
    def results(self) -> ReaderServerResult: ...

class ReaderResultTuple(NamedTuple):
    r: _ChannelInterfaceModule._ReaderInterfaceModule.Server | ReaderClient

class WriterRequest(Protocol):
    def send(self) -> WriterResult: ...

class WriterResult(Awaitable[WriterResult], Protocol):
    w: WriterClient

class WriterServerResult(_DynamicStructBuilder):
    @property
    def w(
        self,
    ) -> _ChannelInterfaceModule._WriterInterfaceModule.Server | WriterClient: ...
    @w.setter
    def w(
        self,
        value: _ChannelInterfaceModule._WriterInterfaceModule.Server | WriterClient,
    ) -> None: ...

class WriterParams(Protocol): ...

class WriterCallContext(Protocol):
    params: WriterParams
    @property
    def results(self) -> WriterServerResult: ...

class WriterResultTuple(NamedTuple):
    w: _ChannelInterfaceModule._WriterInterfaceModule.Server | WriterClient

class EndpointsRequest(Protocol):
    def send(self) -> EndpointsResult: ...

class EndpointsResult(Awaitable[EndpointsResult], Protocol):
    r: ReaderClient
    w: WriterClient

class EndpointsServerResult(_DynamicStructBuilder):
    @property
    def r(
        self,
    ) -> _ChannelInterfaceModule._ReaderInterfaceModule.Server | ReaderClient: ...
    @r.setter
    def r(
        self,
        value: _ChannelInterfaceModule._ReaderInterfaceModule.Server | ReaderClient,
    ) -> None: ...
    @property
    def w(
        self,
    ) -> _ChannelInterfaceModule._WriterInterfaceModule.Server | WriterClient: ...
    @w.setter
    def w(
        self,
        value: _ChannelInterfaceModule._WriterInterfaceModule.Server | WriterClient,
    ) -> None: ...

class EndpointsParams(Protocol): ...

class EndpointsCallContext(Protocol):
    params: EndpointsParams
    @property
    def results(self) -> EndpointsServerResult: ...

class EndpointsResultTuple(NamedTuple):
    r: _ChannelInterfaceModule._ReaderInterfaceModule.Server | ReaderClient
    w: _ChannelInterfaceModule._WriterInterfaceModule.Server | WriterClient

class SetautoclosesemanticsRequest(Protocol):
    cs: ChannelCloseSemanticsEnum
    def send(self) -> SetautoclosesemanticsResult: ...

class SetautoclosesemanticsResult(Awaitable[None], Protocol): ...

class SetautoclosesemanticsParams(Protocol):
    cs: ChannelCloseSemanticsEnum

class SetautoclosesemanticsCallContext(Protocol):
    params: SetautoclosesemanticsParams

class ChannelCloseRequest(Protocol):
    waitForEmptyBuffer: bool
    def send(self) -> ChannelCloseResult: ...

class ChannelCloseResult(Awaitable[None], Protocol): ...

class ChannelCloseParams(Protocol):
    waitForEmptyBuffer: bool

class ChannelCloseCallContext(Protocol):
    params: ChannelCloseParams

class RegisterstatscallbackRequest(Protocol):
    callback: (
        StatsCallbackClient
        | _ChannelInterfaceModule._StatsCallbackInterfaceModule.Server
    )
    updateIntervalInMs: int
    def send(self) -> RegisterstatscallbackResult: ...

class RegisterstatscallbackResult(Awaitable[RegisterstatscallbackResult], Protocol):
    unregisterCallback: UnregisterClient

class RegisterstatscallbackServerResult(_DynamicStructBuilder):
    @property
    def unregisterCallback(
        self,
    ) -> (
        _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server
        | UnregisterClient
    ): ...
    @unregisterCallback.setter
    def unregisterCallback(
        self,
        value: _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server
        | UnregisterClient,
    ) -> None: ...

class RegisterstatscallbackParams(Protocol):
    callback: StatsCallbackClient
    updateIntervalInMs: int

class RegisterstatscallbackCallContext(Protocol):
    params: RegisterstatscallbackParams
    @property
    def results(self) -> RegisterstatscallbackServerResult: ...

class RegisterstatscallbackResultTuple(NamedTuple):
    unregisterCallback: (
        _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server
        | UnregisterClient
    )

class ChannelClient(IdentifiableClient, PersistentClient):
    def setBufferSize(self, size: int | None = None) -> SetbuffersizeResult: ...
    def reader(self) -> ReaderResult: ...
    def writer(self) -> WriterResult: ...
    def endpoints(self) -> EndpointsResult: ...
    def setAutoCloseSemantics(
        self,
        cs: ChannelCloseSemanticsEnum | None = None,
    ) -> SetautoclosesemanticsResult: ...
    def close(self, waitForEmptyBuffer: bool | None = None) -> ChannelCloseResult: ...
    def registerStatsCallback(
        self,
        callback: StatsCallbackClient
        | _ChannelInterfaceModule._StatsCallbackInterfaceModule.Server
        | None = None,
        updateIntervalInMs: int | None = None,
    ) -> RegisterstatscallbackResult: ...
    def setBufferSize_request(
        self,
        size: int | None = None,
    ) -> SetbuffersizeRequest: ...
    def reader_request(self) -> ReaderRequest: ...
    def writer_request(self) -> WriterRequest: ...
    def endpoints_request(self) -> EndpointsRequest: ...
    def setAutoCloseSemantics_request(
        self,
        cs: ChannelCloseSemanticsEnum | None = None,
    ) -> SetautoclosesemanticsRequest: ...
    def close_request(
        self,
        waitForEmptyBuffer: bool | None = None,
    ) -> ChannelCloseRequest: ...
    def registerStatsCallback_request(
        self,
        callback: StatsCallbackClient
        | _ChannelInterfaceModule._StatsCallbackInterfaceModule.Server
        | None = None,
        updateIntervalInMs: int | None = None,
    ) -> RegisterstatscallbackRequest: ...

Channel: _ChannelInterfaceModule

class _StartChannelsServiceInterfaceModule(_IdentifiableInterfaceModule):
    class _ParamsStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            name: str | None = None,
            noOfChannels: int | None = None,
            noOfReaders: int | None = None,
            noOfWriters: int | None = None,
            readerSrts: TextListBuilder | dict[str, Any] | None = None,
            writerSrts: TextListBuilder | dict[str, Any] | None = None,
            bufferSize: int | None = None,
            **kwargs: object,
        ) -> ParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[ParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ParamsBuilder]: ...
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
        ) -> ParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> ParamsReader: ...

    Params: _ParamsStructModule
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> StartChannelsServiceClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def start(
            self,
            name: str,
            noOfChannels: int,
            noOfReaders: int,
            noOfWriters: int,
            readerSrts: TextListReader,
            writerSrts: TextListReader,
            bufferSize: int,
            _context: StartChannelsServiceStartCallContext,
            **kwargs: object,
        ) -> Awaitable[StartChannelsServiceStartResultTuple | None]: ...
        def start_context(
            self,
            context: StartChannelsServiceStartCallContext,
        ) -> Awaitable[None]: ...

class _TextList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> str: ...
        @override
        def __iter__(self) -> Iterator[str]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> str: ...
        @override
        def __setitem__(self, key: int, value: str) -> None: ...
        @override
        def __iter__(self) -> Iterator[str]: ...

class ParamsReader(_DynamicStructReader):
    @property
    def name(self) -> str: ...
    @property
    def noOfChannels(self) -> int: ...
    @property
    def noOfReaders(self) -> int: ...
    @property
    def noOfWriters(self) -> int: ...
    @property
    def readerSrts(self) -> TextListReader: ...
    @property
    def writerSrts(self) -> TextListReader: ...
    @property
    def bufferSize(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ParamsBuilder: ...

class ParamsBuilder(_DynamicStructBuilder):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def noOfChannels(self) -> int: ...
    @noOfChannels.setter
    def noOfChannels(self, value: int) -> None: ...
    @property
    def noOfReaders(self) -> int: ...
    @noOfReaders.setter
    def noOfReaders(self, value: int) -> None: ...
    @property
    def noOfWriters(self) -> int: ...
    @noOfWriters.setter
    def noOfWriters(self, value: int) -> None: ...
    @property
    def readerSrts(self) -> TextListBuilder: ...
    @readerSrts.setter
    def readerSrts(
        self,
        value: TextListBuilder | TextListReader | dict[str, Any],
    ) -> None: ...
    @property
    def writerSrts(self) -> TextListBuilder: ...
    @writerSrts.setter
    def writerSrts(
        self,
        value: TextListBuilder | TextListReader | dict[str, Any],
    ) -> None: ...
    @property
    def bufferSize(self) -> int: ...
    @bufferSize.setter
    def bufferSize(self, value: int) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["readerSrts"],
        size: int | None = None,
    ) -> TextListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["writerSrts"],
        size: int | None = None,
    ) -> TextListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> ParamsReader: ...

class StartChannelsServiceStartRequest(Protocol):
    name: str
    noOfChannels: int
    noOfReaders: int
    noOfWriters: int
    readerSrts: TextListBuilder | TextListReader | Sequence[Any]
    writerSrts: TextListBuilder | TextListReader | Sequence[Any]
    bufferSize: int
    @overload
    def init(self, name: Literal["readerSrts"], size: int = ...) -> TextListBuilder: ...
    @overload
    def init(self, name: Literal["writerSrts"], size: int = ...) -> TextListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> StartChannelsServiceStartResult: ...

class _StartupInfoList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> StartupInfoReader: ...
        @override
        def __iter__(self) -> Iterator[StartupInfoReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> StartupInfoBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: StartupInfoReader | StartupInfoBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[StartupInfoBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> StartupInfoBuilder: ...

class StartChannelsServiceStartResult(
    Awaitable[StartChannelsServiceStartResult],
    Protocol,
):
    startupInfos: StartupInfoListReader
    stop: StoppableClient

class StartChannelsServiceStartServerResult(_DynamicStructBuilder):
    @property
    def startupInfos(self) -> StartupInfoListBuilder: ...
    @startupInfos.setter
    def startupInfos(
        self,
        value: StartupInfoListBuilder | StartupInfoListReader | Sequence[Any],
    ) -> None: ...
    @property
    def stop(self) -> _StoppableInterfaceModule.Server | StoppableClient: ...
    @stop.setter
    def stop(
        self,
        value: _StoppableInterfaceModule.Server | StoppableClient,
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["startupInfos"],
        size: int | None = None,
    ) -> StartupInfoListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class StartChannelsServiceStartCallContext(Protocol):
    params: ParamsReader
    @property
    def results(self) -> StartChannelsServiceStartServerResult: ...

class StartChannelsServiceStartResultTuple(NamedTuple):
    startupInfos: StartupInfoListBuilder | StartupInfoListReader | Sequence[Any]
    stop: _StoppableInterfaceModule.Server | StoppableClient

class StartChannelsServiceClient(IdentifiableClient):
    def start(
        self,
        name: str | None = None,
        noOfChannels: int | None = None,
        noOfReaders: int | None = None,
        noOfWriters: int | None = None,
        readerSrts: TextListBuilder | TextListReader | Sequence[Any] | None = None,
        writerSrts: TextListBuilder | TextListReader | Sequence[Any] | None = None,
        bufferSize: int | None = None,
    ) -> StartChannelsServiceStartResult: ...
    def start_request(
        self,
        name: str | None = None,
        noOfChannels: int | None = None,
        noOfReaders: int | None = None,
        noOfWriters: int | None = None,
        readerSrts: TextListBuilder | TextListReader | Sequence[Any] | None = None,
        writerSrts: TextListBuilder | TextListReader | Sequence[Any] | None = None,
        bufferSize: int | None = None,
    ) -> StartChannelsServiceStartRequest: ...

StartChannelsService: _StartChannelsServiceInterfaceModule

class NameAndSRReader(_DynamicStructReader):
    @property
    def name(self) -> str: ...
    @property
    def sr(self) -> SturdyRefReader: ...
    @property
    def srs(self) -> SturdyRefListReader: ...
    @override
    def which(self) -> Literal["sr", "srs"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> NameAndSRBuilder: ...

class NameAndSRBuilder(_DynamicStructBuilder):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def sr(self) -> SturdyRefBuilder: ...
    @sr.setter
    def sr(
        self,
        value: SturdyRefBuilder | SturdyRefReader | dict[str, Any],
    ) -> None: ...
    @property
    def srs(self) -> SturdyRefListBuilder: ...
    @srs.setter
    def srs(
        self,
        value: SturdyRefListBuilder | SturdyRefListReader | dict[str, Any],
    ) -> None: ...
    @override
    def which(self) -> Literal["sr", "srs"]: ...
    @override
    @overload
    def init(
        self,
        field: Literal["sr"],
        size: int | None = None,
    ) -> SturdyRefBuilder: ...
    @overload
    def init(
        self,
        field: Literal["srs"],
        size: int | None = None,
    ) -> SturdyRefListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> NameAndSRReader: ...

class _NameAndSRList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> NameAndSRReader: ...
        @override
        def __iter__(self) -> Iterator[NameAndSRReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> NameAndSRBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: NameAndSRReader | NameAndSRBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[NameAndSRBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> NameAndSRBuilder: ...

class _PortInfosStructModule(_StructModule):
    class _NameAndSRStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            name: str | None = None,
            sr: SturdyRefBuilder | dict[str, Any] | None = None,
            srs: SturdyRefListBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> NameAndSRBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[NameAndSRReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[NameAndSRReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[NameAndSRBuilder]: ...
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
        ) -> NameAndSRReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> NameAndSRReader: ...

    NameAndSR: _NameAndSRStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        inPorts: NameAndSRListBuilder | dict[str, Any] | None = None,
        outPorts: NameAndSRListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> PortInfosBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[PortInfosReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[PortInfosReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[PortInfosBuilder]: ...
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
    ) -> PortInfosReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> PortInfosReader: ...

class PortInfosReader(_DynamicStructReader):
    @property
    def inPorts(self) -> NameAndSRListReader: ...
    @property
    def outPorts(self) -> NameAndSRListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> PortInfosBuilder: ...

class PortInfosBuilder(_DynamicStructBuilder):
    @property
    def inPorts(self) -> NameAndSRListBuilder: ...
    @inPorts.setter
    def inPorts(
        self,
        value: NameAndSRListBuilder | NameAndSRListReader | dict[str, Any],
    ) -> None: ...
    @property
    def outPorts(self) -> NameAndSRListBuilder: ...
    @outPorts.setter
    def outPorts(
        self,
        value: NameAndSRListBuilder | NameAndSRListReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["inPorts"],
        size: int | None = None,
    ) -> NameAndSRListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["outPorts"],
        size: int | None = None,
    ) -> NameAndSRListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> PortInfosReader: ...

PortInfos: _PortInfosStructModule

class PortReader(_DynamicStructReader):
    @property
    def name(self) -> str: ...
    @property
    def contentType(self) -> str: ...
    @property
    def type(self) -> ComponentPortPortTypeEnum: ...
    @property
    def desc(self) -> str: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> PortBuilder: ...

class PortBuilder(_DynamicStructBuilder):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def contentType(self) -> str: ...
    @contentType.setter
    def contentType(self, value: str) -> None: ...
    @property
    def type(self) -> ComponentPortPortTypeEnum: ...
    @type.setter
    def type(self, value: ComponentPortPortTypeEnum) -> None: ...
    @property
    def desc(self) -> str: ...
    @desc.setter
    def desc(self, value: str) -> None: ...
    @override
    def as_reader(self) -> PortReader: ...

class _PortList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> PortReader: ...
        @override
        def __iter__(self) -> Iterator[PortReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> PortBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: PortReader | PortBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[PortBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> PortBuilder: ...

class _RunnableInterfaceModule(_IdentifiableInterfaceModule):
    class _FactoryInterfaceModule(_IdentifiableInterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> RunnableFactoryClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def create(
                self,
                _context: RunnableFactoryCreateCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _RunnableInterfaceModule.Server
                | RunnableClient
                | RunnableFactoryCreateResultTuple
                | None
            ]: ...
            def create_context(
                self,
                context: RunnableFactoryCreateCallContext,
            ) -> Awaitable[None]: ...

    Factory: _FactoryInterfaceModule
    type FactoryServer = _RunnableInterfaceModule._FactoryInterfaceModule.Server
    class _StoppedCallbackInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> StoppedCallbackClient: ...
        class Server(_DynamicCapabilityServer):
            def stopped(
                self,
                _context: StoppedCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def stopped_context(
                self,
                context: StoppedCallContext,
            ) -> Awaitable[None]: ...

    StoppedCallback: _StoppedCallbackInterfaceModule
    type StoppedCallbackServer = (
        _RunnableInterfaceModule._StoppedCallbackInterfaceModule.Server
    )
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> RunnableClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def start(
            self,
            portInfosReaderSr: SturdyRefReader,
            name: str,
            stoppedCb: StoppedCallbackClient,
            _context: RunnableStartCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | RunnableStartResultTuple | None]: ...
        def start_context(
            self,
            context: RunnableStartCallContext,
        ) -> Awaitable[None]: ...
        def stop(
            self,
            _context: RunnableStopCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | RunnableStopResultTuple | None]: ...
        def stop_context(self, context: RunnableStopCallContext) -> Awaitable[None]: ...

class RunnableFactoryCreateRequest(Protocol):
    def send(self) -> RunnableFactoryCreateResult: ...

class RunnableFactoryCreateResult(Awaitable[RunnableFactoryCreateResult], Protocol):
    out: RunnableClient

class RunnableFactoryCreateServerResult(_DynamicStructBuilder):
    @property
    def out(self) -> _RunnableInterfaceModule.Server | RunnableClient: ...
    @out.setter
    def out(self, value: _RunnableInterfaceModule.Server | RunnableClient) -> None: ...

class RunnableFactoryCreateParams(Protocol): ...

class RunnableFactoryCreateCallContext(Protocol):
    params: RunnableFactoryCreateParams
    @property
    def results(self) -> RunnableFactoryCreateServerResult: ...

class RunnableFactoryCreateResultTuple(NamedTuple):
    out: _RunnableInterfaceModule.Server | RunnableClient

class RunnableFactoryClient(IdentifiableClient):
    def create(self) -> RunnableFactoryCreateResult: ...
    def create_request(self) -> RunnableFactoryCreateRequest: ...

class StoppedRequest(Protocol):
    def send(self) -> StoppedResult: ...

class StoppedResult(Awaitable[None], Protocol): ...
class StoppedParams(Protocol): ...

class StoppedCallContext(Protocol):
    params: StoppedParams

class StoppedCallbackClient(_DynamicCapabilityClient):
    def stopped(self) -> StoppedResult: ...
    def stopped_request(self) -> StoppedRequest: ...

class RunnableStartRequest(Protocol):
    portInfosReaderSr: SturdyRefBuilder
    name: str
    stoppedCb: (
        StoppedCallbackClient
        | _RunnableInterfaceModule._StoppedCallbackInterfaceModule.Server
    )
    @overload
    def init(self, name: Literal["portInfosReaderSr"]) -> SturdyRefBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> RunnableStartResult: ...

class RunnableStartResult(Awaitable[RunnableStartResult], Protocol):
    success: bool

class RunnableStartServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class RunnableStartParams(Protocol):
    portInfosReaderSr: SturdyRefReader
    name: str
    stoppedCb: StoppedCallbackClient

class RunnableStartCallContext(Protocol):
    params: RunnableStartParams
    @property
    def results(self) -> RunnableStartServerResult: ...

class RunnableStartResultTuple(NamedTuple):
    success: bool

class RunnableStopRequest(Protocol):
    def send(self) -> RunnableStopResult: ...

class RunnableStopResult(Awaitable[RunnableStopResult], Protocol):
    success: bool

class RunnableStopServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class RunnableStopParams(Protocol): ...

class RunnableStopCallContext(Protocol):
    params: RunnableStopParams
    @property
    def results(self) -> RunnableStopServerResult: ...

class RunnableStopResultTuple(NamedTuple):
    success: bool

class RunnableClient(IdentifiableClient):
    def start(
        self,
        portInfosReaderSr: SturdyRefBuilder
        | SturdyRefReader
        | dict[str, Any]
        | None = None,
        name: str | None = None,
        stoppedCb: StoppedCallbackClient
        | _RunnableInterfaceModule._StoppedCallbackInterfaceModule.Server
        | None = None,
    ) -> RunnableStartResult: ...
    def stop(self) -> RunnableStopResult: ...
    def start_request(
        self,
        portInfosReaderSr: SturdyRefBuilder | None = None,
        name: str | None = None,
        stoppedCb: StoppedCallbackClient
        | _RunnableInterfaceModule._StoppedCallbackInterfaceModule.Server
        | None = None,
    ) -> RunnableStartRequest: ...
    def stop_request(self) -> RunnableStopRequest: ...

Runnable: _RunnableInterfaceModule

class _ProcessInterfaceModule(
    _IdentifiableInterfaceModule,
    _GatewayRegistrableInterfaceModule,
):
    class _FactoryInterfaceModule(_IdentifiableInterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> ProcessFactoryClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def create(
                self,
                _context: ProcessFactoryCreateCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ProcessInterfaceModule.Server
                | ProcessClient
                | ProcessFactoryCreateResultTuple
                | None
            ]: ...
            def create_context(
                self,
                context: ProcessFactoryCreateCallContext,
            ) -> Awaitable[None]: ...

    Factory: _FactoryInterfaceModule
    type FactoryServer = _ProcessInterfaceModule._FactoryInterfaceModule.Server
    class _ConfigEntryStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            name: str | None = None,
            val: ValueBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> ConfigEntryBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[ConfigEntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ConfigEntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ConfigEntryBuilder]: ...
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
        ) -> ConfigEntryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> ConfigEntryReader: ...

    ConfigEntry: _ConfigEntryStructModule
    class _StateEnumModule:
        started: int
        stopped: int
        canceled: int

    State: _StateEnumModule
    class _StateTransitionInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> StateTransitionClient: ...
        class Server(_DynamicCapabilityServer):
            def stateChanged(
                self,
                old: ProcessStateEnum,
                new: ProcessStateEnum,
                _context: StatechangedCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def stateChanged_context(
                self,
                context: StatechangedCallContext,
            ) -> Awaitable[None]: ...

    StateTransition: _StateTransitionInterfaceModule
    type StateTransitionServer = (
        _ProcessInterfaceModule._StateTransitionInterfaceModule.Server
    )
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> ProcessClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _GatewayRegistrableInterfaceModule.Server,
    ):
        def inPorts(
            self,
            _context: InportsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            PortListBuilder | PortListReader | Sequence[Any] | InportsResultTuple | None
        ]: ...
        def inPorts_context(self, context: InportsCallContext) -> Awaitable[None]: ...
        def connectInPort(
            self,
            name: str,
            sturdyRef: SturdyRefReader,
            _context: ConnectinportCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | ConnectinportResultTuple | None]: ...
        def connectInPort_context(
            self,
            context: ConnectinportCallContext,
        ) -> Awaitable[None]: ...
        def outPorts(
            self,
            _context: OutportsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            PortListBuilder
            | PortListReader
            | Sequence[Any]
            | OutportsResultTuple
            | None
        ]: ...
        def outPorts_context(self, context: OutportsCallContext) -> Awaitable[None]: ...
        def connectOutPort(
            self,
            name: str,
            sturdyRef: SturdyRefReader,
            _context: ConnectoutportCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | ConnectoutportResultTuple | None]: ...
        def connectOutPort_context(
            self,
            context: ConnectoutportCallContext,
        ) -> Awaitable[None]: ...
        def configEntries(
            self,
            _context: ConfigentriesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            ConfigEntryListBuilder
            | ConfigEntryListReader
            | Sequence[Any]
            | ConfigentriesResultTuple
            | None
        ]: ...
        def configEntries_context(
            self,
            context: ConfigentriesCallContext,
        ) -> Awaitable[None]: ...
        def start(
            self,
            _context: ProcessStartCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def start_context(
            self,
            context: ProcessStartCallContext,
        ) -> Awaitable[None]: ...
        def stop(
            self,
            _context: ProcessStopCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def stop_context(self, context: ProcessStopCallContext) -> Awaitable[None]: ...
        def setConfigEntry(
            self,
            name: str,
            val: ValueReader,
            _context: SetconfigentryCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def setConfigEntry_context(
            self,
            context: SetconfigentryCallContext,
        ) -> Awaitable[None]: ...
        def state(
            self,
            transitionCallback: StateTransitionClient,
            _context: StateCallContext,
            **kwargs: object,
        ) -> Awaitable[ProcessStateEnum | StateResultTuple | None]: ...
        def state_context(self, context: StateCallContext) -> Awaitable[None]: ...

class ProcessFactoryCreateRequest(Protocol):
    def send(self) -> ProcessFactoryCreateResult: ...

class ProcessFactoryCreateResult(Awaitable[ProcessFactoryCreateResult], Protocol):
    out: ProcessClient

class ProcessFactoryCreateServerResult(_DynamicStructBuilder):
    @property
    def out(self) -> _ProcessInterfaceModule.Server | ProcessClient: ...
    @out.setter
    def out(self, value: _ProcessInterfaceModule.Server | ProcessClient) -> None: ...

class ProcessFactoryCreateParams(Protocol): ...

class ProcessFactoryCreateCallContext(Protocol):
    params: ProcessFactoryCreateParams
    @property
    def results(self) -> ProcessFactoryCreateServerResult: ...

class ProcessFactoryCreateResultTuple(NamedTuple):
    out: _ProcessInterfaceModule.Server | ProcessClient

class ProcessFactoryClient(IdentifiableClient):
    def create(self) -> ProcessFactoryCreateResult: ...
    def create_request(self) -> ProcessFactoryCreateRequest: ...

class ConfigEntryReader(_DynamicStructReader):
    @property
    def name(self) -> str: ...
    @property
    def val(self) -> ValueReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ConfigEntryBuilder: ...

class ConfigEntryBuilder(_DynamicStructBuilder):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def val(self) -> ValueBuilder: ...
    @val.setter
    def val(self, value: ValueBuilder | ValueReader | dict[str, Any]) -> None: ...
    @override
    def init(self, field: Literal["val"], size: int | None = None) -> ValueBuilder: ...
    @override
    def as_reader(self) -> ConfigEntryReader: ...

class StatechangedRequest(Protocol):
    old: ProcessStateEnum
    new: ProcessStateEnum
    def send(self) -> StatechangedResult: ...

class StatechangedResult(Awaitable[None], Protocol): ...

class StatechangedParams(Protocol):
    old: ProcessStateEnum
    new: ProcessStateEnum

class StatechangedCallContext(Protocol):
    params: StatechangedParams

class StateTransitionClient(_DynamicCapabilityClient):
    def stateChanged(
        self,
        old: ProcessStateEnum | None = None,
        new: ProcessStateEnum | None = None,
    ) -> StatechangedResult: ...
    def stateChanged_request(
        self,
        old: ProcessStateEnum | None = None,
        new: ProcessStateEnum | None = None,
    ) -> StatechangedRequest: ...

class InportsRequest(Protocol):
    def send(self) -> InportsResult: ...

class InportsResult(Awaitable[InportsResult], Protocol):
    ports: PortListReader

class InportsServerResult(_DynamicStructBuilder):
    @property
    def ports(self) -> PortListBuilder: ...
    @ports.setter
    def ports(
        self,
        value: PortListBuilder | PortListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["ports"],
        size: int | None = None,
    ) -> PortListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class InportsParams(Protocol): ...

class InportsCallContext(Protocol):
    params: InportsParams
    @property
    def results(self) -> InportsServerResult: ...

class InportsResultTuple(NamedTuple):
    ports: PortListBuilder | PortListReader | Sequence[Any]

class ConnectinportRequest(Protocol):
    name: str
    sturdyRef: SturdyRefBuilder
    @overload
    def init(self, name: Literal["sturdyRef"]) -> SturdyRefBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> ConnectinportResult: ...

class ConnectinportResult(Awaitable[ConnectinportResult], Protocol):
    connected: bool

class ConnectinportServerResult(_DynamicStructBuilder):
    @property
    def connected(self) -> bool: ...
    @connected.setter
    def connected(self, value: bool) -> None: ...

class ConnectinportParams(Protocol):
    name: str
    sturdyRef: SturdyRefReader

class ConnectinportCallContext(Protocol):
    params: ConnectinportParams
    @property
    def results(self) -> ConnectinportServerResult: ...

class ConnectinportResultTuple(NamedTuple):
    connected: bool

class OutportsRequest(Protocol):
    def send(self) -> OutportsResult: ...

class OutportsResult(Awaitable[OutportsResult], Protocol):
    ports: PortListReader

class OutportsServerResult(_DynamicStructBuilder):
    @property
    def ports(self) -> PortListBuilder: ...
    @ports.setter
    def ports(
        self,
        value: PortListBuilder | PortListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["ports"],
        size: int | None = None,
    ) -> PortListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class OutportsParams(Protocol): ...

class OutportsCallContext(Protocol):
    params: OutportsParams
    @property
    def results(self) -> OutportsServerResult: ...

class OutportsResultTuple(NamedTuple):
    ports: PortListBuilder | PortListReader | Sequence[Any]

class ConnectoutportRequest(Protocol):
    name: str
    sturdyRef: SturdyRefBuilder
    @overload
    def init(self, name: Literal["sturdyRef"]) -> SturdyRefBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> ConnectoutportResult: ...

class ConnectoutportResult(Awaitable[ConnectoutportResult], Protocol):
    connected: bool

class ConnectoutportServerResult(_DynamicStructBuilder):
    @property
    def connected(self) -> bool: ...
    @connected.setter
    def connected(self, value: bool) -> None: ...

class ConnectoutportParams(Protocol):
    name: str
    sturdyRef: SturdyRefReader

class ConnectoutportCallContext(Protocol):
    params: ConnectoutportParams
    @property
    def results(self) -> ConnectoutportServerResult: ...

class ConnectoutportResultTuple(NamedTuple):
    connected: bool

class ConfigentriesRequest(Protocol):
    def send(self) -> ConfigentriesResult: ...

class _ConfigEntryList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> ConfigEntryReader: ...
        @override
        def __iter__(self) -> Iterator[ConfigEntryReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> ConfigEntryBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: ConfigEntryReader | ConfigEntryBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[ConfigEntryBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> ConfigEntryBuilder: ...

class ConfigentriesResult(Awaitable[ConfigentriesResult], Protocol):
    config: ConfigEntryListReader

class ConfigentriesServerResult(_DynamicStructBuilder):
    @property
    def config(self) -> ConfigEntryListBuilder: ...
    @config.setter
    def config(
        self,
        value: ConfigEntryListBuilder | ConfigEntryListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["config"],
        size: int | None = None,
    ) -> ConfigEntryListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ConfigentriesParams(Protocol): ...

class ConfigentriesCallContext(Protocol):
    params: ConfigentriesParams
    @property
    def results(self) -> ConfigentriesServerResult: ...

class ConfigentriesResultTuple(NamedTuple):
    config: ConfigEntryListBuilder | ConfigEntryListReader | Sequence[Any]

class ProcessStartRequest(Protocol):
    def send(self) -> ProcessStartResult: ...

class ProcessStartResult(Awaitable[None], Protocol): ...
class ProcessStartParams(Protocol): ...

class ProcessStartCallContext(Protocol):
    params: ProcessStartParams

class ProcessStopRequest(Protocol):
    def send(self) -> ProcessStopResult: ...

class ProcessStopResult(Awaitable[None], Protocol): ...
class ProcessStopParams(Protocol): ...

class ProcessStopCallContext(Protocol):
    params: ProcessStopParams

class SetconfigentryRequest(Protocol):
    name: str
    val: ValueBuilder
    @overload
    def init(self, name: Literal["val"]) -> ValueBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> SetconfigentryResult: ...

class SetconfigentryResult(Awaitable[None], Protocol): ...

class SetconfigentryCallContext(Protocol):
    params: ConfigEntryReader

class StateRequest(Protocol):
    transitionCallback: (
        StateTransitionClient
        | _ProcessInterfaceModule._StateTransitionInterfaceModule.Server
    )
    def send(self) -> StateResult: ...

class StateResult(Awaitable[StateResult], Protocol):
    currentState: ProcessStateEnum

class StateServerResult(_DynamicStructBuilder):
    @property
    def currentState(self) -> ProcessStateEnum: ...
    @currentState.setter
    def currentState(self, value: ProcessStateEnum) -> None: ...

class StateParams(Protocol):
    transitionCallback: StateTransitionClient

class StateCallContext(Protocol):
    params: StateParams
    @property
    def results(self) -> StateServerResult: ...

class StateResultTuple(NamedTuple):
    currentState: ProcessStateEnum

class ProcessClient(IdentifiableClient, GatewayRegistrableClient):
    def inPorts(self) -> InportsResult: ...
    def connectInPort(
        self,
        name: str | None = None,
        sturdyRef: SturdyRefBuilder | SturdyRefReader | dict[str, Any] | None = None,
    ) -> ConnectinportResult: ...
    def outPorts(self) -> OutportsResult: ...
    def connectOutPort(
        self,
        name: str | None = None,
        sturdyRef: SturdyRefBuilder | SturdyRefReader | dict[str, Any] | None = None,
    ) -> ConnectoutportResult: ...
    def configEntries(self) -> ConfigentriesResult: ...
    def start(self) -> ProcessStartResult: ...
    def stop(self) -> ProcessStopResult: ...
    def setConfigEntry(
        self,
        name: str | None = None,
        val: ValueBuilder | ValueReader | dict[str, Any] | None = None,
    ) -> SetconfigentryResult: ...
    def state(
        self,
        transitionCallback: StateTransitionClient
        | _ProcessInterfaceModule._StateTransitionInterfaceModule.Server
        | None = None,
    ) -> StateResult: ...
    def inPorts_request(self) -> InportsRequest: ...
    def connectInPort_request(
        self,
        name: str | None = None,
        sturdyRef: SturdyRefBuilder | None = None,
    ) -> ConnectinportRequest: ...
    def outPorts_request(self) -> OutportsRequest: ...
    def connectOutPort_request(
        self,
        name: str | None = None,
        sturdyRef: SturdyRefBuilder | None = None,
    ) -> ConnectoutportRequest: ...
    def configEntries_request(self) -> ConfigentriesRequest: ...
    def start_request(self) -> ProcessStartRequest: ...
    def stop_request(self) -> ProcessStopRequest: ...
    def setConfigEntry_request(
        self,
        name: str | None = None,
        val: ValueBuilder | None = None,
    ) -> SetconfigentryRequest: ...
    def state_request(
        self,
        transitionCallback: StateTransitionClient
        | _ProcessInterfaceModule._StateTransitionInterfaceModule.Server
        | None = None,
    ) -> StateRequest: ...

Process: _ProcessInterfaceModule

class ComponentFactoryReader(_DynamicStructReader):
    @property
    def none(self) -> None: ...
    @property
    def runnable(self) -> RunnableFactoryClient: ...
    @property
    def process(self) -> ProcessFactoryClient: ...
    @override
    def which(self) -> Literal["none", "runnable", "process"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ComponentFactoryBuilder: ...

class ComponentFactoryBuilder(_DynamicStructBuilder):
    @property
    def none(self) -> None: ...
    @none.setter
    def none(self, value: None) -> None: ...
    @property
    def runnable(self) -> RunnableFactoryClient: ...
    @runnable.setter
    def runnable(
        self,
        value: RunnableFactoryClient
        | _RunnableInterfaceModule._FactoryInterfaceModule.Server,
    ) -> None: ...
    @property
    def process(self) -> ProcessFactoryClient: ...
    @process.setter
    def process(
        self,
        value: ProcessFactoryClient
        | _ProcessInterfaceModule._FactoryInterfaceModule.Server,
    ) -> None: ...
    @override
    def which(self) -> Literal["none", "runnable", "process"]: ...
    @override
    def as_reader(self) -> ComponentFactoryReader: ...

class _ComponentStructModule(_StructModule):
    class _ComponentTypeEnumModule:
        standard: int
        iip: int
        subflow: int
        view: int
        process: int

    ComponentType: _ComponentTypeEnumModule
    class _PortStructModule(_StructModule):
        class _PortTypeEnumModule:
            standard: int
            array: int

        PortType: _PortTypeEnumModule
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            name: str | None = None,
            contentType: str | None = None,
            type: ComponentPortPortTypeEnum | None = None,
            desc: str | None = None,
            **kwargs: object,
        ) -> PortBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[PortReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[PortReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[PortBuilder]: ...
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
        ) -> PortReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> PortReader: ...

    Port: _PortStructModule
    class _ComponentFactoryStructModule(_StructModule):
        class Reader(_DynamicStructReader): ...
        class Builder(_DynamicStructBuilder): ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Callable[[int], bytearray] | None = None,
            none: None | None = None,
            runnable: RunnableFactoryClient
            | _RunnableInterfaceModule._FactoryInterfaceModule.Server
            | None = None,
            process: ProcessFactoryClient
            | _ProcessInterfaceModule._FactoryInterfaceModule.Server
            | None = None,
            **kwargs: object,
        ) -> ComponentFactoryBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[ComponentFactoryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ComponentFactoryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ComponentFactoryBuilder]: ...
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
        ) -> ComponentFactoryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> ComponentFactoryReader: ...

    ComponentFactory: _ComponentFactoryStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        info: IdInformationBuilder | dict[str, Any] | None = None,
        type: ComponentComponentTypeEnum | None = None,
        inPorts: PortListBuilder | dict[str, Any] | None = None,
        outPorts: PortListBuilder | dict[str, Any] | None = None,
        defaultConfig: StructuredTextBuilder | dict[str, Any] | None = None,
        factory: ComponentFactoryBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> ComponentBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[ComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[ComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[ComponentBuilder]: ...
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
    ) -> ComponentReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> ComponentReader: ...

class ComponentReader(_DynamicStructReader):
    @property
    def info(self) -> IdInformationReader: ...
    @property
    def type(self) -> ComponentComponentTypeEnum: ...
    @property
    def inPorts(self) -> PortListReader: ...
    @property
    def outPorts(self) -> PortListReader: ...
    @property
    def defaultConfig(self) -> StructuredTextReader: ...
    @property
    def factory(self) -> ComponentFactoryReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> ComponentBuilder: ...

class ComponentBuilder(_DynamicStructBuilder):
    @property
    def info(self) -> IdInformationBuilder: ...
    @info.setter
    def info(
        self,
        value: IdInformationBuilder | IdInformationReader | dict[str, Any],
    ) -> None: ...
    @property
    def type(self) -> ComponentComponentTypeEnum: ...
    @type.setter
    def type(self, value: ComponentComponentTypeEnum) -> None: ...
    @property
    def inPorts(self) -> PortListBuilder: ...
    @inPorts.setter
    def inPorts(
        self,
        value: PortListBuilder | PortListReader | dict[str, Any],
    ) -> None: ...
    @property
    def outPorts(self) -> PortListBuilder: ...
    @outPorts.setter
    def outPorts(
        self,
        value: PortListBuilder | PortListReader | dict[str, Any],
    ) -> None: ...
    @property
    def defaultConfig(self) -> StructuredTextBuilder: ...
    @defaultConfig.setter
    def defaultConfig(
        self,
        value: StructuredTextBuilder | StructuredTextReader | dict[str, Any],
    ) -> None: ...
    @property
    def factory(self) -> ComponentFactoryBuilder: ...
    @factory.setter
    def factory(
        self,
        value: ComponentFactoryBuilder | ComponentFactoryReader | dict[str, Any],
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
        field: Literal["defaultConfig"],
        size: int | None = None,
    ) -> StructuredTextBuilder: ...
    @overload
    def init(
        self,
        field: Literal["factory"],
        size: int | None = None,
    ) -> ComponentFactoryBuilder: ...
    @overload
    def init(
        self,
        field: Literal["inPorts"],
        size: int | None = None,
    ) -> PortListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["outPorts"],
        size: int | None = None,
    ) -> PortListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> ComponentReader: ...

Component: _ComponentStructModule

# Top-level type aliases for use in type annotations
type ChannelCloseSemanticsEnum = int | Literal["fbp", "no"]
ChannelServer = _ChannelInterfaceModule.Server
type ComponentComponentTypeEnum = (
    int | Literal["standard", "iip", "subflow", "view", "process"]
)
type ComponentPortPortTypeEnum = int | Literal["standard", "array"]
type ConfigEntryListBuilder = _ConfigEntryList.Builder
type ConfigEntryListReader = _ConfigEntryList.Reader
FactoryServer = _ProcessInterfaceModule._FactoryInterfaceModule.Server
type IPTypeEnum = int | Literal["standard", "openBracket", "closeBracket"]
type KVListBuilder = _KVList.Builder
type KVListReader = _KVList.Reader
type NameAndSRListBuilder = _NameAndSRList.Builder
type NameAndSRListReader = _NameAndSRList.Reader
type PortListBuilder = _PortList.Builder
type PortListReader = _PortList.Reader
ProcessServer = _ProcessInterfaceModule.Server
type ProcessStateEnum = int | Literal["started", "stopped", "canceled"]
type ReaderClientListBuilder = _ReaderClientList.Builder
type ReaderClientListReader = _ReaderClientList.Reader
ReaderServer = _ChannelInterfaceModule._ReaderInterfaceModule.Server
RunnableServer = _RunnableInterfaceModule.Server
StartChannelsServiceServer = _StartChannelsServiceInterfaceModule.Server
type StartupInfoListBuilder = _StartupInfoList.Builder
type StartupInfoListReader = _StartupInfoList.Reader
StateTransitionServer = _ProcessInterfaceModule._StateTransitionInterfaceModule.Server
StatsCallbackServer = _ChannelInterfaceModule._StatsCallbackInterfaceModule.Server
StoppedCallbackServer = _RunnableInterfaceModule._StoppedCallbackInterfaceModule.Server
type SturdyRefListBuilder = _SturdyRefList.Builder
type SturdyRefListReader = _SturdyRefList.Reader
type TextListBuilder = _TextList.Builder
type TextListReader = _TextList.Reader
UnregisterServer = _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server
type WriterClientListBuilder = _WriterClientList.Builder
type WriterClientListReader = _WriterClientList.Reader
WriterServer = _ChannelInterfaceModule._WriterInterfaceModule.Server
