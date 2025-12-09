"""This is an automatically generated stub for `service.capnp`."""

import base64
from typing import NamedTuple

import capnp
import schema_capnp
from capnp.lib.capnp import _InterfaceModule, _StructModule

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EEtQBgb/wMa70pjfKvUAAQgAAxEVchEZRxFRZwAC/3NlcnZpY2UuAB9jYXBucFEQAQH/SfaNGYv4wf4AERky/8sTwiKSgqWrABEVcv9/nCacueywigARFUL/dpIuI1hkX80AERFSH0FkbWlu/1NpbXBsZUZhAB9jdG9yeX9GYWN0b3J5/1N0b3BwYWJsAAFlURABAv8sX4C/nvnGuQBRKAIBQTwB/2z5sOP+o16MAFE4AgFBTAH/4Ct5IxB/qb4AUUgCAUFUAf+1RA4mAbYw4QBRUAIBQXwBAQwAABEBqv9tYXM6OnNjaAFlbWE6OnNlcg92aWNlAAABDAAAEQGa/21hcy5zY2hlAW1hLnNlcnZpA2NlAAABDAAAEQFCf3NlcnZpY2UAAAEMAAAxAUIC/2dpdGh1Yi5jCG9tL3phbGYtcnBtL21hcy1pbmZyYXN0cnVjdHVyZS9jYXBucHJvdG9fc2NoZW1hcy9nZW4vZ28vc2VydmljZQAAAA==",  # service.capnp
    "EEtQBgb/SfaNGYv4wf4AEQ4D/8DGu9KY3yr1AAABM6wBDQQRFaIRHQcAADEZRwER8RcAAP9zZXJ2aWNlLgFjYXBucDpBZAdtaW5QAQFRFAMFAAD/NPLn2hvzJ9YBWZdUrpAiHOARkVIAAhGJBwEB//0QEWmKNb+aAcFLxxpKGf3WEX1aAAIRdQcBAv94W+83zdPD3QGHl3U+BhoqzhFpKgACEV0HAQP/llgpjWJxQv8BmLPbeIU9QvURUVoAAhFJBwEE/4O6aLb5coTcASyr4gjbeV6xET16AAIRNQf/aGVhcnRiZWEAAXRAAf9zZXRUaW1lbwADdXRAAQ9zdG9wQAH/aWRlbnRpdGkAA2VzQAH/dXBkYXRlSWQAP2VudGl0eUABUQQBAf/VSJxZy9GvsgAAAA==",  # service.capnp:Admin
    "EBJQBgb/NPLn2hvzJ9YAERQBAAAEBwABMRUqAQAE/3NlcnZpY2UuA2NhcG5wOkFkbWluLmhlYXJ0YmVhdCRQYQ9yYW1z",  # service.capnp:Admin.heartbeat$Params
    "EBJQBgb/WZdUrpAiHOAAERQBAAAEBwABMRUyAQAE/3NlcnZpY2UuA2NhcG5wOkFkbWluLmhlYXJ0YmVhdCRSZR9zdWx0cw==",  # service.capnp:Admin.heartbeat$Results
    "ECJQBgb//RARaYo1v5oAURQBAQAABAcAATEVMgEAAREdPwAB/3NlcnZpY2UuA2NhcG5wOkFkbWluLnNldFRpbWVvdXQkUB9hcmFtc1EEAwQAAAQBAAARDUIAAFEIAwFRFAIBf3NlY29uZHMBCQACAQkAAQ==",  # service.capnp:Admin.setTimeout$Params
    "EBJQBgb/wUvHGkoZ/dYAERQBAAAEBwABMRU6AQAE/3NlcnZpY2UuA2NhcG5wOkFkbWluLnNldFRpbWVvdXQkUj9lc3VsdHM=",  # service.capnp:Admin.setTimeout$Results
    "EBFQBgb/eFvvN83Tw90AERQBAAAEBwABMRUCAQAE/3NlcnZpY2UuA2NhcG5wOkFkbWluLnN0b3AkUGFyYW1zAA==",  # service.capnp:Admin.stop$Params
    "EBJQBgb/h5d1PgYaKs4AERQBAAAEBwABMRUKAQAE/3NlcnZpY2UuA2NhcG5wOkFkbWluLnN0b3AkUmVzdWx0cwAA",  # service.capnp:Admin.stop$Results
    "EBJQBgb/llgpjWJxQv8AERQBAAAEBwABMRUyAQAE/3NlcnZpY2UuA2NhcG5wOkFkbWluLmlkZW50aXRpZXMkUB9hcmFtcw==",  # service.capnp:Admin.identities$Params
    "ECZQBgb/mLPbeIU9QvUAERQBAAAFAQcAATEVOgEAAREdPwAB/3NlcnZpY2UuA2NhcG5wOkFkbWluLmlkZW50aXRpZXMkUj9lc3VsdHNRBAMEAAAEAQAAEQ0yAABRCAMBUSQCAR9pbmZvcwEOAAFQAwEBEP/T2gP+y37L1AAAAQEOAAE=",  # service.capnp:Admin.identities$Results
    "EEFQBgb/09oD/st+y9QAEQ0B/8mKqHWnyfGZAAUDBwAAM0sBrgERFdoRIQcAABEdrwAB/2NvbW1vbi5jAmFwbnA6SWRJbmZvcm1hdGkDb25QAQFRDAMEAAAEAQAAEUUaAABRQAMBUUwCAREBARQBAQAAEUkqAABRRAMBUVACARECAhQBAgAAEU1iAABRTAMBUVgCAQNpZAEMAAIBDAABD25hbWUBDAACAQwAAf9kZXNjcmlwdAAHaW9uAQwAAgEMAAE=",  # common.capnp:IdInformation
    "EDJQBgb/g7potvlyhNwAERQBAAAFAgcAATEVUgEAAREhdwAB/3NlcnZpY2UuBGNhcG5wOkFkbWluLnVwZGF0ZUlkZW50aXR5JFBhcmFtAXNRCAMEAAAEAQAAESkyAABRJAMBUTACAREBARQBAQAAES1CAABRKAMBUTQCAR9vbGRJZAEMAAIBDAABf25ld0luZm8BEP/T2gP+y37L1AAAAQEQAAE=",  # service.capnp:Admin.updateIdentity$Params
    "EBNQBgb/LKviCNt5XrEAERQBAAAEBwABMRVaAQAE/3NlcnZpY2UuBGNhcG5wOkFkbWluLnVwZGF0ZUlkZW50aXR5JFJlc3VsA3Rz",  # service.capnp:Admin.updateIdentity$Results
    "ECBQBgb/yxPCIpKCpasAEQ4D/8DGu9KY3yr1AAABMw8ELQURFeIRIQcAABEdRxFFFwAA/3NlcnZpY2UuAmNhcG5wOlNpbXBsZUZhY3QHb3J5UAEBUQQDBQAA/9223GDcbymoAaoe3uAoOKOJERE6AAIRBQc/Y3JlYXRlQAFRBAEB/9VInFnL0a+yAAAA",  # service.capnp:SimpleFactory
    "EBNQBgb/3bbcYNxvKagAERwBAAAEBwABMRVSAQAE/3NlcnZpY2UuBGNhcG5wOlNpbXBsZUZhY3RvcnkuY3JlYXRlJFBhcmFtAXM=",  # service.capnp:SimpleFactory.create$Params
    "ECdQBgb/qh7e4Cg4o4kAERwBAAAFAQcAATEVWgEAAREhPwAB/3NlcnZpY2UuBGNhcG5wOlNpbXBsZUZhY3RvcnkuY3JlYXRlJFJlc3VsA3RzUQQDBAAABAEAABENKgAAUQgDAVEkAgEPY2FwcwEOAAFQAwEBEf/VSJxZy9GvsgAAAQEOAAE=",  # service.capnp:SimpleFactory.create$Results
    "EB5QBgb/1UicWcvRr7IAEQ0D/8mKqHWnyfGZAAABM7ABIQIRFdIRIQcAABEdRxFFBwAA/2NvbW1vbi5jAmFwbnA6SWRlbnRpZmlhYmwBZVABAVEEAwUAAP+x3kkez6GKnQHT2gP+y37L1BERKgACEQUHD2luZm9AAVABAQ==",  # common.capnp:Identifiable
    "EBJQBgb/sd5JHs+hip0AERoBAAAEBwABMRUyAQAE/2NvbW1vbi5jA2FwbnA6SWRlbnRpZmlhYmxlLmluZm8kUB9hcmFtcw==",  # common.capnp:Identifiable.info$Params
    "EEpQBgb/f5wmnLnssIoAEQ4D/8DGu9KY3yr1AAAAEAEzLwWtCREVshEdJwAAETmHEeEXEekP/3NlcnZpY2UuAWNhcG5wOkZhH2N0b3J5UQgBAf+XkarMF4W4wgARCWr/LrZ831NqgbkAEQla/0NyZWF0ZVBhAA9yYW1z/0FjY2Vzc0luAANmb1EIAwUAAP+XkarMF4W4wgEutnzfU2qBuRExOgAAQSwBQTwBEU0HAQH/KoizKjVn1dQBBc/ctSfBYqkRQbIAAEFEAUFUARFlBz9jcmVhdGURAR9RBAIB/3+cJpy57LCKAAEBAAARAR9RBAIB/3+cJpy57LCKAAEBAABAAf9zZXJ2aWNlSQFudGVyZmFjZR9OYW1lcxEBH1EEAgH/f5wmnLnssIoAAQEAABEBH1EEAgH/f5wmnLnssIoAAQEAAEABUQQBAf/VSJxZy9GvsgAAAEEEAREBQn9QYXlsb2Fk",  # service.capnp:Factory
    "EFxQBgb/l5GqzBeFuMIAURYBAf9/nCacueywigAFAgcQATPbBSwHMRUaARElBwAAESGvAAH/c2VydmljZS4DY2FwbnA6RmFjdG9yeS5DcmVhdGVQYXJhA21zUAEBUQwDBAAABAEBARFFegAAUUQDAVFQAgEBARQBAQAAEU3SAABRVAMBUbgCARECARQBAgAAEbVaAABRtAMBUcACAf90aW1lb3V0UwA/ZWNvbmRzAQkAAgEJAxAOAAD/aW50ZXJmYWMCZU5hbWVUb1JlZ2lzdHJ5UwFSAQ4AAVADAQEQ/zNHFyVHhtS5AAAAQAERAR9RBAIB/zNHFyVHhtS5AAAAEQEnUQgBAQEBUQgDAQEBURADAQEMAAIBDAACAQ4AAf9tc2dQYXlsbwADYWQBEgEB/3+cJpy57LCKAAAAARIAAQ==",  # service.capnp:Factory.CreateParams
    "EDVQBgb/M0cXJUeG1LkAEQ0B/8mKqHWnyfGZAAUCBxABM6II0QgRFZIRHQcAABEZdwAAEY0X/2NvbW1vbi5jAWFwbnA6UGFpAXJQAQFRCAMEAAAEAQAAESkiAABRJAMBUTACAREBARQBAQAAES0iAABRKAMBUTQCAQdmc3QBEgEB/zNHFyVHhtS5AAAAARIAAQdzbmQBEgUBAf8zRxclR4bUuQAAAAESAAFBCAERBRIRBRIBRgFT",  # common.capnp:Pair
    "EEdQBgb/LrZ831NqgbkAERYB/3+cJpy57LCKAAUDBxABMzAHQQgxFQoBESUHAAARIa8AAf9zZXJ2aWNlLgNjYXBucDpGYWN0b3J5LkFjY2Vzc0luZm8AAFABAVEMAwQAAAQBAAARRUoAAFFEAwFRUAIBEQEBFAEBAAARTWIAAFFMAwFRaAIBEQICFAECAAARZTIAAFFgAwFRbAIB/2FkbWluQ2FwAAAAARIEAwABARIAAf9zZXJ2aWNlQwAHYXBzAQ4AAVADAQER/9VInFnL0a+yAAABAQ4AAR9lcnJvcgEMAAIBDAAB",  # service.capnp:Factory.AccessInfo
    "EBRQBgb/KoizKjVn1dQAERYBAAAEBxABAAAxFZoBAAT/c2VydmljZS4FY2FwbnA6RmFjdG9yeS5zZXJ2aWNlSW50ZXJmYWNlTmFtZXMkUGFyYQNtcw==",  # service.capnp:Factory.serviceInterfaceNames$Params
    "EChQBgb/Bc/ctSfBYqkAERYBAAAFAQcQAQAAMRWiAQABESU/AAH/c2VydmljZS4FY2FwbnA6RmFjdG9yeS5zZXJ2aWNlSW50ZXJmYWNlTmFtZXMkUmVzdQdsdHNRBAMEAAAEAQAAEQ0yAABRCAMBUSQCAR9uYW1lcwEOAAFQAwEBDAACAQ4AAQ==",  # service.capnp:Factory.serviceInterfaceNames$Results
    "EB1QBgb/dpIuI1hkX80AEQ4D/8DGu9KY3yr1AAABM68JCgoRFcIRHQcAABEZRxFBBwAA/3NlcnZpY2UuAmNhcG5wOlN0b3BwYWJsZQBQAQFRBAMFAAD/korUFs6Pr5QB2M+UwoRlxNIRESoAAhEFBw9zdG9wQAFQAQE=",  # service.capnp:Stoppable
    "EBJQBgb/korUFs6Pr5QAERgBAAAEBwABMRUiAQAE/3NlcnZpY2UuA2NhcG5wOlN0b3BwYWJsZS5zdG9wJFBhcgdhbXM=",  # service.capnp:Stoppable.stop$Params
    "ECJQBgb/2M+UwoRlxNIAURgBAQAABAcAATEVKgEAAREdPwAB/3NlcnZpY2UuA2NhcG5wOlN0b3BwYWJsZS5zdG9wJFJlcw91bHRzUQQDBAAABAEAABENQgAAUQgDAVEUAgF/c3VjY2VzcwEBAAIBAQAB",  # service.capnp:Stoppable.stop$Results
]

