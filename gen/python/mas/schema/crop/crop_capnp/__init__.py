"""This is an automatically generated stub for `crop.capnp`."""

import base64
from typing import NamedTuple

import capnp
import schema_capnp
from capnp.lib.capnp import _InterfaceModule

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EEJQBgb/cvmdluEkivkAAQUAAxEVWhEZJxExZwAC/2Nyb3AuY2FwAANucFEIAQH/hFy/JKOXjegAEQkq/8RrOMC2wtyNABEFQg9Dcm9wf1NlcnZpY2VREAEC/yxfgL+e+ca5AFEoAgFBPAH/bPmw4/6jXowAUTgCAUFIAf/gK3kjEH+pvgBRRAIBQVAB/7VEDiYBtjDhAFFMAgFBeAEBDAAAEQGS/21hczo6c2NoAWVtYTo6Y3JvAXAAAAEMAAARAYL/bWFzLnNjaGUBbWEuY3JvcAAAAAEMAAARASoPY3JvcAAAAQwAADEBKgL/Z2l0aHViLmMHb20vemFsZi1ycG0vbWFzLWluZnJhc3RydWN0dXJlL2NhcG5wcm90b19zY2hlbWFzL2dlbi9nby8PY3JvcAAA",  # crop.capnp
    "EDZQBgb/hFy/JKOXjegAEQsD/3L5nZbhJIr5AAABM9cBMQMRFYIRGQcAABEVxxGVJwAA/2Nyb3AuY2FwAW5wOkNyb3AAUAEBUQwDBQEC/1uOPHQOAW7IAYZUUS1y/PrkEVFaAAIRSQcBAf96UbTfF/Fu8gG6lCSluwQ3vxE9SgACETUHAAD/tDAxKjIc3fQBSGTe7l6JqrQRKUIAAhEdB/9wYXJhbWV0ZQADcnNAAf9jdWx0aXZhcgAAAEABf3NwZWNpZXNAAVEIAQH/1UicWcvRr7IAAAD/Zcs23KDap8EAAAA=",  # crop.capnp:Crop
    "EBJQBgb/W448dA4BbsgAERABAAAEBwABMRUSAQAE/2Nyb3AuY2FwA25wOkNyb3AucGFyYW1ldGVycyRQYXJhbQFz",  # crop.capnp:Crop.parameters$Params
    "ECJQBgb/hlRRLXL8+uQAERABAAAFAQcAATEVGgEAAREdPwAB/2Nyb3AuY2FwA25wOkNyb3AucGFyYW1ldGVycyRSZXN1bAN0c1EEAwQAAAQBAAARDToAAFEIAwFRFAIBP3BhcmFtcwESAAIBEgAB",  # crop.capnp:Crop.parameters$Results
    "EBFQBgb/elG03xfxbvIAERABAAAEBwABMRUCAQAE/2Nyb3AuY2FwA25wOkNyb3AuY3VsdGl2YXIkUGFyYW1zAA==",  # crop.capnp:Crop.cultivar$Params
    "ECJQBgb/upQkpbsEN78AERABAAAFAQcAATEVCgEAAREdPwAB/2Nyb3AuY2FwA25wOkNyb3AuY3VsdGl2YXIkUmVzdWx0cwAAUQQDBAAABAEAABENKgAAUQgDAVEUAgEPaW5mbwEQ/9PaA/7LfsvUAAABARAAAQ==",  # crop.capnp:Crop.cultivar$Results
    "EEFQBgb/09oD/st+y9QAEQ0B/8mKqHWnyfGZAAUDBwAAM0sBrgERFdoRIQcAABEdrwAB/2NvbW1vbi5jAmFwbnA6SWRJbmZvcm1hdGkDb25QAQFRDAMEAAAEAQAAEUUaAABRQAMBUUwCAREBARQBAQAAEUkqAABRRAMBUVACARECAhQBAgAAEU1iAABRTAMBUVgCAQNpZAEMAAIBDAABD25hbWUBDAACAQwAAf9kZXNjcmlwdAAHaW9uAQwAAgEMAAE=",  # common.capnp:IdInformation
    "EBFQBgb/tDAxKjIc3fQAERABAAAEBwABERX6AAT/Y3JvcC5jYXACbnA6Q3JvcC5zcGVjaWVzJD9QYXJhbXM=",  # crop.capnp:Crop.species$Params
    "ECFQBgb/SGTe7l6JqrQAERABAAAFAQcAATEVAgEAAREZPwAB/2Nyb3AuY2FwA25wOkNyb3Auc3BlY2llcyRSZXN1bHRzAFEEAwQAAAQBAAARDSoAAFEIAwFRFAIBD2luZm8BEP/T2gP+y37L1AAAAQEQAAE=",  # crop.capnp:Crop.species$Results
    "EBVQBgb/xGs4wLbC3I0AEQsD/3L5nZbhJIr5AAABMzMDngMRFZoRHQcAABEZBxEZFwAA/2Nyb3AuY2FwAW5wOlNlcnZpA2NlUAEBUAMFUQQBAf+4MwZg0Ut7ygAAAA==",  # crop.capnp:Service
]

# Load schemas and build module structure
_loader = capnp.SchemaLoader()
for _schema_b64 in _SCHEMA_NODES:
    _schema_data = base64.b64decode(_schema_b64)
    _node_reader = schema_capnp.Node.from_bytes_packed(_schema_data)
    _loader.load_dynamic(_node_reader)

# Build module structure inline
Crop = _InterfaceModule(_loader.get(0xE88D97A324BF5C84).as_interface(), "Crop")
Service = _InterfaceModule(_loader.get(0x8DDCC2B6C0386BC4).as_interface(), "Service")

Crop.Server.CultivarResultTuple = NamedTuple("CultivarResultTuple", [("info", object)])
Crop.Server.ParametersResultTuple = NamedTuple(
    "ParametersResultTuple",
    [("params", object)],
)
Crop.Server.SpeciesResultTuple = NamedTuple("SpeciesResultTuple", [("info", object)])
