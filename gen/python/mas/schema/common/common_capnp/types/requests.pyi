"""Request helper types for `common.capnp`."""

from typing import Protocol

from mas.schema.common.common_capnp.types import common as common
from mas.schema.common.common_capnp.types.results import client as results_client

class InfoRequest(Protocol):
    def send(self) -> results_client.InfoResult: ...

class CreateRequest(Protocol):
    def send(self) -> results_client.CreateResult: ...

class ProduceRequest(Protocol):
    in_: common.AnyPointer
    def send(self) -> results_client.ProduceResult: ...

class ValueRequest(Protocol):
    def send(self) -> results_client.ValueResult: ...
