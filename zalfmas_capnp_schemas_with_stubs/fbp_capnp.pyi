"""This is an automatically generated stub for `fbp.capnp`."""

from __future__ import annotations

from collections.abc import Awaitable, Iterator, Sequence
from contextlib import contextmanager
from enum import Enum
from io import BufferedWriter
from typing import (
    Any,
    BinaryIO,
    Generic,
    Literal,
    NamedTuple,
    Protocol,
    TypeAlias,
    TypeVar,
    overload,
)

from .common_capnp import Identifiable, IdentifiableClient, IdInformation
from .persistence_capnp import Persistent, PersistentClient

Channel_V = TypeVar("Channel_V")

IPBuilder: TypeAlias = IP.Builder
IPReader: TypeAlias = IP.Reader

class IP:
    KVBuilder: TypeAlias = KV.Builder
    KVReader: TypeAlias = KV.Reader
    class KV:
        class Reader:
            @property
            def key(self) -> str: ...
            @property
            def desc(self) -> str: ...
            @property
            def value(self) -> Any: ...
            def as_builder(self) -> IP.KV.Builder: ...

        class Builder:
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
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> IP.KV.Builder: ...
            def copy(self) -> IP.KV.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> IP.KV.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[IP.KV.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> IP.KV.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            key: str | None = None,
            desc: str | None = None,
            value: Any | None = None,
        ) -> IP.KV.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> IP.KV.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> IP.KV.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Type(Enum):
        standard = "standard"
        openBracket = "openBracket"
        closeBracket = "closeBracket"

    class Reader:
        @property
        def attributes(self) -> Sequence[IP.KV.Reader]: ...
        @property
        def content(self) -> Any: ...
        @property
        def type(self) -> IP.Type: ...
        def as_builder(self) -> IP.Builder: ...

    class Builder:
        @property
        def attributes(self) -> Sequence[IP.KV.Builder]: ...
        @attributes.setter
        def attributes(
            self,
            value: Sequence[IP.KV.Builder | IP.KV.Reader] | Sequence[dict[str, Any]],
        ) -> None: ...
        @property
        def content(self) -> Any: ...
        @content.setter
        def content(self, value: Any) -> None: ...
        @property
        def type(self) -> IP.Type: ...
        @type.setter
        def type(
            self, value: IP.Type | Literal["standard", "openBracket", "closeBracket"]
        ) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> IP.Builder: ...
        def init(
            self, name: Literal["attributes"], size: int = ...
        ) -> Sequence[IP.KV.Builder]: ...
        def copy(self) -> IP.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> IP.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @contextmanager
    @staticmethod
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[IP.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> IP.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        attributes: Sequence[IP.KV.Builder] | Sequence[dict[str, Any]] | None = None,
        content: Any | None = None,
        type: IP.Type
        | Literal["standard", "openBracket", "closeBracket"]
        | None = None,
    ) -> IP.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> IP.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> IP.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

IIPBuilder: TypeAlias = IIP.Builder
IIPReader: TypeAlias = IIP.Reader

class IIP:
    class Reader:
        @property
        def content(self) -> Any: ...
        def as_builder(self) -> IIP.Builder: ...

    class Builder:
        @property
        def content(self) -> Any: ...
        @content.setter
        def content(self, value: Any) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> IIP.Builder: ...
        def copy(self) -> IIP.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> IIP.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @contextmanager
    @staticmethod
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[IIP.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> IIP.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        content: Any | None = None,
    ) -> IIP.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> IIP.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> IIP.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

