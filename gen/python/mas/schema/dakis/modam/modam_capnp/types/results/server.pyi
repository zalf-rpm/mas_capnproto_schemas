"""Server result helper types for `modam.capnp`."""

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

class RunaemmodelServerResult(_DynamicStructBuilder):
    @property
    def output(self) -> str: ...
    @output.setter
    def output(self, value: str) -> None: ...

class RunfieldmodelServerResult(_DynamicStructBuilder):
    @property
    def output(self) -> str: ...
    @output.setter
    def output(self, value: str) -> None: ...
