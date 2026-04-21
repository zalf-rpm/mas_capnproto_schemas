"""Context helper types for `monica_management.capnp`."""

from typing import Protocol

from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.model.monica.monica_management_capnp.types.results import (
    server as results_server,
)

class ManagementatCallContext(Protocol):
    params: LatLonCoordReader
    @property
    def results(self) -> results_server.ManagementatServerResult: ...
