"""This is an automatically generated stub for `persistence.capnp`."""

import base64
from typing import NamedTuple

import capnp
import schema_capnp
from capnp.lib.capnp import _InterfaceModule, _StructModule

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EGdQBgb/JmtfR9P+XoUAAQwAAxEVkhEdpxG1ZwAC/3BlcnNpc3RlAW5jZS5jYXBuAXBRKAEB/43Ri9V0XQrhABFJMv8NW6BxBoFH+wARRUL/h4DE2/LN7NkAEUFC/03egx0naG2IABE9Uv86ykfR+r2znwARPVL/Zcs23KDap8EAET1a/zwu2SeEIbafABE9Sv+fHdC2+pGNqgARPYr/7ScvYAosnI8AEUFC/41gN98vIlOCABE9mh9WYXRJZH9BZGRyZXNzf1ZhdFBhdGj/U3R1cmR5UmUAAWb/SGVhcnRiZWEAAXT/UGVyc2lzdGUAA250/1Jlc3RvcmVyAAAA/0hvc3RQb3J0AVJlc29sdmVyAAB/R2F0ZXdhef9HYXRld2F5UgFlZ2lzdHJhYgNsZVEQAQL/LF+Av575xrkAUSgCAUFAAf9s+bDj/qNejABRPAIBQVAB/+AreSMQf6m+AFFMAgFBXAH/tUQOJgG2MOEAUVgCAUGIAQEMAAARAcr/bWFzOjpzY2gCZW1hOjpwZXJzaXN0ZW5jZQABAQwAABEBuv9tYXMuc2NoZQFtYS5wZXJzaT9zdGVuY2UAAAEMAAARAWL/cGVyc2lzdGUAB25jZQAAAQwAADEBYgL/Z2l0aHViLmMIb20vemFsZi1ycG0vbWFzLWluZnJhc3RydWN0dXJlL2NhcG5wcm90b19zY2hlbWFzL2dlbi9nby9wZXJzaXN0ZQduY2UAAA==",  # persistence.capnp
    "EFJQBgb/jdGL1XRdCuEAURIBBP8ma19H0/5ehQAEBwAAM9sBFgMRFcIRHQcAABEZ5wAB/3BlcnNpc3RlAm5jZS5jYXBucDpWYXRJZABQAQFREAMEAAAEAQAAEWFaAABRYAMBUWwCAREBARQBAQAAEWlaAABRaAMBUXQCARECAhQBAgAAEXFaAABRcAMBUXwCAREDAxQBAwAAEXlaAABReAMBUYQCAf9wdWJsaWNLZQADeTABCQACAQkAAf9wdWJsaWNLZQADeTEBCQACAQkAAf9wdWJsaWNLZQADeTIBCQACAQkAAf9wdWJsaWNLZQADeTMBCQACAQkAAQ==",  # persistence.capnp:VatId
    "EDlQBgb/DVugcQaBR/sAURIBA/8ma19H0/5ehQBFAQcCAQkzGAPEBxEV0hEhBwAAER2vAAH/cGVyc2lzdGUCbmNlLmNhcG5wOkFkZHJlcwFzUAEBUQwDBAz//wEB/2mKiSgEXbKPABFFIgACEQIIFAECAAARLSoAAFEoAwFRNAIBDQH+/xQBAwAAETEqAABRLAMBUTgCAQdpcDYPcG9ydAEHAAIBBwABD2hvc3QBDAACAQwAAQ==",  # persistence.capnp:Address
    "EDBQBgb/aYqJKARdso8AURoBA/8NW6BxBoFH+wAVAQcBAAERFfIAAREZdwAB/3BlcnNpc3RlAm5jZS5jYXBucDpBZGRyZXMfcy5pcDZRCAMEAAAEAQAAESlCAABRJAMBUTACAREBARQBAQAAES1CAABRKAMBUTQCAX9sb3dlcjY0AQkAAgEJAAF/dXBwZXI2NAEJAAIBCQAB",  # persistence.capnp:Address.ip6
    "EDFQBgb/h4DE2/LN7NkAERIB/yZrX0fT/l6FAAUCBwAAM8YHowgRFdIRIQcAABEddwAB/3BlcnNpc3RlAm5jZS5jYXBucDpWYXRQYXQBaFABAVEIAwQAAAQBAAARKRoAAFEkAwFRMAIBEQEBFAEBAAARLUIAAFEoAwFRNAIBA2lkARD/jdGL1XRdCuEAAAEBEAABf2FkZHJlc3MBEP8NW6BxBoFH+wAAAQEQAAE=",  # persistence.capnp:VatPath
    "EDhQBgb/Td6DHSdobYgAERIB/yZrX0fT/l6FAAUCBwAAM6UIYwsRFeIRIScAABE1dwAB/3BlcnNpc3RlAm5jZS5jYXBucDpTdHVyZHkHUmVmUQgBAf8jd8hg7ZnX/QARCTL/iLQRf7QrQfoAEQUyH093bmVyH1Rva2VuUQgDBAAABAEAABEpIgAAUSQDAVEwAgERAQEUAQEAABEtSgAAUSwDAVE4AgEHdmF0ARD/h4DE2/LN7NkAAAEBEAAB/2xvY2FsUmVmAAAAARD/iLQRf7QrQfoAAAEBEAAB",  # persistence.capnp:SturdyRef
    "ECNQBgb/I3fIYO2Z1/0AERwB/03egx0naG2IAAUBBwAAM0gJOAoxFRIBESUHAAARIT8AAf9wZXJzaXN0ZQNuY2UuY2FwbnA6U3R1cmR5UmVmLk93bmUBclABAVEEAwQAAAQBAAARDSoAAFEIAwFRFAIBD2d1aWQBDAACAQwAAQ==",  # persistence.capnp:SturdyRef.Owner
    "EDJQBgb/iLQRf7QrQfoAURwBAf9N3oMdJ2htiABFAQcCAAAzwgphCzEVEgERJQcAABEhdwAB/3BlcnNpc3RlA25jZS5jYXBucDpTdHVyZHlSZWYuVG9rZQFuUAEBUQgDBAz//wQBAAARKSoAAFEkAwFRMAIBDQH+/xQBAQAAES0qAABRKAMBUTQCAQ90ZXh0AQwAAgEMAAEPZGF0YQENAAIBDQAB",  # persistence.capnp:SturdyRef.Token
    "EB5QBgb/OspH0fq9s58AERID/yZrX0fT/l6FAAABM2ULkAsRFeIRIQcAABEdRxFFBwAA/3BlcnNpc3RlAm5jZS5jYXBucDpIZWFydGIHZWF0UAEBUQQDBQAA/8o0ob/airaKAfgV6KbCgjb0EREqAAIRBQcPYmVhdEABUAEB",  # persistence.capnp:Heartbeat
    "EBJQBgb/yjShv9qKtooAERwBAAAEBwABMRVCAQAE/3BlcnNpc3RlBG5jZS5jYXBucDpIZWFydGJlYXQuYmVhdCRQYXJhbXMA",  # persistence.capnp:Heartbeat.beat$Params
    "EBNQBgb/+BXopsKCNvQAERwBAAAEBwABMRVKAQAE/3BlcnNpc3RlBG5jZS5jYXBucDpIZWFydGJlYXQuYmVhdCRSZXN1bHRzAAA=",  # persistence.capnp:Heartbeat.beat$Results
    "ECtQBgb/Zcs23KDap8EAERID/yZrX0fT/l6FAAABM5ILKhERFeoRITcAABFRRxF5BwAA/3BlcnNpc3RlAm5jZS5jYXBucDpQZXJzaXMPdGVudFEMAQH/QwNeIsSq4NUAERFa/xPsLJjv0VvcABERYv9SLp8WgQ9wjwAREYr/U2F2ZVBhcmEAA21z/1NhdmVSZXN1AAdsdHP/UmVsZWFzZVMBdHVyZHlSZWYAAFEEAwUAAP9DA14ixKrg1QET7CyY79Fb3BERKgACEQUHD3NhdmVAAVABAQ==",  # persistence.capnp:Persistent
    "ECNQBgb/QwNeIsSq4NUAER0B/2XLNtyg2qfBAAUBBwAAM+wMnA4xFUIBESUHAAARIT8AAf9wZXJzaXN0ZQRuY2UuY2FwbnA6UGVyc2lzdGVudC5TYXZlUGFyYW1zAFABAVEEAwQAAAQBAAARDUIAAFEIAwFRFAIBf3NlYWxGb3IBEP8jd8hg7ZnX/QAAAQEQAAE=",  # persistence.capnp:Persistent.SaveParams
    "EDVQBgb/E+wsmO/RW9wAER0B/2XLNtyg2qfBAAUCBwAAM58OyBAxFUoBESkHAAARJXcAAf9wZXJzaXN0ZQRuY2UuY2FwbnA6UGVyc2lzdGVudC5TYXZlUmVzdWx0cwAAUAEBUQgDBAAABAEAABEpUgAAUSgDAVE0AgERAQEUAQEAABExSgAAUTADAVE8AgH/c3R1cmR5UmUAAWYBEP9N3oMdJ2htiAAAAQEQAAH/dW5zYXZlU1IAAAABEP9N3oMdJ2htiAAAAQEQAAE=",  # persistence.capnp:Persistent.SaveResults
    "ECpQBgb/Ui6fFoEPcI8AER0D/2XLNtyg2qfBAAABM8wQKBExFXIBESkHAAARJUcRdQcAAP9wZXJzaXN0ZQRuY2UuY2FwbnA6UGVyc2lzdGVudC5SZWxlYXNlU3R1ch9keVJlZlABAVEEAwUAAP8VfIDZIIzbpAFT6BAk424tkxERQhERHwABES0Hf3JlbGVhc2VRBAEC//GNLxcSYLnCAFEEAgFBFAEBDAAAEQFS/3JlbGVhc2VTAAFSAABAAVABAQ==",  # persistence.capnp:Persistent.ReleaseSturdyRef
    "EBVQBgb/FXyA2SCM26QAES4BAAAEBwABMRXqAQAE/3BlcnNpc3RlBm5jZS5jYXBucDpQZXJzaXN0ZW50LlJlbGVhc2VTdHVyZHlSZWYucmVsZWFzZSRQYQ9yYW1z",  # persistence.capnp:Persistent.ReleaseSturdyRef.release$Params
    "ECVQBgb/U+gQJONuLZMAUS4BAQAABAcAATEV8gEAAREpPwAB/3BlcnNpc3RlBm5jZS5jYXBucDpQZXJzaXN0ZW50LlJlbGVhc2VTdHVyZHlSZWYucmVsZWFzZSRSZR9zdWx0c1EEAwQAAAQBAAARDUIAAFEIAwFRFAIBf3N1Y2Nlc3MBAQACAQEAAQ==",  # persistence.capnp:Persistent.ReleaseSturdyRef.release$Results
    "ECJQBgb/PC7ZJ4Qhtp8AERID/yZrX0fT/l6FAAABMywR4xMRFdoRIRcAABEtRxFVBwAA/3BlcnNpc3RlAm5jZS5jYXBucDpSZXN0b3IDZXJRBAEB/zrXN0p25UHFABEBcv9SZXN0b3JlUAAfYXJhbXNRBAMFAAD/Otc3SnblQcUBJU0uJR1tltoREUIAAhEFB39yZXN0b3JlQAFQAQE=",  # persistence.capnp:Restorer
    "EDVQBgb/Otc3SnblQcUAERsB/zwu2SeEIbafAAUCBwAAM28RZBMxFUoBESkHAAARJXcAAf9wZXJzaXN0ZQRuY2UuY2FwbnA6UmVzdG9yZXIuUmVzdG9yZVBhcmFtcwAAUAEBUQgDBAAABAEAABEpSgAAUSgDAVE0AgERAQEUAQEAABExSgAAUTADAVE8AgH/bG9jYWxSZWYAAAABEP+ItBF/tCtB+gAAAQEQAAH/c2VhbGVkQnkAAAABEP8jd8hg7ZnX/QAAAQEQAAE=",  # persistence.capnp:Restorer.RestoreParams
    "ECNQBgb/JU0uJR1tltoAERsBAAAFAQcAATEVWgEAAREhPwAB/3BlcnNpc3RlBG5jZS5jYXBucDpSZXN0b3Jlci5yZXN0b3JlJFJlc3VsA3RzUQQDBAAABAEAABENIgAAUQgDAVEUAgEHY2FwARIEAwABARIAAQ==",  # persistence.capnp:Restorer.restore$Results
    "EDFQBgb/nx3QtvqRjaoAERID/yZrX0fT/l6FAAABM+UTDxoxFRoBESUXAAARMUcRgScAAP9wZXJzaXN0ZQNuY2UuY2FwbnA6SG9zdFBvcnRSZXNvbHYDZXJRBAEB/7KQRnB198qwABEBUv9SZWdpc3RyYQABclEEAwUAAP8zuywPb5b45gGMCyKNUV8Y/BERQhERHwABES0Hf3Jlc29sdmVRBAEC//GNLxcSYLnCAFEEAgFBFAEBDAAAEQFq/1Jlc29sdmVJAA9kZW50AABAAVEIAQH/1UicWcvRr7IAAAD/PC7ZJ4Qhtp8AAAA=",  # persistence.capnp:HostPortResolver
    "ECVQBgb/spBGcHX3yrAAESMD/58d0Lb6kY2qAAABM7EUZBkxFWoBESkXAAARNUcRYQcAAP9wZXJzaXN0ZQRuY2UuY2FwbnA6SG9zdFBvcnRSZXNvbHZlci5SZWdpcw90cmFyUQQBAf8PDUb/Yo8BvwARAXr/UmVnaXN0ZXIAP1BhcmFtc1EEAwUAAP8PDUb/Yo8BvwG5i/kzZoH8+hERSgACEQkH/3JlZ2lzdGVyAAAAQAFQAQE=",  # persistence.capnp:HostPortResolver.Registrar
    "EGRQBgb/Dw1G/2KPAb8AUS0BAf+ykEZwdffKsAAFBAcAADMyFZoXMRXiARExBwAAMS0fAQAB/3BlcnNpc3RlBm5jZS5jYXBucDpIb3N0UG9ydFJlc29sdmVyLlJlZ2lzdHJhci5SZWdpc3RlclBhcgdhbXNQAQFRFAMEAAAEAQAAEX1iAABRfAMBUYgCAREBARQBAQAAEYUqAABRgAMBUYwCAQECFAECAAARiSoAAFGEAwFRkAIBEQMCFAEDAAARjTIAAFGIAwFRlAIBEQQDFAEEAAARkXIAAFGQAwFRnAIB/2Jhc2U2NFZhAAd0SWQBDAACAQwAAQ9ob3N0AQwAAgEMAAEPcG9ydAEHAAIBBwABH2FsaWFzAQwAAgEMAAH/aWRlbnRpdHkAH1Byb29mAQ0AAgENAAE=",  # persistence.capnp:HostPortResolver.Registrar.RegisterParams
    "EDdQBgb/uYv5M2aB/PoAUS0BAQAABQEHAAExFfIBAAERKXcAAf9wZXJzaXN0ZQZuY2UuY2FwbnA6SG9zdFBvcnRSZXNvbHZlci5SZWdpc3RyYXIucmVnaXN0ZXIkUmUfc3VsdHNRCAMEAAAEAQAAESlSAABRKAMBUTQCAQEBFAEBAAARMbIAAFE0AwFRQAIB/2hlYXJ0YmVhAAF0ARH/OspH0fq9s58AAAEBEQAB/3NlY3NIZWFyAXRiZWF0SW50H2VydmFsAQgAAgEIAAE=",  # persistence.capnp:HostPortResolver.Registrar.register$Results
    "ECRQBgb/M7ssD2+W+OYAESMBAAAFAQcAATEVkgEAARElPwAB/3BlcnNpc3RlBW5jZS5jYXBucDpIb3N0UG9ydFJlc29sdmVyLnJlc29sdmUkUGFyYW0Bc1EEAwQAAAQBAAARDRoAAFEIAwFRFAIBA2lkAQwAAgEMAAE=",  # persistence.capnp:HostPortResolver.resolve$Params
    "EDNQBgb/jAsijVFfGPwAUSMBAQAABQEHAAExFZoBAAERJXcAAf9wZXJzaXN0ZQVuY2UuY2FwbnA6SG9zdFBvcnRSZXNvbHZlci5yZXNvbHZlJFJlc3VsA3RzUQgDBAAABAEAABEpKgAAUSQDAVEwAgEBARQBAQAAES0qAABRKAMBUTQCAQ9ob3N0AQwAAgEMAAEPcG9ydAEHAAIBBwAB",  # persistence.capnp:HostPortResolver.resolve$Results
    "ECdQBgb/7ScvYAosnI8AERID/yZrX0fT/l6FAAABMxEa7B0RFdIRIRcAABEtRxFZJwAA/3BlcnNpc3RlAm5jZS5jYXBucDpHYXRld2EBeVEEAQH/qn/peV3GMqIAEQFa/1JlZ1Jlc3VsAAN0c1EEAwUAAP+rq0SvKRWMxwGqf+l5XcYyohERSgACEQkH/3JlZ2lzdGVyAAAAQAFRCAEB/9VInFnL0a+yAAAA/zwu2SeEIbafAAAA",  # persistence.capnp:Gateway
    "EEVQBgb/qn/peV3GMqIAURoBAf/tJy9gCiycjwAFAgcAADORG+odMRUqARElBwAAESGvAAH/cGVyc2lzdGUDbmNlLmNhcG5wOkdhdGV3YXkuUmVnUmVzD3VsdHNQAQFRDAMEAAAEAQAAEUVSAABRRAMBUVACAREBARQBAQAAEU1SAABRTAMBUVgCAQECFAECAAARVbIAAFFYAwFRZAIB/3N0dXJkeVJlAAFmARD/Td6DHSdobYgAAAEBEAAB/2hlYXJ0YmVhAAF0ARH/OspH0fq9s58AAAEBEQAB/3NlY3NIZWFyAXRiZWF0SW50H2VydmFsAQgAAgEIAAE=",  # persistence.capnp:Gateway.RegResults
    "ECNQBgb/q6tErykVjMcAERoBAAAFAQcAATEVUgEAAREhPwAB/3BlcnNpc3RlBG5jZS5jYXBucDpHYXRld2F5LnJlZ2lzdGVyJFBhcmFtAXNRBAMEAAAEAQAAEQ0iAABRCAMBURQCAQdjYXABEgQDAAEBEgAB",  # persistence.capnp:Gateway.register$Params
    "ECFQBgb/jWA33y8iU4IAERID/yZrX0fT/l6FAAABM+4dNx8xFSoBESUHAAARIUcRUQcAAP9wZXJzaXN0ZQNuY2UuY2FwbnA6R2F0ZXdheVJlZ2lzdHIPYWJsZVABAVEEAwUAAP9EnbfSeF1MtgG28O56hrC49xERmgACEQ0H/3N0dXJkeVJlAWZBdEdhdGV3A2F5QAFQAQE=",  # persistence.capnp:GatewayRegistrable
    "EDZQBgb/RJ230nhdTLYAESUBAAAFAgcAATEV+gEAAREpdwAB/3BlcnNpc3RlBm5jZS5jYXBucDpHYXRld2F5UmVnaXN0cmFibGUuc3R1cmR5UmVmQXRHYXRld2F5JD9QYXJhbXNRCAMEAAAEAQAAESlSAABRKAMBUTQCAREBARQBAQAAETFSAABRMAMBUTwCAf9nYXRld2F5UwABUgEQ/03egx0naG2IAAABARAAAf9nYXRld2F5SQABZAEMAAIBDAAB",  # persistence.capnp:GatewayRegistrable.sturdyRefAtGateway$Params
    "ECZQBgb/tvDueoawuPcAESUBAAAFAQcAATEVAgIAAREpPwAB/3BlcnNpc3RlB25jZS5jYXBucDpHYXRld2F5UmVnaXN0cmFibGUuc3R1cmR5UmVmQXRHYXRld2F5JFJlc3VsdHMAUQQDBAAABAEAABENggAAUQwDAVEYAgH/c2VsZkF0R2EBdGV3YXlTUgABEP9N3oMdJ2htiAAAAQEQAAE=",  # persistence.capnp:GatewayRegistrable.sturdyRefAtGateway$Results
]

