"""Client result helper types for `soil.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from mas.schema.soil.soil_capnp.types import clients as clients
from mas.schema.soil.soil_capnp.types import readers as readers

class DataResult(Awaitable[DataResult], Protocol):
    layers: readers.LayerListReader
    percentageOfArea: float

class GeolocationResult(Awaitable[GeolocationResult], Protocol):
    lat: float
    lon: float

class NextprofilesResult(Awaitable[NextprofilesResult], Protocol):
    profiles: readers.ProfileClientListReader

class CheckavailableparametersResult(
    Awaitable[CheckavailableparametersResult],
    Protocol,
):
    failed: bool
    mandatory: readers.PropertyNameEnumListReader
    optional: readers.PropertyNameEnumListReader

class GetallavailableparametersResult(
    Awaitable[GetallavailableparametersResult],
    Protocol,
):
    mandatory: readers.PropertyNameEnumListReader
    optional: readers.PropertyNameEnumListReader

class ClosestprofilesatResult(Awaitable[ClosestprofilesatResult], Protocol):
    profiles: readers.ProfileClientListReader

class StreamallprofilesResult(Awaitable[StreamallprofilesResult], Protocol):
    allProfiles: clients.StreamClient
