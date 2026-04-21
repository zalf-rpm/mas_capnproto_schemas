"""Context helper types for `a.capnp`."""

from typing import Protocol

from mas.schema.test.a_capnp.types.results import server as results_server

class MethodParams(Protocol):
    param: str

class MethodCallContext(Protocol):
    params: MethodParams
    @property
    def results(self) -> results_server.MethodServerResult: ...
