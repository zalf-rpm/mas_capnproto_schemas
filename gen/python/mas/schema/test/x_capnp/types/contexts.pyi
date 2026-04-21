"""Context helper types for `x.capnp`."""

from typing import Protocol

from mas.schema.test.x_capnp.types.results import server as results_server

class XMParams(Protocol):
    i: int

class XMCallContext(Protocol):
    params: XMParams
    @property
    def results(self) -> results_server.XMServerResult: ...

class YMParams(Protocol):
    hello: str

class YMCallContext(Protocol):
    params: YMParams

class ZMParams(Protocol):
    n: int

class ZMCallContext(Protocol):
    params: ZMParams
    @property
    def results(self) -> results_server.ZMServerResult: ...
