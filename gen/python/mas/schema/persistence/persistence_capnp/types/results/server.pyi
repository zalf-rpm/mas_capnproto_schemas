"""Server result helper types for `persistence.capnp`."""

from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
    _DynamicStructBuilder,
)

from mas.schema.persistence.persistence_capnp.types import builders as builders
from mas.schema.persistence.persistence_capnp.types import clients as clients
from mas.schema.persistence.persistence_capnp.types import common as common
from mas.schema.persistence.persistence_capnp.types import modules as modules
from mas.schema.persistence.persistence_capnp.types import readers as readers

class ReleaseServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class RestoreServerResult(_DynamicStructBuilder):
    @property
    def cap(self) -> _DynamicObjectBuilder: ...
    @cap.setter
    def cap(self, value: common.Capability) -> None: ...

class RegistrarRegisterServerResult(_DynamicStructBuilder):
    @property
    def heartbeat(
        self,
    ) -> modules._HeartbeatInterfaceModule.Server | clients.HeartbeatClient: ...
    @heartbeat.setter
    def heartbeat(
        self,
        value: modules._HeartbeatInterfaceModule.Server | clients.HeartbeatClient,
    ) -> None: ...
    @property
    def secsHeartbeatInterval(self) -> int: ...
    @secsHeartbeatInterval.setter
    def secsHeartbeatInterval(self, value: int) -> None: ...

class ResolveServerResult(_DynamicStructBuilder):
    @property
    def host(self) -> str: ...
    @host.setter
    def host(self, value: str) -> None: ...
    @property
    def port(self) -> int: ...
    @port.setter
    def port(self, value: int) -> None: ...

class SturdyrefatgatewayServerResult(_DynamicStructBuilder):
    @property
    def selfAtGatewaySR(self) -> builders.SturdyRefBuilder: ...
    @selfAtGatewaySR.setter
    def selfAtGatewaySR(
        self,
        value: builders.SturdyRefBuilder | readers.SturdyRefReader | dict[str, Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["selfAtGatewaySR"],
        size: int | None = None,
    ) -> builders.SturdyRefBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
