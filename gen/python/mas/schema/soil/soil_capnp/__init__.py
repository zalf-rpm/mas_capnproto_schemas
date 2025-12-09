"""This is an automatically generated stub for `soil.capnp`."""

import base64
from typing import NamedTuple

import capnp
import schema_capnp
from capnp.lib.capnp import _EnumModule, _InterfaceModule, _StructModule

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EFNQBgb/URmJEQ81P/8AAQUAAxEVWhEZdxF1ZwAC/3NvaWwuY2FwAANucFEcAQH/CrRh/8ij5MIAETEy/2clzcbhGjmeABEtav9P2jpb8EBGmAARLTL/DcoifghlQL0AESky/5CHOogcv0vfABElYv8pnEGTpcJn/wARJUL/4WTcJxSnmqAAESFCH1NUeXBl/1Byb3BlcnR5AA9OYW1lH0xheWVyH1F1ZXJ5/1Byb2ZpbGVEAAdhdGF/UHJvZmlsZX9TZXJ2aWNlURABAv8sX4C/nvnGuQBRKAIBQTwB/2z5sOP+o16MAFE4AgFBSAH/4Ct5IxB/qb4AUUQCAUFQAf+1RA4mAbYw4QBRTAIBQXgBAQwAABEBkv9tYXM6OnNjaAFlbWE6OnNvaQFsAAABDAAAEQGC/21hcy5zY2hlAW1hLnNvaWwAAAABDAAAEQEqD3NvaWwAAAEMAAAxASoC/2dpdGh1Yi5jB29tL3phbGYtcnBtL21hcy1pbmZyYXN0cnVjdHVyZS9jYXBucHJvdG9fc2NoZW1hcy9nZW4vZ28vD3NvaWwAAA==",  # soil.capnp
    "EBpQBgb/CrRh/8ij5MIAEQsC/1EZiREPNT//AAABMw0CeQIRFYoRHQcAABEZNwAB/3NvaWwuY2FwAW5wOlNUeXBlAABQAQFRCAECAAAREUIAAAEBEQkiAAB/dW5rbm93bgdrYTU=",  # soil.capnp:SType
    "EHRQBgb/ZyXNxuEaOZ4AEQsC/1EZiREPNT//AAABM3sCsQcRFcIRHQcAADEZ5wEAAf9zb2lsLmNhcAJucDpQcm9wZXJ0eU5hbWUAUAEBUVABAgAAEelKAAABARHlKgAAAQIR3SoAAAEDEdUqAAABBBHNGgAAAQURxUoAAAEGEcFyAAABBxG9cgAAAQgRuWIAAAEJEbVaAAABChGxcgAAAQsRrbIAAAEMEa1aAAABDRGpagAAAQ4xpQoBAAABDxGtSgAAARARqUIAAAEREaFCAAABEhGZcgAAARMRlWoAAP9zb2lsVHlwZQAAAA9zYW5kD2NsYXkPc2lsdANwSP9zY2VsZXRvbgAAAP9vcmdhbmljQwAfYXJib27/b3JnYW5pY00AH2F0dGVy/2J1bGtEZW5zAAdpdHn/cmF3RGVuc2kAA3R5/2ZpZWxkQ2FwAB9hY2l0ef9wZXJtYW5lbgF0V2lsdGluZx9Qb2ludP9zYXR1cmF0aQADb27/c29pbE1vaXMAD3R1cmX/c29pbFdhdGUDckNvbmR1Y3Rpdml0eUNvZWZmaWNpZW50AAD/YW1tb25pdW0AAAB/bml0cmF0ZX9jblJhdGlv/2luR3JvdW5kAB93YXRlcv9pbXBlbmV0cgAPYWJsZQ==",  # soil.capnp:PropertyName
    "EElQBgb/T9o6W/BARpgAUQsBAf9RGYkRDzU//wAFAgcAADOzB34JERWKER0XAAARKa8AAf9zb2lsLmNhcAFucDpMYXllcgAAUQQBAf+wcdvPG7j0kgARAUr/UHJvcGVydHkAAABRDAMEAAAEAQAAEUVaAABRRAMBUWACAQEBFAEBAAARXSoAAFFYAwFRZAIBEQIBFAECAAARYWIAAFFgAwFRbAIB/3Byb3BlcnRpAANlcwEOAAFQAwEBEP+wcdvPG7j0kgAAAQEOAAEPc2l6ZQEKAAIBCgAB/2Rlc2NyaXB0AAdpb24BDAACAQwAAQ==",  # soil.capnp:Layer
    "EF9QBgb/sHHbzxu49JIAUREBAf9P2jpb8EBGmABFAQcEAQEz5wexCBEV0hEhBwAAMR0fAQAB/3NvaWwuY2FwAm5wOkxheWVyLlByb3BlcnQBeVABAVEUAwQAAAQBAAARfSoAAFF4AwFRhAIBHQH//wEUAQEAABGBSgAAUYADAVGMAgEdAv7/IBQBAgAAEYk6AABRhAMBUZACAQ0D/f8UAQMAABGNKgAAUYgDAVGUAgENBPz/FAEEAAARkTIAAFGMAwFRmAIBD25hbWUBD/9nJc3G4Ro5ngAAAQEPAAH/ZjMyVmFsdWUAAAABCgACAQoAAT9iVmFsdWUBAQACAQEAAQ90eXBlAQwAAgEMAAEfdW5zZXQABg==",  # soil.capnp:Layer.Property
    "EE1QBgb/DcoifghlQL0AUQsBAf9RGYkRDzU//wAFAgcAADOACeEMERWKER0XAAARJa8AAf9zb2lsLmNhcAFucDpRdWVyeQAAUQQBAf8/lIitBxtOvwARATo/UmVzdWx0UQwDBAAABAEAABFFUgAAUUQDAVFgAgERAQEUAQEAABFdSgAAUVwDAVF4AgEBAhQBAgEBEXViAABRdAMBUYACAf9tYW5kYXRvcgABeQEOAAFQAwEBD/9nJc3G4Ro5ngAAAQEOAAH/b3B0aW9uYWwAAAABDgABUAMBAQ//ZyXNxuEaOZ4AAAEBDgAB/29ubHlSYXdEAAdhdGEBAQACBQEBAAE=",  # soil.capnp:Query
    "EElQBgb/P5SIrQcbTr8AUREBAf8NyiJ+CGVAvQAFAgcAADMgCm4LERXCER0HAAARGa8AAf9zb2lsLmNhcAJucDpRdWVyeS5SZXN1bHQAUAEBUQwDBAAABAEAABFFOgAAUUADAVFMAgEBARQBAQAAEUlSAABRSAMBUWQCARECARQBAgAAEWFKAABRYAMBUXwCAT9mYWlsZWQBAQACAQEAAf9tYW5kYXRvcgABeQEOAAFQAwEBD/9nJc3G4Ro5ngAAAQEOAAH/b3B0aW9uYWwAAAABDgABUAMBAQ//ZyXNxuEaOZ4AAAEBDgAB",  # soil.capnp:Query.Result
    "EDZQBgb/kIc6iBy/S98AUQsBAf9RGYkRDzU//wAFAQcAADPjDLYNERW6ER0HAAARGXcAAf9zb2lsLmNhcAFucDpQcm9maT9sZURhdGFQAQFRCAMEAAAEAQAAESk6AABRJAMBUUACAQEBFAEBAQERPYoAAFFAAwFRTAIBP2xheWVycwEOAAFQAwEBEP9P2jpb8EBGmAAAAQEOAAH/cGVyY2VudGEBZ2VPZkFyZWEAAAEKAALBCshCAAE=",  # soil.capnp:ProfileData
    "ECxQBgb/KZxBk6XCZ/8AEQsD/1EZiREPNT//AAABM7gNoQ4RFZoRHQcAABEZhxFtJwAA/3NvaWwuY2FwAW5wOlByb2ZpA2xlUAEBUQgDBQAA/+J0Y3SVtgTnAZCHOogcv0vfETEqAAIRJQcBAf9RkRv9+CMqjQH7j8w5MPzx7BEZYgACEREHD2RhdGFAAf9nZW9Mb2NhdAAHaW9uQAFRCAEB/9VInFnL0a+yAAAA/2XLNtyg2qfBAAAA",  # soil.capnp:Profile
    "EBFQBgb/4nRjdJW2BOcAERMBAAAEBwABERX6AAT/c29pbC5jYXACbnA6UHJvZmlsZS5kYXRhJD9QYXJhbXM=",  # soil.capnp:Profile.data$Params
    "EBJQBgb/UZEb/fgjKo0AERMBAAAEBwABMRUyAQAE/3NvaWwuY2FwA25wOlByb2ZpbGUuZ2VvTG9jYXRpb24kUB9hcmFtcw==",  # soil.capnp:Profile.geoLocation$Params
    "EDBQBgb/+4/MOTD88ewAUQoBAv8k/Md5IFSQkAAEBwAAMx8DjgMRFbIRHQcAABEZdwAB/2dlby5jYXBuAXA6TGF0TG9uH0Nvb3JkUAEBUQgDBAAABAEAABEpIgAAUSQDAVEwAgERAQEUAQEAABEtIgAAUSgDAVE0AgEHbGF0AQsAAgELAAEHbG9uAQsAAgELAAE=",  # geo.capnp:LatLonCoord
    "EExQBgb/4WTcJxSnmqAAEQsD/1EZiREPNT//AAABM6MOGBIRFZoRHRcAADElBwER7ScAAP9zb2lsLmNhcAFucDpTZXJ2aQNjZVEEAQH/Ocn7j1ar+PQAEQE6P1N0cmVhbVEQAwUAAP8NyiJ+CGVAvQE/lIitBxtOvxFxygACEXEHAQH/J3w+69hf7I0B437Zao6/opgRZdIAAhFlBwEC/8GTlr8555fbAa0Xk4xmXpGgEVmSAAIRVQcBA/8NyiJ+CGVAvQFXeSvJR0Gn0RFJkgACEUUH/2NoZWNrQXZhAmlsYWJsZVBhcmFtZXRlcnMAAEAB/2dldEFsbEF2AmFpbGFibGVQYXJhbWV0ZXIBc0AB/2Nsb3Nlc3RQAXJvZmlsZXNBAXRAAf9zdHJlYW1BbAFsUHJvZmlsZQFzQAFRCAEB/9VInFnL0a+yAAAA/2XLNtyg2qfBAAAA",  # soil.capnp:Service
    "EB9QBgb/Ocn7j1ar+PQAERMD/+Fk3CcUp5qgAAABM/MQsRERFdIRIQcAABEdRxFJBwAA/3NvaWwuY2FwAm5wOlNlcnZpY2UuU3RyZWEBbVABAVEEAwUAAP8FvBP2jSTagQH43Yt0wuR6nxERagACEQkH/25leHRQcm9mAA9pbGVzQAFQAQE=",  # soil.capnp:Service.Stream
    "ECRQBgb/BbwT9o0k2oEAURoBAQAABAcAATEVcgEAAREhPwAB/3NvaWwuY2FwBG5wOlNlcnZpY2UuU3RyZWFtLm5leHRQcm9maWxlcyRQH2FyYW1zUQQDBAAABAEBARENSgAAUQwDAVEYAgH/bWF4Q291bnQAAAABBQACAQUBZAAA",  # soil.capnp:Service.Stream.nextProfiles$Params
    "EChQBgb/+N2LdMLkep8AERoBAAAFAQcAATEVegEAAREhPwAB/3NvaWwuY2FwBG5wOlNlcnZpY2UuU3RyZWFtLm5leHRQcm9maWxlcyRSP2VzdWx0c1EEAwQAAAQBAAARDUoAAFEMAwFRKAIB/3Byb2ZpbGVzAAAAAQ4AAVADAQER/ymcQZOlwmf/AAABAQ4AAQ==",  # soil.capnp:Service.Stream.nextProfiles$Results
    "ECVQBgb/J3w+69hf7I0AURMBAQAABAcAATEVogEAARElPwAB/3NvaWwuY2FwBW5wOlNlcnZpY2UuZ2V0QWxsQXZhaWxhYmxlUGFyYW1ldGVycyRQYXIHYW1zUQQDBAAABAEAABENYgAAUQwDAVEYAgH/b25seVJhd0QAB2F0YQEBAAIBAQAB",  # soil.capnp:Service.getAllAvailableParameters$Params
    "ED1QBgb/437Zao6/opgAERMBAAAFAgcAATEVqgEAAREldwAB/3NvaWwuY2FwBW5wOlNlcnZpY2UuZ2V0QWxsQXZhaWxhYmxlUGFyYW1ldGVycyRSZXMPdWx0c1EIAwQAAAQBAAARKVIAAFEoAwFRRAIBEQEBFAEBAAARQUoAAFFAAwFRXAIB/21hbmRhdG9yAAF5AQ4AAVADAQEP/2clzcbhGjmeAAABAQ4AAf9vcHRpb25hbAAAAAEOAAFQAwEBD/9nJc3G4Ro5ngAAAQEOAAE=",  # soil.capnp:Service.getAllAvailableParameters$Results
    "EDJQBgb/wZOWvznnl9sAERMBAAAFAgcAATEVYgEAAREhdwAB/3NvaWwuY2FwBG5wOlNlcnZpY2UuY2xvc2VzdFByb2ZpbGVzQXQkUGFyB2Ftc1EIAwQAAAQBAAARKTIAAFEkAwFRMAIBEQEBFAEBAAARLTIAAFEoAwFRNAIBH2Nvb3JkARD/+4/MOTD88ewAAAEBEAABH3F1ZXJ5ARD/DcoifghlQL0AAAEBEAAB",  # soil.capnp:Service.closestProfilesAt$Params
    "EChQBgb/rReTjGZekaAAERMBAAAFAQcAATEVagEAAREhPwAB/3NvaWwuY2FwBG5wOlNlcnZpY2UuY2xvc2VzdFByb2ZpbGVzQXQkUmVzD3VsdHNRBAMEAAAEAQAAEQ1KAABRDAMBUSgCAf9wcm9maWxlcwAAAAEOAAFQAwEBEf8pnEGTpcJn/wAAAQEOAAE=",  # soil.capnp:Service.closestProfilesAt$Results
    "ECRQBgb/V3kryUdBp9EAERMBAAAFAQcAATEVagEAAREhPwAB/3NvaWwuY2FwBG5wOlNlcnZpY2Uuc3RyZWFtQWxsUHJvZmlsZXMkUmVzD3VsdHNRBAMEAAAEAQAAEQ1iAABRDAMBURgCAf9hbGxQcm9maQAHbGVzARH/Ocn7j1ar+PQAAAEBEQAB",  # soil.capnp:Service.streamAllProfiles$Results
]

