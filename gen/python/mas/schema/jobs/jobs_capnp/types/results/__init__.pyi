"""Result helper modules for `jobs.capnp`."""

from mas.schema.jobs.jobs_capnp.types.results import client as client
from mas.schema.jobs.jobs_capnp.types.results import server as server
from mas.schema.jobs.jobs_capnp.types.results import tuples as tuples

__all__ = ["client", "server", "tuples"]
