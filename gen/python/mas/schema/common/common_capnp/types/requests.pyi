"""Request helper types for `common.capnp`."""

from typing import Protocol

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
)

from mas.schema.common.common_capnp.types import common as common
from mas.schema.common.common_capnp.types.results import client as results_client

class InfoRequest(Protocol):
    def send(self) -> results_client.InfoResult: ...

class CreateRequest(Protocol):
    def send(self) -> results_client.CreateResult: ...

class ProduceRequest(Protocol):
    @property
    def in_(self) -> _DynamicObjectBuilder: ...
    @in_.setter
    def in_(self, value: common.AnyPointer) -> None: ...
    def send(self) -> results_client.ProduceResult: ...

class ValueRequest(Protocol):
    def send(self) -> results_client.ValueResult: ...
