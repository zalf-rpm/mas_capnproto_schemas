"""Server result helper types for `x.capnp`."""

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

class XMServerResult(_DynamicStructBuilder):
    @property
    def t(self) -> str: ...
    @t.setter
    def t(self, value: str) -> None: ...

class ZMServerResult(_DynamicStructBuilder):
    @property
    def r(self) -> float: ...
    @r.setter
    def r(self, value: float) -> None: ...
