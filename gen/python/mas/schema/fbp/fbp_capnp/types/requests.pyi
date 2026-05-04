"""Request helper types for `fbp.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, Protocol, overload

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
)

from mas.schema.common.common_capnp.types.builders import ValueBuilder
from mas.schema.fbp.fbp_capnp.types import builders as builders
from mas.schema.fbp.fbp_capnp.types import clients as clients
from mas.schema.fbp.fbp_capnp.types import common as common
from mas.schema.fbp.fbp_capnp.types import enums as enums
from mas.schema.fbp.fbp_capnp.types import modules as modules
from mas.schema.fbp.fbp_capnp.types import readers as readers
from mas.schema.fbp.fbp_capnp.types.results import client as results_client
from mas.schema.persistence.persistence_capnp.types.builders import SturdyRefBuilder

class ReadRequest(Protocol):
    def send(self) -> results_client.ReadResult: ...

class ReaderCloseRequest(Protocol):
    def send(self) -> results_client.ReaderCloseResult: ...

class ReadifmsgRequest(Protocol):
    def send(self) -> results_client.ReadifmsgResult: ...

class WriteRequest(Protocol):
    @property
    def value(self) -> _DynamicObjectBuilder: ...
    @value.setter
    def value(self, value: common.AnyPointer) -> None: ...
    done: None
    noMsg: None
    def send(self) -> results_client.WriteResult: ...

class WriterCloseRequest(Protocol):
    def send(self) -> results_client.WriterCloseResult: ...

class WriteifspaceRequest(Protocol):
    @property
    def value(self) -> _DynamicObjectBuilder: ...
    @value.setter
    def value(self, value: common.AnyPointer) -> None: ...
    done: None
    noMsg: None
    def send(self) -> results_client.WriteifspaceResult: ...

class UnregRequest(Protocol):
    def send(self) -> results_client.UnregResult: ...

class StatusRequest(Protocol):
    stats: builders.StatsBuilder
    @overload
    def init(self, name: Literal["stats"]) -> builders.StatsBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.StatusResult: ...

class SetbuffersizeRequest(Protocol):
    size: int
    def send(self) -> results_client.SetbuffersizeResult: ...

class ReaderRequest(Protocol):
    def send(self) -> results_client.ReaderResult: ...

class WriterRequest(Protocol):
    def send(self) -> results_client.WriterResult: ...

class EndpointsRequest(Protocol):
    def send(self) -> results_client.EndpointsResult: ...

class SetautoclosesemanticsRequest(Protocol):
    cs: enums.ChannelCloseSemanticsEnum
    def send(self) -> results_client.SetautoclosesemanticsResult: ...

class ChannelCloseRequest(Protocol):
    waitForEmptyBuffer: bool
    def send(self) -> results_client.ChannelCloseResult: ...

class RegisterstatscallbackRequest(Protocol):
    callback: (
        clients.StatsCallbackClient
        | modules._ChannelInterfaceModule._StatsCallbackInterfaceModule.Server
    )
    updateIntervalInMs: int
    def send(self) -> results_client.RegisterstatscallbackResult: ...

class StartChannelsServiceStartRequest(Protocol):
    name: str
    noOfChannels: int
    noOfReaders: int
    noOfWriters: int
    readerSrts: builders.TextListBuilder | readers.TextListReader | Sequence[Any]
    writerSrts: builders.TextListBuilder | readers.TextListReader | Sequence[Any]
    bufferSize: int
    @overload
    def init(
        self,
        name: Literal["readerSrts"],
        size: int = ...,
    ) -> builders.TextListBuilder: ...
    @overload
    def init(
        self,
        name: Literal["writerSrts"],
        size: int = ...,
    ) -> builders.TextListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.StartChannelsServiceStartResult: ...

class RunnableFactoryCreateRequest(Protocol):
    def send(self) -> results_client.RunnableFactoryCreateResult: ...

class StoppedRequest(Protocol):
    def send(self) -> results_client.StoppedResult: ...

class RunnableStartRequest(Protocol):
    portInfosReaderSr: SturdyRefBuilder
    name: str
    stoppedCb: (
        clients.StoppedCallbackClient
        | modules._RunnableInterfaceModule._StoppedCallbackInterfaceModule.Server
    )
    @overload
    def init(self, name: Literal["portInfosReaderSr"]) -> SturdyRefBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.RunnableStartResult: ...

class RunnableStopRequest(Protocol):
    def send(self) -> results_client.RunnableStopResult: ...

class ProcessRequest(Protocol):
    def send(self) -> results_client.ProcessResult: ...

class ProcessHandleCloseRequest(Protocol):
    def send(self) -> results_client.ProcessHandleCloseResult: ...

class AliveRequest(Protocol):
    def send(self) -> results_client.AliveResult: ...

class ProcessFactoryCreateRequest(Protocol):
    def send(self) -> results_client.ProcessFactoryCreateResult: ...

class DisconnectRequest(Protocol):
    def send(self) -> results_client.DisconnectResult: ...

class StatechangedRequest(Protocol):
    old: enums.ProcessStateEnum
    new: enums.ProcessStateEnum
    def send(self) -> results_client.StatechangedResult: ...

class InportsRequest(Protocol):
    def send(self) -> results_client.InportsResult: ...

class ConnectinportRequest(Protocol):
    name: str
    sturdyRef: SturdyRefBuilder
    @overload
    def init(self, name: Literal["sturdyRef"]) -> SturdyRefBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.ConnectinportResult: ...

class OutportsRequest(Protocol):
    def send(self) -> results_client.OutportsResult: ...

class ConnectoutportRequest(Protocol):
    name: str
    sturdyRef: SturdyRefBuilder
    @overload
    def init(self, name: Literal["sturdyRef"]) -> SturdyRefBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.ConnectoutportResult: ...

class ConfigentriesRequest(Protocol):
    def send(self) -> results_client.ConfigentriesResult: ...

class ProcessStartRequest(Protocol):
    def send(self) -> results_client.ProcessStartResult: ...

class ProcessStopRequest(Protocol):
    def send(self) -> results_client.ProcessStopResult: ...

class SetconfigentryRequest(Protocol):
    name: str
    val: ValueBuilder
    @overload
    def init(self, name: Literal["val"]) -> ValueBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.SetconfigentryResult: ...

class StateRequest(Protocol):
    transitionCallback: (
        clients.StateTransitionClient
        | modules._ProcessInterfaceModule._StateTransitionInterfaceModule.Server
    )
    def send(self) -> results_client.StateResult: ...
