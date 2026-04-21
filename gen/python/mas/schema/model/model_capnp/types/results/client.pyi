"""Client result helper types for `model.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from capnp.lib.capnp import (
    _DynamicObjectReader,
)

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.model.model_capnp.types import clients as clients
from mas.schema.model.model_capnp.types import readers as readers

class ClimateInstanceRunResult(Awaitable[ClimateInstanceRunResult], Protocol):
    result: readers.XYResultReader

class RunsetResult(Awaitable[RunsetResult], Protocol):
    result: readers.XYPlusResultReader

class EnvInstanceRunResult(Awaitable[EnvInstanceRunResult], Protocol):
    result: _DynamicObjectReader

class UnregisterResult(Awaitable[UnregisterResult], Protocol):
    success: bool

class RegisterenvinstanceResult(Awaitable[RegisterenvinstanceResult], Protocol):
    unregister: clients.UnregisterClient

class ModelinfoResult(Awaitable[ModelinfoResult], Protocol):
    id: str
    name: str
    description: str

class NewinstanceResult(Awaitable[NewinstanceResult], Protocol):
    instance: IdentifiableClient

class NewinstancesResult(Awaitable[NewinstancesResult], Protocol):
    instances: readers.IdentifiableClientListReader
