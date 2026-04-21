"""Runtime placeholder package for typing helpers of `cluster_admin_service.capnp`."""

# pyright: reportUnusedClass=none

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mas.schema.cluster.cluster_admin_service_capnp.types import (
        builders as builders,
    )
    from mas.schema.cluster.cluster_admin_service_capnp.types import clients as clients
    from mas.schema.cluster.cluster_admin_service_capnp.types import common as common
    from mas.schema.cluster.cluster_admin_service_capnp.types import (
        contexts as contexts,
    )
    from mas.schema.cluster.cluster_admin_service_capnp.types import enums as enums
    from mas.schema.cluster.cluster_admin_service_capnp.types import lists as lists
    from mas.schema.cluster.cluster_admin_service_capnp.types import modules as modules
    from mas.schema.cluster.cluster_admin_service_capnp.types import readers as readers
    from mas.schema.cluster.cluster_admin_service_capnp.types import (
        requests as requests,
    )
    from mas.schema.cluster.cluster_admin_service_capnp.types import results as results
    from mas.schema.cluster.cluster_admin_service_capnp.types import schemas as schemas
    from mas.schema.cluster.cluster_admin_service_capnp.types import servers as servers

__all__ = [
    "builders",
    "clients",
    "common",
    "contexts",
    "enums",
    "lists",
    "modules",
    "readers",
    "requests",
    "results",
    "schemas",
    "servers",
]
