"""Result tuple helper types for `service.capnp`."""

from collections.abc import Sequence
from typing import Any, NamedTuple

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.service.service_capnp.types import builders as builders
from mas.schema.service.service_capnp.types import common as common
from mas.schema.service.service_capnp.types import readers as readers

class IdentitiesResultTuple(NamedTuple):
    infos: (
        builders.IdInformationListBuilder
        | readers.IdInformationListReader
        | Sequence[IdInformationReader | IdInformationBuilder | dict[str, Any]]
    )

class SimpleFactoryCreateResultTuple(NamedTuple):
    caps: (
        builders.IdentifiableClientListBuilder
        | readers.IdentifiableClientListReader
        | Sequence[IdentifiableClient | _IdentifiableInterfaceModule.Server]
    )

class FactoryCreateResultTuple(NamedTuple):
    adminCap: common.Capability
    serviceCaps: (
        builders.IdentifiableClientListBuilder
        | readers.IdentifiableClientListReader
        | Sequence[IdentifiableClient | _IdentifiableInterfaceModule.Server]
    )
    error: str

class ServiceinterfacenamesResultTuple(NamedTuple):
    names: builders.TextListBuilder | readers.TextListReader | Sequence[str]

class StoppableStopResultTuple(NamedTuple):
    success: bool
