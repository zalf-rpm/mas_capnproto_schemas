"""Module helper types for `fbp.capnp`."""

from collections.abc import Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from typing import IO, Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicCapabilityServer,
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
from mas.schema.common.common_capnp.types.modules import (
    _IdentifiableInterfaceModule,
)
from mas.schema.common.common_capnp.types.readers import ValueReader
from mas.schema.persistence.persistence_capnp.types.builders import SturdyRefBuilder
from mas.schema.persistence.persistence_capnp.types.modules import (
    _GatewayRegistrableInterfaceModule,
    _PersistentInterfaceModule,
)
from mas.schema.persistence.persistence_capnp.types.readers import SturdyRefReader

from . import _all as _all

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
            value: _all.AnyPointer | None = None,
            **kwargs: object,
        ) -> _all.KVBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.KVReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.KVReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.KVBuilder]: ...
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
        ) -> _all.KVReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.KVReader: ...

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
        attributes: _all.KVListBuilder | dict[str, Any] | None = None,
        content: _all.AnyPointer | None = None,
        type: _all.IPTypeEnum | None = None,
        **kwargs: object,
    ) -> _all.IPBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.IPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.IPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.IPBuilder]: ...
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
    ) -> _all.IPReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.IPReader: ...

class _IIPStructModule(_StructModule):
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        content: _all.AnyPointer | None = None,
        **kwargs: object,
    ) -> _all.IIPBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.IIPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.IIPReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.IIPBuilder]: ...
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
    ) -> _all.IIPReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.IIPReader: ...

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
            value: _all.AnyPointer | None = None,
            done: None | None = None,
            noMsg: None | None = None,
            **kwargs: object,
        ) -> _all.MsgBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.MsgReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.MsgReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.MsgBuilder]: ...
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
        ) -> _all.MsgReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.MsgReader: ...

    Msg: _MsgStructModule
    class _ReaderInterfaceModule(
        _IdentifiableInterfaceModule,
        _PersistentInterfaceModule,
    ):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.ReaderClient: ...
        class Server(
            _IdentifiableInterfaceModule.Server,
            _PersistentInterfaceModule.Server,
        ):
            def read(
                self,
                _context: _all.ReadCallContext,
                **kwargs: object,
            ) -> Awaitable[_all.ReadResultTuple | None]: ...
            def read_context(
                self,
                context: _all.ReadCallContext,
            ) -> Awaitable[None]: ...
            def close(
                self,
                _context: _all.ReaderCloseCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def close_context(
                self,
                context: _all.ReaderCloseCallContext,
            ) -> Awaitable[None]: ...
            def readIfMsg(
                self,
                _context: _all.ReadifmsgCallContext,
                **kwargs: object,
            ) -> Awaitable[_all.ReadifmsgResultTuple | None]: ...
            def readIfMsg_context(
                self,
                context: _all.ReadifmsgCallContext,
            ) -> Awaitable[None]: ...

    Reader: _ReaderInterfaceModule
    type ReaderServer = _ChannelInterfaceModule._ReaderInterfaceModule.Server
    class _WriterInterfaceModule(
        _IdentifiableInterfaceModule,
        _PersistentInterfaceModule,
    ):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.WriterClient: ...
        class Server(
            _IdentifiableInterfaceModule.Server,
            _PersistentInterfaceModule.Server,
        ):
            def write_context(
                self,
                context: _all.WriteCallContext,
            ) -> Awaitable[None]: ...
            def close(
                self,
                _context: _all.WriterCloseCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def close_context(
                self,
                context: _all.WriterCloseCallContext,
            ) -> Awaitable[None]: ...
            def writeIfSpace_context(
                self,
                context: _all.WriteifspaceCallContext,
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
            closeSemantics: _all.ChannelCloseSemanticsEnum | None = None,
            channelSR: SturdyRefBuilder | dict[str, Any] | None = None,
            readerSRs: _all.SturdyRefListBuilder | dict[str, Any] | None = None,
            writerSRs: _all.SturdyRefListBuilder | dict[str, Any] | None = None,
            channel: _all.ChannelClient | _ChannelInterfaceModule.Server | None = None,
            readers: _all.ReaderClientListBuilder | dict[str, Any] | None = None,
            writers: _all.WriterClientListBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> _all.StartupInfoBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.StartupInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.StartupInfoReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.StartupInfoBuilder]: ...
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
        ) -> _all.StartupInfoReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.StartupInfoReader: ...

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
            ) -> _all.StatsBuilder: ...
            @override
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> AbstractContextManager[_all.StatsReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[False],
            ) -> AbstractContextManager[_all.StatsReader]: ...
            @overload
            def from_bytes(
                self,
                buf: bytes,
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
                *,
                builder: Literal[True],
            ) -> AbstractContextManager[_all.StatsBuilder]: ...
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
            ) -> _all.StatsReader: ...
            @override
            def read_packed(
                self,
                file: IO[str] | IO[bytes],
                traversal_limit_in_words: int | None = None,
                nesting_limit: int | None = None,
            ) -> _all.StatsReader: ...

        Stats: _StatsStructModule
        class _UnregisterInterfaceModule(_InterfaceModule):
            @override
            def _new_client(
                self,
                server: _DynamicCapabilityServer,
            ) -> _all.UnregisterClient: ...
            class Server(_DynamicCapabilityServer):
                def unreg(
                    self,
                    _context: _all.UnregCallContext,
                    **kwargs: object,
                ) -> Awaitable[bool | _all.UnregResultTuple | None]: ...
                def unreg_context(
                    self,
                    context: _all.UnregCallContext,
                ) -> Awaitable[None]: ...

        Unregister: _UnregisterInterfaceModule
        type UnregisterServer = _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.StatsCallbackClient: ...
        class Server(_DynamicCapabilityServer):
            def status(
                self,
                stats: _all.StatsReader,
                _context: _all.StatusCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def status_context(
                self,
                context: _all.StatusCallContext,
            ) -> Awaitable[None]: ...

    StatsCallback: _StatsCallbackInterfaceModule
    type StatsCallbackServer = (
        _ChannelInterfaceModule._StatsCallbackInterfaceModule.Server
    )
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.ChannelClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _PersistentInterfaceModule.Server,
    ):
        def setBufferSize(
            self,
            size: int,
            _context: _all.SetbuffersizeCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def setBufferSize_context(
            self,
            context: _all.SetbuffersizeCallContext,
        ) -> Awaitable[None]: ...
        def reader(
            self,
            _context: _all.ReaderCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _ChannelInterfaceModule._ReaderInterfaceModule.Server
            | _all.ReaderClient
            | _all.ReaderResultTuple
            | None
        ]: ...
        def reader_context(
            self,
            context: _all.ReaderCallContext,
        ) -> Awaitable[None]: ...
        def writer(
            self,
            _context: _all.WriterCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _ChannelInterfaceModule._WriterInterfaceModule.Server
            | _all.WriterClient
            | _all.WriterResultTuple
            | None
        ]: ...
        def writer_context(
            self,
            context: _all.WriterCallContext,
        ) -> Awaitable[None]: ...
        def endpoints(
            self,
            _context: _all.EndpointsCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.EndpointsResultTuple | None]: ...
        def endpoints_context(
            self,
            context: _all.EndpointsCallContext,
        ) -> Awaitable[None]: ...
        def setAutoCloseSemantics(
            self,
            cs: _all.ChannelCloseSemanticsEnum,
            _context: _all.SetautoclosesemanticsCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def setAutoCloseSemantics_context(
            self,
            context: _all.SetautoclosesemanticsCallContext,
        ) -> Awaitable[None]: ...
        def close(
            self,
            waitForEmptyBuffer: bool,
            _context: _all.ChannelCloseCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def close_context(
            self,
            context: _all.ChannelCloseCallContext,
        ) -> Awaitable[None]: ...
        def registerStatsCallback(
            self,
            callback: _all.StatsCallbackClient,
            updateIntervalInMs: int,
            _context: _all.RegisterstatscallbackCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server
            | _all.UnregisterClient
            | _all.RegisterstatscallbackResultTuple
            | None
        ]: ...
        def registerStatsCallback_context(
            self,
            context: _all.RegisterstatscallbackCallContext,
        ) -> Awaitable[None]: ...

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
            readerSrts: _all.TextListBuilder | dict[str, Any] | None = None,
            writerSrts: _all.TextListBuilder | dict[str, Any] | None = None,
            bufferSize: int | None = None,
            **kwargs: object,
        ) -> _all.ParamsBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.ParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.ParamsReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.ParamsBuilder]: ...
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
        ) -> _all.ParamsReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.ParamsReader: ...

    Params: _ParamsStructModule
    @override
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _all.StartChannelsServiceClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def start(
            self,
            name: str,
            noOfChannels: int,
            noOfReaders: int,
            noOfWriters: int,
            readerSrts: _all.TextListReader,
            writerSrts: _all.TextListReader,
            bufferSize: int,
            _context: _all.StartChannelsServiceStartCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.StartChannelsServiceStartResultTuple | None]: ...
        def start_context(
            self,
            context: _all.StartChannelsServiceStartCallContext,
        ) -> Awaitable[None]: ...

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
            srs: _all.SturdyRefListBuilder | dict[str, Any] | None = None,
            **kwargs: object,
        ) -> _all.NameAndSRBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.NameAndSRReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.NameAndSRReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.NameAndSRBuilder]: ...
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
        ) -> _all.NameAndSRReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.NameAndSRReader: ...

    NameAndSR: _NameAndSRStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        inPorts: _all.NameAndSRListBuilder | dict[str, Any] | None = None,
        outPorts: _all.NameAndSRListBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.PortInfosBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.PortInfosReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.PortInfosReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.PortInfosBuilder]: ...
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
    ) -> _all.PortInfosReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.PortInfosReader: ...

