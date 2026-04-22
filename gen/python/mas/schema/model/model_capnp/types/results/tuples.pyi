"""Result tuple helper types for `model.capnp`."""

from collections.abc import Sequence
from typing import Any, NamedTuple

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.model.model_capnp.types import builders as builders
from mas.schema.model.model_capnp.types import clients as clients
from mas.schema.model.model_capnp.types import common as common
from mas.schema.model.model_capnp.types import modules as modules
from mas.schema.model.model_capnp.types import readers as readers

class ClimateInstanceRunResultTuple(NamedTuple):
    result: builders.XYResultBuilder | readers.XYResultReader | dict[str, Any]

class RunsetResultTuple(NamedTuple):
    result: builders.XYPlusResultBuilder | readers.XYPlusResultReader | dict[str, Any]

class EnvInstanceRunResultTuple(NamedTuple):
    result: common.AnyPointer

class UnregisterResultTuple(NamedTuple):
    success: bool

class RegisterenvinstanceResultTuple(NamedTuple):
    unregister: (
        modules._EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule.Server
        | clients.UnregisterClient
    )

class ModelinfoResultTuple(NamedTuple):
    id: str
    name: str
    description: str

class NewinstanceResultTuple(NamedTuple):
    instance: _IdentifiableInterfaceModule.Server | IdentifiableClient

class NewinstancesResultTuple(NamedTuple):
    instances: (
        builders.IdentifiableClientListBuilder
        | readers.IdentifiableClientListReader
        | Sequence[Any]
    )
