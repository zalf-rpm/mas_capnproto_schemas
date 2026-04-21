"""Server result helper types for `monica_management.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.model.monica.monica_management_capnp.types import builders as builders
from mas.schema.model.monica.monica_management_capnp.types import readers as readers

class ManagementatServerResult(_DynamicStructBuilder):
    @property
    def mgmt(self) -> builders.EventListBuilder: ...
    @mgmt.setter
    def mgmt(
        self,
        value: builders.EventListBuilder | readers.EventListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["mgmt"],
        size: int | None = None,
    ) -> builders.EventListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