class Channel:
    class CloseSemantics(Enum):
        fbp = "fbp"
        no = "no"

    MsgBuilder: TypeAlias = Msg.Builder
    MsgReader: TypeAlias = Msg.Reader
    class Msg(Generic[Channel_V]):
        class Reader:
            @property
            def value(self) -> Channel_V: ...
            @property
            def done(self) -> None: ...
            @property
            def noMsg(self) -> None: ...
            def which(self) -> Literal["value", "done", "noMsg"]: ...
            def as_builder(self) -> Channel.Msg.Builder: ...

        class Builder:
            @property
            def value(self) -> Channel_V: ...
            @value.setter
            def value(self, value: Channel_V) -> None: ...
            @property
            def done(self) -> None: ...
            @done.setter
            def done(self, value: None) -> None: ...
            @property
            def noMsg(self) -> None: ...
            @noMsg.setter
            def noMsg(self, value: None) -> None: ...
            def which(self) -> Literal["value", "done", "noMsg"]: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Channel.Msg.Builder: ...
            def copy(self) -> Channel.Msg.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Channel.Msg.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def which(self) -> Literal["value", "done", "noMsg"]: ...
        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Channel.Msg.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Channel.Msg.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            value: Channel_V | None = None,
            done: None | None = None,
            noMsg: None | None = None,
        ) -> Channel.Msg.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Channel.Msg.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Channel.Msg.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Reader:
        class ReadRequest(Protocol):
            def send(self) -> Channel.Reader.ReadResult: ...

        class ReadResult(Awaitable[ReadResult], Protocol):
            value: Any
            done: None
            noMsg: None
            def which(self) -> Literal["value", "done", "noMsg"]: ...

        class CloseRequest(Protocol):
            def send(self) -> None: ...

        class ReadifmsgRequest(Protocol):
            def send(self) -> Channel.Reader.ReadifmsgResult: ...

        class ReadifmsgResult(Awaitable[ReadifmsgResult], Protocol):
            value: Any
            done: None
            noMsg: None
            def which(self) -> Literal["value", "done", "noMsg"]: ...

        @classmethod
        def _new_client(
            cls, server: Channel.Reader.Server | Identifiable.Server | Persistent.Server
        ) -> Channel.ReaderClient: ...
        class Server(Identifiable.Server, Persistent.Server):
            class ReadResultTuple(NamedTuple):
                value: Any
                done: None
                noMsg: None

            class ReadifmsgResultTuple(NamedTuple):
                value: Any
                done: None
                noMsg: None

            class ReadCallContext(Protocol):
                params: Channel.Reader.ReadRequest
                results: Channel.Reader.ReadResult

            class CloseCallContext(Protocol):
                params: Channel.Reader.CloseRequest

            class ReadifmsgCallContext(Protocol):
                params: Channel.Reader.ReadifmsgRequest
                results: Channel.Reader.ReadifmsgResult

            def read(
                self, _context: Channel.Reader.Server.ReadCallContext, **kwargs: Any
            ) -> Awaitable[Channel.Reader.Server.ReadResultTuple | None]: ...
            def read_context(
                self, context: Channel.Reader.Server.ReadCallContext
            ) -> Awaitable[None]: ...
            def close(
                self, _context: Channel.Reader.Server.CloseCallContext, **kwargs: Any
            ) -> Awaitable[None]: ...
            def close_context(
                self, context: Channel.Reader.Server.CloseCallContext
            ) -> Awaitable[None]: ...
            def readIfMsg(
                self,
                _context: Channel.Reader.Server.ReadifmsgCallContext,
                **kwargs: Any,
            ) -> Awaitable[Channel.Reader.Server.ReadifmsgResultTuple | None]: ...
            def readIfMsg_context(
                self, context: Channel.Reader.Server.ReadifmsgCallContext
            ) -> Awaitable[None]: ...

    class ReaderClient(IdentifiableClient, PersistentClient):
        def read(self) -> Channel.Reader.ReadResult: ...
        def close(self) -> None: ...
        def readIfMsg(self) -> Channel.Reader.ReadifmsgResult: ...
        def read_request(self) -> Channel.Reader.ReadRequest: ...
        def close_request(self) -> Channel.Reader.CloseRequest: ...
        def readIfMsg_request(self) -> Channel.Reader.ReadifmsgRequest: ...

    class Writer:
        class WriteRequest(Protocol):
            value: Any
            done: None
            noMsg: None
            def send(self) -> None: ...

        class CloseRequest(Protocol):
            def send(self) -> None: ...

        class WriteifspaceRequest(Protocol):
            value: Any
            done: None
            noMsg: None
            def send(self) -> Channel.Writer.WriteifspaceResult: ...

        class WriteifspaceResult(Awaitable[WriteifspaceResult], Protocol):
            success: bool

        @classmethod
        def _new_client(
            cls, server: Channel.Writer.Server | Identifiable.Server | Persistent.Server
        ) -> Channel.WriterClient: ...
        class Server(Identifiable.Server, Persistent.Server):
            class WriteifspaceResultTuple(NamedTuple):
                success: bool

            class WriteCallContext(Protocol):
                params: Channel.Writer.WriteRequest

            class CloseCallContext(Protocol):
                params: Channel.Writer.CloseRequest

            class WriteifspaceCallContext(Protocol):
                params: Channel.Writer.WriteifspaceRequest
                results: Channel.Writer.WriteifspaceResult

            def write(
                self,
                value: Any,
                done: None,
                noMsg: None,
                _context: Channel.Writer.Server.WriteCallContext,
                **kwargs: Any,
            ) -> Awaitable[None]: ...
            def write_context(
                self, context: Channel.Writer.Server.WriteCallContext
            ) -> Awaitable[None]: ...
            def close(
                self, _context: Channel.Writer.Server.CloseCallContext, **kwargs: Any
            ) -> Awaitable[None]: ...
            def close_context(
                self, context: Channel.Writer.Server.CloseCallContext
            ) -> Awaitable[None]: ...
            def writeIfSpace(
                self,
                value: Any,
                done: None,
                noMsg: None,
                _context: Channel.Writer.Server.WriteifspaceCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                bool | Channel.Writer.Server.WriteifspaceResultTuple | None
            ]: ...
            def writeIfSpace_context(
                self, context: Channel.Writer.Server.WriteifspaceCallContext
            ) -> Awaitable[None]: ...

    class WriterClient(IdentifiableClient, PersistentClient):
        def write(
            self,
            value: Any | None = None,
            done: None | None = None,
            noMsg: None | None = None,
        ) -> None: ...
        def close(self) -> None: ...
        def writeIfSpace(
            self,
            value: Any | None = None,
            done: None | None = None,
            noMsg: None | None = None,
        ) -> Channel.Writer.WriteifspaceResult: ...
        def write_request(
            self,
            value: Any | None = None,
            done: None | None = None,
            noMsg: None | None = None,
        ) -> Channel.Writer.WriteRequest: ...
        def close_request(self) -> Channel.Writer.CloseRequest: ...
        def writeIfSpace_request(
            self,
            value: Any | None = None,
            done: None | None = None,
            noMsg: None | None = None,
        ) -> Channel.Writer.WriteifspaceRequest: ...

    StartupInfoBuilder: TypeAlias = StartupInfo.Builder
    StartupInfoReader: TypeAlias = StartupInfo.Reader
    class StartupInfo:
        class Reader:
            @property
            def bufferSize(self) -> int: ...
            @property
            def closeSemantics(self) -> Channel.CloseSemantics: ...
            @property
            def channelSR(self) -> str: ...
            @property
            def readerSRs(self) -> Sequence[str]: ...
            @property
            def writerSRs(self) -> Sequence[str]: ...
            @property
            def channel(self) -> ChannelClient: ...
            @property
            def readers(self) -> Sequence[Channel.Reader]: ...
            @property
            def writers(self) -> Sequence[Channel.Writer]: ...
            def as_builder(self) -> Channel.StartupInfo.Builder: ...

        class Builder:
            @property
            def bufferSize(self) -> int: ...
            @bufferSize.setter
            def bufferSize(self, value: int) -> None: ...
            @property
            def closeSemantics(self) -> Channel.CloseSemantics: ...
            @closeSemantics.setter
            def closeSemantics(
                self, value: Channel.CloseSemantics | Literal["fbp", "no"]
            ) -> None: ...
            @property
            def channelSR(self) -> str: ...
            @channelSR.setter
            def channelSR(self, value: str) -> None: ...
            @property
            def readerSRs(self) -> Sequence[str]: ...
            @readerSRs.setter
            def readerSRs(self, value: Sequence[str]) -> None: ...
            @property
            def writerSRs(self) -> Sequence[str]: ...
            @writerSRs.setter
            def writerSRs(self, value: Sequence[str]) -> None: ...
            @property
            def channel(self) -> ChannelClient: ...
            @channel.setter
            def channel(self, value: ChannelClient | Channel.Server) -> None: ...
            @property
            def readers(self) -> Sequence[Channel.Reader]: ...
            @readers.setter
            def readers(self, value: Sequence[Channel.Reader]) -> None: ...
            @property
            def writers(self) -> Sequence[Channel.Writer]: ...
            @writers.setter
            def writers(self, value: Sequence[Channel.Writer]) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> Channel.StartupInfo.Builder: ...
            @overload
            def init(
                self: Any, name: Literal["readerSRs"], size: int = ...
            ) -> Sequence[str]: ...
            @overload
            def init(
                self: Any, name: Literal["writerSRs"], size: int = ...
            ) -> Sequence[str]: ...
            @overload
            def init(
                self: Any, name: Literal["readers"], size: int = ...
            ) -> Sequence[Channel.Reader]: ...
            @overload
            def init(
                self: Any, name: Literal["writers"], size: int = ...
            ) -> Sequence[Channel.Writer]: ...
            def init(self: Any, name: str, size: int = ...) -> Any: ...
            def copy(self) -> Channel.StartupInfo.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Channel.StartupInfo.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Channel.StartupInfo.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Channel.StartupInfo.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            bufferSize: int | None = None,
            closeSemantics: Channel.CloseSemantics | Literal["fbp", "no"] | None = None,
            channelSR: str | None = None,
            readerSRs: Sequence[str] | None = None,
            writerSRs: Sequence[str] | None = None,
            channel: ChannelClient | Channel.Server | None = None,
            readers: Sequence[Channel.Reader] | None = None,
            writers: Sequence[Channel.Writer] | None = None,
        ) -> Channel.StartupInfo.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Channel.StartupInfo.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Channel.StartupInfo.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class SetbuffersizeRequest(Protocol):
        size: int
        def send(self) -> None: ...

    class ReaderRequest(Protocol):
        def send(self) -> Channel.ReaderResult: ...

    class ReaderResult(Awaitable[ReaderResult], Protocol):
        r: Channel.ReaderClient

    class WriterRequest(Protocol):
        def send(self) -> Channel.WriterResult: ...

    class WriterResult(Awaitable[WriterResult], Protocol):
        w: Channel.WriterClient

    class EndpointsRequest(Protocol):
        def send(self) -> Channel.EndpointsResult: ...

    class EndpointsResult(Awaitable[EndpointsResult], Protocol):
        r: Channel.ReaderClient
        w: Channel.WriterClient

    class SetautoclosesemanticsRequest(Protocol):
        cs: Channel.CloseSemantics | Literal["fbp", "no"]
        def send(self) -> None: ...

    class CloseRequest(Protocol):
        waitForEmptyBuffer: bool
        def send(self) -> None: ...

    @classmethod
    def _new_client(
        cls, server: Channel.Server | Identifiable.Server | Persistent.Server
    ) -> ChannelClient: ...
    class Server(Identifiable.Server, Persistent.Server):
        class ReaderResultTuple(NamedTuple):
            r: Channel.Reader.Server

        class WriterResultTuple(NamedTuple):
            w: Channel.Writer.Server

        class EndpointsResultTuple(NamedTuple):
            r: Channel.Reader.Server
            w: Channel.Writer.Server

        class SetbuffersizeCallContext(Protocol):
            params: Channel.SetbuffersizeRequest

        class ReaderCallContext(Protocol):
            params: Channel.ReaderRequest
            results: Channel.ReaderResult

        class WriterCallContext(Protocol):
            params: Channel.WriterRequest
            results: Channel.WriterResult

        class EndpointsCallContext(Protocol):
            params: Channel.EndpointsRequest
            results: Channel.EndpointsResult

        class SetautoclosesemanticsCallContext(Protocol):
            params: Channel.SetautoclosesemanticsRequest

        class CloseCallContext(Protocol):
            params: Channel.CloseRequest

        def setBufferSize(
            self,
            size: int,
            _context: Channel.Server.SetbuffersizeCallContext,
            **kwargs: Any,
        ) -> Awaitable[None]: ...
        def setBufferSize_context(
            self, context: Channel.Server.SetbuffersizeCallContext
        ) -> Awaitable[None]: ...
        def reader(
            self, _context: Channel.Server.ReaderCallContext, **kwargs: Any
        ) -> Awaitable[
            Channel.Reader.Server | Channel.Server.ReaderResultTuple | None
        ]: ...
        def reader_context(
            self, context: Channel.Server.ReaderCallContext
        ) -> Awaitable[None]: ...
        def writer(
            self, _context: Channel.Server.WriterCallContext, **kwargs: Any
        ) -> Awaitable[
            Channel.Writer.Server | Channel.Server.WriterResultTuple | None
        ]: ...
        def writer_context(
            self, context: Channel.Server.WriterCallContext
        ) -> Awaitable[None]: ...
        def endpoints(
            self, _context: Channel.Server.EndpointsCallContext, **kwargs: Any
        ) -> Awaitable[Channel.Server.EndpointsResultTuple | None]: ...
        def endpoints_context(
            self, context: Channel.Server.EndpointsCallContext
        ) -> Awaitable[None]: ...
        def setAutoCloseSemantics(
            self,
            cs: Channel.CloseSemantics | Literal["fbp", "no"],
            _context: Channel.Server.SetautoclosesemanticsCallContext,
            **kwargs: Any,
        ) -> Awaitable[None]: ...
        def setAutoCloseSemantics_context(
            self, context: Channel.Server.SetautoclosesemanticsCallContext
        ) -> Awaitable[None]: ...
        def close(
            self,
            waitForEmptyBuffer: bool,
            _context: Channel.Server.CloseCallContext,
            **kwargs: Any,
        ) -> Awaitable[None]: ...
        def close_context(
            self, context: Channel.Server.CloseCallContext
        ) -> Awaitable[None]: ...

