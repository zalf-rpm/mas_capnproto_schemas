"""Client result helper types for `modam.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

class RunaemmodelResult(Awaitable[RunaemmodelResult], Protocol):
    output: str

class RunfieldmodelResult(Awaitable[RunfieldmodelResult], Protocol):
    output: str
