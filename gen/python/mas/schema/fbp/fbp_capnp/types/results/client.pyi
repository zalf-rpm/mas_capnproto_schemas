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

class AckResult(Awaitable[None], Protocol): ...

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

class ReadleasedResult(Awaitable[ReadleasedResult], Protocol):
    msg: readers.MsgReader
    lease: clients.LeaseClient

class WriteResult(Awaitable[None], Protocol): ...
class WriterCloseResult(Awaitable[None], Protocol): ...

class WriteifspaceResult(Awaitable[WriteifspaceResult], Protocol):
    success: bool

class ChannelStatsCallbackUnregisterUnregResult(
    Awaitable[ChannelStatsCallbackUnregisterUnregResult],
    Protocol,
):
    success: bool

class StatusResult(Awaitable[None], Protocol): ...

class ChannelObserverUnregisterUnregResult(
    Awaitable[ChannelObserverUnregisterUnregResult],
    Protocol,
):
    success: bool

class SawResult(Awaitable[None], Protocol): ...
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
    unregisterCallback: clients.ChannelStatsCallbackUnregisterClient

class ObserveResult(Awaitable[ObserveResult], Protocol):
    unregister: clients.ChannelObserverUnregisterClient

class PauseResult(Awaitable[None], Protocol): ...
class ResumeResult(Awaitable[None], Protocol): ...

class StepResult(Awaitable[StepResult], Protocol):
    delivered: int

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

class ProcessResult(Awaitable[ProcessResult], Protocol):
    process: clients.ProcessClient

class ProcessHandleCloseResult(Awaitable[ProcessHandleCloseResult], Protocol):
    closed: bool

class AliveResult(Awaitable[AliveResult], Protocol):
    alive: bool

class ProcessFactoryCreateResult(Awaitable[ProcessFactoryCreateResult], Protocol):
    out: clients.ProcessHandleClient

class DisconnectResult(Awaitable[DisconnectResult], Protocol):
    disconnected: bool

class StatechangedResult(Awaitable[None], Protocol): ...
class ActivitychangedResult(Awaitable[None], Protocol): ...

class InportsResult(Awaitable[InportsResult], Protocol):
    ports: readers.PortListReader

class ConnectinportResult(Awaitable[ConnectinportResult], Protocol):
    connected: bool
    disconnect: clients.DisconnectClient

class OutportsResult(Awaitable[OutportsResult], Protocol):
    ports: readers.PortListReader

class ConnectoutportResult(Awaitable[ConnectoutportResult], Protocol):
    connected: bool
    disconnect: clients.DisconnectClient

class ConfigentriesResult(Awaitable[ConfigentriesResult], Protocol):
    config: readers.ConfigEntryListReader

class ProcessStartResult(Awaitable[ProcessStartResult], Protocol):
    started: bool

class ProcessStopResult(Awaitable[ProcessStopResult], Protocol):
    stopped: bool

class SetconfigentryResult(Awaitable[None], Protocol): ...

class StateResult(Awaitable[StateResult], Protocol):
    currentState: enums.ProcessStateEnum

class LastrunResult(Awaitable[LastrunResult], Protocol):
    info: readers.RunInfoReader

class ActivityResult(Awaitable[ActivityResult], Protocol):
    currentActivity: readers.ActivityInfoReader
