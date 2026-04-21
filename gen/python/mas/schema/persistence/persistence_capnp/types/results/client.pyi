"""Client result helper types for `persistence.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from capnp.lib.capnp import (
    _DynamicObjectReader,
)

from mas.schema.persistence.persistence_capnp.types import clients as clients
from mas.schema.persistence.persistence_capnp.types import readers as readers

class BeatResult(Awaitable[None], Protocol): ...

class ReleaseResult(Awaitable[ReleaseResult], Protocol):
    success: bool

class SaveResult(Awaitable[SaveResult], Protocol):
    sturdyRef: readers.SturdyRefReader
    unsaveSR: readers.SturdyRefReader

class RestoreResult(Awaitable[RestoreResult], Protocol):
    cap: _DynamicObjectReader

class RegistrarRegisterResult(Awaitable[RegistrarRegisterResult], Protocol):
    heartbeat: clients.HeartbeatClient
    secsHeartbeatInterval: int

class ResolveResult(Awaitable[ResolveResult], Protocol):
    host: str
    port: int

class GatewayRegisterResult(Awaitable[GatewayRegisterResult], Protocol):
    sturdyRef: readers.SturdyRefReader
    heartbeat: clients.HeartbeatClient
    secsHeartbeatInterval: int

class SturdyrefatgatewayResult(Awaitable[SturdyrefatgatewayResult], Protocol):
    selfAtGatewaySR: readers.SturdyRefReader
