"""Enum helper aliases for `geo.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import _DynamicEnum

class CoordTypeValue(_DynamicEnum):
    @override
    def __str__(self) -> Literal["gk", "utm", "latlon"]: ...

type CoordTypeEnum = int | Literal["gk", "utm", "latlon"]
