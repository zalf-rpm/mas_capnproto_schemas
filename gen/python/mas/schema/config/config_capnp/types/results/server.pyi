"""Server result helper types for `config.capnp`."""

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
    _DynamicStructBuilder,
)

from mas.schema.config.config_capnp.types import common as common

class NextconfigServerResult(_DynamicStructBuilder):
    @property
    def config(self) -> _DynamicObjectBuilder: ...
    @config.setter
    def config(self, value: common.AnyPointer) -> None: ...
    @property
    def noFurtherConfigs(self) -> bool: ...
    @noFurtherConfigs.setter
    def noFurtherConfigs(self, value: bool) -> None: ...