class _RunnableInterfaceModule(_IdentifiableInterfaceModule):
    class _FactoryInterfaceModule(_IdentifiableInterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.RunnableFactoryClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def create(
                self,
                _context: _all.RunnableFactoryCreateCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _RunnableInterfaceModule.Server
                | _all.RunnableClient
                | _all.RunnableFactoryCreateResultTuple
                | None
            ]: ...
            def create_context(
                self,
                context: _all.RunnableFactoryCreateCallContext,
            ) -> Awaitable[None]: ...

    Factory: _FactoryInterfaceModule
    type FactoryServer = _RunnableInterfaceModule._FactoryInterfaceModule.Server
    class _StoppedCallbackInterfaceModule(_InterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.StoppedCallbackClient: ...
        class Server(_DynamicCapabilityServer):
            def stopped(
                self,
                _context: _all.StoppedCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def stopped_context(
                self,
                context: _all.StoppedCallContext,
            ) -> Awaitable[None]: ...

    StoppedCallback: _StoppedCallbackInterfaceModule
    type StoppedCallbackServer = (
        _RunnableInterfaceModule._StoppedCallbackInterfaceModule.Server
    )
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.RunnableClient: ...
    class Server(_IdentifiableInterfaceModule.Server):
        def start(
            self,
            portInfosReaderSr: SturdyRefReader,
            name: str,
            stoppedCb: _all.StoppedCallbackClient,
            _context: _all.RunnableStartCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | _all.RunnableStartResultTuple | None]: ...
        def start_context(
            self,
            context: _all.RunnableStartCallContext,
        ) -> Awaitable[None]: ...
        def stop(
            self,
            _context: _all.RunnableStopCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | _all.RunnableStopResultTuple | None]: ...
        def stop_context(
            self,
            context: _all.RunnableStopCallContext,
        ) -> Awaitable[None]: ...

class _ProcessInterfaceModule(
    _IdentifiableInterfaceModule,
    _GatewayRegistrableInterfaceModule,
):
    class _FactoryInterfaceModule(_IdentifiableInterfaceModule):
        @override
        def _new_client(
            self,
            server: _DynamicCapabilityServer,
        ) -> _all.ProcessFactoryClient: ...
        class Server(_IdentifiableInterfaceModule.Server):
            def create(
                self,
                _context: _all.ProcessFactoryCreateCallContext,
                **kwargs: object,
            ) -> Awaitable[
                _ProcessInterfaceModule.Server
                | _all.ProcessClient
                | _all.ProcessFactoryCreateResultTuple
                | None
            ]: ...
            def create_context(
                self,
                context: _all.ProcessFactoryCreateCallContext,
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
        ) -> _all.ConfigEntryBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.ConfigEntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.ConfigEntryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.ConfigEntryBuilder]: ...
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
        ) -> _all.ConfigEntryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.ConfigEntryReader: ...

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
        ) -> _all.StateTransitionClient: ...
        class Server(_DynamicCapabilityServer):
            def stateChanged(
                self,
                old: _all.ProcessStateEnum,
                new: _all.ProcessStateEnum,
                _context: _all.StatechangedCallContext,
                **kwargs: object,
            ) -> Awaitable[None]: ...
            def stateChanged_context(
                self,
                context: _all.StatechangedCallContext,
            ) -> Awaitable[None]: ...

    StateTransition: _StateTransitionInterfaceModule
    type StateTransitionServer = (
        _ProcessInterfaceModule._StateTransitionInterfaceModule.Server
    )
    @override
    def _new_client(self, server: _DynamicCapabilityServer) -> _all.ProcessClient: ...
    class Server(
        _IdentifiableInterfaceModule.Server,
        _GatewayRegistrableInterfaceModule.Server,
    ):
        def inPorts(
            self,
            _context: _all.InportsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.PortListBuilder
            | _all.PortListReader
            | Sequence[Any]
            | _all.InportsResultTuple
            | None
        ]: ...
        def inPorts_context(
            self,
            context: _all.InportsCallContext,
        ) -> Awaitable[None]: ...
        def connectInPort(
            self,
            name: str,
            sturdyRef: SturdyRefReader,
            _context: _all.ConnectinportCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | _all.ConnectinportResultTuple | None]: ...
        def connectInPort_context(
            self,
            context: _all.ConnectinportCallContext,
        ) -> Awaitable[None]: ...
        def outPorts(
            self,
            _context: _all.OutportsCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.PortListBuilder
            | _all.PortListReader
            | Sequence[Any]
            | _all.OutportsResultTuple
            | None
        ]: ...
        def outPorts_context(
            self,
            context: _all.OutportsCallContext,
        ) -> Awaitable[None]: ...
        def connectOutPort(
            self,
            name: str,
            sturdyRef: SturdyRefReader,
            _context: _all.ConnectoutportCallContext,
            **kwargs: object,
        ) -> Awaitable[bool | _all.ConnectoutportResultTuple | None]: ...
        def connectOutPort_context(
            self,
            context: _all.ConnectoutportCallContext,
        ) -> Awaitable[None]: ...
        def configEntries(
            self,
            _context: _all.ConfigentriesCallContext,
            **kwargs: object,
        ) -> Awaitable[
            _all.ConfigEntryListBuilder
            | _all.ConfigEntryListReader
            | Sequence[Any]
            | _all.ConfigentriesResultTuple
            | None
        ]: ...
        def configEntries_context(
            self,
            context: _all.ConfigentriesCallContext,
        ) -> Awaitable[None]: ...
        def start(
            self,
            _context: _all.ProcessStartCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def start_context(
            self,
            context: _all.ProcessStartCallContext,
        ) -> Awaitable[None]: ...
        def stop(
            self,
            _context: _all.ProcessStopCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def stop_context(
            self,
            context: _all.ProcessStopCallContext,
        ) -> Awaitable[None]: ...
        def setConfigEntry(
            self,
            name: str,
            val: ValueReader,
            _context: _all.SetconfigentryCallContext,
            **kwargs: object,
        ) -> Awaitable[None]: ...
        def setConfigEntry_context(
            self,
            context: _all.SetconfigentryCallContext,
        ) -> Awaitable[None]: ...
        def state(
            self,
            transitionCallback: _all.StateTransitionClient,
            _context: _all.StateCallContext,
            **kwargs: object,
        ) -> Awaitable[_all.ProcessStateEnum | _all.StateResultTuple | None]: ...
        def state_context(self, context: _all.StateCallContext) -> Awaitable[None]: ...

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
            type: _all.ComponentPortPortTypeEnum | None = None,
            desc: str | None = None,
            **kwargs: object,
        ) -> _all.PortBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.PortReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.PortReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.PortBuilder]: ...
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
        ) -> _all.PortReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.PortReader: ...

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
            runnable: _all.RunnableFactoryClient
            | _RunnableInterfaceModule._FactoryInterfaceModule.Server
            | None = None,
            process: _all.ProcessFactoryClient
            | _ProcessInterfaceModule._FactoryInterfaceModule.Server
            | None = None,
            **kwargs: object,
        ) -> _all.ComponentFactoryBuilder: ...
        @override
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> AbstractContextManager[_all.ComponentFactoryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[False],
        ) -> AbstractContextManager[_all.ComponentFactoryReader]: ...
        @overload
        def from_bytes(
            self,
            buf: bytes,
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
            *,
            builder: Literal[True],
        ) -> AbstractContextManager[_all.ComponentFactoryBuilder]: ...
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
        ) -> _all.ComponentFactoryReader: ...
        @override
        def read_packed(
            self,
            file: IO[str] | IO[bytes],
            traversal_limit_in_words: int | None = None,
            nesting_limit: int | None = None,
        ) -> _all.ComponentFactoryReader: ...

    ComponentFactory: _ComponentFactoryStructModule
    class Reader(_DynamicStructReader): ...
    class Builder(_DynamicStructBuilder): ...

    @override
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        info: IdInformationBuilder | dict[str, Any] | None = None,
        type: _all.ComponentComponentTypeEnum | None = None,
        inPorts: _all.PortListBuilder | dict[str, Any] | None = None,
        outPorts: _all.PortListBuilder | dict[str, Any] | None = None,
        defaultConfig: StructuredTextBuilder | dict[str, Any] | None = None,
        factory: _all.ComponentFactoryBuilder | dict[str, Any] | None = None,
        **kwargs: object,
    ) -> _all.ComponentBuilder: ...
    @override
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_all.ComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_all.ComponentReader]: ...
    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_all.ComponentBuilder]: ...
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
    ) -> _all.ComponentReader: ...
    @override
    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _all.ComponentReader: ...