class ChannelClient(IdentifiableClient, PersistentClient):
    def setBufferSize(self, size: int | None = None) -> None: ...
    def reader(self) -> Channel.ReaderResult: ...
    def writer(self) -> Channel.WriterResult: ...
    def endpoints(self) -> Channel.EndpointsResult: ...
    def setAutoCloseSemantics(
        self, cs: Channel.CloseSemantics | Literal["fbp", "no"] | None = None
    ) -> None: ...
    def close(self, waitForEmptyBuffer: bool | None = None) -> None: ...
    def setBufferSize_request(
        self, size: int | None = None
    ) -> Channel.SetbuffersizeRequest: ...
    def reader_request(self) -> Channel.ReaderRequest: ...
    def writer_request(self) -> Channel.WriterRequest: ...
    def endpoints_request(self) -> Channel.EndpointsRequest: ...
    def setAutoCloseSemantics_request(
        self, cs: Channel.CloseSemantics | Literal["fbp", "no"] | None = None
    ) -> Channel.SetautoclosesemanticsRequest: ...
    def close_request(
        self, waitForEmptyBuffer: bool | None = None
    ) -> Channel.CloseRequest: ...

class StartChannelsService:
    ParamsBuilder: TypeAlias = Params.Builder
    ParamsReader: TypeAlias = Params.Reader
    class Params:
        class Reader:
            @property
            def name(self) -> str: ...
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
            def as_builder(self) -> StartChannelsService.Params.Builder: ...

        class Builder:
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
            def readerSrts(self) -> Sequence[str]: ...
            @readerSrts.setter
            def readerSrts(self, value: Sequence[str]) -> None: ...
            @property
            def writerSrts(self) -> Sequence[str]: ...
            @writerSrts.setter
            def writerSrts(self, value: Sequence[str]) -> None: ...
            @property
            def bufferSize(self) -> int: ...
            @bufferSize.setter
            def bufferSize(self, value: int) -> None: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> StartChannelsService.Params.Builder: ...
            @overload
            def init(
                self: Any, name: Literal["readerSrts"], size: int = ...
            ) -> Sequence[str]: ...
            @overload
            def init(
                self: Any, name: Literal["writerSrts"], size: int = ...
            ) -> Sequence[str]: ...
            def init(self: Any, name: str, size: int = ...) -> Any: ...
            def copy(self) -> StartChannelsService.Params.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> StartChannelsService.Params.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[StartChannelsService.Params.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> StartChannelsService.Params.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            name: str | None = None,
            noOfChannels: int | None = None,
            noOfReaders: int | None = None,
            noOfWriters: int | None = None,
            readerSrts: Sequence[str] | None = None,
            writerSrts: Sequence[str] | None = None,
            bufferSize: int | None = None,
        ) -> StartChannelsService.Params.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> StartChannelsService.Params.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> StartChannelsService.Params.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

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
        ) -> Sequence[str]: ...
        @overload
        def init(
            self, name: Literal["writerSrts"], size: int = ...
        ) -> Sequence[str]: ...
        @overload
        def init(self, name: str, size: int = ...) -> Any: ...
        def send(self) -> StartChannelsService.StartResult: ...

    class StartResult(Awaitable[StartResult], Protocol):
        startupInfos: Sequence[Channel.StartupInfo.Builder | Channel.StartupInfo.Reader]
        stop: Any

    @classmethod
    def _new_client(
        cls, server: StartChannelsService.Server | Identifiable.Server
    ) -> StartChannelsServiceClient: ...
    class Server(Identifiable.Server):
        class StartResultTuple(NamedTuple):
            startupInfos: Sequence[Channel.StartupInfo]

        class StartCallContext(Protocol):
            params: StartChannelsService.StartRequest
            results: StartChannelsService.StartResult

        def start(
            self,
            name: str,
            noOfChannels: int,
            noOfReaders: int,
            noOfWriters: int,
            readerSrts: Sequence[str],
            writerSrts: Sequence[str],
            bufferSize: int,
            _context: StartChannelsService.Server.StartCallContext,
            **kwargs: Any,
        ) -> Awaitable[StartChannelsService.Server.StartResultTuple | None]: ...
        def start_context(
            self, context: StartChannelsService.Server.StartCallContext
        ) -> Awaitable[None]: ...

