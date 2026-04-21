"""Result helper modules for `cluster_admin_service.capnp`."""

from mas.schema.cluster.cluster_admin_service_capnp.types.results import (
    client as client,
)
from mas.schema.cluster.cluster_admin_service_capnp.types.results import (
    server as server,
)
from mas.schema.cluster.cluster_admin_service_capnp.types.results import (
    tuples as tuples,
)

__all__ = ["client", "server", "tuples"]
