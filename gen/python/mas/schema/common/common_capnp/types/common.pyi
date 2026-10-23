"""Common typing aliases for `common.capnp`."""

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

# Type alias for Capability parameters
type Capability = (
    _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class _ValueModuleWhich(_StructModuleWhich):
    F64: _ValueModuleWhich
    F32: _ValueModuleWhich
    I64: _ValueModuleWhich
    I32: _ValueModuleWhich
    I16: _ValueModuleWhich
    I8: _ValueModuleWhich
    Ui64: _ValueModuleWhich
    Ui32: _ValueModuleWhich
    Ui16: _ValueModuleWhich
    Ui8: _ValueModuleWhich
    B: _ValueModuleWhich
    T: _ValueModuleWhich
    D: _ValueModuleWhich
    P: _ValueModuleWhich
    Cap: _ValueModuleWhich
    Lf64: _ValueModuleWhich
    Lf32: _ValueModuleWhich
    Li64: _ValueModuleWhich
    Li32: _ValueModuleWhich
    Li16: _ValueModuleWhich
    Li8: _ValueModuleWhich
    Lui64: _ValueModuleWhich
    Lui32: _ValueModuleWhich
    Lui16: _ValueModuleWhich
    Lui8: _ValueModuleWhich
    Lb: _ValueModuleWhich
    Lt: _ValueModuleWhich
    Ld: _ValueModuleWhich
    Lcap: _ValueModuleWhich
    Lpair: _ValueModuleWhich
    Lv: _ValueModuleWhich

class _ValueWhich(_DynamicEnumField):
    @override
    def __call__(
        self,
    ) -> Literal[
        "f64",
        "f32",
        "i64",
        "i32",
        "i16",
        "i8",
        "ui64",
        "ui32",
        "ui16",
        "ui8",
        "b",
        "t",
        "d",
        "p",
        "cap",
        "lf64",
        "lf32",
        "li64",
        "li32",
        "li16",
        "li8",
        "lui64",
        "lui32",
        "lui16",
        "lui8",
        "lb",
        "lt",
        "ld",
        "lcap",
        "lpair",
        "lv",
    ]: ...
