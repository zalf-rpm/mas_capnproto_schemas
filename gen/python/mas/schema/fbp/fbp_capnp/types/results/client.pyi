"""Client result helper types for `fbp.capnp`."""

from collections.abc import Awaitable
from typing import Literal, Protocol

from capnp.lib.capnp import (
    _DynamicObjectReader,
)

from mas.schema.fbp.fbp_capnp.types import clients as clients
from mas.schema.fbp.fbp_capnp.types import enums as enums
from mas.schema.fbp.fbp_capnp.types import readers as readers
from mas.schema.service.service_capnp.types.clients import StoppableClient

class ReadResult(Awaitable[ReadResult], Protocol):
    value: _DynamicObjectReader
    done: None
    noMsg: None
    def which(self) -> Literal["value", "done", "noMsg"]: ...

class ReaderCloseResult(Awaitable[None], Protocol): ...

class ReadifmsgResult(Awaitable[ReadifmsgResult], Protocol):
    value: _DynamicObjectReader
    done: None
    noMsg: None
    def which(self) -> Literal["value", "done", "noMsg"]: ...

class WriteResult(Awaitable[None], Protocol): ...
class WriterCloseResult(Awaitable[None], Protocol): ...

class WriteifspaceResult(Awaitable[WriteifspaceResult], Protocol):
    success: bool

class UnregResult(Awaitable[UnregResult], Protocol):
    success: bool

class StatusResult(Awaitable[None], Protocol): ...
class SetbuffersizeResult(Awaitable[None], Protocol): ...

class ReaderResult(Awaitable[ReaderResult], Protocol):
    r: clients.ReaderClient

class WriterResult(Awaitable[WriterResult], Protocol):
    w: clients.WriterClient

class EndpointsResult(Awaitable[EndpointsResult], Protocol):
    r: clients.ReaderClient
    w: clients.WriterClient

class SetautoclosesemanticsResult(Awaitable[None], Protocol): ...
class ChannelCloseResult(Awaitable[None], Protocol): ...

class RegisterstatscallbackResult(Awaitable[RegisterstatscallbackResult], Protocol):
    unregisterCallback: clients.UnregisterClient

class StartChannelsServiceStartResult(
    Awaitable[StartChannelsServiceStartResult],
    Protocol,
):
    startupInfos: readers.StartupInfoListReader
    stop: StoppableClient

class RunnableFactoryCreateResult(Awaitable[RunnableFactoryCreateResult], Protocol):
    out: clients.RunnableClient

class StoppedResult(Awaitable[None], Protocol): ...

class RunnableStartResult(Awaitable[RunnableStartResult], Protocol):
    success: bool

class RunnableStopResult(Awaitable[RunnableStopResult], Protocol):
    success: bool

class ProcessFactoryCreateResult(Awaitable[ProcessFactoryCreateResult], Protocol):
    out: clients.ProcessClient

class StatechangedResult(Awaitable[None], Protocol): ...

class InportsResult(Awaitable[InportsResult], Protocol):
    ports: readers.PortListReader

class ConnectinportResult(Awaitable[ConnectinportResult], Protocol):
    connected: bool

class OutportsResult(Awaitable[OutportsResult], Protocol):
    ports: readers.PortListReader

class ConnectoutportResult(Awaitable[ConnectoutportResult], Protocol):
    connected: bool

class ConfigentriesResult(Awaitable[ConfigentriesResult], Protocol):
    config: readers.ConfigEntryListReader

class ProcessStartResult(Awaitable[None], Protocol): ...
class ProcessStopResult(Awaitable[None], Protocol): ...
class SetconfigentryResult(Awaitable[None], Protocol): ...

class StateResult(Awaitable[StateResult], Protocol):
    currentState: enums.ProcessStateEnum
