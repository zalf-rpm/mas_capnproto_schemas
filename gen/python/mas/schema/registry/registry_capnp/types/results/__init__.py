"""Runtime placeholder package for result helpers of `registry.capnp`."""

# pyright: reportUnusedClass=none

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mas.schema.registry.registry_capnp.types.results import client as client
    from mas.schema.registry.registry_capnp.types.results import server as server
    from mas.schema.registry.registry_capnp.types.results import tuples as tuples

__all__ = ["client", "server", "tuples"]
