"""Result tuple helper types for `crop.capnp`."""

from typing import Any, NamedTuple

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.crop.crop_capnp.types import common as common

class ParametersResultTuple(NamedTuple):
    params: common.AnyPointer

class CultivarResultTuple(NamedTuple):
    info: IdInformationBuilder | IdInformationReader | dict[str, Any]

class SpeciesResultTuple(NamedTuple):
    info: IdInformationBuilder | IdInformationReader | dict[str, Any]
