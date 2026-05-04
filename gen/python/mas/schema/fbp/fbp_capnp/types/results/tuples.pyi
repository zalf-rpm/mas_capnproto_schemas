"""Result tuple helper types for `fbp.capnp`."""

from collections.abc import Sequence
from typing import Any, NamedTuple

from mas.schema.fbp.fbp_capnp.types import builders as builders
from mas.schema.fbp.fbp_capnp.types import clients as clients
from mas.schema.fbp.fbp_capnp.types import common as common
from mas.schema.fbp.fbp_capnp.types import enums as enums
from mas.schema.fbp.fbp_capnp.types import modules as modules
from mas.schema.fbp.fbp_capnp.types import readers as readers
from mas.schema.service.service_capnp.types.clients import StoppableClient
from mas.schema.service.service_capnp.types.modules import _StoppableInterfaceModule

class ReadResultTuple(NamedTuple):
    value: common.AnyPointer
    done: None
    noMsg: None

class ReadifmsgResultTuple(NamedTuple):
    value: common.AnyPointer
    done: None
    noMsg: None

class WriteifspaceResultTuple(NamedTuple):
    success: bool

class UnregResultTuple(NamedTuple):
    success: bool

class ReaderResultTuple(NamedTuple):
    r: (
        modules._ChannelInterfaceModule._ReaderInterfaceModule.Server
        | clients.ReaderClient
    )

class WriterResultTuple(NamedTuple):
    w: (
        modules._ChannelInterfaceModule._WriterInterfaceModule.Server
        | clients.WriterClient
    )

class EndpointsResultTuple(NamedTuple):
    r: (
        modules._ChannelInterfaceModule._ReaderInterfaceModule.Server
        | clients.ReaderClient
    )
    w: (
        modules._ChannelInterfaceModule._WriterInterfaceModule.Server
        | clients.WriterClient
    )

class RegisterstatscallbackResultTuple(NamedTuple):
    unregisterCallback: (
        modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient
    )

class StartChannelsServiceStartResultTuple(NamedTuple):
    startupInfos: (
        builders.StartupInfoListBuilder | readers.StartupInfoListReader | Sequence[Any]
    )
    stop: _StoppableInterfaceModule.Server | StoppableClient

class RunnableFactoryCreateResultTuple(NamedTuple):
    out: modules._RunnableInterfaceModule.Server | clients.RunnableClient

class RunnableStartResultTuple(NamedTuple):
    success: bool

class RunnableStopResultTuple(NamedTuple):
    success: bool

class ProcessFactoryCreateResultTuple(NamedTuple):
    out: modules._ProcessInterfaceModule.Server | clients.ProcessClient

class DisconnectResultTuple(NamedTuple):
    disconnected: bool

class InportsResultTuple(NamedTuple):
    ports: builders.PortListBuilder | readers.PortListReader | Sequence[Any]

class ConnectinportResultTuple(NamedTuple):
    connected: bool
    disconnect: (
        modules._ProcessInterfaceModule._DisconnectInterfaceModule.Server
        | clients.DisconnectClient
    )

class OutportsResultTuple(NamedTuple):
    ports: builders.PortListBuilder | readers.PortListReader | Sequence[Any]

class ConnectoutportResultTuple(NamedTuple):
    connected: bool
    disconnect: (
        modules._ProcessInterfaceModule._DisconnectInterfaceModule.Server
        | clients.DisconnectClient
    )

class ConfigentriesResultTuple(NamedTuple):
    config: (
        builders.ConfigEntryListBuilder | readers.ConfigEntryListReader | Sequence[Any]
    )

class StateResultTuple(NamedTuple):
    currentState: enums.ProcessStateEnum

class ProcessCloseResultTuple(NamedTuple):
    closed: bool
