"""Result tuple helper types for `x.capnp`."""

from typing import NamedTuple

class XMResultTuple(NamedTuple):
    t: str

class ZMResultTuple(NamedTuple):
    r: float
