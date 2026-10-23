"""Common typing aliases for `storage.capnp`."""

from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicEnumField,
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _DynamicStructBuilder,
    _DynamicStructReader,
    _StructModuleWhich,
)

# Type alias for AnyStruct parameters
type AnyStruct = (
    _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)

class _ValueModuleWhich(_StructModuleWhich):
    BoolValue: _ValueModuleWhich
    BoolListValue: _ValueModuleWhich
    Int8Value: _ValueModuleWhich
    Int8ListValue: _ValueModuleWhich
    Int16Value: _ValueModuleWhich
    Int16ListValue: _ValueModuleWhich
    Int32Value: _ValueModuleWhich
    Int32ListValue: _ValueModuleWhich
    Int64Value: _ValueModuleWhich
    Int64ListValue: _ValueModuleWhich
    Uint8Value: _ValueModuleWhich
    Uint8ListValue: _ValueModuleWhich
    Uint16Value: _ValueModuleWhich
    Uint16ListValue: _ValueModuleWhich
    Uint32Value: _ValueModuleWhich
    Uint32ListValue: _ValueModuleWhich
    Uint64Value: _ValueModuleWhich
    Uint64ListValue: _ValueModuleWhich
    Float32Value: _ValueModuleWhich
    Float32ListValue: _ValueModuleWhich
    Float64Value: _ValueModuleWhich
    Float64ListValue: _ValueModuleWhich
    TextValue: _ValueModuleWhich
    TextListValue: _ValueModuleWhich
    DataValue: _ValueModuleWhich
    DataListValue: _ValueModuleWhich
    AnyValue: _ValueModuleWhich

class _ValueWhich(_DynamicEnumField):
    @override
    def __call__(
        self,
    ) -> Literal[
        "boolValue",
        "boolListValue",
        "int8Value",
        "int8ListValue",
        "int16Value",
        "int16ListValue",
        "int32Value",
        "int32ListValue",
        "int64Value",
        "int64ListValue",
        "uint8Value",
        "uint8ListValue",
        "uint16Value",
        "uint16ListValue",
        "uint32Value",
        "uint32ListValue",
        "uint64Value",
        "uint64ListValue",
        "float32Value",
        "float32ListValue",
        "float64Value",
        "float64ListValue",
        "textValue",
        "textListValue",
        "dataValue",
        "dataListValue",
        "anyValue",
    ]: ...
