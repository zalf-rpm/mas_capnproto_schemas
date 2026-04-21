"""Request helper types for `soil.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, Protocol, overload

from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.soil.soil_capnp.types import builders as builders
from mas.schema.soil.soil_capnp.types import readers as readers
from mas.schema.soil.soil_capnp.types.results import client as results_client

class DataRequest(Protocol):
    def send(self) -> results_client.DataResult: ...

class GeolocationRequest(Protocol):
    def send(self) -> results_client.GeolocationResult: ...

class NextprofilesRequest(Protocol):
    maxCount: int
    def send(self) -> results_client.NextprofilesResult: ...

class CheckavailableparametersRequest(Protocol):
    mandatory: (
        builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any]
    )
    optional: (
        builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any]
    )
    onlyRawData: bool
    @overload
    def init(
        self,
        name: Literal["mandatory"],
        size: int = ...,
    ) -> builders.PropertyNameEnumListBuilder: ...
    @overload
    def init(
        self,
        name: Literal["optional"],
        size: int = ...,
    ) -> builders.PropertyNameEnumListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.CheckavailableparametersResult: ...

class GetallavailableparametersRequest(Protocol):
    onlyRawData: bool
    def send(self) -> results_client.GetallavailableparametersResult: ...

class ClosestprofilesatRequest(Protocol):
    coord: LatLonCoordBuilder
    query: builders.QueryBuilder
    @overload
    def init(self, name: Literal["coord"]) -> LatLonCoordBuilder: ...
    @overload
    def init(self, name: Literal["query"]) -> builders.QueryBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.ClosestprofilesatResult: ...

class StreamallprofilesRequest(Protocol):
    mandatory: (
        builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any]
    )
    optional: (
        builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any]
    )
    onlyRawData: bool
    @overload
    def init(
        self,
        name: Literal["mandatory"],
        size: int = ...,
    ) -> builders.PropertyNameEnumListBuilder: ...
    @overload
    def init(
        self,
        name: Literal["optional"],
        size: int = ...,
    ) -> builders.PropertyNameEnumListBuilder: ...
    @overload
    def init(self, name: str, size: int = ...) -> Any: ...
    def send(self) -> results_client.StreamallprofilesResult: ...
