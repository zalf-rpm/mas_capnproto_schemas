"""Context helper types for `crop.capnp`."""

from typing import Protocol

from mas.schema.crop.crop_capnp.types.results import server as results_server

class ParametersParams(Protocol): ...

class ParametersCallContext(Protocol):
    params: ParametersParams
    @property
    def results(self) -> results_server.ParametersServerResult: ...

class CultivarParams(Protocol): ...

class CultivarCallContext(Protocol):
    params: CultivarParams
    @property
    def results(self) -> results_server.CultivarServerResult: ...

class SpeciesParams(Protocol): ...

class SpeciesCallContext(Protocol):
    params: SpeciesParams
    @property
    def results(self) -> results_server.SpeciesServerResult: ...
