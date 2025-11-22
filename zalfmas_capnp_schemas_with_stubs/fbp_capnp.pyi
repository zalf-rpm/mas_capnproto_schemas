"""This is an automatically generated stub for `fbp.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
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
    _StructModule,
)

from .common_capnp import (
    IdInformationBuilder,
    IdInformationReader,
    _IdentifiableModule,
)
from .persistence_capnp import _PersistentModule
from .service_capnp import _StoppableModule

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

class _KVList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> KVReader: ...
        def __iter__(self) -> Iterator[KVReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> KVBuilder: ...
        def __setitem__(
            self, key: int, value: KVReader | KVBuilder | dict[str, Any]
        ) -> None: ...
        def __iter__(self) -> Iterator[KVBuilder]: ...
        def init(self, index: int, size: int | None = None) -> KVBuilder: ...

class _IPModule(_StructModule):
    class _KVModule(_StructModule):
        class Reader(_DynamicStructReader):
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
                allocate_seg_callable: Any = None,
            ) -> KVBuilder: ...

        class Builder(_DynamicStructBuilder):
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

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            key: str | None = None,
            desc: str | None = None,
            value: AnyPointer | None = None,
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
    class _TypeModule:
        standard: int
        openBracket: int
        closeBracket: int

    Type: _TypeModule
    class Reader(_DynamicStructReader):
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
            allocate_seg_callable: Any = None,
        ) -> IPBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def attributes(self) -> KVListBuilder: ...
        @attributes.setter
        def attributes(
            self, value: KVListBuilder | KVListReader | dict[str, Any]
        ) -> None: ...
        @property
        def content(self) -> _DynamicObjectBuilder: ...
        @content.setter
        def content(self, value: AnyPointer) -> None: ...
        @property
        def type(self) -> IPTypeEnum: ...
        @type.setter
        def type(self, value: IPTypeEnum) -> None: ...
        def init(
            self, field: Literal["attributes"], size: int | None = None
        ) -> KVListBuilder: ...
        @override
        def as_reader(self) -> IPReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        attributes: KVListBuilder | dict[str, Any] | None = None,
        content: AnyPointer | None = None,
        type: IPTypeEnum | None = None,
        **kwargs: Any,
    ) -> IPBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[IPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[IPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[IPBuilder]: ...
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
    ) -> IPReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> IPReader: ...

IP: _IPModule

class _IIPModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def content(self) -> _DynamicObjectReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> IIPBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def content(self) -> _DynamicObjectBuilder: ...
        @content.setter
        def content(self, value: AnyPointer) -> None: ...
        @override
        def as_reader(self) -> IIPReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        content: AnyPointer | None = None,
        **kwargs: Any,
    ) -> IIPBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[IIPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[IIPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[IIPBuilder]: ...
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
    ) -> IIPReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> IIPReader: ...

IIP: _IIPModule

class _ChannelModule(_IdentifiableModule, _PersistentModule):
    class _CloseSemanticsModule:
        fbp: int
        no: int

    CloseSemantics: _CloseSemanticsModule
    class _MsgModule(_StructModule):
        class Reader(_DynamicStructReader):
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
                allocate_seg_callable: Any = None,
            ) -> MsgBuilder: ...

        class Builder(_DynamicStructBuilder):
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

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            value: AnyPointer | None = None,
            done: None | None = None,
            noMsg: None | None = None,
            **kwargs: Any,
        ) -> MsgBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[MsgReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[MsgReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[MsgBuilder]: ...
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
        ) -> MsgReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> MsgReader: ...

    type MsgReader = _MsgModule.Reader
    type MsgBuilder = _MsgModule.Builder
    Msg: _MsgModule
    class _ReaderModule(_IdentifiableModule, _PersistentModule):
        class ReadRequest(Protocol):
            def send(self) -> _ChannelModule._ReaderModule.ReaderClient.ReadResult: ...

        class CloseRequest(Protocol):
            def send(self) -> _ChannelModule._ReaderModule.ReaderClient.CloseResult: ...

        class ReadifmsgRequest(Protocol):
            def send(
                self,
            ) -> _ChannelModule._ReaderModule.ReaderClient.ReadifmsgResult: ...

        def _new_client(
            self, server: _DynamicCapabilityServer
        ) -> _ChannelModule._ReaderModule.ReaderClient: ...
        class Server(_IdentifiableModule.Server, _PersistentModule.Server):
            class ReadResult(Awaitable[ReadResult], Protocol):
                value: AnyPointer
                done: None
                noMsg: None
                def which(self) -> Literal["value", "done", "noMsg"]: ...

            class CloseResult(Awaitable[None], Protocol): ...

            class ReadifmsgResult(Awaitable[ReadifmsgResult], Protocol):
                value: AnyPointer
                done: None
                noMsg: None
                def which(self) -> Literal["value", "done", "noMsg"]: ...

            class ReadResultTuple(NamedTuple):
                value: AnyPointer
                done: None
                noMsg: None

            class ReadifmsgResultTuple(NamedTuple):
                value: AnyPointer
                done: None
                noMsg: None

            class ReadParams(Protocol): ...

            class ReadCallContext(Protocol):
                params: _ChannelModule._ReaderModule.Server.ReadParams
                @property
                def results(self) -> MsgBuilder: ...

            class CloseParams(Protocol): ...

            class CloseCallContext(Protocol):
                params: _ChannelModule._ReaderModule.Server.CloseParams

            class ReadifmsgParams(Protocol): ...

            class ReadifmsgCallContext(Protocol):
                params: _ChannelModule._ReaderModule.Server.ReadifmsgParams
                @property
                def results(self) -> MsgBuilder: ...

            def read(
                self,
                _context: _ChannelModule._ReaderModule.Server.ReadCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                _ChannelModule._ReaderModule.Server.ReadResultTuple | None
            ]: ...
            def read_context(
                self, context: _ChannelModule._ReaderModule.Server.ReadCallContext
            ) -> Awaitable[None]: ...
            def close(
                self,
                _context: _ChannelModule._ReaderModule.Server.CloseCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[None]: ...
            def close_context(
                self, context: _ChannelModule._ReaderModule.Server.CloseCallContext
            ) -> Awaitable[None]: ...
            def readIfMsg(
                self,
                _context: _ChannelModule._ReaderModule.Server.ReadifmsgCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                _ChannelModule._ReaderModule.Server.ReadifmsgResultTuple | None
            ]: ...
            def readIfMsg_context(
                self, context: _ChannelModule._ReaderModule.Server.ReadifmsgCallContext
            ) -> Awaitable[None]: ...

        class ReaderClient(
            _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
        ):
            class ReadResult(Awaitable[ReadResult], Protocol):
                value: _DynamicObjectReader
                done: None
                noMsg: None
                def which(self) -> Literal["value", "done", "noMsg"]: ...

            class CloseResult(Awaitable[None], Protocol): ...

            class ReadifmsgResult(Awaitable[ReadifmsgResult], Protocol):
                value: _DynamicObjectReader
                done: None
                noMsg: None
                def which(self) -> Literal["value", "done", "noMsg"]: ...

            def read(self) -> _ChannelModule._ReaderModule.ReaderClient.ReadResult: ...
            def close(
                self,
            ) -> _ChannelModule._ReaderModule.ReaderClient.CloseResult: ...
            def readIfMsg(
                self,
            ) -> _ChannelModule._ReaderModule.ReaderClient.ReadifmsgResult: ...
            def read_request(self) -> _ChannelModule._ReaderModule.ReadRequest: ...
            def close_request(self) -> _ChannelModule._ReaderModule.CloseRequest: ...
            def readIfMsg_request(
                self,
            ) -> _ChannelModule._ReaderModule.ReadifmsgRequest: ...

    Reader: _ReaderModule
    type ReaderClient = _ChannelModule._ReaderModule.ReaderClient
    type ReaderServer = _ChannelModule._ReaderModule.Server
    class _WriterModule(_IdentifiableModule, _PersistentModule):
        class WriteRequest(Protocol):
            value: AnyPointer
            done: None
            noMsg: None
            def send(self) -> _ChannelModule._WriterModule.WriterClient.WriteResult: ...

        class CloseRequest(Protocol):
            def send(self) -> _ChannelModule._WriterModule.WriterClient.CloseResult: ...

        class WriteifspaceRequest(Protocol):
            value: AnyPointer
            done: None
            noMsg: None
            def send(
                self,
            ) -> _ChannelModule._WriterModule.WriterClient.WriteifspaceResult: ...

        def _new_client(
            self, server: _DynamicCapabilityServer
        ) -> _ChannelModule._WriterModule.WriterClient: ...
        class Server(_IdentifiableModule.Server, _PersistentModule.Server):
            class WriteResult(Awaitable[None], Protocol): ...
            class CloseResult(Awaitable[None], Protocol): ...

            class WriteifspaceResult(_DynamicStructBuilder):
                @property
                def success(self) -> bool: ...
                @success.setter
                def success(self, value: bool) -> None: ...

            class WriteifspaceResultTuple(NamedTuple):
                success: bool

            class WriteParams(Protocol):
                value: AnyPointer
                done: None
                noMsg: None

            class WriteCallContext(Protocol):
                params: _ChannelModule._WriterModule.Server.WriteParams

            class CloseParams(Protocol): ...

            class CloseCallContext(Protocol):
                params: _ChannelModule._WriterModule.Server.CloseParams

            class WriteifspaceParams(Protocol):
                value: AnyPointer
                done: None
                noMsg: None

            class WriteifspaceCallContext(Protocol):
                params: _ChannelModule._WriterModule.Server.WriteifspaceParams
                @property
                def results(
                    self,
                ) -> _ChannelModule._WriterModule.Server.WriteifspaceResult: ...

            def write(
                self,
                value: AnyPointer,
                done: None,
                noMsg: None,
                _context: _ChannelModule._WriterModule.Server.WriteCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[None]: ...
            def write_context(
                self, context: _ChannelModule._WriterModule.Server.WriteCallContext
            ) -> Awaitable[None]: ...
            def close(
                self,
                _context: _ChannelModule._WriterModule.Server.CloseCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[None]: ...
            def close_context(
                self, context: _ChannelModule._WriterModule.Server.CloseCallContext
            ) -> Awaitable[None]: ...
            def writeIfSpace(
                self,
                value: AnyPointer,
                done: None,
                noMsg: None,
                _context: _ChannelModule._WriterModule.Server.WriteifspaceCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                bool
                | _ChannelModule._WriterModule.Server.WriteifspaceResultTuple
                | None
            ]: ...
            def writeIfSpace_context(
                self,
                context: _ChannelModule._WriterModule.Server.WriteifspaceCallContext,
            ) -> Awaitable[None]: ...

        class WriterClient(
            _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
        ):
            class WriteResult(Awaitable[None], Protocol): ...
            class CloseResult(Awaitable[None], Protocol): ...

            class WriteifspaceResult(Awaitable[WriteifspaceResult], Protocol):
                success: bool

            def write(
                self,
                value: AnyPointer | None = None,
                done: None | None = None,
                noMsg: None | None = None,
            ) -> _ChannelModule._WriterModule.WriterClient.WriteResult: ...
            def close(
                self,
            ) -> _ChannelModule._WriterModule.WriterClient.CloseResult: ...
            def writeIfSpace(
                self,
                value: AnyPointer | None = None,
                done: None | None = None,
                noMsg: None | None = None,
            ) -> _ChannelModule._WriterModule.WriterClient.WriteifspaceResult: ...
            def write_request(
                self,
                value: AnyPointer | None = None,
                done: None | None = None,
                noMsg: None | None = None,
            ) -> _ChannelModule._WriterModule.WriteRequest: ...
            def close_request(self) -> _ChannelModule._WriterModule.CloseRequest: ...
            def writeIfSpace_request(
                self,
                value: AnyPointer | None = None,
                done: None | None = None,
                noMsg: None | None = None,
            ) -> _ChannelModule._WriterModule.WriteifspaceRequest: ...

    Writer: _WriterModule
    type WriterClient = _ChannelModule._WriterModule.WriterClient
    type WriterServer = _ChannelModule._WriterModule.Server
    class _StartupInfoModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def bufferSize(self) -> int: ...
            @property
            def closeSemantics(self) -> ChannelCloseSemanticsEnum: ...
            @property
            def channelSR(self) -> str: ...
            @property
            def readerSRs(self) -> TextListReader: ...
            @property
            def writerSRs(self) -> TextListReader: ...
            @property
            def channel(self) -> _ChannelModule.ChannelClient: ...
            @property
            def readers(self) -> ReaderClientListReader: ...
            @property
            def writers(self) -> WriterClientListReader: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> StartupInfoBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def bufferSize(self) -> int: ...
            @bufferSize.setter
            def bufferSize(self, value: int) -> None: ...
            @property
            def closeSemantics(self) -> ChannelCloseSemanticsEnum: ...
            @closeSemantics.setter
            def closeSemantics(self, value: ChannelCloseSemanticsEnum) -> None: ...
            @property
            def channelSR(self) -> str: ...
            @channelSR.setter
            def channelSR(self, value: str) -> None: ...
            @property
            def readerSRs(self) -> TextListBuilder: ...
            @readerSRs.setter
            def readerSRs(
                self, value: TextListBuilder | TextListReader | dict[str, Any]
            ) -> None: ...
            @property
            def writerSRs(self) -> TextListBuilder: ...
            @writerSRs.setter
            def writerSRs(
                self, value: TextListBuilder | TextListReader | dict[str, Any]
            ) -> None: ...
            @property
            def channel(self) -> _ChannelModule.ChannelClient: ...
            @channel.setter
            def channel(
                self, value: _ChannelModule.ChannelClient | _ChannelModule.Server
            ) -> None: ...
            @property
            def readers(self) -> ReaderClientListBuilder: ...
            @readers.setter
            def readers(
                self,
                value: ReaderClientListBuilder
                | ReaderClientListReader
                | dict[str, Any],
            ) -> None: ...
            @property
            def writers(self) -> WriterClientListBuilder: ...
            @writers.setter
            def writers(
                self,
                value: WriterClientListBuilder
                | WriterClientListReader
                | dict[str, Any],
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["readerSRs"], size: int | None = None
            ) -> TextListBuilder: ...
            @overload
            def init(
                self, field: Literal["writerSRs"], size: int | None = None
            ) -> TextListBuilder: ...
            @overload
            def init(
                self, field: Literal["readers"], size: int | None = None
            ) -> ReaderClientListBuilder: ...
            @overload
            def init(
                self, field: Literal["writers"], size: int | None = None
            ) -> WriterClientListBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> StartupInfoReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            bufferSize: int | None = None,
            closeSemantics: ChannelCloseSemanticsEnum | None = None,
            channelSR: str | None = None,
            readerSRs: TextListBuilder | dict[str, Any] | None = None,
            writerSRs: TextListBuilder | dict[str, Any] | None = None,
            channel: _ChannelModule.ChannelClient | _ChannelModule.Server | None = None,
            readers: ReaderClientListBuilder | dict[str, Any] | None = None,
            writers: WriterClientListBuilder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> StartupInfoBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[StartupInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[StartupInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[StartupInfoBuilder]: ...
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
        ) -> StartupInfoReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> StartupInfoReader: ...

    type StartupInfoReader = _StartupInfoModule.Reader
    type StartupInfoBuilder = _StartupInfoModule.Builder
    StartupInfo: _StartupInfoModule
    class SetbuffersizeRequest(Protocol):
        size: int
        def send(self) -> _ChannelModule.ChannelClient.SetbuffersizeResult: ...

    class ReaderRequest(Protocol):
        def send(self) -> _ChannelModule.ChannelClient.ReaderResult: ...

    class WriterRequest(Protocol):
        def send(self) -> _ChannelModule.ChannelClient.WriterResult: ...

    class EndpointsRequest(Protocol):
        def send(self) -> _ChannelModule.ChannelClient.EndpointsResult: ...

    class SetautoclosesemanticsRequest(Protocol):
        cs: ChannelCloseSemanticsEnum
        def send(self) -> _ChannelModule.ChannelClient.SetautoclosesemanticsResult: ...

    class CloseRequest(Protocol):
        waitForEmptyBuffer: bool
        def send(self) -> _ChannelModule.ChannelClient.CloseResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _ChannelModule.ChannelClient: ...
    class Server(_IdentifiableModule.Server, _PersistentModule.Server):
        class SetbuffersizeResult(Awaitable[None], Protocol): ...

        class ReaderResult(_DynamicStructBuilder):
            @property
            def r(
                self,
            ) -> (
                _ChannelModule._ReaderModule.Server
                | _ChannelModule._ReaderModule.ReaderClient
            ): ...
            @r.setter
            def r(
                self,
                value: _ChannelModule._ReaderModule.Server
                | _ChannelModule._ReaderModule.ReaderClient,
            ) -> None: ...

        class WriterResult(_DynamicStructBuilder):
            @property
            def w(
                self,
            ) -> (
                _ChannelModule._WriterModule.Server
                | _ChannelModule._WriterModule.WriterClient
            ): ...
            @w.setter
            def w(
                self,
                value: _ChannelModule._WriterModule.Server
                | _ChannelModule._WriterModule.WriterClient,
            ) -> None: ...

        class EndpointsResult(_DynamicStructBuilder):
            @property
            def r(
                self,
            ) -> (
                _ChannelModule._ReaderModule.Server
                | _ChannelModule._ReaderModule.ReaderClient
            ): ...
            @r.setter
            def r(
                self,
                value: _ChannelModule._ReaderModule.Server
                | _ChannelModule._ReaderModule.ReaderClient,
            ) -> None: ...
            @property
            def w(
                self,
            ) -> (
                _ChannelModule._WriterModule.Server
                | _ChannelModule._WriterModule.WriterClient
            ): ...
            @w.setter
            def w(
                self,
                value: _ChannelModule._WriterModule.Server
                | _ChannelModule._WriterModule.WriterClient,
            ) -> None: ...

        class SetautoclosesemanticsResult(Awaitable[None], Protocol): ...
        class CloseResult(Awaitable[None], Protocol): ...

        class ReaderResultTuple(NamedTuple):
            r: (
                _ChannelModule._ReaderModule.Server
                | _ChannelModule._ReaderModule.ReaderClient
            )

        class WriterResultTuple(NamedTuple):
            w: (
                _ChannelModule._WriterModule.Server
                | _ChannelModule._WriterModule.WriterClient
            )

        class EndpointsResultTuple(NamedTuple):
            r: (
                _ChannelModule._ReaderModule.Server
                | _ChannelModule._ReaderModule.ReaderClient
            )
            w: (
                _ChannelModule._WriterModule.Server
                | _ChannelModule._WriterModule.WriterClient
            )

        class SetbuffersizeParams(Protocol):
            size: int

        class SetbuffersizeCallContext(Protocol):
            params: _ChannelModule.Server.SetbuffersizeParams

        class ReaderParams(Protocol): ...

        class ReaderCallContext(Protocol):
            params: _ChannelModule.Server.ReaderParams
            @property
            def results(self) -> _ChannelModule.Server.ReaderResult: ...

        class WriterParams(Protocol): ...

        class WriterCallContext(Protocol):
            params: _ChannelModule.Server.WriterParams
            @property
            def results(self) -> _ChannelModule.Server.WriterResult: ...

        class EndpointsParams(Protocol): ...

        class EndpointsCallContext(Protocol):
            params: _ChannelModule.Server.EndpointsParams
            @property
            def results(self) -> _ChannelModule.Server.EndpointsResult: ...

        class SetautoclosesemanticsParams(Protocol):
            cs: ChannelCloseSemanticsEnum

        class SetautoclosesemanticsCallContext(Protocol):
            params: _ChannelModule.Server.SetautoclosesemanticsParams

        class CloseParams(Protocol):
            waitForEmptyBuffer: bool

        class CloseCallContext(Protocol):
            params: _ChannelModule.Server.CloseParams

        def setBufferSize(
            self,
            size: int,
            _context: _ChannelModule.Server.SetbuffersizeCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[None]: ...
        def setBufferSize_context(
            self, context: _ChannelModule.Server.SetbuffersizeCallContext
        ) -> Awaitable[None]: ...
        def reader(
            self,
            _context: _ChannelModule.Server.ReaderCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _ChannelModule._ReaderModule.Server
            | _ChannelModule.Server.ReaderResultTuple
            | None
        ]: ...
        def reader_context(
            self, context: _ChannelModule.Server.ReaderCallContext
        ) -> Awaitable[None]: ...
        def writer(
            self,
            _context: _ChannelModule.Server.WriterCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[
            _ChannelModule._WriterModule.Server
            | _ChannelModule.Server.WriterResultTuple
            | None
        ]: ...
        def writer_context(
            self, context: _ChannelModule.Server.WriterCallContext
        ) -> Awaitable[None]: ...
        def endpoints(
            self,
            _context: _ChannelModule.Server.EndpointsCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_ChannelModule.Server.EndpointsResultTuple | None]: ...
        def endpoints_context(
            self, context: _ChannelModule.Server.EndpointsCallContext
        ) -> Awaitable[None]: ...
        def setAutoCloseSemantics(
            self,
            cs: ChannelCloseSemanticsEnum,
            _context: _ChannelModule.Server.SetautoclosesemanticsCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[None]: ...
        def setAutoCloseSemantics_context(
            self, context: _ChannelModule.Server.SetautoclosesemanticsCallContext
        ) -> Awaitable[None]: ...
        def close(
            self,
            waitForEmptyBuffer: bool,
            _context: _ChannelModule.Server.CloseCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[None]: ...
        def close_context(
            self, context: _ChannelModule.Server.CloseCallContext
        ) -> Awaitable[None]: ...

    class ChannelClient(
        _IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient
    ):
        class SetbuffersizeResult(Awaitable[None], Protocol): ...

        class ReaderResult(Awaitable[ReaderResult], Protocol):
            r: _ChannelModule._ReaderModule.ReaderClient

        class WriterResult(Awaitable[WriterResult], Protocol):
            w: _ChannelModule._WriterModule.WriterClient

        class EndpointsResult(Awaitable[EndpointsResult], Protocol):
            r: _ChannelModule._ReaderModule.ReaderClient
            w: _ChannelModule._WriterModule.WriterClient

        class SetautoclosesemanticsResult(Awaitable[None], Protocol): ...
        class CloseResult(Awaitable[None], Protocol): ...

        def setBufferSize(
            self, size: int | None = None
        ) -> _ChannelModule.ChannelClient.SetbuffersizeResult: ...
        def reader(self) -> _ChannelModule.ChannelClient.ReaderResult: ...
        def writer(self) -> _ChannelModule.ChannelClient.WriterResult: ...
        def endpoints(self) -> _ChannelModule.ChannelClient.EndpointsResult: ...
        def setAutoCloseSemantics(
            self, cs: ChannelCloseSemanticsEnum | None = None
        ) -> _ChannelModule.ChannelClient.SetautoclosesemanticsResult: ...
        def close(
            self, waitForEmptyBuffer: bool | None = None
        ) -> _ChannelModule.ChannelClient.CloseResult: ...
        def setBufferSize_request(
            self, size: int | None = None
        ) -> _ChannelModule.SetbuffersizeRequest: ...
        def reader_request(self) -> _ChannelModule.ReaderRequest: ...
        def writer_request(self) -> _ChannelModule.WriterRequest: ...
        def endpoints_request(self) -> _ChannelModule.EndpointsRequest: ...
        def setAutoCloseSemantics_request(
            self, cs: ChannelCloseSemanticsEnum | None = None
        ) -> _ChannelModule.SetautoclosesemanticsRequest: ...
        def close_request(
            self, waitForEmptyBuffer: bool | None = None
        ) -> _ChannelModule.CloseRequest: ...

class _TextList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> str: ...
        def __iter__(self) -> Iterator[str]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> str: ...
        def __setitem__(self, key: int, value: str) -> None: ...
        def __iter__(self) -> Iterator[str]: ...

class _ReaderClientList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> ReaderClient: ...
        def __iter__(self) -> Iterator[ReaderClient]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> ReaderClient: ...
        def __setitem__(
            self, key: int, value: ReaderClient | _ChannelModule._ReaderModule.Server
        ) -> None: ...
        def __iter__(self) -> Iterator[ReaderClient]: ...

class _WriterClientList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> WriterClient: ...
        def __iter__(self) -> Iterator[WriterClient]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> WriterClient: ...
        def __setitem__(
            self, key: int, value: WriterClient | _ChannelModule._WriterModule.Server
        ) -> None: ...
        def __iter__(self) -> Iterator[WriterClient]: ...

Channel: _ChannelModule

class _StartChannelsServiceModule(_IdentifiableModule):
    class _ParamsModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
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
                allocate_seg_callable: Any = None,
            ) -> ParamsBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @name.setter
            def name(self, value: str) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
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
                self, value: TextListBuilder | TextListReader | dict[str, Any]
            ) -> None: ...
            @property
            def writerSrts(self) -> TextListBuilder: ...
            @writerSrts.setter
            def writerSrts(
                self, value: TextListBuilder | TextListReader | dict[str, Any]
            ) -> None: ...
            @property
            def bufferSize(self) -> int: ...
            @bufferSize.setter
            def bufferSize(self, value: int) -> None: ...
            @overload
            def init(
                self, field: Literal["readerSrts"], size: int | None = None
            ) -> TextListBuilder: ...
            @overload
            def init(
                self, field: Literal["writerSrts"], size: int | None = None
            ) -> TextListBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> ParamsReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            name: str | None = None,
            noOfChannels: int | None = None,
            noOfReaders: int | None = None,
            noOfWriters: int | None = None,
            readerSrts: TextListBuilder | dict[str, Any] | None = None,
            writerSrts: TextListBuilder | dict[str, Any] | None = None,
            bufferSize: int | None = None,
            **kwargs: Any,
        ) -> ParamsBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[ParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[ParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[ParamsBuilder]: ...
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
        ) -> ParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> ParamsReader: ...

    type ParamsReader = _ParamsModule.Reader
    type ParamsBuilder = _ParamsModule.Builder
    Params: _ParamsModule
    class StartRequest(Protocol):
        name: str
        noOfChannels: int
        noOfReaders: int
        noOfWriters: int
        readerSrts: TextListBuilder | TextListReader | Sequence[Any]
        writerSrts: TextListBuilder | TextListReader | Sequence[Any]
        bufferSize: int
        @overload
        def init(
            self, name: Literal["readerSrts"], size: int = ...
        ) -> TextListBuilder: ...
        @overload
        def init(
            self, name: Literal["writerSrts"], size: int = ...
        ) -> TextListBuilder: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(
            self,
        ) -> _StartChannelsServiceModule.StartChannelsServiceClient.StartResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _StartChannelsServiceModule.StartChannelsServiceClient: ...
    class Server(_IdentifiableModule.Server):
        class StartResult(_DynamicStructBuilder):
            @property
            def startupInfos(self) -> StartupInfoListBuilder: ...
            @startupInfos.setter
            def startupInfos(
                self,
                value: StartupInfoListBuilder | StartupInfoListReader | Sequence[Any],
            ) -> None: ...
            @property
            def stop(
                self,
            ) -> _StoppableModule.Server | _StoppableModule.StoppableClient: ...
            @stop.setter
            def stop(
                self, value: _StoppableModule.Server | _StoppableModule.StoppableClient
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["startupInfos"], size: int | None = None
            ) -> StartupInfoListBuilder: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...

        class StartResultTuple(NamedTuple):
            startupInfos: StartupInfoListBuilder | StartupInfoListReader
            stop: _StoppableModule.Server | _StoppableModule.StoppableClient

        class StartParams(Protocol):
            name: str
            noOfChannels: int
            noOfReaders: int
            noOfWriters: int
            readerSrts: TextListReader
            writerSrts: TextListReader
            bufferSize: int

        class StartCallContext(Protocol):
            params: _StartChannelsServiceModule.Server.StartParams
            @property
            def results(self) -> _StartChannelsServiceModule.Server.StartResult: ...

        def start(
            self,
            name: str,
            noOfChannels: int,
            noOfReaders: int,
            noOfWriters: int,
            readerSrts: TextListReader,
            writerSrts: TextListReader,
            bufferSize: int,
            _context: _StartChannelsServiceModule.Server.StartCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_StartChannelsServiceModule.Server.StartResultTuple | None]: ...
        def start_context(
            self, context: _StartChannelsServiceModule.Server.StartCallContext
        ) -> Awaitable[None]: ...

    class StartChannelsServiceClient(_IdentifiableModule.IdentifiableClient):
        class StartResult(Awaitable[StartResult], Protocol):
            startupInfos: StartupInfoListReader
            stop: _StoppableModule.StoppableClient

        def start(
            self,
            name: str | None = None,
            noOfChannels: int | None = None,
            noOfReaders: int | None = None,
            noOfWriters: int | None = None,
            readerSrts: TextListBuilder | TextListReader | Sequence[Any] | None = None,
            writerSrts: TextListBuilder | TextListReader | Sequence[Any] | None = None,
            bufferSize: int | None = None,
        ) -> _StartChannelsServiceModule.StartChannelsServiceClient.StartResult: ...
        def start_request(
            self,
            name: str | None = None,
            noOfChannels: int | None = None,
            noOfReaders: int | None = None,
            noOfWriters: int | None = None,
            readerSrts: TextListBuilder | TextListReader | Sequence[Any] | None = None,
            writerSrts: TextListBuilder | TextListReader | Sequence[Any] | None = None,
            bufferSize: int | None = None,
        ) -> _StartChannelsServiceModule.StartRequest: ...

class _StartupInfoList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> StartupInfoReader: ...
        def __iter__(self) -> Iterator[StartupInfoReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> StartupInfoBuilder: ...
        def __setitem__(
            self,
            key: int,
            value: StartupInfoReader | StartupInfoBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[StartupInfoBuilder]: ...
        def init(self, index: int, size: int | None = None) -> StartupInfoBuilder: ...

StartChannelsService: _StartChannelsServiceModule

class _NameAndSRList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> NameAndSRReader: ...
        def __iter__(self) -> Iterator[NameAndSRReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> NameAndSRBuilder: ...
        def __setitem__(
            self, key: int, value: NameAndSRReader | NameAndSRBuilder | dict[str, Any]
        ) -> None: ...
        def __iter__(self) -> Iterator[NameAndSRBuilder]: ...
        def init(self, index: int, size: int | None = None) -> NameAndSRBuilder: ...

class _PortInfosModule(_StructModule):
    class _NameAndSRModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @property
            def sr(self) -> str: ...
            @property
            def srs(self) -> TextListReader: ...
            @override
            def which(self) -> Literal["sr", "srs"]: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> NameAndSRBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @name.setter
            def name(self, value: str) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @property
            def sr(self) -> str: ...
            @sr.setter
            def sr(self, value: str) -> None: ...
            @property
            def srs(self) -> TextListBuilder: ...
            @srs.setter
            def srs(
                self, value: TextListBuilder | TextListReader | dict[str, Any]
            ) -> None: ...
            @override
            def which(self) -> Literal["sr", "srs"]: ...
            def init(
                self, field: Literal["srs"], size: int | None = None
            ) -> TextListBuilder: ...
            @override
            def as_reader(self) -> NameAndSRReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            name: str | None = None,
            sr: str | None = None,
            srs: TextListBuilder | dict[str, Any] | None = None,
            **kwargs: Any,
        ) -> NameAndSRBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[NameAndSRReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[NameAndSRReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[NameAndSRBuilder]: ...
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
        ) -> NameAndSRReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> NameAndSRReader: ...

    type NameAndSRReader = _NameAndSRModule.Reader
    type NameAndSRBuilder = _NameAndSRModule.Builder
    NameAndSR: _NameAndSRModule
    class Reader(_DynamicStructReader):
        @property
        def inPorts(self) -> NameAndSRListReader: ...
        @property
        def outPorts(self) -> NameAndSRListReader: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> PortInfosBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def inPorts(self) -> NameAndSRListBuilder: ...
        @inPorts.setter
        def inPorts(
            self, value: NameAndSRListBuilder | NameAndSRListReader | dict[str, Any]
        ) -> None: ...
        @property
        def outPorts(self) -> NameAndSRListBuilder: ...
        @outPorts.setter
        def outPorts(
            self, value: NameAndSRListBuilder | NameAndSRListReader | dict[str, Any]
        ) -> None: ...
        @overload
        def init(
            self, field: Literal["inPorts"], size: int | None = None
        ) -> NameAndSRListBuilder: ...
        @overload
        def init(
            self, field: Literal["outPorts"], size: int | None = None
        ) -> NameAndSRListBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> PortInfosReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        inPorts: NameAndSRListBuilder | dict[str, Any] | None = None,
        outPorts: NameAndSRListBuilder | dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> PortInfosBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[PortInfosReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[PortInfosReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[PortInfosBuilder]: ...
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
    ) -> PortInfosReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> PortInfosReader: ...

PortInfos: _PortInfosModule

class _PortList:
    class Reader(_DynamicListReader):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> PortReader: ...
        def __iter__(self) -> Iterator[PortReader]: ...

    class Builder(_DynamicListBuilder):
        def __len__(self) -> int: ...
        def __getitem__(self, key: int) -> PortBuilder: ...
        def __setitem__(
            self, key: int, value: PortReader | PortBuilder | dict[str, Any]
        ) -> None: ...
        def __iter__(self) -> Iterator[PortBuilder]: ...
        def init(self, index: int, size: int | None = None) -> PortBuilder: ...

class _ComponentModule(_StructModule):
    class _RunnableModule(_IdentifiableModule):
        class StartRequest(Protocol):
            portInfosReaderSr: str
            name: str
            def send(
                self,
            ) -> _ComponentModule._RunnableModule.RunnableClient.StartResult: ...

        class StopRequest(Protocol):
            def send(
                self,
            ) -> _ComponentModule._RunnableModule.RunnableClient.StopResult: ...

        def _new_client(
            self, server: _DynamicCapabilityServer
        ) -> _ComponentModule._RunnableModule.RunnableClient: ...
        class Server(_IdentifiableModule.Server):
            class StartResult(_DynamicStructBuilder):
                @property
                def success(self) -> bool: ...
                @success.setter
                def success(self, value: bool) -> None: ...

            class StopResult(_DynamicStructBuilder):
                @property
                def success(self) -> bool: ...
                @success.setter
                def success(self, value: bool) -> None: ...

            class StartResultTuple(NamedTuple):
                success: bool

            class StopResultTuple(NamedTuple):
                success: bool

            class StartParams(Protocol):
                portInfosReaderSr: str
                name: str

            class StartCallContext(Protocol):
                params: _ComponentModule._RunnableModule.Server.StartParams
                @property
                def results(
                    self,
                ) -> _ComponentModule._RunnableModule.Server.StartResult: ...

            class StopParams(Protocol): ...

            class StopCallContext(Protocol):
                params: _ComponentModule._RunnableModule.Server.StopParams
                @property
                def results(
                    self,
                ) -> _ComponentModule._RunnableModule.Server.StopResult: ...

            def start(
                self,
                portInfosReaderSr: str,
                name: str,
                _context: _ComponentModule._RunnableModule.Server.StartCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                bool | _ComponentModule._RunnableModule.Server.StartResultTuple | None
            ]: ...
            def start_context(
                self, context: _ComponentModule._RunnableModule.Server.StartCallContext
            ) -> Awaitable[None]: ...
            def stop(
                self,
                _context: _ComponentModule._RunnableModule.Server.StopCallContext,
                **kwargs: dict[str, Any],
            ) -> Awaitable[
                bool | _ComponentModule._RunnableModule.Server.StopResultTuple | None
            ]: ...
            def stop_context(
                self, context: _ComponentModule._RunnableModule.Server.StopCallContext
            ) -> Awaitable[None]: ...

        class RunnableClient(_IdentifiableModule.IdentifiableClient):
            class StartResult(Awaitable[StartResult], Protocol):
                success: bool

            class StopResult(Awaitable[StopResult], Protocol):
                success: bool

            def start(
                self, portInfosReaderSr: str | None = None, name: str | None = None
            ) -> _ComponentModule._RunnableModule.RunnableClient.StartResult: ...
            def stop(
                self,
            ) -> _ComponentModule._RunnableModule.RunnableClient.StopResult: ...
            def start_request(
                self, portInfosReaderSr: str | None = None, name: str | None = None
            ) -> _ComponentModule._RunnableModule.StartRequest: ...
            def stop_request(self) -> _ComponentModule._RunnableModule.StopRequest: ...

    Runnable: _RunnableModule
    type RunnableClient = _ComponentModule._RunnableModule.RunnableClient
    type RunnableServer = _ComponentModule._RunnableModule.Server
    class _ComponentTypeModule:
        standard: int
        iip: int
        subflow: int
        view: int

    ComponentType: _ComponentTypeModule
    class _PortModule(_StructModule):
        class _PortTypeModule:
            standard: int

        PortType: _PortTypeModule
        class _ContentTypeModule:
            structuredText: int

        ContentType: _ContentTypeModule
        class Reader(_DynamicStructReader):
            @property
            def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @property
            def contentType(self) -> str: ...
            @property
            def type(self) -> ComponentPortPortTypeEnum: ...
            @override
            def as_builder(
                self,
                num_first_segment_words: int | None = None,
                allocate_seg_callable: Any = None,
            ) -> PortBuilder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @name.setter
            def name(self, value: str) -> None: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @property
            def contentType(self) -> str: ...
            @contentType.setter
            def contentType(self, value: str) -> None: ...
            @property
            def type(self) -> ComponentPortPortTypeEnum: ...
            @type.setter
            def type(self, value: ComponentPortPortTypeEnum) -> None: ...
            @override
            def as_reader(self) -> PortReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            name: str | None = None,
            contentType: str | None = None,
            type: ComponentPortPortTypeEnum | None = None,
            **kwargs: Any,
        ) -> PortBuilder: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> AbstractContextManager[PortReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[PortReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[PortBuilder]: ...
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
        ) -> PortReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> PortReader: ...

    type PortReader = _PortModule.Reader
    type PortBuilder = _PortModule.Builder
    Port: _PortModule
    class Reader(_DynamicStructReader):
        @property
        def info(self) -> IdInformationReader: ...
        @property
        def type(self) -> ComponentComponentTypeEnum: ...
        @property
        def inPorts(self) -> PortListReader: ...
        @property
        def outPorts(self) -> PortListReader: ...
        @property
        def run(self) -> _ComponentModule._RunnableModule.RunnableClient: ...
        @property
        def defaultConfig(self) -> str: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> ComponentBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def info(self) -> IdInformationBuilder: ...
        @info.setter
        def info(
            self, value: IdInformationBuilder | IdInformationReader | dict[str, Any]
        ) -> None: ...
        @property
        def type(self) -> ComponentComponentTypeEnum: ...
        @type.setter
        def type(self, value: ComponentComponentTypeEnum) -> None: ...
        @property
        def inPorts(self) -> PortListBuilder: ...
        @inPorts.setter
        def inPorts(
            self, value: PortListBuilder | PortListReader | dict[str, Any]
        ) -> None: ...
        @property
        def outPorts(self) -> PortListBuilder: ...
        @outPorts.setter
        def outPorts(
            self, value: PortListBuilder | PortListReader | dict[str, Any]
        ) -> None: ...
        @property
        def run(self) -> _ComponentModule._RunnableModule.RunnableClient: ...
        @run.setter
        def run(
            self,
            value: _ComponentModule._RunnableModule.RunnableClient
            | _ComponentModule._RunnableModule.Server,
        ) -> None: ...
        @property
        def defaultConfig(self) -> str: ...
        @defaultConfig.setter
        def defaultConfig(self, value: str) -> None: ...
        @overload
        def init(
            self, field: Literal["info"], size: int | None = None
        ) -> IdInformationBuilder: ...
        @overload
        def init(
            self, field: Literal["inPorts"], size: int | None = None
        ) -> PortListBuilder: ...
        @overload
        def init(
            self, field: Literal["outPorts"], size: int | None = None
        ) -> PortListBuilder: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> ComponentReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        info: IdInformationBuilder | dict[str, Any] | None = None,
        type: ComponentComponentTypeEnum | None = None,
        inPorts: PortListBuilder | dict[str, Any] | None = None,
        outPorts: PortListBuilder | dict[str, Any] | None = None,
        run: _ComponentModule._RunnableModule.RunnableClient
        | _ComponentModule._RunnableModule.Server
        | None = None,
        defaultConfig: str | None = None,
        **kwargs: Any,
    ) -> ComponentBuilder: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> AbstractContextManager[ComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[ComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[ComponentBuilder]: ...
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
    ) -> ComponentReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> ComponentReader: ...

Component: _ComponentModule

# Top-level type aliases for use in type annotations
type ChannelClient = _ChannelModule.ChannelClient
type ChannelCloseSemanticsEnum = int | Literal["fbp", "no"]
type ChannelServer = _ChannelModule.Server
type CloseResult = _ChannelModule.ChannelClient.CloseResult
type ComponentBuilder = _ComponentModule.Builder
type ComponentComponentTypeEnum = int | Literal["standard", "iip", "subflow", "view"]
type ComponentPortContentTypeEnum = int | Literal["structuredText"]
type ComponentPortPortTypeEnum = int | Literal["standard"]
type ComponentReader = _ComponentModule.Reader
type EndpointsResult = _ChannelModule.ChannelClient.EndpointsResult
type IIPBuilder = _IIPModule.Builder
type IIPReader = _IIPModule.Reader
type IPBuilder = _IPModule.Builder
type IPReader = _IPModule.Reader
type IPTypeEnum = int | Literal["standard", "openBracket", "closeBracket"]
type KVBuilder = _IPModule._KVModule.Builder
type KVListBuilder = _KVList.Builder
type KVListReader = _KVList.Reader
type KVReader = _IPModule._KVModule.Reader
type MsgBuilder = _ChannelModule._MsgModule.Builder
type MsgReader = _ChannelModule._MsgModule.Reader
type NameAndSRBuilder = _PortInfosModule._NameAndSRModule.Builder
type NameAndSRListBuilder = _NameAndSRList.Builder
type NameAndSRListReader = _NameAndSRList.Reader
type NameAndSRReader = _PortInfosModule._NameAndSRModule.Reader
type ParamsBuilder = _StartChannelsServiceModule._ParamsModule.Builder
type ParamsReader = _StartChannelsServiceModule._ParamsModule.Reader
type PortBuilder = _ComponentModule._PortModule.Builder
type PortInfosBuilder = _PortInfosModule.Builder
type PortInfosReader = _PortInfosModule.Reader
type PortListBuilder = _PortList.Builder
type PortListReader = _PortList.Reader
type PortReader = _ComponentModule._PortModule.Reader
type ReadResult = _ChannelModule._ReaderModule.ReaderClient.ReadResult
type ReaderClient = _ChannelModule._ReaderModule.ReaderClient
type ReaderClientListBuilder = _ReaderClientList.Builder
type ReaderClientListReader = _ReaderClientList.Reader
type ReaderResult = _ChannelModule.ChannelClient.ReaderResult
type ReaderServer = _ChannelModule._ReaderModule.Server
type ReadifmsgResult = _ChannelModule._ReaderModule.ReaderClient.ReadifmsgResult
type RunnableClient = _ComponentModule._RunnableModule.RunnableClient
type RunnableServer = _ComponentModule._RunnableModule.Server
type SetautoclosesemanticsResult = (
    _ChannelModule.ChannelClient.SetautoclosesemanticsResult
)
type SetbuffersizeResult = _ChannelModule.ChannelClient.SetbuffersizeResult
type StartChannelsServiceClient = _StartChannelsServiceModule.StartChannelsServiceClient
type StartChannelsServiceServer = _StartChannelsServiceModule.Server
type StartResult = _ComponentModule._RunnableModule.RunnableClient.StartResult
type StartupInfoBuilder = _ChannelModule._StartupInfoModule.Builder
type StartupInfoListBuilder = _StartupInfoList.Builder
type StartupInfoListReader = _StartupInfoList.Reader
type StartupInfoReader = _ChannelModule._StartupInfoModule.Reader
type StopResult = _ComponentModule._RunnableModule.RunnableClient.StopResult
type TextListBuilder = _TextList.Builder
type TextListReader = _TextList.Reader
type WriteResult = _ChannelModule._WriterModule.WriterClient.WriteResult
type WriteifspaceResult = _ChannelModule._WriterModule.WriterClient.WriteifspaceResult
type WriterClient = _ChannelModule._WriterModule.WriterClient
type WriterClientListBuilder = _WriterClientList.Builder
type WriterClientListReader = _WriterClientList.Reader
type WriterResult = _ChannelModule.ChannelClient.WriterResult
type WriterServer = _ChannelModule._WriterModule.Server
