"""Enum helper aliases for `monica_params.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import _DynamicEnum

class AutomaticHarvestParametersHarvestTimeValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["maturity", "unknown"]: ...

type AutomaticHarvestParametersHarvestTimeEnum = int | Literal["maturity", "unknown"]
