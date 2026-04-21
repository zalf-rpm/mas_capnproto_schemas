"""Runtime placeholder package for result helpers of `sim_setup.capnp`."""

# pyright: reportUnusedClass=none

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mas.schema.model.monica.sim_setup_capnp.types.results import client as client
    from mas.schema.model.monica.sim_setup_capnp.types.results import server as server
    from mas.schema.model.monica.sim_setup_capnp.types.results import tuples as tuples

__all__ = ["client", "server", "tuples"]
