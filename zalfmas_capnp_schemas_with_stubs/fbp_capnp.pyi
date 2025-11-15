"""This is an automatically generated stub for `fbp.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, MutableSequence, Sequence
from enum import Enum
from typing import (
    Any,
    Generic,
    Literal,
    NamedTuple,
    Protocol,
    TypeAlias,
    TypeVar,
    overload,
    override,
)

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _InterfaceModule,
    _Request,
    _StructModule,
)

from .common_capnp import (
    Identifiable,
    IdentifiableClient,
    _IdentifiableModule,
    _IdInformationModule,
)
from .persistence_capnp import Persistent, PersistentClient, _PersistentModule

_ChannelModule_V = TypeVar("_ChannelModule_V")

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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _IPModule._KVModule.Builder: ...

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
            def as_reader(self) -> _IPModule._KVModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, key: str | None = None, desc: str | None = None, value: Any | None = None) -> _IPModule._KVModule.Builder: ...

    KVReader: TypeAlias = _KVModule.Reader
    KVBuilder: TypeAlias = _KVModule.Builder
    KV: _KVModule
    class _TypeModule(Enum):
        standard = 0
        openBracket = 1
        closeBracket = 2

    Type: TypeAlias = _TypeModule
    class Reader(_DynamicStructReader):
        @property
        def attributes(self) -> Sequence[_IPModule._KVModule.Reader]: ...
        @property
        def content(self) -> Any: ...
        @property
        def type(self) -> _IPModule._TypeModule: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _IPModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def attributes(self) -> MutableSequence[_IPModule._KVModule.Builder]: ...
        @attributes.setter
        def attributes(self, value: Sequence[_IPModule._KVModule.Builder | _IPModule._KVModule.Reader] | Sequence[dict[str, Any]]) -> None: ...
        @property
        def content(self) -> Any: ...
        @content.setter
        def content(self, value: Any) -> None: ...
        @property
        def type(self) -> _IPModule._TypeModule: ...
        @type.setter
        def type(self, value: _IPModule._TypeModule | Literal["standard", "openBracket", "closeBracket"]) -> None: ...
        def init(self, field: Literal["attributes"], size: int | None = None) -> MutableSequence[_IPModule._KVModule.Builder]: ...
        @override
        def as_reader(self) -> _IPModule.Reader: ...

    @override
    def new_message(
        self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, attributes: Sequence[_IPModule._KVModule.Builder] | Sequence[dict[str, Any]] | None = None, content: Any | None = None, type: _IPModule._TypeModule | Literal["standard", "openBracket", "closeBracket"] | None = None
    ) -> _IPModule.Builder: ...

IPReader: TypeAlias = _IPModule.Reader
IPBuilder: TypeAlias = _IPModule.Builder
IP: _IPModule

class _IIPModule(_StructModule):
    class Reader(_DynamicStructReader):
        @property
        def content(self) -> Any: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _IIPModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def content(self) -> Any: ...
        @content.setter
        def content(self, value: Any) -> None: ...
        @override
        def as_reader(self) -> _IIPModule.Reader: ...

    @override
    def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, content: Any | None = None) -> _IIPModule.Builder: ...

IIPReader: TypeAlias = _IIPModule.Reader
IIPBuilder: TypeAlias = _IIPModule.Builder
IIP: _IIPModule

class _ChannelModule(_IdentifiableModule, _PersistentModule):
    class _CloseSemanticsModule(Enum):
        fbp = 0
        no = 1

    CloseSemantics: TypeAlias = _CloseSemanticsModule
    class _MsgModule(Generic[_ChannelModule_V], _StructModule):
        class Reader(_DynamicStructReader):
            @property
            def value(self) -> _ChannelModule_V: ...
            @property
            def done(self) -> None: ...
            @property
            def noMsg(self) -> None: ...
            @override
            def which(self) -> Literal["value", "done", "noMsg"]: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ChannelModule._MsgModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def value(self) -> _ChannelModule_V: ...
            @value.setter
            def value(self, value: _ChannelModule_V) -> None: ...
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
            def as_reader(self) -> _ChannelModule._MsgModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, value: _ChannelModule_V | None = None, done: None | None = None, noMsg: None | None = None) -> _ChannelModule._MsgModule.Builder: ...

    MsgReader: TypeAlias = _MsgModule.Reader
    MsgBuilder: TypeAlias = _MsgModule.Builder
    Msg: _MsgModule
    class _ReaderModule(_IdentifiableModule, _PersistentModule):
        class ReadRequest(Protocol):
            def send(self) -> _ChannelModule._ReaderModule.ReaderClient.ReadResult: ...

        class CloseRequest(Protocol):
            def send(self) -> _ChannelModule._ReaderModule.ReaderClient.CloseResult: ...

        class ReadifmsgRequest(Protocol):
            def send(self) -> _ChannelModule._ReaderModule.ReaderClient.ReadifmsgResult: ...

        @classmethod
        def _new_client(cls, server: _ChannelModule._ReaderModule.Server | _IdentifiableModule.Server | _PersistentModule.Server) -> _ChannelModule._ReaderModule.ReaderClient: ...
        class Server(_IdentifiableModule.Server, _PersistentModule.Server):
            class ReadResult(Awaitable[ReadResult], Protocol):
                value: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer
                done: None
                noMsg: None
                def which(self) -> Literal["value", "done", "noMsg"]: ...

            class CloseResult(Awaitable[None], Protocol): ...

            class ReadifmsgResult(Awaitable[ReadifmsgResult], Protocol):
                value: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer
                done: None
                noMsg: None
                def which(self) -> Literal["value", "done", "noMsg"]: ...

            class ReadResultTuple(NamedTuple):
                value: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer
                done: None
                noMsg: None

            class ReadifmsgResultTuple(NamedTuple):
                value: str | bytes | _DynamicStructBuilder | _DynamicStructReader | _DynamicCapabilityClient | _DynamicCapabilityServer
                done: None
                noMsg: None

            class ReadCallContext(Protocol):
                params: _ChannelModule._ReaderModule.ReadRequest
                results: _ChannelModule._ReaderModule.Server.ReadResult

            class CloseCallContext(Protocol):
                params: _ChannelModule._ReaderModule.CloseRequest

            class ReadifmsgCallContext(Protocol):
                params: _ChannelModule._ReaderModule.ReadifmsgRequest
                results: _ChannelModule._ReaderModule.Server.ReadifmsgResult

            def read(self, _context: _ChannelModule._ReaderModule.Server.ReadCallContext, **kwargs: Any) -> Awaitable[_ChannelModule._ReaderModule.Server.ReadResultTuple | None]: ...
            def read_context(self, context: _ChannelModule._ReaderModule.Server.ReadCallContext) -> Awaitable[None]: ...
            def close(self, _context: _ChannelModule._ReaderModule.Server.CloseCallContext, **kwargs: Any) -> Awaitable[None]: ...
            def close_context(self, context: _ChannelModule._ReaderModule.Server.CloseCallContext) -> Awaitable[None]: ...
            def readIfMsg(self, _context: _ChannelModule._ReaderModule.Server.ReadifmsgCallContext, **kwargs: Any) -> Awaitable[_ChannelModule._ReaderModule.Server.ReadifmsgResultTuple | None]: ...
            def readIfMsg_context(self, context: _ChannelModule._ReaderModule.Server.ReadifmsgCallContext) -> Awaitable[None]: ...

        class ReaderClient(_IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient):
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
            def close(self) -> _ChannelModule._ReaderModule.ReaderClient.CloseResult: ...
            def readIfMsg(self) -> _ChannelModule._ReaderModule.ReaderClient.ReadifmsgResult: ...
            def read_request(self) -> _ChannelModule._ReaderModule.ReadRequest: ...
            def close_request(self) -> _ChannelModule._ReaderModule.CloseRequest: ...
            def readIfMsg_request(self) -> _ChannelModule._ReaderModule.ReadifmsgRequest: ...

    Reader: _ReaderModule
    ReaderClient: TypeAlias = _ChannelModule._ReaderModule.ReaderClient
    class _WriterModule(_IdentifiableModule, _PersistentModule):
        class WriteRequest(Protocol):
            value: _DynamicObjectReader
            done: None
            noMsg: None
            def send(self) -> _ChannelModule._WriterModule.WriterClient.WriteResult: ...

        class CloseRequest(Protocol):
            def send(self) -> _ChannelModule._WriterModule.WriterClient.CloseResult: ...

        class WriteifspaceRequest(Protocol):
            value: _DynamicObjectReader
            done: None
            noMsg: None
            def send(self) -> _ChannelModule._WriterModule.WriterClient.WriteifspaceResult: ...

        @classmethod
        def _new_client(cls, server: _ChannelModule._WriterModule.Server | _IdentifiableModule.Server | _PersistentModule.Server) -> _ChannelModule._WriterModule.WriterClient: ...
        class Server(_IdentifiableModule.Server, _PersistentModule.Server):
            class WriteResult(Awaitable[None], Protocol): ...
            class CloseResult(Awaitable[None], Protocol): ...

            class WriteifspaceResult(Awaitable[WriteifspaceResult], Protocol):
                success: bool

            class WriteifspaceResultTuple(NamedTuple):
                success: bool

            class WriteCallContext(Protocol):
                params: _ChannelModule._WriterModule.WriteRequest

            class CloseCallContext(Protocol):
                params: _ChannelModule._WriterModule.CloseRequest

            class WriteifspaceCallContext(Protocol):
                params: _ChannelModule._WriterModule.WriteifspaceRequest
                results: _ChannelModule._WriterModule.Server.WriteifspaceResult

            def write(self, value: _DynamicObjectReader, done: None, noMsg: None, _context: _ChannelModule._WriterModule.Server.WriteCallContext, **kwargs: Any) -> Awaitable[None]: ...
            def write_context(self, context: _ChannelModule._WriterModule.Server.WriteCallContext) -> Awaitable[None]: ...
            def close(self, _context: _ChannelModule._WriterModule.Server.CloseCallContext, **kwargs: Any) -> Awaitable[None]: ...
            def close_context(self, context: _ChannelModule._WriterModule.Server.CloseCallContext) -> Awaitable[None]: ...
            def writeIfSpace(self, value: _DynamicObjectReader, done: None, noMsg: None, _context: _ChannelModule._WriterModule.Server.WriteifspaceCallContext, **kwargs: Any) -> Awaitable[bool | _ChannelModule._WriterModule.Server.WriteifspaceResultTuple | None]: ...
            def writeIfSpace_context(self, context: _ChannelModule._WriterModule.Server.WriteifspaceCallContext) -> Awaitable[None]: ...

        class WriterClient(_IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient):
            class WriteResult(Awaitable[None], Protocol): ...
            class CloseResult(Awaitable[None], Protocol): ...

            class WriteifspaceResult(Awaitable[WriteifspaceResult], Protocol):
                success: bool

            def write(self, value: _DynamicObjectReader | None = None, done: None | None = None, noMsg: None | None = None) -> _ChannelModule._WriterModule.WriterClient.WriteResult: ...
            def close(self) -> _ChannelModule._WriterModule.WriterClient.CloseResult: ...
            def writeIfSpace(self, value: _DynamicObjectReader | None = None, done: None | None = None, noMsg: None | None = None) -> _ChannelModule._WriterModule.WriterClient.WriteifspaceResult: ...
            def write_request(self, value: _DynamicObjectReader | None = None, done: None | None = None, noMsg: None | None = None) -> _ChannelModule._WriterModule.WriteRequest: ...
            def close_request(self) -> _ChannelModule._WriterModule.CloseRequest: ...
            def writeIfSpace_request(self, value: _DynamicObjectReader | None = None, done: None | None = None, noMsg: None | None = None) -> _ChannelModule._WriterModule.WriteifspaceRequest: ...

    Writer: _WriterModule
    WriterClient: TypeAlias = _ChannelModule._WriterModule.WriterClient
    class _StartupInfoModule(_StructModule):
        class Reader(_DynamicStructReader):
            @property
            def bufferSize(self) -> int: ...
            @property
            def closeSemantics(self) -> _ChannelModule._CloseSemanticsModule: ...
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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ChannelModule._StartupInfoModule.Builder: ...

        class Builder(_DynamicStructBuilder):
            @property
            def bufferSize(self) -> int: ...
            @bufferSize.setter
            def bufferSize(self, value: int) -> None: ...
            @property
            def closeSemantics(self) -> _ChannelModule._CloseSemanticsModule: ...
            @closeSemantics.setter
            def closeSemantics(self, value: _ChannelModule._CloseSemanticsModule | Literal["fbp", "no"]) -> None: ...
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
            def channel(self, value: _ChannelModule.ChannelClient | _ChannelModule.Server) -> None: ...
            @property
            def readers(self) -> MutableSequence[_ChannelModule._ReaderModule]: ...
            @readers.setter
            def readers(self, value: Sequence[_ChannelModule._ReaderModule]) -> None: ...
            @property
            def writers(self) -> MutableSequence[_ChannelModule._WriterModule]: ...
            @writers.setter
            def writers(self, value: Sequence[_ChannelModule._WriterModule]) -> None: ...
            @overload
            def init(self, field: Literal["readerSRs"], size: int | None = None) -> MutableSequence[str]: ...
            @overload
            def init(self, field: Literal["writerSRs"], size: int | None = None) -> MutableSequence[str]: ...
            @overload
            def init(self, field: Literal["readers"], size: int | None = None) -> MutableSequence[_ChannelModule._ReaderModule]: ...
            @overload
            def init(self, field: Literal["writers"], size: int | None = None) -> MutableSequence[_ChannelModule._WriterModule]: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> _ChannelModule._StartupInfoModule.Reader: ...

        @override
        def new_message(
            self,
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            bufferSize: int | None = None,
            closeSemantics: _ChannelModule._CloseSemanticsModule | Literal["fbp", "no"] | None = None,
            channelSR: str | None = None,
            readerSRs: Sequence[str] | None = None,
            writerSRs: Sequence[str] | None = None,
            channel: _ChannelModule.ChannelClient | _ChannelModule.Server | None = None,
            readers: Sequence[_ChannelModule._ReaderModule] | None = None,
            writers: Sequence[_ChannelModule._WriterModule] | None = None,
        ) -> _ChannelModule._StartupInfoModule.Builder: ...

    StartupInfoReader: TypeAlias = _StartupInfoModule.Reader
    StartupInfoBuilder: TypeAlias = _StartupInfoModule.Builder
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
        cs: _ChannelModule._CloseSemanticsModule | Literal["fbp", "no"]
        def send(self) -> _ChannelModule.ChannelClient.SetautoclosesemanticsResult: ...

    class CloseRequest(Protocol):
        waitForEmptyBuffer: bool
        def send(self) -> _ChannelModule.ChannelClient.CloseResult: ...

    @classmethod
    def _new_client(cls, server: _ChannelModule.Server | _IdentifiableModule.Server | _PersistentModule.Server) -> _ChannelModule.ChannelClient: ...
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

        class SetbuffersizeCallContext(Protocol):
            params: _ChannelModule.SetbuffersizeRequest

        class ReaderCallContext(Protocol):
            params: _ChannelModule.ReaderRequest
            results: _ChannelModule.Server.ReaderResult

        class WriterCallContext(Protocol):
            params: _ChannelModule.WriterRequest
            results: _ChannelModule.Server.WriterResult

        class EndpointsCallContext(Protocol):
            params: _ChannelModule.EndpointsRequest
            results: _ChannelModule.Server.EndpointsResult

        class SetautoclosesemanticsCallContext(Protocol):
            params: _ChannelModule.SetautoclosesemanticsRequest

        class CloseCallContext(Protocol):
            params: _ChannelModule.CloseRequest

        def setBufferSize(self, size: int, _context: _ChannelModule.Server.SetbuffersizeCallContext, **kwargs: Any) -> Awaitable[None]: ...
        def setBufferSize_context(self, context: _ChannelModule.Server.SetbuffersizeCallContext) -> Awaitable[None]: ...
        def reader(self, _context: _ChannelModule.Server.ReaderCallContext, **kwargs: Any) -> Awaitable[_ChannelModule._ReaderModule.Server | _ChannelModule.Server.ReaderResultTuple | None]: ...
        def reader_context(self, context: _ChannelModule.Server.ReaderCallContext) -> Awaitable[None]: ...
        def writer(self, _context: _ChannelModule.Server.WriterCallContext, **kwargs: Any) -> Awaitable[_ChannelModule._WriterModule.Server | _ChannelModule.Server.WriterResultTuple | None]: ...
        def writer_context(self, context: _ChannelModule.Server.WriterCallContext) -> Awaitable[None]: ...
        def endpoints(self, _context: _ChannelModule.Server.EndpointsCallContext, **kwargs: Any) -> Awaitable[_ChannelModule.Server.EndpointsResultTuple | None]: ...
        def endpoints_context(self, context: _ChannelModule.Server.EndpointsCallContext) -> Awaitable[None]: ...
        def setAutoCloseSemantics(self, cs: _ChannelModule._CloseSemanticsModule | Literal["fbp", "no"], _context: _ChannelModule.Server.SetautoclosesemanticsCallContext, **kwargs: Any) -> Awaitable[None]: ...
        def setAutoCloseSemantics_context(self, context: _ChannelModule.Server.SetautoclosesemanticsCallContext) -> Awaitable[None]: ...
        def close(self, waitForEmptyBuffer: bool, _context: _ChannelModule.Server.CloseCallContext, **kwargs: Any) -> Awaitable[None]: ...
        def close_context(self, context: _ChannelModule.Server.CloseCallContext) -> Awaitable[None]: ...

    class ChannelClient(_IdentifiableModule.IdentifiableClient, _PersistentModule.PersistentClient):
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

        def setBufferSize(self, size: int | None = None) -> _ChannelModule.ChannelClient.SetbuffersizeResult: ...
        def reader(self) -> _ChannelModule.ChannelClient.ReaderResult: ...
        def writer(self) -> _ChannelModule.ChannelClient.WriterResult: ...
        def endpoints(self) -> _ChannelModule.ChannelClient.EndpointsResult: ...
        def setAutoCloseSemantics(self, cs: _ChannelModule._CloseSemanticsModule | Literal["fbp", "no"] | None = None) -> _ChannelModule.ChannelClient.SetautoclosesemanticsResult: ...
        def close(self, waitForEmptyBuffer: bool | None = None) -> _ChannelModule.ChannelClient.CloseResult: ...
        def setBufferSize_request(self, size: int | None = None) -> _ChannelModule.SetbuffersizeRequest: ...
        def reader_request(self) -> _ChannelModule.ReaderRequest: ...
        def writer_request(self) -> _ChannelModule.WriterRequest: ...
        def endpoints_request(self) -> _ChannelModule.EndpointsRequest: ...
        def setAutoCloseSemantics_request(self, cs: _ChannelModule._CloseSemanticsModule | Literal["fbp", "no"] | None = None) -> _ChannelModule.SetautoclosesemanticsRequest: ...
        def close_request(self, waitForEmptyBuffer: bool | None = None) -> _ChannelModule.CloseRequest: ...

Channel: _ChannelModule
ChannelClient: TypeAlias = _ChannelModule.ChannelClient

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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _StartChannelsServiceModule._ParamsModule.Builder: ...

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
            def init(self, field: Literal["readerSrts"], size: int | None = None) -> MutableSequence[str]: ...
            @overload
            def init(self, field: Literal["writerSrts"], size: int | None = None) -> MutableSequence[str]: ...
            @overload
            def init(self, field: str, size: int | None = None) -> Any: ...
            @override
            def as_reader(self) -> _StartChannelsServiceModule._ParamsModule.Reader: ...

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
        ) -> _StartChannelsServiceModule._ParamsModule.Builder: ...

    ParamsReader: TypeAlias = _ParamsModule.Reader
    ParamsBuilder: TypeAlias = _ParamsModule.Builder
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
        def init(self, name: Literal["readerSrts"], size: int = ...) -> MutableSequence[str]: ...
        @overload
        def init(self, name: Literal["writerSrts"], size: int = ...) -> MutableSequence[str]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> _StartChannelsServiceModule.StartChannelsServiceClient.StartResult: ...

    @classmethod
    def _new_client(cls, server: _StartChannelsServiceModule.Server | _IdentifiableModule.Server) -> _StartChannelsServiceModule.StartChannelsServiceClient: ...
    class Server(_IdentifiableModule.Server):
        class StartResult(Awaitable[StartResult], Protocol):
            startupInfos: Sequence[_ChannelModule._StartupInfoModule.Builder | _ChannelModule._StartupInfoModule.Reader]
            stop: Any

        class StartResultTuple(NamedTuple):
            startupInfos: Sequence[_ChannelModule._StartupInfoModule]

        class StartCallContext(Protocol):
            params: _StartChannelsServiceModule.StartRequest
            results: _StartChannelsServiceModule.Server.StartResult

        def start(self, name: str, noOfChannels: int, noOfReaders: int, noOfWriters: int, readerSrts: Sequence[str], writerSrts: Sequence[str], bufferSize: int, _context: _StartChannelsServiceModule.Server.StartCallContext, **kwargs: Any) -> Awaitable[_StartChannelsServiceModule.Server.StartResultTuple | None]: ...
        def start_context(self, context: _StartChannelsServiceModule.Server.StartCallContext) -> Awaitable[None]: ...

    class StartChannelsServiceClient(_IdentifiableModule.IdentifiableClient):
        class StartResult(Awaitable[StartResult], Protocol):
            startupInfos: Sequence[_ChannelModule._StartupInfoModule.Builder | _ChannelModule._StartupInfoModule.Reader]
            stop: Any

        def start(
            self, name: str | None = None, noOfChannels: int | None = None, noOfReaders: int | None = None, noOfWriters: int | None = None, readerSrts: Sequence[str] | None = None, writerSrts: Sequence[str] | None = None, bufferSize: int | None = None
        ) -> _StartChannelsServiceModule.StartChannelsServiceClient.StartResult: ...
        def start_request(self, name: str | None = None, noOfChannels: int | None = None, noOfReaders: int | None = None, noOfWriters: int | None = None, readerSrts: Sequence[str] | None = None, writerSrts: Sequence[str] | None = None, bufferSize: int | None = None) -> _StartChannelsServiceModule.StartRequest: ...

StartChannelsService: _StartChannelsServiceModule
StartChannelsServiceClient: TypeAlias = _StartChannelsServiceModule.StartChannelsServiceClient

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
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _PortInfosModule._NameAndSRModule.Builder: ...

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
            def init(self, field: Literal["srs"], size: int | None = None) -> MutableSequence[str]: ...
            @override
            def as_reader(self) -> _PortInfosModule._NameAndSRModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, name: str | None = None, sr: str | None = None, srs: Sequence[str] | None = None) -> _PortInfosModule._NameAndSRModule.Builder: ...

    NameAndSRReader: TypeAlias = _NameAndSRModule.Reader
    NameAndSRBuilder: TypeAlias = _NameAndSRModule.Builder
    NameAndSR: _NameAndSRModule
    class Reader(_DynamicStructReader):
        @property
        def inPorts(self) -> Sequence[_PortInfosModule._NameAndSRModule.Reader]: ...
        @property
        def outPorts(self) -> Sequence[_PortInfosModule._NameAndSRModule.Reader]: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _PortInfosModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def inPorts(self) -> MutableSequence[_PortInfosModule._NameAndSRModule.Builder]: ...
        @inPorts.setter
        def inPorts(self, value: Sequence[_PortInfosModule._NameAndSRModule.Builder | _PortInfosModule._NameAndSRModule.Reader] | Sequence[dict[str, Any]]) -> None: ...
        @property
        def outPorts(self) -> MutableSequence[_PortInfosModule._NameAndSRModule.Builder]: ...
        @outPorts.setter
        def outPorts(self, value: Sequence[_PortInfosModule._NameAndSRModule.Builder | _PortInfosModule._NameAndSRModule.Reader] | Sequence[dict[str, Any]]) -> None: ...
        @overload
        def init(self, field: Literal["inPorts"], size: int | None = None) -> MutableSequence[_PortInfosModule._NameAndSRModule.Builder]: ...
        @overload
        def init(self, field: Literal["outPorts"], size: int | None = None) -> MutableSequence[_PortInfosModule._NameAndSRModule.Builder]: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> _PortInfosModule.Reader: ...

    @override
    def new_message(
        self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, inPorts: Sequence[_PortInfosModule._NameAndSRModule.Builder] | Sequence[dict[str, Any]] | None = None, outPorts: Sequence[_PortInfosModule._NameAndSRModule.Builder] | Sequence[dict[str, Any]] | None = None
    ) -> _PortInfosModule.Builder: ...

PortInfosReader: TypeAlias = _PortInfosModule.Reader
PortInfosBuilder: TypeAlias = _PortInfosModule.Builder
PortInfos: _PortInfosModule

class _ComponentModule(_StructModule):
    class _RunnableModule(_IdentifiableModule):
        class StartRequest(Protocol):
            portInfosReaderSr: str
            name: str
            def send(self) -> _ComponentModule._RunnableModule.RunnableClient.StartResult: ...

        class StopRequest(Protocol):
            def send(self) -> _ComponentModule._RunnableModule.RunnableClient.StopResult: ...

        @classmethod
        def _new_client(cls, server: _ComponentModule._RunnableModule.Server | _IdentifiableModule.Server) -> _ComponentModule._RunnableModule.RunnableClient: ...
        class Server(_IdentifiableModule.Server):
            class StartResult(Awaitable[StartResult], Protocol):
                success: bool

            class StopResult(Awaitable[StopResult], Protocol):
                success: bool

            class StartResultTuple(NamedTuple):
                success: bool

            class StopResultTuple(NamedTuple):
                success: bool

            class StartCallContext(Protocol):
                params: _ComponentModule._RunnableModule.StartRequest
                results: _ComponentModule._RunnableModule.Server.StartResult

            class StopCallContext(Protocol):
                params: _ComponentModule._RunnableModule.StopRequest
                results: _ComponentModule._RunnableModule.Server.StopResult

            def start(self, portInfosReaderSr: str, name: str, _context: _ComponentModule._RunnableModule.Server.StartCallContext, **kwargs: Any) -> Awaitable[bool | _ComponentModule._RunnableModule.Server.StartResultTuple | None]: ...
            def start_context(self, context: _ComponentModule._RunnableModule.Server.StartCallContext) -> Awaitable[None]: ...
            def stop(self, _context: _ComponentModule._RunnableModule.Server.StopCallContext, **kwargs: Any) -> Awaitable[bool | _ComponentModule._RunnableModule.Server.StopResultTuple | None]: ...
            def stop_context(self, context: _ComponentModule._RunnableModule.Server.StopCallContext) -> Awaitable[None]: ...

        class RunnableClient(_IdentifiableModule.IdentifiableClient):
            class StartResult(Awaitable[StartResult], Protocol):
                success: bool

            class StopResult(Awaitable[StopResult], Protocol):
                success: bool

            def start(self, portInfosReaderSr: str | None = None, name: str | None = None) -> _ComponentModule._RunnableModule.RunnableClient.StartResult: ...
            def stop(self) -> _ComponentModule._RunnableModule.RunnableClient.StopResult: ...
            def start_request(self, portInfosReaderSr: str | None = None, name: str | None = None) -> _ComponentModule._RunnableModule.StartRequest: ...
            def stop_request(self) -> _ComponentModule._RunnableModule.StopRequest: ...

    Runnable: _RunnableModule
    RunnableClient: TypeAlias = _ComponentModule._RunnableModule.RunnableClient
    class _ComponentTypeModule(Enum):
        standard = 0
        iip = 1
        subflow = 2
        view = 3

    ComponentType: TypeAlias = _ComponentTypeModule
    class _PortModule(_StructModule):
        class _PortTypeModule(Enum):
            standard = 0

        PortType: TypeAlias = _PortTypeModule
        class _ContentTypeModule(Enum):
            structuredText = 0

        ContentType: TypeAlias = _ContentTypeModule
        class Reader(_DynamicStructReader):
            @property
            def name(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride,reportIncompatibleMethodOverride]
            @property
            def contentType(self) -> str: ...
            @property
            def type(self) -> _ComponentModule._PortModule._PortTypeModule: ...
            @override
            def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ComponentModule._PortModule.Builder: ...

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
            def type(self) -> _ComponentModule._PortModule._PortTypeModule: ...
            @type.setter
            def type(self, value: _ComponentModule._PortModule._PortTypeModule | Literal["standard"]) -> None: ...
            @override
            def as_reader(self) -> _ComponentModule._PortModule.Reader: ...

        @override
        def new_message(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None, name: str | None = None, contentType: str | None = None, type: _ComponentModule._PortModule._PortTypeModule | Literal["standard"] | None = None) -> _ComponentModule._PortModule.Builder: ...

    PortReader: TypeAlias = _PortModule.Reader
    PortBuilder: TypeAlias = _PortModule.Builder
    Port: _PortModule
    class Reader(_DynamicStructReader):
        @property
        def info(self) -> _IdInformationModule.Reader: ...
        @property
        def type(self) -> _ComponentModule._ComponentTypeModule: ...
        @property
        def inPorts(self) -> Sequence[_ComponentModule._PortModule.Reader]: ...
        @property
        def outPorts(self) -> Sequence[_ComponentModule._PortModule.Reader]: ...
        @property
        def run(self) -> _ComponentModule._RunnableModule.RunnableClient: ...
        @property
        def defaultConfig(self) -> str: ...
        @override
        def as_builder(self, num_first_segment_words: int | None = None, allocate_seg_callable: Any = None) -> _ComponentModule.Builder: ...

    class Builder(_DynamicStructBuilder):
        @property
        def info(self) -> _IdInformationModule.Builder: ...
        @info.setter
        def info(self, value: _IdInformationModule.Builder | _IdInformationModule.Reader | dict[str, Any]) -> None: ...
        @property
        def type(self) -> _ComponentModule._ComponentTypeModule: ...
        @type.setter
        def type(self, value: _ComponentModule._ComponentTypeModule | Literal["standard", "iip", "subflow", "view"]) -> None: ...
        @property
        def inPorts(self) -> MutableSequence[_ComponentModule._PortModule.Builder]: ...
        @inPorts.setter
        def inPorts(self, value: Sequence[_ComponentModule._PortModule.Builder | _ComponentModule._PortModule.Reader] | Sequence[dict[str, Any]]) -> None: ...
        @property
        def outPorts(self) -> MutableSequence[_ComponentModule._PortModule.Builder]: ...
        @outPorts.setter
        def outPorts(self, value: Sequence[_ComponentModule._PortModule.Builder | _ComponentModule._PortModule.Reader] | Sequence[dict[str, Any]]) -> None: ...
        @property
        def run(self) -> _ComponentModule._RunnableModule.RunnableClient: ...
        @run.setter
        def run(self, value: _ComponentModule._RunnableModule.RunnableClient | _ComponentModule._RunnableModule.Server) -> None: ...
        @property
        def defaultConfig(self) -> str: ...
        @defaultConfig.setter
        def defaultConfig(self, value: str) -> None: ...
        @overload
        def init(self, field: Literal["info"], size: int | None = None) -> _IdInformationModule.Builder: ...
        @overload
        def init(self, field: Literal["inPorts"], size: int | None = None) -> MutableSequence[_ComponentModule._PortModule.Builder]: ...
        @overload
        def init(self, field: Literal["outPorts"], size: int | None = None) -> MutableSequence[_ComponentModule._PortModule.Builder]: ...
        @overload
        def init(self, field: str, size: int | None = None) -> Any: ...
        @override
        def as_reader(self) -> _ComponentModule.Reader: ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        info: _IdInformationModule.Builder | dict[str, Any] | None = None,
        type: _ComponentModule._ComponentTypeModule | Literal["standard", "iip", "subflow", "view"] | None = None,
        inPorts: Sequence[_ComponentModule._PortModule.Builder] | Sequence[dict[str, Any]] | None = None,
        outPorts: Sequence[_ComponentModule._PortModule.Builder] | Sequence[dict[str, Any]] | None = None,
        run: _ComponentModule._RunnableModule.RunnableClient | _ComponentModule._RunnableModule.Server | None = None,
        defaultConfig: str | None = None,
    ) -> _ComponentModule.Builder: ...

ComponentReader: TypeAlias = _ComponentModule.Reader
ComponentBuilder: TypeAlias = _ComponentModule.Builder
Component: _ComponentModule

# Top-level type aliases for use in type annotations
KVBuilder: TypeAlias = _IPModule._KVModule.Builder
KVReader: TypeAlias = _IPModule._KVModule.Reader
MsgBuilder: TypeAlias = _ChannelModule._MsgModule.Builder
MsgReader: TypeAlias = _ChannelModule._MsgModule.Reader
NameAndSRBuilder: TypeAlias = _PortInfosModule._NameAndSRModule.Builder
NameAndSRReader: TypeAlias = _PortInfosModule._NameAndSRModule.Reader
ParamsBuilder: TypeAlias = _StartChannelsServiceModule._ParamsModule.Builder
ParamsReader: TypeAlias = _StartChannelsServiceModule._ParamsModule.Reader
PortBuilder: TypeAlias = _ComponentModule._PortModule.Builder
PortReader: TypeAlias = _ComponentModule._PortModule.Reader
ReaderClient: TypeAlias = _ChannelModule._ReaderModule.ReaderClient
RunnableClient: TypeAlias = _ComponentModule._RunnableModule.RunnableClient
StartupInfoBuilder: TypeAlias = _ChannelModule._StartupInfoModule.Builder
StartupInfoReader: TypeAlias = _ChannelModule._StartupInfoModule.Reader
WriterClient: TypeAlias = _ChannelModule._WriterModule.WriterClient
