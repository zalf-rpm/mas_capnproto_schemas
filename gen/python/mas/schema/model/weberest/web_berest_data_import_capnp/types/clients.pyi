"""Client helper types for `web_berest_data_import.capnp`."""

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.model.weberest.web_berest_data_import_capnp.types import (
    requests as requests,
)
from mas.schema.model.weberest.web_berest_data_import_capnp.types.results import (
    client as results_client,
)

class DWLABImportClient(_DynamicCapabilityClient):
    def importData(
        self,
        id: str | None = None,
        dwla: bytes | None = None,
        dwlb: bytes | None = None,
    ) -> results_client.ImportdataResult: ...
    def importData_request(
        self,
        id: str | None = None,
        dwla: bytes | None = None,
        dwlb: bytes | None = None,
    ) -> requests.ImportdataRequest: ...
