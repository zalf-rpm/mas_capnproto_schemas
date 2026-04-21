"""Request helper types for `a.capnp`."""

from typing import Protocol

from mas.schema.test.a_capnp.types.results import client as results_client

class MethodRequest(Protocol):
    param: str
    def send(self) -> results_client.MethodResult: ...
