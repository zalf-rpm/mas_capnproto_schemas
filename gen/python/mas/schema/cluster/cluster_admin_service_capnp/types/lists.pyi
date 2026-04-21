"""List helper types for `cluster_admin_service.capnp`."""

from collections.abc import Iterator
from typing import override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
)

from mas.schema.cluster.cluster_admin_service_capnp.types import clients as clients
from mas.schema.cluster.cluster_admin_service_capnp.types import modules as modules

class _ModelInstanceFactoryClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> clients.ModelInstanceFactoryClient: ...
        @override
        def __iter__(self) -> Iterator[clients.ModelInstanceFactoryClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> clients.ModelInstanceFactoryClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: clients.ModelInstanceFactoryClient
            | modules._ClusterStructModule._ModelInstanceFactoryInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[clients.ModelInstanceFactoryClient]: ...
