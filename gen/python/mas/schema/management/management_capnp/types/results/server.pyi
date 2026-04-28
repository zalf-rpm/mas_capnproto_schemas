"""Server result helper types for `management.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
    _DynamicStructBuilder,
)

from mas.schema.management.management_capnp.types import builders as builders
from mas.schema.management.management_capnp.types import common as common
from mas.schema.management.management_capnp.types import readers as readers

class NutrientsServerResult(_DynamicStructBuilder):
    @property
    def nutrients(self) -> builders.NutrientListBuilder: ...
    @nutrients.setter
    def nutrients(
        self,
        value: builders.NutrientListBuilder
        | readers.NutrientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["nutrients"],
        size: int | None = None,
    ) -> builders.NutrientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ParametersServerResult(_DynamicStructBuilder):
    @property
    def params(self) -> _DynamicObjectBuilder: ...
    @params.setter
    def params(self, value: common.AnyPointer) -> None: ...

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
