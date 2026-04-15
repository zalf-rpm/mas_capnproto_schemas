# pyright: reportAttributeAccessIssue=false, reportArgumentType=false
"""This is an automatically generated stub for `crop.capnp`."""

import base64

import capnp
import schema_capnp
from capnp.lib.capnp import _EnumModule, _InterfaceModule, _StructModule

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EEBQBgb/cvmdluEkivkAAQoAAxEVghEZJxExZwAC/2Nyb3AvY3JvAXAuY2FwbnAAUQgBAf+EXL8ko5eN6AARCSr/xGs4wLbC3I0AEQVCD0Nyb3B/U2VydmljZVEQAQL/LF+Av575xrkAUSgCAUE8Af9s+bDj/qNejABROAIBQUgB/+AreSMQf6m+AFFEAgFBUAH/tUQOJgG2MOEAUUwCAUFwAQEMAAARAZL/bWFzOjpzY2gBZW1hOjpjcm8BcAAAAQwAABEBgv9tYXMuc2NoZQFtYS5jcm9wAAAAAQwAABEBKg9jcm9wAAABDAAAMQGyAf9naXRodWIuYwVvbS96YWxmLXJwbS9tYXNfY2FwbnByb3RvX3NjaGVtYXMvZ2VuL2dvHy9jcm9wAAA=",  # crop/crop.capnp
    "EDdQBgb/hFy/JKOXjegAERAD/3L5nZbhJIr5AAABM+cBQQMRFaoRHQcAABEZxxGZJwAA/2Nyb3AvY3JvAXAuY2FwbnA6D0Nyb3BQAQFRDAMFAQL/W448dA4BbsgBhlRRLXL8+uQRUVoAAhFJBwEB/3pRtN8X8W7yAbqUJKW7BDe/ET1KAAIRNQcAAP+0MDEqMhzd9AFIZN7uXomqtBEpQgACER0H/3BhcmFtZXRlAANyc0AB/2N1bHRpdmFyAAAAQAF/c3BlY2llc0ABUQgBAf/VSJxZy9GvsgAAAP9lyzbcoNqnwQAAAA==",  # crop/crop.capnp:Crop
    "EBJQBgb/W448dA4BbsgAERUBAAAEBwABMRU6AQAE/2Nyb3AvY3JvA3AuY2FwbnA6Q3JvcC5wYXJhbWV0ZXJzJD9QYXJhbXM=",  # crop/crop.capnp:Crop.parameters$Params
    "ECJQBgb/hlRRLXL8+uQAERUBAAAFAQcAATEVQgEAAREdPwAB/2Nyb3AvY3JvBHAuY2FwbnA6Q3JvcC5wYXJhbWV0ZXJzJFJlc3VsdHMAUQQDBAAABAEAABENOgAAUQgDAVEUAgE/cGFyYW1zARIAAgESAAE=",  # crop/crop.capnp:Crop.parameters$Results
    "EBJQBgb/elG03xfxbvIAERUBAAAEBwABMRUqAQAE/2Nyb3AvY3JvA3AuY2FwbnA6Q3JvcC5jdWx0aXZhciRQYQ9yYW1z",  # crop/crop.capnp:Crop.cultivar$Params
    "ECJQBgb/upQkpbsEN78AERUBAAAFAQcAATEVMgEAAREdPwAB/2Nyb3AvY3JvA3AuY2FwbnA6Q3JvcC5jdWx0aXZhciRSZR9zdWx0c1EEAwQAAAQBAAARDSoAAFEIAwFRFAIBD2luZm8BEP/T2gP+y37L1AAAAQEQAAE=",  # crop/crop.capnp:Crop.cultivar$Results
    "EEJQBgb/09oD/st+y9QAERQB/8mKqHWnyfGZAAUDBwAAMzwBnwExFRIBESUHAAARIa8AAf9jb21tb24vYwNvbW1vbi5jYXBucDpJZEluZm9ybWF0aW8BblABAVEMAwQAAAQBAAARRRoAAFFAAwFRTAIBEQEBFAEBAAARSSoAAFFEAwFRUAIBEQICFAECAAARTWIAAFFMAwFRWAIBA2lkAQwAAgEMAAEPbmFtZQEMAAIBDAAB/2Rlc2NyaXB0AAdpb24BDAACAQwAAQ==",  # common/common.capnp:IdInformation
    "EBJQBgb/tDAxKjIc3fQAERUBAAAEBwABMRUiAQAE/2Nyb3AvY3JvA3AuY2FwbnA6Q3JvcC5zcGVjaWVzJFBhcgdhbXM=",  # crop/crop.capnp:Crop.species$Params
    "ECJQBgb/SGTe7l6JqrQAERUBAAAFAQcAATEVKgEAAREdPwAB/2Nyb3AvY3JvA3AuY2FwbnA6Q3JvcC5zcGVjaWVzJFJlcw91bHRzUQQDBAAABAEAABENKgAAUQgDAVEUAgEPaW5mbwEQ/9PaA/7LfsvUAAABARAAAQ==",  # crop/crop.capnp:Crop.species$Results
    "EBVQBgb/xGs4wLbC3I0AERAD/3L5nZbhJIr5AAABM0MDrgMRFcIRHQcAABEZBxEZFwAA/2Nyb3AvY3JvAnAuY2FwbnA6U2VydmljZQBQAQFQAwVRBAEB/7gzBmDRS3vKAAAA",  # crop/crop.capnp:Service
    "EB9QBgb/1UicWcvRr7IAERQD/8mKqHWnyfGZAAABM6EBEgIxFQoBESUHAAARIUcRSQcAAP9jb21tb24vYwNvbW1vbi5jYXBucDpJZGVudGlmaWFibGUAAFABAVEEAwUAAP+x3kkez6GKnQHT2gP+y37L1BERKgACEQUHD2luZm9AAVABAQ==",  # common/common.capnp:Identifiable
    "EC1QBgb/Zcs23KDap8EAER4D/yZrX0fT/l6FAAABM4sLIxExFUoBESk3AAARWUcRgQcAAP9wZXJzaXN0ZQRuY2UvcGVyc2lzdGVuY2UuY2FwbnA6UGVyc2lzdGVudAAAUQwBAf9DA14ixKrg1QAREVr/E+wsmO/RW9wAERFi/1IunxaBD3CPABERiv9TYXZlUGFyYQADbXP/U2F2ZVJlc3UAB2x0c/9SZWxlYXNlUwF0dXJkeVJlZgAAUQQDBQAA/0MDXiLEquDVARPsLJjv0VvcEREqAAIRBQcPc2F2ZUABUAEB",  # persistence/persistence.capnp:Persistent
    "EDtQBgb/uDMGYNFLe8oAERgD/2mCfpzD4Bv+AAABMwEHtAoxFQoBESUXAAARLccRsRcAAP9yZWdpc3RyeQMvcmVnaXN0cnkuY2FwbnA6UmVnaXN0cnkAAFEEAQH/E6z3DFGHecEAEQEyH0VudHJ5UQwDBQAA/5vCNF7m5kmcAbAwc4G1YL+yEVGiAAIRTQcBAf+dvEiy4YMSiQHT2gP+y37L1BFBagACETkHAQL/+sVRYXFT/J8BTQaGtG716uQRLUIAAhEhB/9zdXBwb3J0ZQFkQ2F0ZWdvcgdpZXNAAf9jYXRlZ29yeQAPSW5mb0ABf2VudHJpZXNAAVEEAQH/1UicWcvRr7IAAAA=",  # registry/registry.capnp:Registry
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

Crop = _InterfaceModule(_loader.get(0xE88D97A324BF5C84).as_interface(), "Crop")
Service = _InterfaceModule(_loader.get(0x8DDCC2B6C0386BC4).as_interface(), "Service")
