"""Client result helper types for `a.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

class MethodResult(Awaitable[MethodResult], Protocol):
    res: str
