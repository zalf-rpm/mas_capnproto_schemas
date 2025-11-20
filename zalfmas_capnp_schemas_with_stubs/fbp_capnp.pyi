"""This is an automatically generated stub for `fbp.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, MutableSequence, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, NamedTuple, Protocol, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModule,
)

from .common_capnp import (
    _IdentifiableModule,
    _IdInformationModule,
)
from .persistence_capnp import _PersistentModule

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = (
    str
    | bytes
    | _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicCapabilityClient
    | _DynamicCapabilityServer
)

class _IPModule(_StructModule):
    class _KVModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def key(self) -> str: ...
            @property
            def desc(self) -> str: ...
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
            def desc(self) -> str: ...
            @desc.setter
            def desc(self, value: str) -> None: ...
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
            desc: str | None = None,
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
    class _TypeModule:
        standard: int
        openBracket: int
        closeBracket: int

    Type: _TypeModule
    class Reader(_DynamicStructReader):
        @property
        def attributes(self) -> Sequence[KVReader]: ...
        @property
        def content(self) -> Any: ...
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
        def attributes(self) -> MutableSequence[KVBuilder]: ...
        @attributes.setter
        def attributes(
            self, value: Sequence[KVBuilder | KVReader] | Sequence[dict[str, Any]]
        ) -> None: ...
        @property
        def content(self) -> Any: ...
        @content.setter
        def content(self, value: Any) -> None: ...
        @property
        def type(self) -> IPTypeEnum: ...
        @type.setter
        def type(self, value: IPTypeEnum) -> None: ...
        def init(
            self, field: Literal["attributes"], size: int | None = None
        ) -> MutableSequence[KVBuilder]: ...
        @override
        def as_reader(self) -> IPReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        attributes: Sequence[KVBuilder] | Sequence[dict[str, Any]] | None = None,
        content: Any | None = None,
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
        def content(self) -> Any: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> IIPBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def content(self) -> Any: ...
        @content.setter
        def content(self, value: Any) -> None: ...
        @override
        def as_reader(self) -> IIPReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        content: Any | None = None,
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
                results: _ChannelModule._ReaderModule.Server.ReadResult

            class CloseParams(Protocol): ...

            class CloseCallContext(Protocol):
                params: _ChannelModule._ReaderModule.Server.CloseParams

            class ReadifmsgParams(Protocol): ...

            class ReadifmsgCallContext(Protocol):
                params: _ChannelModule._ReaderModule.Server.ReadifmsgParams
                results: _ChannelModule._ReaderModule.Server.ReadifmsgResult

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

            class WriteifspaceResult(Awaitable[WriteifspaceResult], Protocol):
                success: bool

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
                results: _ChannelModule._WriterModule.Server.WriteifspaceResult

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
                value: _DynamicObjectReader | None = None,
                done: None | None = None,
                noMsg: None | None = None,
            ) -> _ChannelModule._WriterModule.WriterClient.WriteResult: ...
            def close(
                self,
            ) -> _ChannelModule._WriterModule.WriterClient.CloseResult: ...
            def writeIfSpace(
                self,
                value: _DynamicObjectReader | None = None,
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
    class _StartupInfoModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def bufferSize(self) -> int: ...
            @property
            def closeSemantics(self) -> ChannelCloseSemanticsEnum: ...
            @property
            def channelSR(self) -> str: ...
            @property
            def readerSRs(self) -> Sequence[str]: ...
            @property
            def writerSRs(self) -> Sequence[str]: ...
            @property
            def channel(self) -> _ChannelModule.ChannelClient: ...
            @property
            def readers(self) -> Sequence[_ChannelModule._ReaderModule]: ...
            @property
            def writers(self) -> Sequence[_ChannelModule._WriterModule]: ...
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
            def readerSRs(self) -> MutableSequence[str]: ...
            @readerSRs.setter
            def readerSRs(self, value: Sequence[str]) -> None: ...
            @property
            def writerSRs(self) -> MutableSequence[str]: ...
            @writerSRs.setter
            def writerSRs(self, value: Sequence[str]) -> None: ...
            @property
            def channel(self) -> _ChannelModule.ChannelClient: ...
            @channel.setter
            def channel(
                self, value: _ChannelModule.ChannelClient | _ChannelModule.Server
            ) -> None: ...
            @property
            def readers(self) -> MutableSequence[_ChannelModule._ReaderModule]: ...
            @readers.setter
            def readers(
                self, value: Sequence[_ChannelModule._ReaderModule]
            ) -> None: ...
            @property
            def writers(self) -> MutableSequence[_ChannelModule._WriterModule]: ...
            @writers.setter
            def writers(
                self, value: Sequence[_ChannelModule._WriterModule]
            ) -> None: ...
            @overload
            def init(
                self, field: Literal["readerSRs"], size: int | None = None
            ) -> MutableSequence[str]: ...
            @overload
            def init(
                self, field: Literal["writerSRs"], size: int | None = None
            ) -> MutableSequence[str]: ...
            @overload
            def init(
                self, field: Literal["readers"], size: int | None = None
            ) -> MutableSequence[_ChannelModule._ReaderModule]: ...
            @overload
            def init(
                self, field: Literal["writers"], size: int | None = None
            ) -> MutableSequence[_ChannelModule._WriterModule]: ...
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
            readerSRs: Sequence[str] | None = None,
            writerSRs: Sequence[str] | None = None,
            channel: _ChannelModule.ChannelClient | _ChannelModule.Server | None = None,
            readers: Sequence[_ChannelModule._ReaderModule] | None = None,
            writers: Sequence[_ChannelModule._WriterModule] | None = None,
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

        class ReaderResult(Awaitable[ReaderResult], Protocol):
            r: _ChannelModule._ReaderModule.ReaderClient

        class WriterResult(Awaitable[WriterResult], Protocol):
            w: _ChannelModule._WriterModule.WriterClient

        class EndpointsResult(Awaitable[EndpointsResult], Protocol):
            r: _ChannelModule._ReaderModule.ReaderClient
            w: _ChannelModule._WriterModule.WriterClient

        class SetautoclosesemanticsResult(Awaitable[None], Protocol): ...
        class CloseResult(Awaitable[None], Protocol): ...

        class ReaderResultTuple(NamedTuple):
            r: _ChannelModule._ReaderModule.Server

        class WriterResultTuple(NamedTuple):
            w: _ChannelModule._WriterModule.Server

        class EndpointsResultTuple(NamedTuple):
            r: _ChannelModule._ReaderModule.Server
            w: _ChannelModule._WriterModule.Server

        class SetbuffersizeParams(Protocol):
            size: int

        class SetbuffersizeCallContext(Protocol):
            params: _ChannelModule.Server.SetbuffersizeParams

        class ReaderParams(Protocol): ...

        class ReaderCallContext(Protocol):
            params: _ChannelModule.Server.ReaderParams
            results: _ChannelModule.Server.ReaderResult

        class WriterParams(Protocol): ...

        class WriterCallContext(Protocol):
            params: _ChannelModule.Server.WriterParams
            results: _ChannelModule.Server.WriterResult

        class EndpointsParams(Protocol): ...

        class EndpointsCallContext(Protocol):
            params: _ChannelModule.Server.EndpointsParams
            results: _ChannelModule.Server.EndpointsResult

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
            def readerSrts(self) -> Sequence[str]: ...
            @property
            def writerSrts(self) -> Sequence[str]: ...
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
            def readerSrts(self) -> MutableSequence[str]: ...
            @readerSrts.setter
            def readerSrts(self, value: Sequence[str]) -> None: ...
            @property
            def writerSrts(self) -> MutableSequence[str]: ...
            @writerSrts.setter
            def writerSrts(self, value: Sequence[str]) -> None: ...
            @property
            def bufferSize(self) -> int: ...
            @bufferSize.setter
            def bufferSize(self, value: int) -> None: ...
            @overload
            def init(
                self, field: Literal["readerSrts"], size: int | None = None
            ) -> MutableSequence[str]: ...
            @overload
            def init(
                self, field: Literal["writerSrts"], size: int | None = None
            ) -> MutableSequence[str]: ...
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
            readerSrts: Sequence[str] | None = None,
            writerSrts: Sequence[str] | None = None,
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
        readerSrts: Sequence[str]
        writerSrts: Sequence[str]
        bufferSize: int
        @overload
        def init(
            self, name: Literal["readerSrts"], size: int = ...
        ) -> MutableSequence[str]: ...
        @overload
        def init(
            self, name: Literal["writerSrts"], size: int = ...
        ) -> MutableSequence[str]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(
            self,
        ) -> _StartChannelsServiceModule.StartChannelsServiceClient.StartResult: ...

    def _new_client(
        self, server: _DynamicCapabilityServer
    ) -> _StartChannelsServiceModule.StartChannelsServiceClient: ...
    class Server(_IdentifiableModule.Server):
        class StartResult(Awaitable[StartResult], Protocol):
            startupInfos: Sequence[StartupInfoBuilder | StartupInfoReader]
            stop: Any

        class StartResultTuple(NamedTuple):
            startupInfos: Sequence[StartupInfoBuilder | StartupInfoReader]

        class StartParams(Protocol):
            name: str
            noOfChannels: int
            noOfReaders: int
            noOfWriters: int
            readerSrts: Sequence[str]
            writerSrts: Sequence[str]
            bufferSize: int

        class StartCallContext(Protocol):
            params: _StartChannelsServiceModule.Server.StartParams
            results: _StartChannelsServiceModule.Server.StartResult

        def start(
            self,
            name: str,
            noOfChannels: int,
            noOfReaders: int,
            noOfWriters: int,
            readerSrts: Sequence[str],
            writerSrts: Sequence[str],
            bufferSize: int,
            _context: _StartChannelsServiceModule.Server.StartCallContext,
            **kwargs: dict[str, Any],
        ) -> Awaitable[_StartChannelsServiceModule.Server.StartResultTuple | None]: ...
        def start_context(
            self, context: _StartChannelsServiceModule.Server.StartCallContext
        ) -> Awaitable[None]: ...

    class StartChannelsServiceClient(_IdentifiableModule.IdentifiableClient):
        class StartResult(Awaitable[StartResult], Protocol):
            startupInfos: Sequence[StartupInfoReader]
            stop: Any

        def start(
            self,
            name: str | None = None,
            noOfChannels: int | None = None,
            noOfReaders: int | None = None,
            noOfWriters: int | None = None,
            readerSrts: Sequence[str] | None = None,
            writerSrts: Sequence[str] | None = None,
            bufferSize: int | None = None,
        ) -> _StartChannelsServiceModule.StartChannelsServiceClient.StartResult: ...
        def start_request(
            self,
            name: str | None = None,
            noOfChannels: int | None = None,
            noOfReaders: int | None = None,
            noOfWriters: int | None = None,
            readerSrts: Sequence[str] | None = None,
            writerSrts: Sequence[str] | None = None,
            bufferSize: int | None = None,
        ) -> _StartChannelsServiceModule.StartRequest: ...

StartChannelsService: _StartChannelsServiceModule

class _PortInfosModule(_StructModule):
    class _NameAndSRModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @property
            def sr(self) -> str: ...
            @property
            def srs(self) -> Sequence[str]: ...
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
            def srs(self) -> MutableSequence[str]: ...
            @srs.setter
            def srs(self, value: Sequence[str]) -> None: ...
            @override
            def which(self) -> Literal["sr", "srs"]: ...
            def init(
                self, field: Literal["srs"], size: int | None = None
            ) -> MutableSequence[str]: ...
            @override
            def as_reader(self) -> NameAndSRReader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            name: str | None = None,
            sr: str | None = None,
            srs: Sequence[str] | None = None,
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
        def inPorts(self) -> Sequence[NameAndSRReader]: ...
        @property
        def outPorts(self) -> Sequence[NameAndSRReader]: ...
        @override
        def as_builder(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
        ) -> PortInfosBuilder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def inPorts(self) -> MutableSequence[NameAndSRBuilder]: ...
        @inPorts.setter
        def inPorts(
            self,
            value: Sequence[NameAndSRBuilder | NameAndSRReader]
            | Sequence[dict[str, Any]],
        ) -> None: ...
        @property
        def outPorts(self) -> MutableSequence[NameAndSRBuilder]: ...
        @outPorts.setter
        def outPorts(
            self,
            value: Sequence[NameAndSRBuilder | NameAndSRReader]
            | Sequence[dict[str, Any]],
        ) -> None: ...
        @overload
        def init(
            self, field: Literal["inPorts"], size: int | None = None
        ) -> MutableSequence[NameAndSRBuilder]: ...
        @overload
        def init(
            self, field: Literal["outPorts"], size: int | None = None
        ) -> MutableSequence[NameAndSRBuilder]: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> PortInfosReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        inPorts: Sequence[NameAndSRBuilder] | Sequence[dict[str, Any]] | None = None,
        outPorts: Sequence[NameAndSRBuilder] | Sequence[dict[str, Any]] | None = None,
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
            class StartResult(Awaitable[StartResult], Protocol):
                success: bool

            class StopResult(Awaitable[StopResult], Protocol):
                success: bool

            class StartResultTuple(NamedTuple):
                success: bool

            class StopResultTuple(NamedTuple):
                success: bool

            class StartParams(Protocol):
                portInfosReaderSr: str
                name: str

            class StartCallContext(Protocol):
                params: _ComponentModule._RunnableModule.Server.StartParams
                results: _ComponentModule._RunnableModule.Server.StartResult

            class StopParams(Protocol): ...

            class StopCallContext(Protocol):
                params: _ComponentModule._RunnableModule.Server.StopParams
                results: _ComponentModule._RunnableModule.Server.StopResult

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
        def info(self) -> _IdInformationModule.Reader: ...
        @property
        def type(self) -> ComponentComponentTypeEnum: ...
        @property
        def inPorts(self) -> Sequence[PortReader]: ...
        @property
        def outPorts(self) -> Sequence[PortReader]: ...
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
        def info(self) -> _IdInformationModule.Builder: ...
        @info.setter
        def info(
            self,
            value: _IdInformationModule.Builder
            | _IdInformationModule.Reader
            | dict[str, Any],
        ) -> None: ...
        @property
        def type(self) -> ComponentComponentTypeEnum: ...
        @type.setter
        def type(self, value: ComponentComponentTypeEnum) -> None: ...
        @property
        def inPorts(self) -> MutableSequence[PortBuilder]: ...
        @inPorts.setter
        def inPorts(
            self, value: Sequence[PortBuilder | PortReader] | Sequence[dict[str, Any]]
        ) -> None: ...
        @property
        def outPorts(self) -> MutableSequence[PortBuilder]: ...
        @outPorts.setter
        def outPorts(
            self, value: Sequence[PortBuilder | PortReader] | Sequence[dict[str, Any]]
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
        ) -> _IdInformationModule.Builder: ...
        @overload
        def init(
            self, field: Literal["inPorts"], size: int | None = None
        ) -> MutableSequence[PortBuilder]: ...
        @overload
        def init(
            self, field: Literal["outPorts"], size: int | None = None
        ) -> MutableSequence[PortBuilder]: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> ComponentReader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        info: _IdInformationModule.Builder | dict[str, Any] | None = None,
        type: ComponentComponentTypeEnum | None = None,
        inPorts: Sequence[PortBuilder] | Sequence[dict[str, Any]] | None = None,
        outPorts: Sequence[PortBuilder] | Sequence[dict[str, Any]] | None = None,
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
type KVReader = _IPModule._KVModule.Reader
type MsgBuilder = _ChannelModule._MsgModule.Builder
type MsgReader = _ChannelModule._MsgModule.Reader
type NameAndSRBuilder = _PortInfosModule._NameAndSRModule.Builder
type NameAndSRReader = _PortInfosModule._NameAndSRModule.Reader
type ParamsBuilder = _StartChannelsServiceModule._ParamsModule.Builder
type ParamsReader = _StartChannelsServiceModule._ParamsModule.Reader
type PortBuilder = _ComponentModule._PortModule.Builder
type PortInfosBuilder = _PortInfosModule.Builder
type PortInfosReader = _PortInfosModule.Reader
type PortReader = _ComponentModule._PortModule.Reader
type ReadResult = _ChannelModule._ReaderModule.ReaderClient.ReadResult
type ReaderClient = _ChannelModule._ReaderModule.ReaderClient
type ReaderResult = _ChannelModule.ChannelClient.ReaderResult
type ReadifmsgResult = _ChannelModule._ReaderModule.ReaderClient.ReadifmsgResult
type RunnableClient = _ComponentModule._RunnableModule.RunnableClient
type SetautoclosesemanticsResult = (
    _ChannelModule.ChannelClient.SetautoclosesemanticsResult
)
type SetbuffersizeResult = _ChannelModule.ChannelClient.SetbuffersizeResult
type StartChannelsServiceClient = _StartChannelsServiceModule.StartChannelsServiceClient
type StartResult = _ComponentModule._RunnableModule.RunnableClient.StartResult
type StartupInfoBuilder = _ChannelModule._StartupInfoModule.Builder
type StartupInfoReader = _ChannelModule._StartupInfoModule.Reader
type StopResult = _ComponentModule._RunnableModule.RunnableClient.StopResult
type WriteResult = _ChannelModule._WriterModule.WriterClient.WriteResult
type WriteifspaceResult = _ChannelModule._WriterModule.WriterClient.WriteifspaceResult
type WriterClient = _ChannelModule._WriterModule.WriterClient
type WriterResult = _ChannelModule.ChannelClient.WriterResult
