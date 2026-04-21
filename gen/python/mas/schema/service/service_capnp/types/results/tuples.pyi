"""Result tuple helper types for `service.capnp`."""

from collections.abc import Sequence
from typing import Any, NamedTuple

from mas.schema.service.service_capnp.types import builders as builders
from mas.schema.service.service_capnp.types import common as common
from mas.schema.service.service_capnp.types import readers as readers

class IdentitiesResultTuple(NamedTuple):
    infos: (
        builders.IdInformationListBuilder
        | readers.IdInformationListReader
        | Sequence[Any]
    )

class SimpleFactoryCreateResultTuple(NamedTuple):
    caps: (
        builders.IdentifiableClientListBuilder
        | readers.IdentifiableClientListReader
        | Sequence[Any]
    )

class FactoryCreateResultTuple(NamedTuple):
    adminCap: common.Capability
    serviceCaps: (
        builders.IdentifiableClientListBuilder
        | readers.IdentifiableClientListReader
        | Sequence[Any]
    )
    error: str

class ServiceinterfacenamesResultTuple(NamedTuple):
    names: builders.TextListBuilder | readers.TextListReader | Sequence[Any]

class StoppableStopResultTuple(NamedTuple):
    success: bool
