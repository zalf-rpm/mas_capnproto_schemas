"""Result tuple helper types for `persistence.capnp`."""

from typing import Any, NamedTuple

from mas.schema.persistence.persistence_capnp.types import builders as builders
from mas.schema.persistence.persistence_capnp.types import clients as clients
from mas.schema.persistence.persistence_capnp.types import common as common
from mas.schema.persistence.persistence_capnp.types import modules as modules
from mas.schema.persistence.persistence_capnp.types import readers as readers

class ReleaseResultTuple(NamedTuple):
    success: bool

class SaveResultTuple(NamedTuple):
    sturdyRef: builders.SturdyRefBuilder | readers.SturdyRefReader | dict[str, Any]
    unsaveSR: builders.SturdyRefBuilder | readers.SturdyRefReader | dict[str, Any]

class RestoreResultTuple(NamedTuple):
    cap: common.Capability

class RegistrarRegisterResultTuple(NamedTuple):
    heartbeat: modules._HeartbeatInterfaceModule.Server | clients.HeartbeatClient
    secsHeartbeatInterval: int

class ResolveResultTuple(NamedTuple):
    host: str
    port: int

class GatewayRegisterResultTuple(NamedTuple):
    sturdyRef: builders.SturdyRefBuilder | readers.SturdyRefReader | dict[str, Any]
    heartbeat: modules._HeartbeatInterfaceModule.Server | clients.HeartbeatClient
    secsHeartbeatInterval: int

class SturdyrefatgatewayResultTuple(NamedTuple):
    selfAtGatewaySR: (
        builders.SturdyRefBuilder | readers.SturdyRefReader | dict[str, Any]
    )
