"""Common typing aliases for `monica_management.capnp`."""

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

class _EventWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["at", "between", "after"]: ...

class _TypeModuleWhich(_StructModuleWhich):
    External: _TypeModuleWhich
    Internal: _TypeModuleWhich

class _TypeWhich(_DynamicEnumField):
    @override
    def __call__(self) -> Literal["external", "internal"]: ...
