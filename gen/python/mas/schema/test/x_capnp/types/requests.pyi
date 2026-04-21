"""Request helper types for `x.capnp`."""

from typing import Protocol

from mas.schema.test.x_capnp.types.results import client as results_client

class XMRequest(Protocol):
    i: int
    def send(self) -> results_client.XMResult: ...

class YMRequest(Protocol):
    hello: str
    def send(self) -> results_client.YMResult: ...

class ZMRequest(Protocol):
    n: int
    def send(self) -> results_client.ZMResult: ...
