"""This is an automatically generated stub for `web-berest-data-import.capnp`."""

import base64
from typing import NamedTuple

import capnp
import schema_capnp
from capnp.lib.capnp import _InterfaceModule

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EFxQBgb/m7drgqJotMQAASYAAzEVYgERKRcROZcAAv9tb2RlbC93ZQRiZXJlc3Qvd2ViLWJlcmVzdC1kYXRhLWltcG9ydC5jYQdwbnBRBAEB/2+qPhSdraShABEBYv9EV0xBQkltcAAHb3J0URgBAv8sX4C/nvnGuQBRQAIBQVgB/2z5sOP+o16MAFFUAgFBbAH/lrWzA/jI5J4AUWgCAUF4Af/TfB+ItGsGmwBRdAIBQYgB/+AreSMQf6m+AFGEAgFBlAH/tUQOJgG2MOEAUZACAUHAAQEMAAARAer/bWFzOjpzY2gCZW1hOjptb2RlbDo6d2ViZQ9yZXN0AAABDAAAEQHS/21hcy5zY2hlAm1hLm1vZGVsLndlYmVyZXMBdAAAAQwAABEBYv9kZS56YWxmLgAHbWFzAAABDAAAEQGa/1dlYkJlcmVzAXREV0RJbXBvA3J0AAABDAAAEQFK/3dlYmVyZXN0AAABAQwAADEBegL/Z2l0aHViLmMIb20vemFsZi1ycG0vbWFzLWluZnJhc3RydWN0dXJlL2NhcG5wcm90b19zY2hlbWFzL2dlbi9nby9tb2RlbC93ZT9iZXJlc3QAAA==",  # model/weberest/web-berest-data-import.capnp
    "ECJQBgb/b6o+FJ2tpKEAESwD/5u3a4KiaLTEAAABM9oBVwIxFcIBES0HAAARKUcRVQcAAP9tb2RlbC93ZQZiZXJlc3Qvd2ViLWJlcmVzdC1kYXRhLWltcG9ydC5jYXBucDpEV0xBQkltcG9ydABQAQFRBAMFAAD/0scjqiyXA+sBB8r8SYxWvLkREVoAAhEJB/9pbXBvcnREYQADdGFAAVABAQ==",  # model/weberest/web-berest-data-import.capnp:DWLABImport
    "EEVQBgb/0scjqiyXA+sAETgBAAAFAwcAATEVUgIAARExrwAB/21vZGVsL3dlCGJlcmVzdC93ZWItYmVyZXN0LWRhdGEtaW1wb3J0LmNhcG5wOkRXTEFCSW1wb3J0LmltcG9ydERhdGEkUGFyYW0Bc1EMAwQAAAQBAAARRRoAAFFAAwFRTAIBEQEBFAEBAAARSSoAAFFEAwFRUAIBEQICFAECAAARTSoAAFFIAwFRVAIBA2lkAQwAAgEMAAEPZHdsYQENAAIBDQABD2R3bGIBDQACAQ0AAQ==",  # model/weberest/web-berest-data-import.capnp:DWLABImport.importData$Params
    "EEdQBgb/B8r8SYxWvLkAUTgBAQAABQEHAAExFVoCAAERMa8AAf9tb2RlbC93ZQhiZXJlc3Qvd2ViLWJlcmVzdC1kYXRhLWltcG9ydC5jYXBucDpEV0xBQkltcG9ydC5pbXBvcnREYXRhJFJlc3VsA3RzUQwDBAAABAEAABFFGgAAUUADAVFMAgEBARQBAQAAEUlKAABRSAMBUVQCARECARQBAgAAEVFKAABRUAMBUVwCAQNpZAEMAAIBDAAB/3N1Y2Nlc3NBAAAAAQEAAgEBAAH/c3VjY2Vzc0IAAAABAQACAQEAAQ==",  # model/weberest/web-berest-data-import.capnp:DWLABImport.importData$Results
]

# Load schemas and build module structure
_loader = capnp.SchemaLoader()
for _schema_b64 in _SCHEMA_NODES:
    _schema_data = base64.b64decode(_schema_b64)
    _node_reader = schema_capnp.Node.from_bytes_packed(_schema_data)
    _loader.load_dynamic(_node_reader)

# Build module structure inline
DWLABImport = _InterfaceModule(
    _loader.get(0xA1A4AD9D143EAA6F).as_interface(),
    "DWLABImport",
)

DWLABImport.Server.ImportdataResultTuple = NamedTuple(
    "ImportdataResultTuple",
    [("id", object), ("successA", object), ("successB", object)],
)
