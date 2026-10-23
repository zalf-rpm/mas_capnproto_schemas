"""Enum helper aliases for `model.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import _DynamicEnum

class StatTypeValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["min", "max", "sd", "avg", "median"]: ...

type StatTypeEnum = int | Literal["min", "max", "sd", "avg", "median"]
