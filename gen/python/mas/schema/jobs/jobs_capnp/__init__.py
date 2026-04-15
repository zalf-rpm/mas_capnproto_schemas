# pyright: reportAttributeAccessIssue=false, reportArgumentType=false
"""This is an automatically generated stub for `jobs.capnp`."""

import base64

import capnp
import schema_capnp
from capnp.lib.capnp import _EnumModule, _InterfaceModule, _StructModule

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EEBQBgb/DGYux+3i5+cAAQoAAxEVghEZJxExZwAC/2pvYnMvam9iAXMuY2FwbnAAUQgBAf9IiKMct2BboAARCSL/8MsT0FRUdLgAEQVCB0pvYn9TZXJ2aWNlURABAv8sX4C/nvnGuQBRKAIBQTwB/2z5sOP+o16MAFE4AgFBSAH/4Ct5IxB/qb4AUUQCAUFQAf+1RA4mAbYw4QBRTAIBQXABAQwAABEBkv9tYXM6OnNjaAFlbWE6OmpvYgFzAAABDAAAEQGC/21hcy5zY2hlAW1hLmpvYnMAAAABDAAAEQEqD2pvYnMAAAEMAAAxAbIB/2dpdGh1Yi5jBW9tL3phbGYtcnBtL21hc19jYXBucHJvdG9fc2NoZW1hcy9nZW4vZ28fL2pvYnMAAA==",  # jobs/jobs.capnp
    "EDRQBgb/SIijHLdgW6AAURABAf8MZi7H7eLn5wAFAQcQATO9ARsCERWiER0HAAARGXcAABGRD/9qb2JzL2pvYgFzLmNhcG5wOgdKb2JQAQFRCAMEAAAEAQAAESkqAABRJAMBUTACAQEBFAEBAQERLXIAAFEsAwFROAIBD2RhdGEBEgEB/0iIoxy3YFugAAAAARIAAf9ub0Z1cnRoZQAfckpvYnMBAQACAQEAAUEEAREBQn9QYXlsb2Fk",  # jobs/jobs.capnp:Job
    "ECFQBgb/8MsT0FRUdLgAERAD/wxmLsft4ufnAAABMx0CdQIRFcIRHQcAABEZRxFBJwAA/2pvYnMvam9iAnMuY2FwbnA6U2VydmljZQBQAQFRBAMFAAD/HANKdn6pO+oBu74eUiLsZ+AREUIAAhEFB39uZXh0Sm9iQAFRCAEB/9VInFnL0a+yAAAA/2XLNtyg2qfBAAAA",  # jobs/jobs.capnp:Service
    "EBJQBgb/HANKdn6pO+oAERgBAAAEBwABMRU6AQAE/2pvYnMvam9iA3MuY2FwbnA6U2VydmljZS5uZXh0Sm9iJD9QYXJhbXM=",  # jobs/jobs.capnp:Service.nextJob$Params
    "ECJQBgb/u74eUiLsZ+AAERgBAAAFAQcAATEVQgEAAREdPwAB/2pvYnMvam9iBHMuY2FwbnA6U2VydmljZS5uZXh0Sm9iJFJlc3VsdHMAUQQDBAAABAEAABENIgAAUQgDAVEUAgEHam9iARD/SIijHLdgW6AAAAEBEAAB",  # jobs/jobs.capnp:Service.nextJob$Results
    "EB9QBgb/1UicWcvRr7IAERQD/8mKqHWnyfGZAAABM6EBEgIxFQoBESUHAAARIUcRSQcAAP9jb21tb24vYwNvbW1vbi5jYXBucDpJZGVudGlmaWFibGUAAFABAVEEAwUAAP+x3kkez6GKnQHT2gP+y37L1BERKgACEQUHD2luZm9AAVABAQ==",  # common/common.capnp:Identifiable
    "EC1QBgb/Zcs23KDap8EAER4D/yZrX0fT/l6FAAABM4sLIxExFUoBESk3AAARWUcRgQcAAP9wZXJzaXN0ZQRuY2UvcGVyc2lzdGVuY2UuY2FwbnA6UGVyc2lzdGVudAAAUQwBAf9DA14ixKrg1QAREVr/E+wsmO/RW9wAERFi/1IunxaBD3CPABERiv9TYXZlUGFyYQADbXP/U2F2ZVJlc3UAB2x0c/9SZWxlYXNlUwF0dXJkeVJlZgAAUQQDBQAA/0MDXiLEquDVARPsLJjv0VvcEREqAAIRBQcPc2F2ZUABUAEB",  # persistence/persistence.capnp:Persistent
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

Job = _StructModule(_loader.get(0xA05B60B71CA38848).as_struct(), "Job")
Service = _InterfaceModule(_loader.get(0xB8745454D013CBF0).as_interface(), "Service")
