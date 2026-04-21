"""Result tuple helper types for `common.capnp`."""

from typing import NamedTuple

from mas.schema.common.common_capnp.types import common as common

class InfoResultTuple(NamedTuple):
    id: str
    name: str
    description: str

class CreateResultTuple(NamedTuple):
    out: common.AnyPointer

class ProduceResultTuple(NamedTuple):
    out: common.AnyPointer

class ValueResultTuple(NamedTuple):
    value: common.AnyPointer
