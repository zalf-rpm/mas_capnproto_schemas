"""Server result helper types for `fbp.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.fbp.fbp_capnp.types import builders as builders
from mas.schema.fbp.fbp_capnp.types import clients as clients
from mas.schema.fbp.fbp_capnp.types import enums as enums
from mas.schema.fbp.fbp_capnp.types import modules as modules
from mas.schema.fbp.fbp_capnp.types import readers as readers
from mas.schema.service.service_capnp.types.clients import StoppableClient
from mas.schema.service.service_capnp.types.modules import _StoppableInterfaceModule

class WriteifspaceServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class UnregServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class ReaderServerResult(_DynamicStructBuilder):
    @property
    def r(
        self,
    ) -> (
        modules._ChannelInterfaceModule._ReaderInterfaceModule.Server
        | clients.ReaderClient
    ): ...
    @r.setter
    def r(
        self,
        value: modules._ChannelInterfaceModule._ReaderInterfaceModule.Server
        | clients.ReaderClient,
    ) -> None: ...

class WriterServerResult(_DynamicStructBuilder):
    @property
    def w(
        self,
    ) -> (
        modules._ChannelInterfaceModule._WriterInterfaceModule.Server
        | clients.WriterClient
    ): ...
    @w.setter
    def w(
        self,
        value: modules._ChannelInterfaceModule._WriterInterfaceModule.Server
        | clients.WriterClient,
    ) -> None: ...

class EndpointsServerResult(_DynamicStructBuilder):
    @property
    def r(
        self,
    ) -> (
        modules._ChannelInterfaceModule._ReaderInterfaceModule.Server
        | clients.ReaderClient
    ): ...
    @r.setter
    def r(
        self,
        value: modules._ChannelInterfaceModule._ReaderInterfaceModule.Server
        | clients.ReaderClient,
    ) -> None: ...
    @property
    def w(
        self,
    ) -> (
        modules._ChannelInterfaceModule._WriterInterfaceModule.Server
        | clients.WriterClient
    ): ...
    @w.setter
    def w(
        self,
        value: modules._ChannelInterfaceModule._WriterInterfaceModule.Server
        | clients.WriterClient,
    ) -> None: ...

class RegisterstatscallbackServerResult(_DynamicStructBuilder):
    @property
    def unregisterCallback(
        self,
    ) -> (
        modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient
    ): ...
    @unregisterCallback.setter
    def unregisterCallback(
        self,
        value: modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient,
    ) -> None: ...

class StartChannelsServiceStartServerResult(_DynamicStructBuilder):
    @property
    def startupInfos(self) -> builders.StartupInfoListBuilder: ...
    @startupInfos.setter
    def startupInfos(
        self,
        value: builders.StartupInfoListBuilder
        | readers.StartupInfoListReader
        | Sequence[Any],
    ) -> None: ...
    @property
    def stop(self) -> _StoppableInterfaceModule.Server | StoppableClient: ...
    @stop.setter
    def stop(
        self,
        value: _StoppableInterfaceModule.Server | StoppableClient,
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["startupInfos"],
        size: int | None = None,
    ) -> builders.StartupInfoListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class RunnableFactoryCreateServerResult(_DynamicStructBuilder):
    @property
    def out(
        self,
    ) -> modules._RunnableInterfaceModule.Server | clients.RunnableClient: ...
    @out.setter
    def out(
        self,
        value: modules._RunnableInterfaceModule.Server | clients.RunnableClient,
    ) -> None: ...

class RunnableStartServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class RunnableStopServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class ProcessFactoryCreateServerResult(_DynamicStructBuilder):
    @property
    def out(self) -> modules._ProcessInterfaceModule.Server | clients.ProcessClient: ...
    @out.setter
    def out(
        self,
        value: modules._ProcessInterfaceModule.Server | clients.ProcessClient,
    ) -> None: ...

class DisconnectServerResult(_DynamicStructBuilder):
    @property
    def disconnected(self) -> bool: ...
    @disconnected.setter
    def disconnected(self, value: bool) -> None: ...

class InportsServerResult(_DynamicStructBuilder):
    @property
    def ports(self) -> builders.PortListBuilder: ...
    @ports.setter
    def ports(
        self,
        value: builders.PortListBuilder | readers.PortListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["ports"],
        size: int | None = None,
    ) -> builders.PortListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ConnectinportServerResult(_DynamicStructBuilder):
    @property
    def connected(self) -> bool: ...
    @connected.setter
    def connected(self, value: bool) -> None: ...
    @property
    def disconnect(
        self,
    ) -> (
        modules._ProcessInterfaceModule._DisconnectInterfaceModule.Server
        | clients.DisconnectClient
    ): ...
    @disconnect.setter
    def disconnect(
        self,
        value: modules._ProcessInterfaceModule._DisconnectInterfaceModule.Server
        | clients.DisconnectClient,
    ) -> None: ...

class OutportsServerResult(_DynamicStructBuilder):
    @property
    def ports(self) -> builders.PortListBuilder: ...
    @ports.setter
    def ports(
        self,
        value: builders.PortListBuilder | readers.PortListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["ports"],
        size: int | None = None,
    ) -> builders.PortListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ConnectoutportServerResult(_DynamicStructBuilder):
    @property
    def connected(self) -> bool: ...
    @connected.setter
    def connected(self, value: bool) -> None: ...
    @property
    def disconnect(
        self,
    ) -> (
        modules._ProcessInterfaceModule._DisconnectInterfaceModule.Server
        | clients.DisconnectClient
    ): ...
    @disconnect.setter
    def disconnect(
        self,
        value: modules._ProcessInterfaceModule._DisconnectInterfaceModule.Server
        | clients.DisconnectClient,
    ) -> None: ...

class ConfigentriesServerResult(_DynamicStructBuilder):
    @property
    def config(self) -> builders.ConfigEntryListBuilder: ...
    @config.setter
    def config(
        self,
        value: builders.ConfigEntryListBuilder
        | readers.ConfigEntryListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["config"],
        size: int | None = None,
    ) -> builders.ConfigEntryListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class StateServerResult(_DynamicStructBuilder):
    @property
    def currentState(self) -> enums.ProcessStateEnum: ...
    @currentState.setter
    def currentState(self, value: enums.ProcessStateEnum) -> None: ...
