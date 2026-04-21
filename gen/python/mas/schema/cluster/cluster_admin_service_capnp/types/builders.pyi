"""Builder helper types for `cluster_admin_service.capnp`."""

from typing import override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.cluster.cluster_admin_service_capnp.types import lists as lists
from mas.schema.cluster.cluster_admin_service_capnp.types import readers as readers

class ZmqPipelineAddressesBuilder(_DynamicStructBuilder):
    @property
    def input(self) -> str: ...
    @input.setter
    def input(self, value: str) -> None: ...
    @property
    def output(self) -> str: ...
    @output.setter
    def output(self, value: str) -> None: ...
    @override
    def as_reader(self) -> readers.ZmqPipelineAddressesReader: ...

class ClusterBuilder(_DynamicStructBuilder):
    @override
    def as_reader(self) -> readers.ClusterReader: ...

type ModelInstanceFactoryClientListBuilder = (
    lists._ModelInstanceFactoryClientList.Builder
)
