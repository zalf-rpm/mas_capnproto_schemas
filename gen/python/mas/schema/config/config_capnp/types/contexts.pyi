"""Context helper types for `config.capnp`."""

from typing import Protocol

from mas.schema.config.config_capnp.types.results import server as results_server

class NextconfigParams(Protocol): ...

class NextconfigCallContext(Protocol):
    params: NextconfigParams
    @property
    def results(self) -> results_server.NextconfigServerResult: ...
