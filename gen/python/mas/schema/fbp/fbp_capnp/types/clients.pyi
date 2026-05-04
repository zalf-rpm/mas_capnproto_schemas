"""Client helper types for `fbp.capnp`."""

from collections.abc import Sequence
from typing import Any

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.common.common_capnp.types.builders import ValueBuilder
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.readers import ValueReader
from mas.schema.fbp.fbp_capnp.types import builders as builders
from mas.schema.fbp.fbp_capnp.types import common as common
from mas.schema.fbp.fbp_capnp.types import enums as enums
from mas.schema.fbp.fbp_capnp.types import modules as modules
from mas.schema.fbp.fbp_capnp.types import readers as readers
from mas.schema.fbp.fbp_capnp.types import requests as requests
from mas.schema.fbp.fbp_capnp.types.results import client as results_client
from mas.schema.persistence.persistence_capnp.types.builders import SturdyRefBuilder
from mas.schema.persistence.persistence_capnp.types.clients import (
    GatewayRegistrableClient,
    PersistentClient,
)
from mas.schema.persistence.persistence_capnp.types.readers import SturdyRefReader

class ReaderClient(IdentifiableClient, PersistentClient):
    def read(self) -> results_client.ReadResult: ...
    def close(self) -> results_client.ReaderCloseResult: ...
    def readIfMsg(self) -> results_client.ReadifmsgResult: ...
    def read_request(self) -> requests.ReadRequest: ...
    def close_request(self) -> requests.ReaderCloseRequest: ...
    def readIfMsg_request(self) -> requests.ReadifmsgRequest: ...

class WriterClient(IdentifiableClient, PersistentClient):
    def write(
        self,
        value: common.AnyPointer | None = None,
        done: None = None,
        noMsg: None = None,
    ) -> results_client.WriteResult: ...
    def close(self) -> results_client.WriterCloseResult: ...
    def writeIfSpace(
        self,
        value: common.AnyPointer | None = None,
        done: None = None,
        noMsg: None = None,
    ) -> results_client.WriteifspaceResult: ...
    def write_request(
        self,
        value: common.AnyPointer | None = None,
        done: None = None,
        noMsg: None = None,
    ) -> requests.WriteRequest: ...
    def close_request(self) -> requests.WriterCloseRequest: ...
    def writeIfSpace_request(
        self,
        value: common.AnyPointer | None = None,
        done: None = None,
        noMsg: None = None,
    ) -> requests.WriteifspaceRequest: ...

class UnregisterClient(_DynamicCapabilityClient):
    def unreg(self) -> results_client.UnregResult: ...
    def unreg_request(self) -> requests.UnregRequest: ...

class StatsCallbackClient(_DynamicCapabilityClient):
    def status(
        self,
        stats: builders.StatsBuilder
        | readers.StatsReader
        | dict[str, Any]
        | None = None,
    ) -> results_client.StatusResult: ...
    def status_request(
        self,
        stats: builders.StatsBuilder | None = None,
    ) -> requests.StatusRequest: ...

class ChannelClient(IdentifiableClient, PersistentClient):
    def setBufferSize(
        self,
        size: int | None = None,
    ) -> results_client.SetbuffersizeResult: ...
    def reader(self) -> results_client.ReaderResult: ...
    def writer(self) -> results_client.WriterResult: ...
    def endpoints(self) -> results_client.EndpointsResult: ...
    def setAutoCloseSemantics(
        self,
        cs: enums.ChannelCloseSemanticsEnum | None = None,
    ) -> results_client.SetautoclosesemanticsResult: ...
    def close(
        self,
        waitForEmptyBuffer: bool | None = None,
    ) -> results_client.ChannelCloseResult: ...
    def registerStatsCallback(
        self,
        callback: StatsCallbackClient
        | modules._ChannelInterfaceModule._StatsCallbackInterfaceModule.Server
        | None = None,
        updateIntervalInMs: int | None = None,
    ) -> results_client.RegisterstatscallbackResult: ...
    def setBufferSize_request(
        self,
        size: int | None = None,
    ) -> requests.SetbuffersizeRequest: ...
    def reader_request(self) -> requests.ReaderRequest: ...
    def writer_request(self) -> requests.WriterRequest: ...
    def endpoints_request(self) -> requests.EndpointsRequest: ...
    def setAutoCloseSemantics_request(
        self,
        cs: enums.ChannelCloseSemanticsEnum | None = None,
    ) -> requests.SetautoclosesemanticsRequest: ...
    def close_request(
        self,
        waitForEmptyBuffer: bool | None = None,
    ) -> requests.ChannelCloseRequest: ...
    def registerStatsCallback_request(
        self,
        callback: StatsCallbackClient
        | modules._ChannelInterfaceModule._StatsCallbackInterfaceModule.Server
        | None = None,
        updateIntervalInMs: int | None = None,
    ) -> requests.RegisterstatscallbackRequest: ...