# Load schemas and build module structure
_loader = capnp.SchemaLoader()
for _schema_b64 in _SCHEMA_NODES:
    _schema_data = base64.b64decode(_schema_b64)
    _node_reader = schema_capnp.Node.from_bytes_packed(_schema_data)
    _loader.load_dynamic(_node_reader)

# Build module structure inline
Admin = _InterfaceModule(_loader.get(0xFEC1F88B198DF649).as_interface(), "Admin")
SimpleFactory = _InterfaceModule(
    _loader.get(0xABA5829222C213CB).as_interface(),
    "SimpleFactory",
)
Factory = _InterfaceModule(_loader.get(0x8AB0ECB99C269C7F).as_interface(), "Factory")
Factory.CreateParams = _StructModule(
    _loader.get(0xC2B88517CCAA9197).as_struct(),
    "CreateParams",
)
Factory.AccessInfo = _StructModule(
    _loader.get(0xB9816A53DF7CB62E).as_struct(),
    "AccessInfo",
)
Stoppable = _InterfaceModule(
    _loader.get(0xCD5F6458232E9276).as_interface(),
    "Stoppable",
)

Admin.Server.IdentitiesResultTuple = NamedTuple(
    "IdentitiesResultTuple",
    [("infos", object)],
)
Factory.Server.CreateResultTuple = NamedTuple(
    "CreateResultTuple",
    [("adminCap", object), ("serviceCaps", object), ("error", object)],
)
Factory.Server.ServiceinterfacenamesResultTuple = NamedTuple(
    "ServiceinterfacenamesResultTuple",
    [("names", object)],
)
SimpleFactory.Server.CreateResultTuple = NamedTuple(
    "CreateResultTuple",
    [("caps", object)],
)
Stoppable.Server.StopResultTuple = NamedTuple("StopResultTuple", [("success", object)])
