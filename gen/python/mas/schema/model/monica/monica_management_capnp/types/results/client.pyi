"""Client result helper types for `monica_management.capnp`."""

from collections.abc import Awaitable
from typing import Protocol

from mas.schema.model.monica.monica_management_capnp.types import readers as readers

class ManagementatResult(Awaitable[ManagementatResult], Protocol):
    mgmt: readers.EventListReader
