"""Context helper types for `fbp.capnp`."""

from typing import Protocol

from mas.schema.fbp.fbp_capnp.types import builders as builders
from mas.schema.fbp.fbp_capnp.types import clients as clients
from mas.schema.fbp.fbp_capnp.types import enums as enums
from mas.schema.fbp.fbp_capnp.types import readers as readers
from mas.schema.fbp.fbp_capnp.types.results import server as results_server
from mas.schema.persistence.persistence_capnp.types.readers import SturdyRefReader

class ReadParams(Protocol): ...

class ReadCallContext(Protocol):
    params: ReadParams
    @property
    def results(self) -> builders.MsgBuilder: ...

class ReaderCloseParams(Protocol): ...

class ReaderCloseCallContext(Protocol):
    params: ReaderCloseParams

class ReadifmsgParams(Protocol): ...

class ReadifmsgCallContext(Protocol):
    params: ReadifmsgParams
    @property
    def results(self) -> builders.MsgBuilder: ...

class WriteCallContext(Protocol):
    params: readers.MsgReader

class WriterCloseParams(Protocol): ...

class WriterCloseCallContext(Protocol):
    params: WriterCloseParams

class WriteifspaceCallContext(Protocol):
    params: readers.MsgReader
    @property
    def results(self) -> results_server.WriteifspaceServerResult: ...

class UnregParams(Protocol): ...

class UnregCallContext(Protocol):
    params: UnregParams
    @property
    def results(self) -> results_server.UnregServerResult: ...

class StatusParams(Protocol):
    stats: readers.StatsReader

class StatusCallContext(Protocol):
    params: StatusParams

class SetbuffersizeParams(Protocol):
    size: int

class SetbuffersizeCallContext(Protocol):
    params: SetbuffersizeParams

class ReaderParams(Protocol): ...

class ReaderCallContext(Protocol):
    params: ReaderParams
    @property
    def results(self) -> results_server.ReaderServerResult: ...

class WriterParams(Protocol): ...

class WriterCallContext(Protocol):
    params: WriterParams
    @property
    def results(self) -> results_server.WriterServerResult: ...

class EndpointsParams(Protocol): ...

class EndpointsCallContext(Protocol):
    params: EndpointsParams
    @property
    def results(self) -> results_server.EndpointsServerResult: ...

class SetautoclosesemanticsParams(Protocol):
    cs: enums.ChannelCloseSemanticsEnum

class SetautoclosesemanticsCallContext(Protocol):
    params: SetautoclosesemanticsParams

class ChannelCloseParams(Protocol):
    waitForEmptyBuffer: bool

class ChannelCloseCallContext(Protocol):
    params: ChannelCloseParams

class RegisterstatscallbackParams(Protocol):
    callback: clients.StatsCallbackClient
    updateIntervalInMs: int

class RegisterstatscallbackCallContext(Protocol):
    params: RegisterstatscallbackParams
    @property
    def results(self) -> results_server.RegisterstatscallbackServerResult: ...

class StartChannelsServiceStartCallContext(Protocol):
    params: readers.ParamsReader
    @property
    def results(self) -> results_server.StartChannelsServiceStartServerResult: ...

class RunnableFactoryCreateParams(Protocol): ...

class RunnableFactoryCreateCallContext(Protocol):
    params: RunnableFactoryCreateParams
    @property
    def results(self) -> results_server.RunnableFactoryCreateServerResult: ...

class StoppedParams(Protocol): ...

class StoppedCallContext(Protocol):
    params: StoppedParams

class RunnableStartParams(Protocol):
    portInfosReaderSr: SturdyRefReader
    name: str
    stoppedCb: clients.StoppedCallbackClient

class RunnableStartCallContext(Protocol):
    params: RunnableStartParams
    @property
    def results(self) -> results_server.RunnableStartServerResult: ...

class RunnableStopParams(Protocol): ...

class RunnableStopCallContext(Protocol):
    params: RunnableStopParams
    @property
    def results(self) -> results_server.RunnableStopServerResult: ...

class ProcessFactoryCreateParams(Protocol): ...

class ProcessFactoryCreateCallContext(Protocol):
    params: ProcessFactoryCreateParams
    @property
    def results(self) -> results_server.ProcessFactoryCreateServerResult: ...

class StatechangedParams(Protocol):
    old: enums.ProcessStateEnum
    new: enums.ProcessStateEnum

class StatechangedCallContext(Protocol):
    params: StatechangedParams

class InportsParams(Protocol): ...

class InportsCallContext(Protocol):
    params: InportsParams
    @property
    def results(self) -> results_server.InportsServerResult: ...

class ConnectinportParams(Protocol):
    name: str
    sturdyRef: SturdyRefReader

class ConnectinportCallContext(Protocol):
    params: ConnectinportParams
    @property
    def results(self) -> results_server.ConnectinportServerResult: ...

class OutportsParams(Protocol): ...

class OutportsCallContext(Protocol):
    params: OutportsParams
    @property
    def results(self) -> results_server.OutportsServerResult: ...

class ConnectoutportParams(Protocol):
    name: str
    sturdyRef: SturdyRefReader

class ConnectoutportCallContext(Protocol):
    params: ConnectoutportParams
    @property
    def results(self) -> results_server.ConnectoutportServerResult: ...

class ConfigentriesParams(Protocol): ...

class ConfigentriesCallContext(Protocol):
    params: ConfigentriesParams
    @property
    def results(self) -> results_server.ConfigentriesServerResult: ...

class ProcessStartParams(Protocol): ...

class ProcessStartCallContext(Protocol):
    params: ProcessStartParams

class ProcessStopParams(Protocol):
    mode: enums.ProcessStopModeEnum

class ProcessStopCallContext(Protocol):
    params: ProcessStopParams

class SetconfigentryCallContext(Protocol):
    params: readers.ConfigEntryReader

class StateParams(Protocol):
    transitionCallback: clients.StateTransitionClient

class StateCallContext(Protocol):
    params: StateParams
    @property
    def results(self) -> results_server.StateServerResult: ...