# Load schemas and build module structure
_loader = capnp.SchemaLoader()
for _schema_b64 in _SCHEMA_NODES:
    _schema_data = base64.b64decode(_schema_b64)
    _node_reader = schema_capnp.Node.from_bytes_packed(_schema_data)
    _loader.load_dynamic(_node_reader)

# Build module structure inline
SType = _EnumModule(_loader.get(0xC2E4A3C8FF61B40A).as_enum(), "SType")
PropertyName = _EnumModule(_loader.get(0x9E391AE1C6CD2567).as_enum(), "PropertyName")
Layer = _StructModule(_loader.get(0x984640F05B3ADA4F).as_struct(), "Layer")
Layer.Property = _StructModule(_loader.get(0x92F4B81BCFDB71B0).as_struct(), "Property")
Query = _StructModule(_loader.get(0xBD4065087E22CA0D).as_struct(), "Query")
Query.Result = _StructModule(_loader.get(0xBF4E1B07AD88943F).as_struct(), "Result")
ProfileData = _StructModule(_loader.get(0xDF4BBF1C883A8790).as_struct(), "ProfileData")
Profile = _InterfaceModule(_loader.get(0xFF67C2A593419C29).as_interface(), "Profile")
Service = _InterfaceModule(_loader.get(0xA09AA71427DC64E1).as_interface(), "Service")
Service.Stream = _InterfaceModule(
    _loader.get(0xF4F8AB568FFBC939).as_interface(),
    "Stream",
)

Profile.Server.DataResultTuple = NamedTuple(
    "DataResultTuple",
    [("layers", object), ("percentageOfArea", object)],
)
Profile.Server.GeolocationResultTuple = NamedTuple(
    "GeolocationResultTuple",
    [("lat", object), ("lon", object)],
)
Service.Server.CheckavailableparametersResultTuple = NamedTuple(
    "CheckavailableparametersResultTuple",
    [("failed", object), ("mandatory", object), ("optional", object)],
)
Service.Server.ClosestprofilesatResultTuple = NamedTuple(
    "ClosestprofilesatResultTuple",
    [("profiles", object)],
)
Service.Server.GetallavailableparametersResultTuple = NamedTuple(
    "GetallavailableparametersResultTuple",
    [("mandatory", object), ("optional", object)],
)
Service.Server.StreamallprofilesResultTuple = NamedTuple(
    "StreamallprofilesResultTuple",
    [("allProfiles", object)],
)
Service.Stream.Server.NextprofilesResultTuple = NamedTuple(
    "NextprofilesResultTuple",
    [("profiles", object)],
)
