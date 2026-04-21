"""Context helper types for `jobs.capnp`."""

from typing import Protocol

from mas.schema.jobs.jobs_capnp.types.results import server as results_server

class NextjobParams(Protocol): ...

class NextjobCallContext(Protocol):
    params: NextjobParams
    @property
    def results(self) -> results_server.NextjobServerResult: ...