class StartChannelsServiceClient(IdentifiableClient):
    def start(
        self,
        name: str | None = None,
        noOfChannels: int | None = None,
        noOfReaders: int | None = None,
        noOfWriters: int | None = None,
        readerSrts: builders.TextListBuilder
        | readers.TextListReader
        | Sequence[Any]
        | None = None,
        writerSrts: builders.TextListBuilder
        | readers.TextListReader
        | Sequence[Any]
        | None = None,
        bufferSize: int | None = None,
    ) -> results_client.StartChannelsServiceStartResult: ...
    def start_request(
        self,
        name: str | None = None,
        noOfChannels: int | None = None,
        noOfReaders: int | None = None,
        noOfWriters: int | None = None,
        readerSrts: builders.TextListBuilder
        | readers.TextListReader
        | Sequence[Any]
        | None = None,
        writerSrts: builders.TextListBuilder
        | readers.TextListReader
        | Sequence[Any]
        | None = None,
        bufferSize: int | None = None,
    ) -> requests.StartChannelsServiceStartRequest: ...

class RunnableFactoryClient(IdentifiableClient):
    def create(self) -> results_client.RunnableFactoryCreateResult: ...
    def create_request(self) -> requests.RunnableFactoryCreateRequest: ...

class StoppedCallbackClient(_DynamicCapabilityClient):
    def stopped(self) -> results_client.StoppedResult: ...
    def stopped_request(self) -> requests.StoppedRequest: ...

class RunnableClient(IdentifiableClient):
    def start(
        self,
        portInfosReaderSr: SturdyRefBuilder
        | SturdyRefReader
        | dict[str, Any]
        | None = None,
        name: str | None = None,
        stoppedCb: StoppedCallbackClient
        | modules._RunnableInterfaceModule._StoppedCallbackInterfaceModule.Server
        | None = None,
    ) -> results_client.RunnableStartResult: ...
    def stop(self) -> results_client.RunnableStopResult: ...
    def start_request(
        self,
        portInfosReaderSr: SturdyRefBuilder | None = None,
        name: str | None = None,
        stoppedCb: StoppedCallbackClient
        | modules._RunnableInterfaceModule._StoppedCallbackInterfaceModule.Server
        | None = None,
    ) -> requests.RunnableStartRequest: ...
    def stop_request(self) -> requests.RunnableStopRequest: ...

class ProcessHandleClient(_DynamicCapabilityClient):
    def process(self) -> results_client.ProcessResult: ...
    def close(self) -> results_client.ProcessHandleCloseResult: ...
    def alive(self) -> results_client.AliveResult: ...
    def process_request(self) -> requests.ProcessRequest: ...
    def close_request(self) -> requests.ProcessHandleCloseRequest: ...
    def alive_request(self) -> requests.AliveRequest: ...

class ProcessFactoryClient(IdentifiableClient):
    def create(self) -> results_client.ProcessFactoryCreateResult: ...
    def create_request(self) -> requests.ProcessFactoryCreateRequest: ...

class DisconnectClient(_DynamicCapabilityClient):
    def disconnect(self) -> results_client.DisconnectResult: ...
    def disconnect_request(self) -> requests.DisconnectRequest: ...

class StateTransitionClient(_DynamicCapabilityClient):
    def stateChanged(
        self,
        old: enums.ProcessStateEnum | None = None,
        new: enums.ProcessStateEnum | None = None,
    ) -> results_client.StatechangedResult: ...
    def stateChanged_request(
        self,
        old: enums.ProcessStateEnum | None = None,
        new: enums.ProcessStateEnum | None = None,
    ) -> requests.StatechangedRequest: ...

class ProcessClient(IdentifiableClient, GatewayRegistrableClient):
    def inPorts(self) -> results_client.InportsResult: ...
    def connectInPort(
        self,
        name: str | None = None,
        sturdyRef: SturdyRefBuilder | SturdyRefReader | dict[str, Any] | None = None,
    ) -> results_client.ConnectinportResult: ...
    def outPorts(self) -> results_client.OutportsResult: ...
    def connectOutPort(
        self,
        name: str | None = None,
        sturdyRef: SturdyRefBuilder | SturdyRefReader | dict[str, Any] | None = None,
    ) -> results_client.ConnectoutportResult: ...
    def configEntries(self) -> results_client.ConfigentriesResult: ...
    def start(self) -> results_client.ProcessStartResult: ...
    def stop(self) -> results_client.ProcessStopResult: ...
    def setConfigEntry(
        self,
        name: str | None = None,
        val: ValueBuilder | ValueReader | dict[str, Any] | None = None,
    ) -> results_client.SetconfigentryResult: ...
    def state(
        self,
        transitionCallback: StateTransitionClient
        | modules._ProcessInterfaceModule._StateTransitionInterfaceModule.Server
        | None = None,
    ) -> results_client.StateResult: ...
    def inPorts_request(self) -> requests.InportsRequest: ...
    def connectInPort_request(
        self,
        name: str | None = None,
        sturdyRef: SturdyRefBuilder | None = None,
    ) -> requests.ConnectinportRequest: ...
    def outPorts_request(self) -> requests.OutportsRequest: ...
    def connectOutPort_request(
        self,
        name: str | None = None,
        sturdyRef: SturdyRefBuilder | None = None,
    ) -> requests.ConnectoutportRequest: ...
    def configEntries_request(self) -> requests.ConfigentriesRequest: ...
    def start_request(self) -> requests.ProcessStartRequest: ...
    def stop_request(self) -> requests.ProcessStopRequest: ...
    def setConfigEntry_request(
        self,
        name: str | None = None,
        val: ValueBuilder | None = None,
    ) -> requests.SetconfigentryRequest: ...
    def state_request(
        self,
        transitionCallback: StateTransitionClient
        | modules._ProcessInterfaceModule._StateTransitionInterfaceModule.Server
        | None = None,
    ) -> requests.StateRequest: ...