# Load schemas and build module structure
_loader = capnp.SchemaLoader()
for _schema_b64 in _SCHEMA_NODES:
    _schema_data = base64.b64decode(_schema_b64)
    _node_reader = schema_capnp.Node.from_bytes_packed(_schema_data)
    _loader.load_dynamic(_node_reader)

# Build module structure inline
VatId = _StructModule(_loader.get(0xE10A5D74D58BD18D).as_struct(), "VatId")
Address = _StructModule(_loader.get(0xFB47810671A05B0D).as_struct(), "Address")
VatPath = _StructModule(_loader.get(0xD9ECCDF2DBC48087).as_struct(), "VatPath")
SturdyRef = _StructModule(_loader.get(0x886D68271D83DE4D).as_struct(), "SturdyRef")
SturdyRef.Owner = _StructModule(_loader.get(0xFDD799ED60C87723).as_struct(), "Owner")
SturdyRef.Token = _StructModule(_loader.get(0xFA412BB47F11B488).as_struct(), "Token")
Heartbeat = _InterfaceModule(
    _loader.get(0x9FB3BDFAD147CA3A).as_interface(),
    "Heartbeat",
)
Persistent = _InterfaceModule(
    _loader.get(0xC1A7DAA0DC36CB65).as_interface(),
    "Persistent",
)
Persistent.SaveParams = _StructModule(
    _loader.get(0xD5E0AAC4225E0343).as_struct(),
    "SaveParams",
)
Persistent.SaveResults = _StructModule(
    _loader.get(0xDC5BD1EF982CEC13).as_struct(),
    "SaveResults",
)
Persistent.ReleaseSturdyRef = _InterfaceModule(
    _loader.get(0x8F700F81169F2E52).as_interface(),
    "ReleaseSturdyRef",
)
Restorer = _InterfaceModule(_loader.get(0x9FB6218427D92E3C).as_interface(), "Restorer")
Restorer.RestoreParams = _StructModule(
    _loader.get(0xC541E5764A37D73A).as_struct(),
    "RestoreParams",
)
HostPortResolver = _InterfaceModule(
    _loader.get(0xAA8D91FAB6D01D9F).as_interface(),
    "HostPortResolver",
)
HostPortResolver.Registrar = _InterfaceModule(
    _loader.get(0xB0CAF775704690B2).as_interface(),
    "Registrar",
)
HostPortResolver.Registrar.RegisterParams = _StructModule(
    _loader.get(0xBF018F62FF460D0F).as_struct(),
    "RegisterParams",
)
Gateway = _InterfaceModule(_loader.get(0x8F9C2C0A602F27ED).as_interface(), "Gateway")
Gateway.RegResults = _StructModule(
    _loader.get(0xA232C65D79E97FAA).as_struct(),
    "RegResults",
)
GatewayRegistrable = _InterfaceModule(
    _loader.get(0x8253222FDF37608D).as_interface(),
    "GatewayRegistrable",
)

Gateway.Server.RegisterResultTuple = NamedTuple(
    "RegisterResultTuple",
    [("sturdyRef", object), ("heartbeat", object), ("secsHeartbeatInterval", object)],
)
GatewayRegistrable.Server.SturdyrefatgatewayResultTuple = NamedTuple(
    "SturdyrefatgatewayResultTuple",
    [("selfAtGatewaySR", object)],
)
HostPortResolver.Server.ResolveResultTuple = NamedTuple(
    "ResolveResultTuple",
    [("host", object), ("port", object)],
)
HostPortResolver.Registrar.Server.RegisterResultTuple = NamedTuple(
    "RegisterResultTuple",
    [("heartbeat", object), ("secsHeartbeatInterval", object)],
)
Persistent.Server.SaveResultTuple = NamedTuple(
    "SaveResultTuple",
    [("sturdyRef", object), ("unsaveSR", object)],
)
Persistent.ReleaseSturdyRef.Server.ReleaseResultTuple = NamedTuple(
    "ReleaseResultTuple",
    [("success", object)],
)
Restorer.Server.RestoreResultTuple = NamedTuple("RestoreResultTuple", [("cap", object)])
