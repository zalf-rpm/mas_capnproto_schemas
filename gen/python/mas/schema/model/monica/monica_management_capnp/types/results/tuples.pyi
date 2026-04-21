"""Result tuple helper types for `monica_management.capnp`."""

from collections.abc import Sequence
from typing import Any, NamedTuple

from mas.schema.model.monica.monica_management_capnp.types import builders as builders
from mas.schema.model.monica.monica_management_capnp.types import readers as readers

class ManagementatResultTuple(NamedTuple):
    mgmt: builders.EventListBuilder | readers.EventListReader | Sequence[Any]
