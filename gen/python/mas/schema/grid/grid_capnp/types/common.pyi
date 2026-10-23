"""Common typing aliases for `grid.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import _DynamicEnumField, _StructModuleWhich

class _ResolutionModuleWhich(_StructModuleWhich):
    Meter: _ResolutionModuleWhich
    Degree: _ResolutionModuleWhich

class _ResolutionWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["meter", "degree"]: ...

class _ValueModuleWhich(_StructModuleWhich):
    F: _ValueModuleWhich
    I: _ValueModuleWhich
    Ui: _ValueModuleWhich
    No: _ValueModuleWhich

class _ValueWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["f", "i", "ui", "no"]: ...
