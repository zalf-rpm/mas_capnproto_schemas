"""This is an automatically generated stub for `jobs.capnp`."""

import base64
from typing import NamedTuple

import capnp
import schema_capnp
from capnp.lib.capnp import _InterfaceModule, _StructModule

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EEJQBgb/DGYux+3i5+cAAQUAAxEVWhEZJxExZwAC/2pvYnMuY2FwAANucFEIAQH/SIijHLdgW6AAEQki//DLE9BUVHS4ABEFQgdKb2J/U2VydmljZVEQAQL/LF+Av575xrkAUSgCAUE8Af9s+bDj/qNejABROAIBQUgB/+AreSMQf6m+AFFEAgFBUAH/tUQOJgG2MOEAUUwCAUF4AQEMAAARAZL/bWFzOjpzY2gBZW1hOjpqb2IBcwAAAQwAABEBgv9tYXMuc2NoZQFtYS5qb2JzAAAAAQwAABEBKg9qb2JzAAABDAAAMQEqAv9naXRodWIuYwdvbS96YWxmLXJwbS9tYXMtaW5mcmFzdHJ1Y3R1cmUvY2FwbnByb3RvX3NjaGVtYXMvZ2VuL2dvLw9qb2JzAAA=",  # jobs.capnp
    "EDNQBgb/SIijHLdgW6AAUQsBAf8MZi7H7eLn5wAFAQcQATO3ARUCERV6ERkHAAARFXcAABGND/9qb2JzLmNhcAA/bnA6Sm9iUAEBUQgDBAAABAEAABEpKgAAUSQDAVEwAgEBARQBAQEBES1yAABRLAMBUTgCAQ9kYXRhARIBAf9IiKMct2BboAAAAAESAAH/bm9GdXJ0aGUAH3JKb2JzAQEAAgEBAAFBBAERAUJ/UGF5bG9hZA==",  # jobs.capnp:Job
    "ECFQBgb/8MsT0FRUdLgAEQsD/wxmLsft4ufnAAABMxcCbwIRFZoRHQcAABEZRxFBJwAA/2pvYnMuY2FwAW5wOlNlcnZpA2NlUAEBUQQDBQAA/xwDSnZ+qTvqAbu+HlIi7GfgERFCAAIRBQd/bmV4dEpvYkABUQgBAf/VSJxZy9GvsgAAAP9lyzbcoNqnwQAAAA==",  # jobs.capnp:Service
    "EBJQBgb/HANKdn6pO+oAERMBAAAEBwABMRUSAQAE/2pvYnMuY2FwA25wOlNlcnZpY2UubmV4dEpvYiRQYXJhbQFz",  # jobs.capnp:Service.nextJob$Params
    "ECJQBgb/u74eUiLsZ+AAERMBAAAFAQcAATEVGgEAAREdPwAB/2pvYnMuY2FwA25wOlNlcnZpY2UubmV4dEpvYiRSZXN1bAN0c1EEAwQAAAQBAAARDSIAAFEIAwFRFAIBB2pvYgEQ/0iIoxy3YFugAAABARAAAQ==",  # jobs.capnp:Service.nextJob$Results
]

# Load schemas and build module structure
_loader = capnp.SchemaLoader()
for _schema_b64 in _SCHEMA_NODES:
    _schema_data = base64.b64decode(_schema_b64)
    _node_reader = schema_capnp.Node.from_bytes_packed(_schema_data)
    _loader.load_dynamic(_node_reader)

# Build module structure inline
Job = _StructModule(_loader.get(0xA05B60B71CA38848).as_struct(), "Job")
Service = _InterfaceModule(_loader.get(0xB8745454D013CBF0).as_interface(), "Service")

Service.Server.NextjobResultTuple = NamedTuple("NextjobResultTuple", [("job", object)])
