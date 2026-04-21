"""Server result helper types for `a.capnp`."""

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

class MethodServerResult(_DynamicStructBuilder):
    @property
    def res(self) -> str: ...
    @res.setter
    def res(self, value: str) -> None: ...
