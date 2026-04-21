"""Result tuple helper types for `config.capnp`."""

from typing import NamedTuple

from mas.schema.config.config_capnp.types import common as common

class NextconfigResultTuple(NamedTuple):
    config: common.AnyPointer
    noFurtherConfigs: bool
