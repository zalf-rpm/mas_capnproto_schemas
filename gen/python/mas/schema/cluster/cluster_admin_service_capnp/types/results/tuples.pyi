"""Result tuple helper types for `cluster_admin_service.capnp`."""

from collections.abc import Sequence
from typing import Any, NamedTuple

from mas.schema.cluster.cluster_admin_service_capnp.types import builders as builders
from mas.schema.cluster.cluster_admin_service_capnp.types import clients as clients
from mas.schema.cluster.cluster_admin_service_capnp.types import common as common
from mas.schema.cluster.cluster_admin_service_capnp.types import modules as modules
from mas.schema.cluster.cluster_admin_service_capnp.types import readers as readers

class UnregisterResultTuple(NamedTuple):
    success: bool

class ValueResultTuple(NamedTuple):
    val: common.AnyPointer

class NewinstanceResultTuple(NamedTuple):
    instance: (
        modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient
    )

class NewinstancesResultTuple(NamedTuple):
    instances: (
        modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient
    )

class NewcloudviazmqpipelineproxiesResultTuple(NamedTuple):
    proxyAddresses: (
        modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient
    )

class NewcloudviaproxyResultTuple(NamedTuple):
    proxy: (
        modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient
    )

class ModelidResultTuple(NamedTuple):
    id: str

class RegistermodelinstanceResultTuple(NamedTuple):
    unregister: (
        modules._ClusterStructModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient
    )

class RestoresturdyrefResultTuple(NamedTuple):
    cap: (
        modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient
    )

class AdminMasterRegistermodelinstancefactoryResultTuple(NamedTuple):
    unregister: (
        modules._ClusterStructModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient
    )

class AdminMasterAvailablemodelsResultTuple(NamedTuple):
    factories: (
        builders.ModelInstanceFactoryClientListBuilder
        | readers.ModelInstanceFactoryClientListReader
        | Sequence[Any]
    )

class UserMasterAvailablemodelsResultTuple(NamedTuple):
    factories: (
        builders.ModelInstanceFactoryClientListBuilder
        | readers.ModelInstanceFactoryClientListReader
        | Sequence[Any]
    )

class RuntimeRegistermodelinstancefactoryResultTuple(NamedTuple):
    unregister: (
        modules._ClusterStructModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient
    )

class RuntimeAvailablemodelsResultTuple(NamedTuple):
    factories: (
        builders.ModelInstanceFactoryClientListBuilder
        | readers.ModelInstanceFactoryClientListReader
        | Sequence[Any]
    )

class NumberofcoresResultTuple(NamedTuple):
    cores: int

class FreenumberofcoresResultTuple(NamedTuple):
    cores: int

class ReservenumberofcoresResultTuple(NamedTuple):
    reservedCores: int
