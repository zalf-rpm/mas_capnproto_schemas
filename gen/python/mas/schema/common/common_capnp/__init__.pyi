"""This is an automatically generated stub for `common.capnp`."""

from collections.abc import Sequence

from capnp.lib.capnp import _Schema

from mas.schema.common.common_capnp import types as types

def get_schema_by_id(schema_id: int) -> _Schema: ...
def load_capnp_file(path: str, imports: Sequence[str] = ...) -> object: ...

IdInformation: types.modules._IdInformationStructModule
Identifiable: types.modules._IdentifiableInterfaceModule
StructuredText: types.modules._StructuredTextStructModule
MimeTypes: types.modules._MimeTypesStructModule
Blob: types.modules._BlobStructModule
Pair: types.modules._PairStructModule
Value: types.modules._ValueStructModule
Factory: types.modules._FactoryInterfaceModule
IOFactory: types.modules._IOFactoryInterfaceModule
Holder: types.modules._HolderInterfaceModule
IdentifiableHolder: types.modules._IdentifiableHolderInterfaceModule

__all__ = [
    "Blob",
    "Factory",
    "Holder",
    "IOFactory",
    "IdInformation",
    "Identifiable",
    "IdentifiableHolder",
    "MimeTypes",
    "Pair",
    "StructuredText",
    "Value",
    "get_schema_by_id",
    "load_capnp_file",
    "types",
]