class StartChannelsServiceClient(IdentifiableClient):
    def start(
        self,
        name: str | None = None,
        noOfChannels: int | None = None,
        noOfReaders: int | None = None,
        noOfWriters: int | None = None,
        readerSrts: Sequence[str] | None = None,
        writerSrts: Sequence[str] | None = None,
        bufferSize: int | None = None,
    ) -> StartChannelsService.StartResult: ...
    def start_request(
        self,
        name: str | None = None,
        noOfChannels: int | None = None,
        noOfReaders: int | None = None,
        noOfWriters: int | None = None,
        readerSrts: Sequence[str] | None = None,
        writerSrts: Sequence[str] | None = None,
        bufferSize: int | None = None,
    ) -> StartChannelsService.StartRequest: ...

PortInfosBuilder: TypeAlias = PortInfos.Builder
PortInfosReader: TypeAlias = PortInfos.Reader

class PortInfos:
    NameAndSRBuilder: TypeAlias = NameAndSR.Builder
    NameAndSRReader: TypeAlias = NameAndSR.Reader
    class NameAndSR:
        class Reader:
            @property
            def name(self) -> str: ...
            @property
            def sr(self) -> str: ...
            @property
            def srs(self) -> Sequence[str]: ...
            def which(self) -> Literal["sr", "srs"]: ...
            def as_builder(self) -> PortInfos.NameAndSR.Builder: ...

        class Builder:
            @property
            def name(self) -> str: ...
            @name.setter
            def name(self, value: str) -> None: ...
            @property
            def sr(self) -> str: ...
            @sr.setter
            def sr(self, value: str) -> None: ...
            @property
            def srs(self) -> Sequence[str]: ...
            @srs.setter
            def srs(self, value: Sequence[str]) -> None: ...
            def which(self) -> Literal["sr", "srs"]: ...
            @staticmethod
            def from_dict(
                dictionary: dict[str, Any],
            ) -> PortInfos.NameAndSR.Builder: ...
            def init(self, name: Literal["srs"], size: int = ...) -> Sequence[str]: ...
            def copy(self) -> PortInfos.NameAndSR.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> PortInfos.NameAndSR.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        def which(self) -> Literal["sr", "srs"]: ...
        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[PortInfos.NameAndSR.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> PortInfos.NameAndSR.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            name: str | None = None,
            sr: str | None = None,
            srs: Sequence[str] | None = None,
        ) -> PortInfos.NameAndSR.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> PortInfos.NameAndSR.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> PortInfos.NameAndSR.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Reader:
        @property
        def inPorts(self) -> Sequence[PortInfos.NameAndSR.Reader]: ...
        @property
        def outPorts(self) -> Sequence[PortInfos.NameAndSR.Reader]: ...
        def as_builder(self) -> PortInfos.Builder: ...

    class Builder:
        @property
        def inPorts(self) -> Sequence[PortInfos.NameAndSR.Builder]: ...
        @inPorts.setter
        def inPorts(
            self,
            value: Sequence[PortInfos.NameAndSR.Builder | PortInfos.NameAndSR.Reader]
            | Sequence[dict[str, Any]],
        ) -> None: ...
        @property
        def outPorts(self) -> Sequence[PortInfos.NameAndSR.Builder]: ...
        @outPorts.setter
        def outPorts(
            self,
            value: Sequence[PortInfos.NameAndSR.Builder | PortInfos.NameAndSR.Reader]
            | Sequence[dict[str, Any]],
        ) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> PortInfos.Builder: ...
        @overload
        def init(
            self: Any, name: Literal["inPorts"], size: int = ...
        ) -> Sequence[PortInfos.NameAndSR.Builder]: ...
        @overload
        def init(
            self: Any, name: Literal["outPorts"], size: int = ...
        ) -> Sequence[PortInfos.NameAndSR.Builder]: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        def copy(self) -> PortInfos.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> PortInfos.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    @contextmanager
    @staticmethod
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[PortInfos.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> PortInfos.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        inPorts: Sequence[PortInfos.NameAndSR.Builder]
        | Sequence[dict[str, Any]]
        | None = None,
        outPorts: Sequence[PortInfos.NameAndSR.Builder]
        | Sequence[dict[str, Any]]
        | None = None,
    ) -> PortInfos.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> PortInfos.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> PortInfos.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...

