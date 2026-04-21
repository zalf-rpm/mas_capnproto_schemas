"""Client result helper types for `x.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

class XMResult(Awaitable[XMResult], Protocol):
    t: str

class YMResult(Awaitable[None], Protocol): ...

class ZMResult(Awaitable[ZMResult], Protocol):
    r: float
