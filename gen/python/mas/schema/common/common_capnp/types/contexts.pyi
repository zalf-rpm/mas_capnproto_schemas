"""Context helper types for `common.capnp`."""

from typing import Protocol

from capnp.lib.capnp import (
    _DynamicObjectReader,
)

from mas.schema.common.common_capnp.types import builders as builders
from mas.schema.common.common_capnp.types.results import server as results_server

class InfoParams(Protocol): ...

class InfoCallContext(Protocol):
    params: InfoParams
    @property
    def results(self) -> builders.IdInformationBuilder: ...

class CreateParams(Protocol): ...

class CreateCallContext(Protocol):
    params: CreateParams
    @property
    def results(self) -> results_server.CreateServerResult: ...

class ProduceParams(Protocol):
    in_: _DynamicObjectReader

class ProduceCallContext(Protocol):
    params: ProduceParams
    @property
    def results(self) -> results_server.ProduceServerResult: ...

class ValueParams(Protocol): ...

class ValueCallContext(Protocol):
    params: ValueParams
    @property
    def results(self) -> results_server.ValueServerResult: ...
