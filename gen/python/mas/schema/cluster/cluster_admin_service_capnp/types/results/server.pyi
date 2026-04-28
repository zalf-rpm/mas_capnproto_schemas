"""Server result helper types for `cluster_admin_service.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
    _DynamicStructBuilder,
)

from mas.schema.cluster.cluster_admin_service_capnp.types import builders as builders
from mas.schema.cluster.cluster_admin_service_capnp.types import clients as clients
from mas.schema.cluster.cluster_admin_service_capnp.types import common as common
from mas.schema.cluster.cluster_admin_service_capnp.types import modules as modules
from mas.schema.cluster.cluster_admin_service_capnp.types import readers as readers

class UnregisterServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...

class ValueServerResult(_DynamicStructBuilder):
    @property
    def val(self) -> _DynamicObjectBuilder: ...
    @val.setter
    def val(self, value: common.AnyPointer) -> None: ...

class NewinstanceServerResult(_DynamicStructBuilder):
    @property
    def instance(
        self,
    ) -> (
        modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient
    ): ...
    @instance.setter
    def instance(
        self,
        value: modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient,
    ) -> None: ...

class NewinstancesServerResult(_DynamicStructBuilder):
    @property
    def instances(
        self,
    ) -> (
        modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient
    ): ...
    @instances.setter
    def instances(
        self,
        value: modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient,
    ) -> None: ...

class NewcloudviazmqpipelineproxiesServerResult(_DynamicStructBuilder):
    @property
    def proxyAddresses(
        self,
    ) -> (
        modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient
    ): ...
    @proxyAddresses.setter
    def proxyAddresses(
        self,
        value: modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient,
    ) -> None: ...

class NewcloudviaproxyServerResult(_DynamicStructBuilder):
    @property
    def proxy(
        self,
    ) -> (
        modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient
    ): ...
    @proxy.setter
    def proxy(
        self,
        value: modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient,
    ) -> None: ...

class ModelidServerResult(_DynamicStructBuilder):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> None: ...

class RegistermodelinstanceServerResult(_DynamicStructBuilder):
    @property
    def unregister(
        self,
    ) -> (
        modules._ClusterStructModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient
    ): ...
    @unregister.setter
    def unregister(
        self,
        value: modules._ClusterStructModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient,
    ) -> None: ...

class RestoresturdyrefServerResult(_DynamicStructBuilder):
    @property
    def cap(
        self,
    ) -> (
        modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient
    ): ...
    @cap.setter
    def cap(
        self,
        value: modules._ClusterStructModule._ValueHolderInterfaceModule.Server
        | clients.ValueHolderClient,
    ) -> None: ...

class AdminMasterRegistermodelinstancefactoryServerResult(_DynamicStructBuilder):
    @property
    def unregister(
        self,
    ) -> (
        modules._ClusterStructModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient
    ): ...
    @unregister.setter
    def unregister(
        self,
        value: modules._ClusterStructModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient,
    ) -> None: ...

class AdminMasterAvailablemodelsServerResult(_DynamicStructBuilder):
    @property
    def factories(self) -> builders.ModelInstanceFactoryClientListBuilder: ...
    @factories.setter
    def factories(
        self,
        value: builders.ModelInstanceFactoryClientListBuilder
        | readers.ModelInstanceFactoryClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["factories"],
        size: int | None = None,
    ) -> builders.ModelInstanceFactoryClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class UserMasterAvailablemodelsServerResult(_DynamicStructBuilder):
    @property
    def factories(self) -> builders.ModelInstanceFactoryClientListBuilder: ...
    @factories.setter
    def factories(
        self,
        value: builders.ModelInstanceFactoryClientListBuilder
        | readers.ModelInstanceFactoryClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["factories"],
        size: int | None = None,
    ) -> builders.ModelInstanceFactoryClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class RuntimeRegistermodelinstancefactoryServerResult(_DynamicStructBuilder):
    @property
    def unregister(
        self,
    ) -> (
        modules._ClusterStructModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient
    ): ...
    @unregister.setter
    def unregister(
        self,
        value: modules._ClusterStructModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient,
    ) -> None: ...

class RuntimeAvailablemodelsServerResult(_DynamicStructBuilder):
    @property
    def factories(self) -> builders.ModelInstanceFactoryClientListBuilder: ...
    @factories.setter
    def factories(
        self,
        value: builders.ModelInstanceFactoryClientListBuilder
        | readers.ModelInstanceFactoryClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["factories"],
        size: int | None = None,
    ) -> builders.ModelInstanceFactoryClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class NumberofcoresServerResult(_DynamicStructBuilder):
    @property
    def cores(self) -> int: ...
    @cores.setter
    def cores(self, value: int) -> None: ...

class FreenumberofcoresServerResult(_DynamicStructBuilder):
    @property
    def cores(self) -> int: ...
    @cores.setter
    def cores(self, value: int) -> None: ...

class ReservenumberofcoresServerResult(_DynamicStructBuilder):
    @property
    def reservedCores(self) -> int: ...
    @reservedCores.setter
    def reservedCores(self, value: int) -> None: ...
