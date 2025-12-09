"""This is an automatically generated stub for `config.capnp`."""

import base64
from typing import NamedTuple

import capnp
import schema_capnp
from capnp.lib.capnp import _InterfaceModule

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EEBQBgb/FwdGGe1Mk5wAAQcAAxEVahEZFxElZwAC/2NvbmZpZy5jAA9hcG5wUQQBAf/a/K4gBmYNhgARAUJ/U2VydmljZVEQAQL/LF+Av575xrkAUSgCAUE8Af9s+bDj/qNejABROAIBQUwB/+AreSMQf6m+AFFIAgFBVAH/tUQOJgG2MOEAUVACAUF8AQEMAAARAaL/bWFzOjpzY2gBZW1hOjpjb24HZmlnAAABDAAAEQGS/21hcy5zY2hlAW1hLmNvbmZpAWcAAAEMAAARATo/Y29uZmlnAAABDAAAMQE6Av9naXRodWIuYwdvbS96YWxmLXJwbS9tYXMtaW5mcmFzdHJ1Y3R1cmUvY2FwbnByb3RvX3NjaGVtYXMvZ2VuL2dvLz9jb25maWcAAA==",  # config.capnp
    "ECtQBgb/2vyuIAZmDYYAEQ0D/xcHRhntTJOcAAAAEAEzSwHeAREVqhEdBwAAERlHEW0HEW0P/2NvbmZpZy5jAWFwbnA6U2VyD3ZpY2VQAQFRBAMFAAD/2HNrRHgXk4oBC7Ir130VzLAREVoAAEEQAUEgARExB/9uZXh0Q29uZgADaWcRAR9RBAIB/9r8riAGZg2GAAEBAAARAR9RBAIB/9r8riAGZg2GAAEBAABAAVABAUEEAREBEgFD",  # config.capnp:Service
    "EBJQBgb/2HNrRHgXk4oAERUBAAAEBxABAAAxFToBAAT/Y29uZmlnLmMDYXBucDpTZXJ2aWNlLm5leHRDb25maWckP1BhcmFtcw==",  # config.capnp:Service.nextConfig$Params
    "EDNQBgb/C7Ir130VzLAAURUBAQAABQEHEAEAADEVQgEAAREddwAB/2NvbmZpZy5jBGFwbnA6U2VydmljZS5uZXh0Q29uZmlnJFJlc3VsdHMAUQgDBAAABAEAABEpOgAAUSQDAVEwAgEBARQBAQEBES2KAABRMAMBUTwCAT9jb25maWcBEgEB/9r8riAGZg2GAAAAARIAAf9ub0Z1cnRoZQFyQ29uZmlncwAAAQEAAgEBAAE=",  # config.capnp:Service.nextConfig$Results
]

# Load schemas and build module structure
_loader = capnp.SchemaLoader()
for _schema_b64 in _SCHEMA_NODES:
    _schema_data = base64.b64decode(_schema_b64)
    _node_reader = schema_capnp.Node.from_bytes_packed(_schema_data)
    _loader.load_dynamic(_node_reader)

# Build module structure inline
Service = _InterfaceModule(_loader.get(0x860D660620AEFCDA).as_interface(), "Service")

Service.Server.NextconfigResultTuple = NamedTuple(
    "NextconfigResultTuple",
    [("config", object), ("noFurtherConfigs", object)],
)
