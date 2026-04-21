"""Context helper types for `modam.capnp`."""

from typing import Protocol

from mas.schema.dakis.modam.modam_capnp.types.results import server as results_server

class RunaemmodelParams(Protocol):
    input: str

class RunaemmodelCallContext(Protocol):
    params: RunaemmodelParams
    @property
    def results(self) -> results_server.RunaemmodelServerResult: ...

class RunfieldmodelParams(Protocol):
    input: str

class RunfieldmodelCallContext(Protocol):
    params: RunfieldmodelParams
    @property
    def results(self) -> results_server.RunfieldmodelServerResult: ...
