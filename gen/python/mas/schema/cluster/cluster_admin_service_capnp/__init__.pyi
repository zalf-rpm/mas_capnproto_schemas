"""This is an automatically generated stub for `cluster_admin_service.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.cluster.cluster_admin_service_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

Cluster: types.modules._ClusterStructModule

__all__ = ["Cluster", "get_schema_by_id", "load_capnp_file", "types"]
