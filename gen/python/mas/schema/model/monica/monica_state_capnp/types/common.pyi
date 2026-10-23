"""Common typing aliases for `monica_state.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import _DynamicEnumField, _StructModuleWhich

class _ICDataModuleWhich(_StructModuleWhich):
    NoCrop: _ICDataModuleWhich
    Height: _ICDataModuleWhich
    Lait: _ICDataModuleWhich

class _ICDataWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["noCrop", "height", "lait"]: ...
