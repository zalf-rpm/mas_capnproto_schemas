"""Context helper types for `management.capnp`."""

from typing import Protocol

from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.management.management_capnp.types.results import (
    server as results_server,
)

class NutrientsParams(Protocol): ...

class NutrientsCallContext(Protocol):
    params: NutrientsParams
    @property
    def results(self) -> results_server.NutrientsServerResult: ...

class ParametersParams(Protocol): ...

class ParametersCallContext(Protocol):
    params: ParametersParams
    @property
    def results(self) -> results_server.ParametersServerResult: ...

class ManagementatCallContext(Protocol):
    params: LatLonCoordReader
    @property
    def results(self) -> results_server.ManagementatServerResult: ...