ComponentBuilder: TypeAlias = Component.Builder
ComponentReader: TypeAlias = Component.Reader

class Component:
    class Runnable:
        class StartRequest(Protocol):
            portInfosReaderSr: str
            name: str
            def send(self) -> Component.Runnable.StartResult: ...

        class StartResult(Awaitable[StartResult], Protocol):
            success: bool

        class StopRequest(Protocol):
            def send(self) -> Component.Runnable.StopResult: ...

        class StopResult(Awaitable[StopResult], Protocol):
            success: bool

        @classmethod
        def _new_client(
            cls, server: Component.Runnable.Server | Identifiable.Server
        ) -> Component.RunnableClient: ...
        class Server(Identifiable.Server):
            class StartResultTuple(NamedTuple):
                success: bool

            class StopResultTuple(NamedTuple):
                success: bool

            class StartCallContext(Protocol):
                params: Component.Runnable.StartRequest
                results: Component.Runnable.StartResult

            class StopCallContext(Protocol):
                params: Component.Runnable.StopRequest
                results: Component.Runnable.StopResult

            def start(
                self,
                portInfosReaderSr: str,
                name: str,
                _context: Component.Runnable.Server.StartCallContext,
                **kwargs: Any,
            ) -> Awaitable[
                bool | Component.Runnable.Server.StartResultTuple | None
            ]: ...
            def start_context(
                self, context: Component.Runnable.Server.StartCallContext
            ) -> Awaitable[None]: ...
            def stop(
                self, _context: Component.Runnable.Server.StopCallContext, **kwargs: Any
            ) -> Awaitable[bool | Component.Runnable.Server.StopResultTuple | None]: ...
            def stop_context(
                self, context: Component.Runnable.Server.StopCallContext
            ) -> Awaitable[None]: ...

    class RunnableClient(IdentifiableClient):
        def start(
            self, portInfosReaderSr: str | None = None, name: str | None = None
        ) -> Component.Runnable.StartResult: ...
        def stop(self) -> Component.Runnable.StopResult: ...
        def start_request(
            self, portInfosReaderSr: str | None = None, name: str | None = None
        ) -> Component.Runnable.StartRequest: ...
        def stop_request(self) -> Component.Runnable.StopRequest: ...

    class ComponentType(Enum):
        standard = "standard"
        iip = "iip"
        subflow = "subflow"
        view = "view"

    PortBuilder: TypeAlias = Port.Builder
    PortReader: TypeAlias = Port.Reader
    class Port:
        class PortType(Enum):
            standard = "standard"

        class ContentType(Enum):
            structuredText = "structuredText"

        class Reader:
            @property
            def name(self) -> str: ...
            @property
            def contentType(self) -> str: ...
            @property
            def type(self) -> Component.Port.PortType: ...
            def as_builder(self) -> Component.Port.Builder: ...

        class Builder:
            @property
            def name(self) -> str: ...
            @name.setter
            def name(self, value: str) -> None: ...
            @property
            def contentType(self) -> str: ...
            @contentType.setter
            def contentType(self, value: str) -> None: ...
            @property
            def type(self) -> Component.Port.PortType: ...
            @type.setter
            def type(
                self, value: Component.Port.PortType | Literal["standard"]
            ) -> None: ...
            @staticmethod
            def from_dict(dictionary: dict[str, Any]) -> Component.Port.Builder: ...
            def copy(self) -> Component.Port.Builder: ...
            def to_bytes(self) -> bytes: ...
            def to_bytes_packed(self) -> bytes: ...
            def to_segments(self) -> list[bytes]: ...
            def as_reader(self) -> Component.Port.Reader: ...
            @staticmethod
            def write(file: BufferedWriter) -> None: ...
            @staticmethod
            def write_packed(file: BufferedWriter) -> None: ...

        @contextmanager
        @staticmethod
        def from_bytes(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Iterator[Component.Port.Reader]: ...
        @staticmethod
        def from_bytes_packed(
            data: bytes,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Component.Port.Reader: ...
        @staticmethod
        def new_message(
            num_first_segment_words: int | None = None,
            allocate_seg_callable: Any = None,
            name: str | None = None,
            contentType: str | None = None,
            type: Component.Port.PortType | Literal["standard"] | None = None,
        ) -> Component.Port.Builder: ...
        @staticmethod
        def read(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Component.Port.Reader: ...
        @staticmethod
        def read_packed(
            file: BinaryIO,
            traversal_limit_in_words: int | None = ...,
            nesting_limit: int | None = ...,
        ) -> Component.Port.Reader: ...
        def to_dict(self) -> dict[str, Any]: ...

    class Reader:
        @property
        def info(self) -> IdInformation.Reader: ...
        @property
        def type(self) -> Component.ComponentType: ...
        @property
        def inPorts(self) -> Sequence[Component.Port.Reader]: ...
        @property
        def outPorts(self) -> Sequence[Component.Port.Reader]: ...
        @property
        def run(self) -> Component.RunnableClient: ...
        @property
        def defaultConfig(self) -> str: ...
        def as_builder(self) -> Component.Builder: ...

    class Builder:
        @property
        def info(self) -> IdInformation.Builder: ...
        @info.setter
        def info(
            self, value: IdInformation.Builder | IdInformation.Reader | dict[str, Any]
        ) -> None: ...
        @property
        def type(self) -> Component.ComponentType: ...
        @type.setter
        def type(
            self,
            value: Component.ComponentType
            | Literal["standard", "iip", "subflow", "view"],
        ) -> None: ...
        @property
        def inPorts(self) -> Sequence[Component.Port.Builder]: ...
        @inPorts.setter
        def inPorts(
            self,
            value: Sequence[Component.Port.Builder | Component.Port.Reader]
            | Sequence[dict[str, Any]],
        ) -> None: ...
        @property
        def outPorts(self) -> Sequence[Component.Port.Builder]: ...
        @outPorts.setter
        def outPorts(
            self,
            value: Sequence[Component.Port.Builder | Component.Port.Reader]
            | Sequence[dict[str, Any]],
        ) -> None: ...
        @property
        def run(self) -> Component.RunnableClient: ...
        @run.setter
        def run(
            self, value: Component.RunnableClient | Component.Runnable.Server
        ) -> None: ...
        @property
        def defaultConfig(self) -> str: ...
        @defaultConfig.setter
        def defaultConfig(self, value: str) -> None: ...
        @staticmethod
        def from_dict(dictionary: dict[str, Any]) -> Component.Builder: ...
        @overload
        def init(self: Any, name: Literal["info"]) -> IdInformation.Builder: ...
        @overload
        def init(
            self: Any, name: Literal["inPorts"], size: int = ...
        ) -> Sequence[Component.Port.Builder]: ...
        @overload
        def init(
            self: Any, name: Literal["outPorts"], size: int = ...
        ) -> Sequence[Component.Port.Builder]: ...
        def init(self: Any, name: str, size: int = ...) -> Any: ...
        def copy(self) -> Component.Builder: ...
        def to_bytes(self) -> bytes: ...
        def to_bytes_packed(self) -> bytes: ...
        def to_segments(self) -> list[bytes]: ...
        def as_reader(self) -> Component.Reader: ...
        @staticmethod
        def write(file: BufferedWriter) -> None: ...
        @staticmethod
        def write_packed(file: BufferedWriter) -> None: ...

    def init(self, name: Literal["info"]) -> IdInformation: ...
    @contextmanager
    @staticmethod
    def from_bytes(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Iterator[Component.Reader]: ...
    @staticmethod
    def from_bytes_packed(
        data: bytes,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Component.Reader: ...
    @staticmethod
    def new_message(
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Any = None,
        info: IdInformation.Builder | dict[str, Any] | None = None,
        type: Component.ComponentType
        | Literal["standard", "iip", "subflow", "view"]
        | None = None,
        inPorts: Sequence[Component.Port.Builder]
        | Sequence[dict[str, Any]]
        | None = None,
        outPorts: Sequence[Component.Port.Builder]
        | Sequence[dict[str, Any]]
        | None = None,
        run: Component.RunnableClient | Component.Runnable.Server | None = None,
        defaultConfig: str | None = None,
    ) -> Component.Builder: ...
    @staticmethod
    def read(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Component.Reader: ...
    @staticmethod
    def read_packed(
        file: BinaryIO,
        traversal_limit_in_words: int | None = ...,
        nesting_limit: int | None = ...,
    ) -> Component.Reader: ...
    def to_dict(self) -> dict[str, Any]: ...
