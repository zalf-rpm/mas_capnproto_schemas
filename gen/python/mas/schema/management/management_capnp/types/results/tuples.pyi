"""Result tuple helper types for `management.capnp`."""

from collections.abc import Sequence
from typing import Any, NamedTuple

from mas.schema.management.management_capnp.types import builders as builders
from mas.schema.management.management_capnp.types import common as common
from mas.schema.management.management_capnp.types import readers as readers

class NutrientsResultTuple(NamedTuple):
    nutrients: builders.NutrientListBuilder | readers.NutrientListReader | Sequence[Any]

class ParametersResultTuple(NamedTuple):
    params: common.AnyPointer

class ManagementatResultTuple(NamedTuple):
    mgmt: builders.EventListBuilder | readers.EventListReader | Sequence[Any]
