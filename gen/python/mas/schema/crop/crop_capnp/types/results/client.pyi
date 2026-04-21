"""Client result helper types for `crop.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from capnp.lib.capnp import (
    _DynamicObjectReader,
)

from mas.schema.common.common_capnp.types.readers import IdInformationReader

class ParametersResult(Awaitable[ParametersResult], Protocol):
    params: _DynamicObjectReader

class CultivarResult(Awaitable[CultivarResult], Protocol):
    info: IdInformationReader

class SpeciesResult(Awaitable[SpeciesResult], Protocol):
    info: IdInformationReader
