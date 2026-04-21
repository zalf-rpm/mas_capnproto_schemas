"""Result tuple helper types for `soil.capnp`."""

from collections.abc import Sequence
from typing import Any, NamedTuple

from mas.schema.soil.soil_capnp.types import builders as builders
from mas.schema.soil.soil_capnp.types import clients as clients
from mas.schema.soil.soil_capnp.types import modules as modules
from mas.schema.soil.soil_capnp.types import readers as readers

class DataResultTuple(NamedTuple):
    layers: builders.LayerListBuilder | readers.LayerListReader | Sequence[Any]
    percentageOfArea: float

class GeolocationResultTuple(NamedTuple):
    lat: float
    lon: float

class NextprofilesResultTuple(NamedTuple):
    profiles: (
        builders.ProfileClientListBuilder
        | readers.ProfileClientListReader
        | Sequence[Any]
    )

class CheckavailableparametersResultTuple(NamedTuple):
    failed: bool
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

class GetallavailableparametersResultTuple(NamedTuple):
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

class ClosestprofilesatResultTuple(NamedTuple):
    profiles: (
        builders.ProfileClientListBuilder
        | readers.ProfileClientListReader
        | Sequence[Any]
    )

class StreamallprofilesResultTuple(NamedTuple):
    allProfiles: (
        modules._ServiceInterfaceModule._StreamInterfaceModule.Server
        | clients.StreamClient
    )
