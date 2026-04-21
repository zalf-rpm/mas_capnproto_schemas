"""Context helper types for `persistence.capnp`."""

from typing import Protocol

from mas.schema.persistence.persistence_capnp.types import builders as builders
from mas.schema.persistence.persistence_capnp.types import common as common
from mas.schema.persistence.persistence_capnp.types import readers as readers
from mas.schema.persistence.persistence_capnp.types.results import (
    server as results_server,
)

class BeatParams(Protocol): ...

class BeatCallContext(Protocol):
    params: BeatParams

class ReleaseParams(Protocol): ...

class ReleaseCallContext(Protocol):
    params: ReleaseParams
    @property
    def results(self) -> results_server.ReleaseServerResult: ...

class SaveCallContext(Protocol):
    params: readers.SaveParamsReader
    @property
    def results(self) -> builders.SaveResultsBuilder: ...

class RestoreCallContext(Protocol):
    params: readers.RestoreParamsReader
    @property
    def results(self) -> results_server.RestoreServerResult: ...

class RegistrarRegisterCallContext(Protocol):
    params: readers.RegisterParamsReader
    @property
    def results(self) -> results_server.RegistrarRegisterServerResult: ...

class ResolveParams(Protocol):
    id: str

class ResolveCallContext(Protocol):
    params: ResolveParams
    @property
    def results(self) -> results_server.ResolveServerResult: ...

class GatewayRegisterParams(Protocol):
    cap: common.AnyPointer
    secretSeed: str

class GatewayRegisterCallContext(Protocol):
    params: GatewayRegisterParams
    @property
    def results(self) -> builders.RegResultsBuilder: ...

class SturdyrefatgatewayParams(Protocol):
    gatewaySR: readers.SturdyRefReader
    gatewayId: str

class SturdyrefatgatewayCallContext(Protocol):
    params: SturdyrefatgatewayParams
    @property
    def results(self) -> results_server.SturdyrefatgatewayServerResult: ...
