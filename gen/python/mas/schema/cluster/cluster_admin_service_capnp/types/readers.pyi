"""Reader helper types for `cluster_admin_service.capnp`."""

from collections.abc import Callable
from typing import override

from capnp.lib.capnp import (
    _DynamicStructReader,
)

from mas.schema.cluster.cluster_admin_service_capnp.types import builders as builders
from mas.schema.cluster.cluster_admin_service_capnp.types import lists as lists

class ZmqPipelineAddressesReader(_DynamicStructReader):
    @property
    def input(self) -> str: ...
    @property
    def output(self) -> str: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ZmqPipelineAddressesBuilder: ...

class ClusterReader(_DynamicStructReader):
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ClusterBuilder: ...

type ModelInstanceFactoryClientListReader = lists._ModelInstanceFactoryClientList.Reader
