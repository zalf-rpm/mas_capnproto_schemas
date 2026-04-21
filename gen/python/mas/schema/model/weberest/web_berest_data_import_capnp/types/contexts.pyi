"""Context helper types for `web_berest_data_import.capnp`."""

from typing import Protocol

from mas.schema.model.weberest.web_berest_data_import_capnp.types.results import (
    server as results_server,
)

class ImportdataParams(Protocol):
    id: str
    dwla: bytes
    dwlb: bytes

class ImportdataCallContext(Protocol):
    params: ImportdataParams
    @property
    def results(self) -> results_server.ImportdataServerResult: ...
