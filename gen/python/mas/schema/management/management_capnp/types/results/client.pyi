"""Client result helper types for `management.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from capnp.lib.capnp import (
    _DynamicObjectReader,
)

from mas.schema.management.management_capnp.types import readers as readers

class NutrientsResult(Awaitable[NutrientsResult], Protocol):
    nutrients: readers.NutrientListReader

class ParametersResult(Awaitable[ParametersResult], Protocol):
    params: _DynamicObjectReader

class ManagementatResult(Awaitable[ManagementatResult], Protocol):
    mgmt: readers.EventListReader
