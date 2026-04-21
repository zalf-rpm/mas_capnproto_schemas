"""Client result helper types for `config.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from capnp.lib.capnp import (
    _DynamicObjectReader,
)

class NextconfigResult(Awaitable[NextconfigResult], Protocol):
    config: _DynamicObjectReader
    noFurtherConfigs: bool
