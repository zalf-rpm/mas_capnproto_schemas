"""Client result helper types for `cluster_admin_service.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from capnp.lib.capnp import (
    _DynamicObjectReader,
)

from mas.schema.cluster.cluster_admin_service_capnp.types import clients as clients
from mas.schema.cluster.cluster_admin_service_capnp.types import readers as readers

class UnregisterResult(Awaitable[UnregisterResult], Protocol):
    success: bool

class ValueResult(Awaitable[ValueResult], Protocol):
    val: _DynamicObjectReader

class ReleaseResult(Awaitable[None], Protocol): ...

class NewinstanceResult(Awaitable[NewinstanceResult], Protocol):
    instance: clients.ValueHolderClient

class NewinstancesResult(Awaitable[NewinstancesResult], Protocol):
    instances: clients.ValueHolderClient

class NewcloudviazmqpipelineproxiesResult(
    Awaitable[NewcloudviazmqpipelineproxiesResult],
    Protocol,
):
    proxyAddresses: clients.ValueHolderClient

class NewcloudviaproxyResult(Awaitable[NewcloudviaproxyResult], Protocol):
    proxy: clients.ValueHolderClient

class ModelidResult(Awaitable[ModelidResult], Protocol):
    id: str

class RegistermodelinstanceResult(Awaitable[RegistermodelinstanceResult], Protocol):
    unregister: clients.UnregisterClient

class RestoresturdyrefResult(Awaitable[RestoresturdyrefResult], Protocol):
    cap: clients.ValueHolderClient

class AdminMasterRegistermodelinstancefactoryResult(
    Awaitable[AdminMasterRegistermodelinstancefactoryResult],
    Protocol,
):
    unregister: clients.UnregisterClient

class AdminMasterAvailablemodelsResult(
    Awaitable[AdminMasterAvailablemodelsResult],
    Protocol,
):
    factories: readers.ModelInstanceFactoryClientListReader

class UserMasterAvailablemodelsResult(
    Awaitable[UserMasterAvailablemodelsResult],
    Protocol,
):
    factories: readers.ModelInstanceFactoryClientListReader

class RuntimeRegistermodelinstancefactoryResult(
    Awaitable[RuntimeRegistermodelinstancefactoryResult],
    Protocol,
):
    unregister: clients.UnregisterClient

class RuntimeAvailablemodelsResult(Awaitable[RuntimeAvailablemodelsResult], Protocol):
    factories: readers.ModelInstanceFactoryClientListReader

class NumberofcoresResult(Awaitable[NumberofcoresResult], Protocol):
    cores: int

class FreenumberofcoresResult(Awaitable[FreenumberofcoresResult], Protocol):
    cores: int

class ReservenumberofcoresResult(Awaitable[ReservenumberofcoresResult], Protocol):
    reservedCores: int
