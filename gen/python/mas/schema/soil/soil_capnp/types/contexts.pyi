"""Context helper types for `soil.capnp`."""

from typing import Protocol

from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.soil.soil_capnp.types import builders as builders
from mas.schema.soil.soil_capnp.types import readers as readers
from mas.schema.soil.soil_capnp.types.results import server as results_server

class DataParams(Protocol): ...

class DataCallContext(Protocol):
    params: DataParams
    @property
    def results(self) -> builders.ProfileDataBuilder: ...

class GeolocationParams(Protocol): ...

class GeolocationCallContext(Protocol):
    params: GeolocationParams
    @property
    def results(self) -> LatLonCoordBuilder: ...

class NextprofilesParams(Protocol):
    maxCount: int

class NextprofilesCallContext(Protocol):
    params: NextprofilesParams
    @property
    def results(self) -> results_server.NextprofilesServerResult: ...

class CheckavailableparametersCallContext(Protocol):
    params: readers.QueryReader
    @property
    def results(self) -> builders.ResultBuilder: ...

class GetallavailableparametersParams(Protocol):
    onlyRawData: bool

class GetallavailableparametersCallContext(Protocol):
    params: GetallavailableparametersParams
    @property
    def results(self) -> results_server.GetallavailableparametersServerResult: ...

class ClosestprofilesatParams(Protocol):
    coord: LatLonCoordReader
    query: readers.QueryReader

class ClosestprofilesatCallContext(Protocol):
    params: ClosestprofilesatParams
    @property
    def results(self) -> results_server.ClosestprofilesatServerResult: ...

class StreamallprofilesCallContext(Protocol):
    params: readers.QueryReader
    @property
    def results(self) -> results_server.StreamallprofilesServerResult: ...
