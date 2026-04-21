"""Client result helper types for `service.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.service.service_capnp.types import readers as readers

class HeartbeatResult(Awaitable[None], Protocol): ...
class SettimeoutResult(Awaitable[None], Protocol): ...
class AdminStopResult(Awaitable[None], Protocol): ...

class IdentitiesResult(Awaitable[IdentitiesResult], Protocol):
    infos: readers.IdInformationListReader

class UpdateidentityResult(Awaitable[None], Protocol): ...

class SimpleFactoryCreateResult(Awaitable[SimpleFactoryCreateResult], Protocol):
    caps: readers.IdentifiableClientListReader

class FactoryCreateResult(Awaitable[FactoryCreateResult], Protocol):
    adminCap: _DynamicCapabilityClient
    serviceCaps: readers.IdentifiableClientListReader
    error: str

class ServiceinterfacenamesResult(Awaitable[ServiceinterfacenamesResult], Protocol):
    names: readers.TextListReader

class StoppableStopResult(Awaitable[StoppableStopResult], Protocol):
    success: bool
