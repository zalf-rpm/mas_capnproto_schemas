"""This is an automatically generated stub for `date.capnp`."""

import base64

import capnp
import schema_capnp
from capnp.lib.capnp import _StructModule

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EEBQBgb/KvYHi8Mr6ugAAQUAAxEVWhEZFxElZwAC/2RhdGUuY2FwAANucFEEAQH/jREiA6z+5pcAEQEqD0RhdGVREAEC/yxfgL+e+ca5AFEoAgFBPAH/bPmw4/6jXowAUTgCAUFMAf/gK3kjEH+pvgBRSAIBQVQB/7VEDiYBtjDhAFFQAgFBfAEBDAAAEQGi/21hczo6c2NoAWVtYTo6Y29tB21vbgAAAQwAABEBkv9tYXMuc2NoZQFtYS5jb21tbwFuAAABDAAAEQE6P2NvbW1vbgAAAQwAADEBOgL/Z2l0aHViLmMHb20vemFsZi1ycG0vbWFzLWluZnJhc3RydWN0dXJlL2NhcG5wcm90b19zY2hlbWFzL2dlbi9nby8/Y29tbW9uAAA=",  # date.capnp
    "ED5QBgb/jREiA6z+5pcAUQsBAf8q9geLwyvq6AAEBwAAM0sBMwIRFYIRGQcAABEVrwAB/2RhdGUuY2FwAW5wOkRhdGUAUAEBUQwDBAAABAEAABFFKgAAUUADAVFMAgERAQIUAQEAABFJMgAAUUQDAVFQAgERAgMUAQIAABFNIgAAUUgDAVFUAgEPeWVhcgEDAAIBAwABH21vbnRoAQYAAgEGAAEHZGF5AQYAAgEGAAE=",  # date.capnp:Date
]

# Load schemas and build module structure
_loader = capnp.SchemaLoader()
for _schema_b64 in _SCHEMA_NODES:
    _schema_data = base64.b64decode(_schema_b64)
    _node_reader = schema_capnp.Node.from_bytes_packed(_schema_data)
    _loader.load_dynamic(_node_reader)

# Build module structure inline
Date = _StructModule(_loader.get(0x97E6FEAC0322118D).as_struct(), "Date")
