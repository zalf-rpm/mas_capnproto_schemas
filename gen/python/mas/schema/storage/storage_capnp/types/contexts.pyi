"""Context helper types for `storage.capnp`."""

from typing import Protocol

from mas.schema.storage.storage_capnp.types import readers as readers
from mas.schema.storage.storage_capnp.types.results import server as results_server

class GetkeyParams(Protocol): ...

class GetkeyCallContext(Protocol):
    params: GetkeyParams
    @property
    def results(self) -> results_server.GetkeyServerResult: ...

class GetvalueParams(Protocol): ...

class GetvalueCallContext(Protocol):
    params: GetvalueParams
    @property
    def results(self) -> results_server.GetvalueServerResult: ...

class SetvalueParams(Protocol):
    value: readers.ValueReader

class SetvalueCallContext(Protocol):
    params: SetvalueParams
    @property
    def results(self) -> results_server.SetvalueServerResult: ...

class ExportParams(Protocol): ...

class ExportCallContext(Protocol):
    params: ExportParams
    @property
    def results(self) -> results_server.ExportServerResult: ...

class DownloadentriesParams(Protocol): ...

class DownloadentriesCallContext(Protocol):
    params: DownloadentriesParams
    @property
    def results(self) -> results_server.DownloadentriesServerResult: ...

class ListentriesParams(Protocol): ...

class ListentriesCallContext(Protocol):
    params: ListentriesParams
    @property
    def results(self) -> results_server.ListentriesServerResult: ...

class GetentryParams(Protocol):
    key: str

class GetentryCallContext(Protocol):
    params: GetentryParams
    @property
    def results(self) -> results_server.GetentryServerResult: ...

class RemoveentryParams(Protocol):
    key: str

class RemoveentryCallContext(Protocol):
    params: RemoveentryParams
    @property
    def results(self) -> results_server.RemoveentryServerResult: ...

class ClearParams(Protocol): ...

class ClearCallContext(Protocol):
    params: ClearParams
    @property
    def results(self) -> results_server.ClearServerResult: ...

class AddentryParams(Protocol):
    key: str
    value: readers.ValueReader
    replaceExisting: bool

class AddentryCallContext(Protocol):
    params: AddentryParams
    @property
    def results(self) -> results_server.AddentryServerResult: ...

class NewcontainerParams(Protocol):
    name: str
    description: str

class NewcontainerCallContext(Protocol):
    params: NewcontainerParams
    @property
    def results(self) -> results_server.NewcontainerServerResult: ...

class ContainerwithidParams(Protocol):
    id: str

class ContainerwithidCallContext(Protocol):
    params: ContainerwithidParams
    @property
    def results(self) -> results_server.ContainerwithidServerResult: ...

class ListcontainersParams(Protocol): ...

class ListcontainersCallContext(Protocol):
    params: ListcontainersParams
    @property
    def results(self) -> results_server.ListcontainersServerResult: ...

class RemovecontainerParams(Protocol):
    id: str

class RemovecontainerCallContext(Protocol):
    params: RemovecontainerParams
    @property
    def results(self) -> results_server.RemovecontainerServerResult: ...

class ImportcontainerParams(Protocol):
    json: str

class ImportcontainerCallContext(Protocol):
    params: ImportcontainerParams
    @property
    def results(self) -> results_server.ImportcontainerServerResult: ...
