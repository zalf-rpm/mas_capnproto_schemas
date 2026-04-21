# pyright: reportAttributeAccessIssue=false, reportArgumentType=false
"""This is an automatically generated stub for `modam.capnp`."""

import base64

import capnp
import schema_capnp

from mas.schema.dakis.modam.modam_capnp.types.modules import (
    _ModamWrapperServiceInterfaceModule,
)

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EEFQBgb/yFUmo1P+tecAAQwAAxEVkhEdFxExZwAC/2Rha2lzL21vAWRhbS5jYXBuAXBRBAEB/3jDq1dgsz/bABEBov9Nb2RhbVdyYQFwcGVyU2VydgdpY2VREAEC/yxfgL+e+ca5AFEoAgFBPAH/bPmw4/6jXowAUTgCAUFMAf/gK3kjEH+pvgBRSAIBQVQB/7VEDiYBtjDhAFFQAgFBdAEBDAAAEQGa/21hczo6c2NoAWVtYTo6ZGFrA2lzAAABDAAAEQG6/21hcy5zY2hlAW1hLmRha2lzPy5tb2RhbQAAAQwAABEBMh9tb2RhbQAAAQwAADEBugH/Z2l0aHViLmMFb20vemFsZi1ycG0vbWFzX2NhcG5wcm90b19zY2hlbWFzL2dlbi9nbz8vZGFraXMAAA==",  # dakis/modam.capnp
    "ECtQBgb/eMOrV2CzP9sAERID/8hVJqNT/rXnAAABMz4BeQIxFTIBESUHAAARIYcReQcAAP9kYWtpcy9tbwNkYW0uY2FwbnA6TW9kYW1XcmFwcGVyU2UfcnZpY2VQAQFRCAMFAAD/zM3a6Yp8AtoBhkbQl2fn3okRMWIAAhEpBwEB/wX2UNCkDjuUAX4YpCvRabqWER1yAAIRFQf/cnVuQWVtTW8AB2RlbEAB/3J1bkZpZWxkAB9Nb2RlbEABUAEB",  # dakis/modam.capnp:ModamWrapperService
    "ECVQBgb/zM3a6Yp8AtoAESYBAAAFAQcAATEVygEAAREpPwAB/2Rha2lzL21vBmRhbS5jYXBucDpNb2RhbVdyYXBwZXJTZXJ2aWNlLnJ1bkFlbU1vZGVsJFBhcmFtcwAAUQQDBAAABAEAABENMgAAUQgDAVEUAgEfaW5wdXQBDAACAQwAAQ==",  # dakis/modam.capnp:ModamWrapperService.runAemModel$Params
    "ECVQBgb/hkbQl2fn3okAESYBAAAFAQcAATEV0gEAAREpPwAB/2Rha2lzL21vBmRhbS5jYXBucDpNb2RhbVdyYXBwZXJTZXJ2aWNlLnJ1bkFlbU1vZGVsJFJlc3VsdAFzUQQDBAAABAEAABENOgAAUQgDAVEUAgE/b3V0cHV0AQwAAgEMAAE=",  # dakis/modam.capnp:ModamWrapperService.runAemModel$Results
    "ECVQBgb/BfZQ0KQOO5QAESYBAAAFAQcAATEV2gEAAREpPwAB/2Rha2lzL21vBmRhbS5jYXBucDpNb2RhbVdyYXBwZXJTZXJ2aWNlLnJ1bkZpZWxkTW9kZWwkUGFyYQNtc1EEAwQAAAQBAAARDTIAAFEIAwFRFAIBH2lucHV0AQwAAgEMAAE=",  # dakis/modam.capnp:ModamWrapperService.runFieldModel$Params
    "ECVQBgb/fhikK9FpupYAESYBAAAFAQcAATEV4gEAAREpPwAB/2Rha2lzL21vBmRhbS5jYXBucDpNb2RhbVdyYXBwZXJTZXJ2aWNlLnJ1bkZpZWxkTW9kZWwkUmVzdQdsdHNRBAMEAAAEAQAAEQ06AABRCAMBURQCAT9vdXRwdXQBDAACAQwAAQ==",  # dakis/modam.capnp:ModamWrapperService.runFieldModel$Results
]

# Load schemas and build module structure
# Use a shared loader stored on capnp module so capabilities work across schema modules
if not hasattr(capnp, "_embedded_schema_loader"):
    capnp._embedded_schema_loader = capnp.SchemaLoader()
_loader = capnp._embedded_schema_loader
for _schema_b64 in _SCHEMA_NODES:
    _schema_data = base64.b64decode(_schema_b64)
    _node_reader = schema_capnp.Node.from_bytes_packed(_schema_data)
    _loader.load_dynamic(_node_reader)

# Build module structure inline

ModamWrapperService = _ModamWrapperServiceInterfaceModule(
    _loader.get(0xDB3FB36057ABC378).as_interface(),
    "ModamWrapperService",
)
