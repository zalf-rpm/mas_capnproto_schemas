"""Client result helper types for `common.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from capnp.lib.capnp import (
    _DynamicObjectReader,
)

class InfoResult(Awaitable[InfoResult], Protocol):
    id: str
    name: str
    description: str

class CreateResult(Awaitable[CreateResult], Protocol):
    out: _DynamicObjectReader

class ProduceResult(Awaitable[ProduceResult], Protocol):
    out: _DynamicObjectReader

class ValueResult(Awaitable[ValueResult], Protocol):
    value: _DynamicObjectReader
