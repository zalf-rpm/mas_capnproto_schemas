"""Request helper types for `web_berest_data_import.capnp`."""

from typing import Protocol

from mas.schema.model.weberest.web_berest_data_import_capnp.types.results import (
    client as results_client,
)

class ImportdataRequest(Protocol):
    id: str
    dwla: bytes
    dwlb: bytes
    def send(self) -> results_client.ImportdataResult: ...
