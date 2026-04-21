"""Server result helper types for `common.capnp`."""

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.common.common_capnp.types import common as common

class CreateServerResult(_DynamicStructBuilder):
    @property
    def out(self) -> common.AnyPointer: ...
    @out.setter
    def out(self, value: common.AnyPointer) -> None: ...

class ProduceServerResult(_DynamicStructBuilder):
    @property
    def out(self) -> common.AnyPointer: ...
    @out.setter
    def out(self, value: common.AnyPointer) -> None: ...

class ValueServerResult(_DynamicStructBuilder):
    @property
    def value(self) -> common.AnyPointer: ...
    @value.setter
    def value(self, value: common.AnyPointer) -> None: ...
