"""Common typing aliases for `climate.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
    _DynamicCapabilityServer,
    _DynamicEnumField,
    _DynamicListBuilder,
    _DynamicListReader,
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModuleWhich,
)

# Type alias for AnyPointer parameters (accepts all Cap'n Proto pointer types)
type AnyPointer = (
    str
    | bytes
    | _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicListBuilder
    | _DynamicListReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class _EntryModuleWhich(_StructModuleWhich):
    Gcm: _EntryModuleWhich
    Rcm: _EntryModuleWhich
    Historical: _EntryModuleWhich
    Rcp: _EntryModuleWhich
    Ssp: _EntryModuleWhich
    EnsMem: _EntryModuleWhich
    Version: _EntryModuleWhich
    Start: _EntryModuleWhich
    End: _EntryModuleWhich
    Co2: _EntryModuleWhich
    Picontrol: _EntryModuleWhich
    Description: _EntryModuleWhich

class _EntryWhich(_DynamicEnumField):
    @override
    def __call__(
        self,
    ) -> Literal[
        "gcm",
        "rcm",
        "historical",
        "rcp",
        "ssp",
        "ensMem",
        "version",
        "start",
        "end",
        "co2",
        "picontrol",
        "description",
    ]: ...

class _ValueModuleWhich(_StructModuleWhich):
    Text: _ValueModuleWhich
    Float: _ValueModuleWhich
    Int: _ValueModuleWhich
    Bool: _ValueModuleWhich
    Date: _ValueModuleWhich

class _ValueWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["text", "float", "int", "bool", "date"]: ...
