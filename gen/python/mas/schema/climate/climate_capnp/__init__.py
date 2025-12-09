"""This is an automatically generated stub for `climate.capnp`."""

import base64
from typing import NamedTuple

import capnp
import schema_capnp
from capnp.lib.capnp import _EnumModule, _InterfaceModule, _StructModule

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EHpQBgb/GEXrEOQ6HaAAAQgAAxEVcjEZBwETDQFnAAL/Y2xpbWF0ZS4AH2NhcG5wUUABAf8Qn97uaWg5zgAReSL/UeODMMXecYYAEXUi/+56NBbkCnjTABFxIv/MlAwxeAfzjgARbSL/NKRdzdGsysgAEWl6/7BtVWbp0jb7ABFpSv/wYFnw0f019gARaUL/oOUiX+x/ptcAEWVq/2S1Wtu0YFfjABFlQv8Z/hPzhXO6hQARYUr/6G1u/kCfdqcAEWFa/0+Wxpv1zMHxABFhev9fDCs11Ah9/gARYUL/2SmZxWzCGKQAEV2q/7KEl5fvgPThABFhuv9EJ6Wi8C3xxQARZfIHR0NNB1JDTQdTU1AHUkNQ/0Vuc2VtYmxlAD9NZW1iZXL/TWV0YWRhdGEAAAB/RGF0YXNldP9NZXRhUGx1cwAPRGF0YX9FbGVtZW50/0xvY2F0aW9uAAAA/1RpbWVTZXJpAANlc/9UaW1lU2VyaQA/ZXNEYXRhf1NlcnZpY2X/Q1NWVGltZVMBZXJpZXNGYWMPdG9yef9BbHRlclRpbQFlU2VyaWVzVz9yYXBwZXL/QWx0ZXJUaW0CZVNlcmllc1dyYXBwZXJGYR9jdG9yeVEQAQL/LF+Av575xrkAUSgCAUE8Af9s+bDj/qNejABROAIBQUwB/+AreSMQf6m+AFFIAgFBVAH/tUQOJgG2MOEAUVACAUF8AQEMAAARAar/bWFzOjpzY2gBZW1hOjpjbGkPbWF0ZQAAAQwAABEBmv9tYXMuc2NoZQFtYS5jbGltYQN0ZQAAAQwAABEBQn9jbGltYXRlAAABDAAAMQFCAv9naXRodWIuYwhvbS96YWxmLXJwbS9tYXMtaW5mcmFzdHJ1Y3R1cmUvY2FwbnByb3RvX3NjaGVtYXMvZ2VuL2dvL2NsaW1hdGUAAAA=",  # climate.capnp
    "EE5QBgb/EJ/e7mloOc4AEQ4C/xhF6xDkOh2gAAABM1ECcQQRFZIRHQcAADEZJwEAAf9jbGltYXRlLgFjYXBucDpHQwFNUAEBUTABAgAAEYlqAAABARGFagAAAQIRgXoAAAEDEX1iAAABBBF5agAAAQURdUoAAAEGEXFaAAABBxFtWgAAAQgRaUoAAAEJEWVSAAABChFhUgAAAQsRXXIAAP9jY2NtYUNhbgAPRXNtMv9pY2hlY0VjRQAPYXJ0aP9pcHNsSXBzbAA/Q201QU1y/21pcm9jTWlyAAdvYzX/bXBpTU1waUUAD3NtTHL/Z2ZkbEVzbTQAAAD/aXBzbENtNmEAA0xy/21waUVzbTEyAANIcv9tcmlFc20yMAAAAP91a2VzbTEwTAABbP9nc3dwM1c1RQABNf9tb2hjSGFkRwAfZW0yRXM=",  # climate.capnp:GCM
    "EDZQBgb/UeODMMXecYYAEQ4C/xhF6xDkOh2gAAABM3MExAURFZIRHQcAABEZrwAB/2NsaW1hdGUuAWNhcG5wOlJDAU1QAQFRHAECAAARTXoAAAEBEUl6AAABAhFFagAAAQMRQUoAAAEEET2SAAABBRE9egAAAQYROWIAAP9jbG1jb21DYwA/bG00ODE3/2dlcmljc1JlAD9tbzIwMTX/a25taVJhY20AD28yMkX/c21oaVJjYTQAAAD/Y2xtY29tQnQBdUNjbG00ODEBN/9tcGlDc2NSZQA/bW8yMDA5/3Vob2hXcmYzAAc2MUg=",  # climate.capnp:RCM
    "ECZQBgb/7no0FuQKeNMAEQ4C/xhF6xDkOh2gAAABM8YFIQcRFZIRHQcAABEZfwAB/2NsaW1hdGUuAWNhcG5wOlNTAVBQAQFRFAECAAARNSoAAAEBES0qAAABAhElKgAAAQMRHSoAAAEEERUqAAAPc3NwMQ9zc3AyD3NzcDMPc3NwNA9zc3A1",  # climate.capnp:SSP
    "EC5QBgb/zJQMMXgH844AEQ4C/xhF6xDkOh2gAAABMyMHBgoRFZIRHQcAABEZrwAB/2NsaW1hdGUuAWNhcG5wOlJDAVBQAQFRHAECAAARTTIAAAEBEUUyAAABAhE9MgAAAQMRNTIAAAEEES0yAAABBRElMgAAAQYRHTIAAB9yY3AxOR9yY3AyNh9yY3AzNB9yY3A0NR9yY3A2MB9yY3A3MB9yY3A4NQ==",  # climate.capnp:RCP
    "EE9QBgb/NKRdzdGsysgAUQ4BAf8YResQ5DodoAAEBwAAMwgK2goRFeoRIQcAABEd5wAB/2NsaW1hdGUuAmNhcG5wOkVuc2VtYmxlTWUPbWJlclABAVEQAwQAAAQBAAARYRIAAFFcAwFRaAIBEQEBFAEBAAARZRIAAFFgAwFRbAIBEQICFAECAAARaRIAAFFkAwFRcAIBEQMDFAEDAAARbRIAAFFoAwFRdAIBAXIBBwACAQcAAQFpAQcAAgEHAAEBcAEHAAIBBwABAWYBBwACAQcAAQ==",  # climate.capnp:EnsembleMember
    "EEJQBgb/sG1VZunSNvsAEQ4B/xhF6xDkOh2gAAUCBwAAM9wKgxARFboRHUcAABFRdwAB/2NsaW1hdGUuAWNhcG5wOk1lP3RhZGF0YVEQAQH/AS5yMEtEBqsAERlS/9s0omjJJI7EABEZMv8MgtAG6n+vhQARFTL/twwWuOrtgccAERFi/1N1cHBvcnRlAAFkH1ZhbHVlH0VudHJ5/0luZm9ybWF0AAdpb25RCAMEAAAEAQAAESlCAABRJAMBUUACAREBARQBAQAAET0qAABROAMBUUQCAX9lbnRyaWVzAQ4AAVADAQEQ/wyC0Abqf6+FAAABAQ4AAQ9pbmZvARH/twwWuOrtgccAAAEBEQAB",  # climate.capnp:Metadata
    "ECtQBgb/AS5yMEtEBqsAERcD/7BtVWbp0jb7AAABMx8LpwwxFQoBESUHAAARIYcReQcAAP9jbGltYXRlLgNjYXBucDpNZXRhZGF0YS5TdXBwb3J0ZWQAAFABAVEIAwUAAP+CVjspd3aIlQFAS8OpjoOe5BExWgACESkHAQH/COL3BZwy0sYBFfdwZvMfp+ARHYIAAhEVB/9jYXRlZ29yaQADZXNAAf9zdXBwb3J0ZQFkVmFsdWVzAEABUAEB",  # climate.capnp:Metadata.Supported
    "EBRQBgb/glY7KXd2iJUAESEBAAAEBwABMRWaAQAE/2NsaW1hdGUuBWNhcG5wOk1ldGFkYXRhLlN1cHBvcnRlZC5jYXRlZ29yaWVzJFBhcmEDbXM=",  # climate.capnp:Metadata.Supported.categories$Params
    "EChQBgb/QEvDqY6DnuQAESEBAAAFAQcAATEVogEAARElPwAB/2NsaW1hdGUuBWNhcG5wOk1ldGFkYXRhLlN1cHBvcnRlZC5jYXRlZ29yaWVzJFJlc3UHbHRzUQQDBAAABAEAABENMgAAUQgDAVEkAgEfdHlwZXMBDgABUAMBARD/09oD/st+y9QAAAEBDgAB",  # climate.capnp:Metadata.Supported.categories$Results
    "EEFQBgb/09oD/st+y9QAEQ0B/8mKqHWnyfGZAAUDBwAAM0sBrgERFdoRIQcAABEdrwAB/2NvbW1vbi5jAmFwbnA6SWRJbmZvcm1hdGkDb25QAQFRDAMEAAAEAQAAEUUaAABRQAMBUUwCAREBARQBAQAAEUkqAABRRAMBUVACARECAhQBAgAAEU1iAABRTAMBUVgCAQNpZAEMAAIBDAABD25hbWUBDAACAQwAAf9kZXNjcmlwdAAHaW9uAQwAAgEMAAE=",  # common.capnp:IdInformation
    "ECRQBgb/COL3BZwy0sYAESEBAAAFAQcAATEVwgEAARElPwAB/2NsaW1hdGUuBmNhcG5wOk1ldGFkYXRhLlN1cHBvcnRlZC5zdXBwb3J0ZWRWYWx1ZXMkUGFyYW1zAFEEAwQAAAQBAAARDToAAFEIAwFRFAIBP3R5cGVJZAEMAAIBDAAB",  # climate.capnp:Metadata.Supported.supportedValues$Params
    "EClQBgb/FfdwZvMfp+AAESEBAAAFAQcAATEVygEAAREpPwAB/2NsaW1hdGUuBmNhcG5wOk1ldGFkYXRhLlN1cHBvcnRlZC5zdXBwb3J0ZWRWYWx1ZXMkUmVzdWx0cwAAUQQDBAAABAEAABENOgAAUQgDAVEkAgE/dmFsdWVzAQ4AAVADAQEQ/9PaA/7LfsvUAAABAQ4AAQ==",  # climate.capnp:Metadata.Supported.supportedValues$Results
    "EF5QBgb/2zSiaMkkjsQAURcBAv+wbVVm6dI2+wBFAQcFAAAzqww8DREV6hEhBwAAMR0fAQAB/2NsaW1hdGUuAmNhcG5wOk1ldGFkYXRhLlYPYWx1ZVABAVEUAwQM//8EAQAAEX0qAABReAMBUYQCAR0B/v8BFAEBAAARgTIAAFF8AwFRiAIBHQL9/wEUAQIAABGFIgAAUYADAVGMAgEdA/z/QBQBAwAAEYkqAABRhAMBUZACAQ0E+/8UAQQAABGNKgAAUYgDAVGUAgEPdGV4dAEMAAIBDAABH2Zsb2F0AQsAAgELAAEHaW50AQUAAgEFAAEPYm9vbAEBAAIBAQABD2RhdGUBEP+NESIDrP7mlwAAAQEQAAE=",  # climate.capnp:Metadata.Value
    "ED5QBgb/jREiA6z+5pcAUQsBAf8q9geLwyvq6AAEBwAAM0sBMwIRFYIRGQcAABEVrwAB/2RhdGUuY2FwAW5wOkRhdGUAUAEBUQwDBAAABAEAABFFKgAAUUADAVFMAgERAQIUAQEAABFJMgAAUUQDAVFQAgERAgMUAQIAABFNIgAAUUgDAVFUAgEPeWVhcgEDAAIBAwABH21vbnRoAQYAAgEGAAEHZGF5AQYAAgEGAAE=",  # date.capnp:Date
    "EMpQBgb/DILQBup/r4UAURcBAf+wbVVm6dI2+wBFAQcMAQEzHA5ZDxEV6hEhBwAAMR2nAgAB/2NsaW1hdGUuAmNhcG5wOk1ldGFkYXRhLkUPbnRyeVABAVEwAwQM//8EAQAAE0EBIgAAUzwBAwFTSAECAQ0B/v8UAQEAABNFASIAAFNAAQMBU0wBAgENAv3/FAECAAATSQFaAABTSAEDAVNUAQIBDQP8/xQBAwAAE1EBIgAAU0wBAwFTWAECAQ0E+/8UAQQAABNVASIAAFNQAQMBU1wBAgENBfr/FAEFAAATWQE6AABTVAEDAVNgAQIBDQb5/xQBBgAAE10BQgAAU1gBAwFTZAECAQ0H+P8UAQcAABNhATIAAFNcAQMBU2gBAgENCPf/FAEIAAATZQEiAABTYAEDAVNsAQIBHQn2/wEUAQkAABNpASIAAFNkAQMBU3ABAgENCvX/FAEKAAATbQFSAABTbAEDAVN4AQIBDQv0/xQBCwAAE3UBYgAAU3QBAwFTgAECAQdnY20BD/8Qn97uaWg5zgAAAQEPAAEHcmNtAQ//UeODMMXecYYAAAEBDwAB/2hpc3RvcmljAANhbAAGB3JjcAEP/8yUDDF4B/OOAAABAQ8AAQdzc3ABD//uejQW5Ap40wAAAQEPAAE/ZW5zTWVtARD/NKRdzdGsysgAAAEBEAABf3ZlcnNpb24BDAACAQwAAR9zdGFydAEQ/40RIgOs/uaXAAABARAAAQdlbmQBEP+NESIDrP7mlwAAAQEQAAEHY28yAQoAAgEKAAH/cGljb250cm8AAWwABv9kZXNjcmlwdAAHaW9uAQwAAgEMAAE=",  # climate.capnp:Metadata.Entry
    "EClQBgb/twwWuOrtgccAERcD/7BtVWbp0jb7AAABM5kPNRAxFRoBESUHAAARIYcRcQcAAP9jbGltYXRlLgNjYXBucDpNZXRhZGF0YS5JbmZvcm1hdGkDb25QAQFRCAMFAAD/BtW34PFecN8B09oD/st+y9QRMToAAhElBwEB/woz+pGc1EbiAXjtX6ULAzWfERk6AAIRDQc/Zm9yT25lQAE/Zm9yQWxsQAFQAQE=",  # climate.capnp:Metadata.Information
    "ECRQBgb/BtW34PFecN8AESMBAAAFAQcAATEVigEAARElPwAB/2NsaW1hdGUuBWNhcG5wOk1ldGFkYXRhLkluZm9ybWF0aW9uLmZvck9uZSRQYXJhbXMAAFEEAwQAAAQBAAARDTIAAFEIAwFRFAIBH2VudHJ5ARD/DILQBup/r4UAAAEBEAAB",  # climate.capnp:Metadata.Information.forOne$Params
    "EBRQBgb/CjP6kZzURuIAESMBAAAEBwABMRWKAQAE/2NsaW1hdGUuBWNhcG5wOk1ldGFkYXRhLkluZm9ybWF0aW9uLmZvckFsbCRQYXJhbXMAAA==",  # climate.capnp:Metadata.Information.forAll$Params
    "EDpQBgb/eO1fpQsDNZ8AESMBAAAFAQcAATEVkgEAARElPwAB/2NsaW1hdGUuBWNhcG5wOk1ldGFkYXRhLkluZm9ybWF0aW9uLmZvckFsbCRSZXN1bHQBc1EEAwQAAAQBAAARDSIAAFEIAwFRbAIBB2FsbAEOAAFQAwEBEP8zRxclR4bUuQAAAEABEQEfUQQCAf8zRxclR4bUuQAAABEBJ1EIAQEBAVEIAwEBAVEQAwEBEP8MgtAG6n+vhQAAAQEQ/9PaA/7LfsvUAAABAQ4AAQ==",  # climate.capnp:Metadata.Information.forAll$Results
    "EDVQBgb/M0cXJUeG1LkAEQ0B/8mKqHWnyfGZAAUCBxABM6II0QgRFZIRHQcAABEZdwAAEY0X/2NvbW1vbi5jAWFwbnA6UGFpAXJQAQFRCAMEAAAEAQAAESkiAABRJAMBUTACAREBARQBAQAAES0iAABRKAMBUTQCAQdmc3QBEgEB/zNHFyVHhtS5AAAAARIAAQdzbmQBEgUBAf8zRxclR4bUuQAAAAESAAFBCAERBRIRBRIBRgFT",  # common.capnp:Pair
    "EFRQBgb/8GBZ8NH9NfYAEQ4D/xhF6xDkOh2gAAABM4UQ2hQRFbIRHRcAADEtRwETDQEnAAD/Y2xpbWF0ZS4BY2FwbnA6RGEfdGFzZXRRBAEB/3XhT/FDoBvWABEBqv9HZXRMb2NhdAFpb25zQ2FsbA9iYWNrURQDBQAA/xVI6G6QRsO0AbBtVWbp0jb7EZFKAAIRiQcBAf8TSk8oPW9JsAEeaq8Dql/u7RF9ogACEXkHAQL/f12horBn+NkBXHPCW25GDOMRbWoAAhFlBwED/7rUKGyFLqDSAd1fHUDc/IyqEVlSAAIRUQcBBP8GRbYx9PCj/AEG+nmLV9u6nhFFggACET0H/21ldGFkYXRhAAAAQAH/Y2xvc2VzdFQBaW1lU2VyaWUHc0F0QAH/dGltZVNlcmkAD2VzQXRAAf9sb2NhdGlvbgABc0AB/3N0cmVhbUxvAWNhdGlvbnMAQAFRCAEB/9VInFnL0a+yAAAA/2XLNtyg2qfBAAAA",  # climate.capnp:Dataset
    "ECFQBgb/deFP8UOgG9YAERYD//BgWfDR/TX2AAABM94SoBMxFVoBESkHAAARJUcRUQcAAP9jbGltYXRlLgRjYXBucDpEYXRhc2V0LkdldExvY2F0aW9uc0NhbGxiYQNja1ABAVEEAwUAAP/g1MQ9mRJB5gHxXQbY1UCF+hERcgACEQkH/25leHRMb2NhAB90aW9uc0ABUAEB",  # climate.capnp:Dataset.GetLocationsCallback
    "ECZQBgb/4NTEPZkSQeYAUSsBAQAABAcAATEVAgIAAREpPwAB/2NsaW1hdGUuB2NhcG5wOkRhdGFzZXQuR2V0TG9jYXRpb25zQ2FsbGJhY2submV4dExvY2F0aW9ucyRQYXJhbXMAUQQDBAAABAEAABENSgAAUQwDAVEYAgH/bWF4Q291bnQAAAABBQACAQUAAQ==",  # climate.capnp:Dataset.GetLocationsCallback.nextLocations$Params
    "ECtQBgb/8V0G2NVAhfoAESsBAAAFAQcAATEVCgIAAREtPwAB/2NsaW1hdGUuB2NhcG5wOkRhdGFzZXQuR2V0TG9jYXRpb25zQ2FsbGJhY2submV4dExvY2F0aW9ucyRSZXN1bHRzAABRBAMEAAAEAQAAEQ1SAABRDAMBUSgCAf9sb2NhdGlvbgABcwEOAAFQAwEBEP8Z/hPzhXO6hQAAAQEOAAE=",  # climate.capnp:Dataset.GetLocationsCallback.nextLocations$Results
    "EGdQBgb/Gf4T84VzuoUAUQ4BAf8YResQ5DodoAAFBAcAADOaGq0cERW6ER0XAAAxJR8BAAH/Y2xpbWF0ZS4BY2FwbnA6TG8/Y2F0aW9uUQQBAf9q1OY6pRP9xQARARoDS1ZRFAMEAAAEAQAAEX0aAABReAMBUYQCAQEBFAEBAAARgUoAAFGAAwFRjAIBEQIBFAECAAARiToAAFGEAwFRkAIBEQMCFAEDAAARjVoAAFGMAwFRmAIBEQQDFAEEAAARlVoAAFGUAwFRsAIBA2lkARD/09oD/st+y9QAAAEBEAAB/2hlaWdodE5OAAAAAQoAAgEKAAE/bGF0bG9uARD/+4/MOTD88ewAAAEBEAAB/3RpbWVTZXJpAANlcwER/+htbv5An3anAAABAREAAf9jdXN0b21EYQADdGEBDgABUAMBARD/atTmOqUT/cUAAAEBDgAB",  # climate.capnp:Location
    "EDFQBgb/atTmOqUT/cUAERcB/xn+E/OFc7qFAAUCBwAAMxAcTRwRFdIRIQcAABEddwAB/2NsaW1hdGUuAmNhcG5wOkxvY2F0aW9uLksBVlABAVEIAwQAAAQBAAARKSIAAFEkAwFRMAIBEQEBFAEBAAARLTIAAFEoAwFRNAIBB2tleQEMAAIBDAABH3ZhbHVlARIAAgESAAE=",  # climate.capnp:Location.KV
    "EDBQBgb/+4/MOTD88ewAUQoBAv8k/Md5IFSQkAAEBwAAMx8DjgMRFbIRHQcAABEZdwAB/2dlby5jYXBuAXA6TGF0TG9uH0Nvb3JkUAEBUQgDBAAABAEAABEpIgAAUSQDAVEwAgERAQEUAQEAABEtIgAAUSgDAVE0AgEHbGF0AQsAAgELAAEHbG9uAQsAAgELAAE=",  # geo.capnp:LatLonCoord
    "EHtQBgb/6G1u/kCfdqcAEQ4D/xhF6xDkOh2gAAABM68ctCIRFcoRIRcAADEtRwITqQEnAAD/Y2xpbWF0ZS4CY2FwbnA6VGltZVNlcmllcwAAUQQBAf/CA+xjz8pmtAARAVr/UmVzb2x1dGkAA29uUSQDBQAA/9H9ctIZBT/qAdZupqHZrQ7NExEBWgACEwkBBwEB/xbJI2sMz2v/ARssAnb0J+y5Ef0yAAIR8QcBAv+hl4quAnDXjwFQoE8UbxR2iRHlOgACEdkHAQP/zX1dxGuYeI4B6eo+10g0PZwRzSoAAhHBBwEE/yU1hbEj+fjvAfuU6qbA3uDCEbUyAAIRqQcBBf/ub0nib1uq+AEytwl9FOff9xGdSgACEZUHAQb/uJP26N5kw4wB34DoymOBI8MRiVIAAhGBBwEH/zRmlVwixCzOAbBtVWbp0jb7EXVKAAIRbQcBCP8Tow8bsJ4yywEZ/hPzhXO6hRFhSgACEVkH/3Jlc29sdXRpAANvbkABH3JhbmdlQAE/aGVhZGVyQAEPZGF0YUABH2RhdGFUQAH/c3VicmFuZ2UAAABAAf9zdWJoZWFkZQABckAB/21ldGFkYXRhAAAAQAH/bG9jYXRpb24AAABAAVEIAQH/1UicWcvRr7IAAAD/Zcs23KDap8EAAAA=",  # climate.capnp:TimeSeries
    "EBxQBgb/wgPsY8/KZrQAERkC/+htbv5An3anAAABMyodhh0xFSIBESUHAAARITcAAf9jbGltYXRlLgNjYXBucDpUaW1lU2VyaWVzLlJlc29sdXQHaW9uUAEBUQgBAgAAEREyAAABAREJOgAAH2RhaWx5P2hvdXJseQ==",  # climate.capnp:TimeSeries.Resolution
    "EBNQBgb/0f1y0hkFP+oAERkBAAAEBwABMRVaAQAE/2NsaW1hdGUuBGNhcG5wOlRpbWVTZXJpZXMucmVzb2x1dGlvbiRQYXJhA21z",  # climate.capnp:TimeSeries.resolution$Params
    "ECRQBgb/1m6modmtDs0AURkBAQAABAcAATEVYgEAAREhPwAB/2NsaW1hdGUuBGNhcG5wOlRpbWVTZXJpZXMucmVzb2x1dGlvbiRSZXN1B2x0c1EEAwQAAAQBAAARDVoAAFEMAwFRGAIB/3Jlc29sdXRpAANvbgEP/8ID7GPPyma0AAABAQ8AAQ==",  # climate.capnp:TimeSeries.resolution$Results
    "EBJQBgb/FskjawzPa/8AERkBAAAEBwABMRUyAQAE/2NsaW1hdGUuA2NhcG5wOlRpbWVTZXJpZXMucmFuZ2UkUB9hcmFtcw==",  # climate.capnp:TimeSeries.range$Params
    "EDJQBgb/GywCdvQn7LkAERkBAAAFAgcAATEVOgEAAREddwAB/2NsaW1hdGUuA2NhcG5wOlRpbWVTZXJpZXMucmFuZ2UkUj9lc3VsdHNRCAMEAAAEAQAAESlSAABRKAMBUTQCAREBARQBAQAAETFCAABRLAMBUTgCAf9zdGFydERhdAABZQEQ/40RIgOs/uaXAAABARAAAX9lbmREYXRlARD/jREiA6z+5pcAAAEBEAAB",  # climate.capnp:TimeSeries.range$Results
    "EBJQBgb/oZeKrgJw148AERkBAAAEBwABMRU6AQAE/2NsaW1hdGUuA2NhcG5wOlRpbWVTZXJpZXMuaGVhZGVyJD9QYXJhbXM=",  # climate.capnp:TimeSeries.header$Params
    "ECZQBgb/UKBPFG8UdokAERkBAAAFAQcAATEVQgEAAREdPwAB/2NsaW1hdGUuBGNhcG5wOlRpbWVTZXJpZXMuaGVhZGVyJFJlc3VsdHMAUQQDBAAABAEAABENOgAAUQgDAVEkAgE/aGVhZGVyAQ4AAVADAQEP/2S1Wtu0YFfjAAABAQ4AAQ==",  # climate.capnp:TimeSeries.header$Results
    "EGtQBgb/ZLVa27RgV+MAEQ4C/xhF6xDkOh2gAAABMx4VmBoRFbIRHQcAADEZzwEAAf9jbGltYXRlLgFjYXBucDpFbB9lbWVudFABAVFMAQIAABHdKgAAAQER1SoAAAECEc0qAAABAxHFOgAAAQQRvUIAAAEFEbUqAAABBhGtSgAAAQcRqWIAAAEIEaVKAAABCRGhSgAAAQoRnVoAAAELEZkiAAABDBGRGgAAAQ0RiSIAAAEOEYFqAAABDxF9igAAARARfWoAAAERMXkiAQAAARIRgTIAAA90bWluD3RhdmcPdG1heD9wcmVjaXB/Z2xvYnJhZA93aW5k/3N1bmhvdXJzAAAA/2Nsb3VkYW1vAAd1bnT/cmVsaHVtaWQAAAD/YWlycHJlc3MAAAD/dmFwb3JwcmUAA3NzB2NvMgNvMwdldDD/ZGV3cG9pbnQAD1RlbXD/c3BlY2lmaWMBSHVtaWRpdHkAAP9zbm93ZmFsbAAPRmx1eP9zdXJmYWNlRANvd253ZWxsaW5nTG9uZ3dhdmVSYWRpYXQHaW9uH3BvdEVU",  # climate.capnp:Element
    "EBJQBgb/zX1dxGuYeI4AERkBAAAEBwABMRUqAQAE/2NsaW1hdGUuA2NhcG5wOlRpbWVTZXJpZXMuZGF0YSRQYQ9yYW1z",  # climate.capnp:TimeSeries.data$Params
    "ECpQBgb/6eo+10g0PZwAERkBAAAFAQcAATEVMgEAAREdPwAB/2NsaW1hdGUuA2NhcG5wOlRpbWVTZXJpZXMuZGF0YSRSZR9zdWx0c1EEAwQAAAQBAAARDSoAAFEIAwFRNAIBD2RhdGEBDgABUAMBAQ4AAVADAQEKAAIBDgAB",  # climate.capnp:TimeSeries.data$Results
    "EBJQBgb/JTWFsSP5+O8AERkBAAAEBwABMRUyAQAE/2NsaW1hdGUuA2NhcG5wOlRpbWVTZXJpZXMuZGF0YVQkUB9hcmFtcw==",  # climate.capnp:TimeSeries.dataT$Params
    "ECpQBgb/+5TqpsDe4MIAERkBAAAFAQcAATEVOgEAAREdPwAB/2NsaW1hdGUuA2NhcG5wOlRpbWVTZXJpZXMuZGF0YVQkUj9lc3VsdHNRBAMEAAAEAQAAEQ0qAABRCAMBUTQCAQ9kYXRhAQ4AAVADAQEOAAFQAwEBCgACAQ4AAQ==",  # climate.capnp:TimeSeries.dataT$Results
    "EDJQBgb/7m9J4m9bqvgAERkBAAAFAgcAATEVSgEAAREhdwAB/2NsaW1hdGUuBGNhcG5wOlRpbWVTZXJpZXMuc3VicmFuZ2UkUGFyYW1zAABRCAMEAAAEAQAAESkyAABRJAMBUTACAREBARQBAQAAES0iAABRKAMBUTQCAR9zdGFydAEQ/40RIgOs/uaXAAABARAAAQdlbmQBEP+NESIDrP7mlwAAAQEQAAE=",  # climate.capnp:TimeSeries.subrange$Params
    "ECRQBgb/MrcJfRTn3/cAERkBAAAFAQcAATEVUgEAAREhPwAB/2NsaW1hdGUuBGNhcG5wOlRpbWVTZXJpZXMuc3VicmFuZ2UkUmVzdWx0AXNRBAMEAAAEAQAAEQ1aAABRDAMBURgCAf90aW1lU2VyaQADZXMBEf/obW7+QJ92pwAAAQERAAE=",  # climate.capnp:TimeSeries.subrange$Results
    "EChQBgb/uJP26N5kw4wAERkBAAAFAQcAATEVUgEAAREhPwAB/2NsaW1hdGUuBGNhcG5wOlRpbWVTZXJpZXMuc3ViaGVhZGVyJFBhcmFtAXNRBAMEAAAEAQAAEQ1KAABRDAMBUSgCAf9lbGVtZW50cwAAAAEOAAFQAwEBD/9ktVrbtGBX4wAAAQEOAAE=",  # climate.capnp:TimeSeries.subheader$Params
    "ECRQBgb/34DoymOBI8MAERkBAAAFAQcAATEVWgEAAREhPwAB/2NsaW1hdGUuBGNhcG5wOlRpbWVTZXJpZXMuc3ViaGVhZGVyJFJlc3VsA3RzUQQDBAAABAEAABENWgAAUQwDAVEYAgH/dGltZVNlcmkAA2VzARH/6G1u/kCfdqcAAAEBEQAB",  # climate.capnp:TimeSeries.subheader$Results
    "EBNQBgb/NGaVXCLELM4AERkBAAAEBwABMRVKAQAE/2NsaW1hdGUuBGNhcG5wOlRpbWVTZXJpZXMubWV0YWRhdGEkUGFyYW1zAAA=",  # climate.capnp:TimeSeries.metadata$Params
    "EBNQBgb/E6MPG7CeMssAERkBAAAEBwABMRVKAQAE/2NsaW1hdGUuBGNhcG5wOlRpbWVTZXJpZXMubG9jYXRpb24kUGFyYW1zAAA=",  # climate.capnp:TimeSeries.location$Params
    "EBJQBgb/FUjobpBGw7QAERYBAAAEBwABMRUyAQAE/2NsaW1hdGUuA2NhcG5wOkRhdGFzZXQubWV0YWRhdGEkUB9hcmFtcw==",  # climate.capnp:Dataset.metadata$Params
    "ECRQBgb/E0pPKD1vSbAAERYBAAAFAQcAATEVigEAARElPwAB/2NsaW1hdGUuBWNhcG5wOkRhdGFzZXQuY2xvc2VzdFRpbWVTZXJpZXNBdCRQYXJhbXMAAFEEAwQAAAQBAAARDToAAFEIAwFRFAIBP2xhdGxvbgEQ//uPzDkw/PHsAAABARAAAQ==",  # climate.capnp:Dataset.closestTimeSeriesAt$Params
    "ECVQBgb/HmqvA6pf7u0AERYBAAAFAQcAATEVkgEAARElPwAB/2NsaW1hdGUuBWNhcG5wOkRhdGFzZXQuY2xvc2VzdFRpbWVTZXJpZXNBdCRSZXN1bHQBc1EEAwQAAAQBAAARDVoAAFEMAwFRGAIB/3RpbWVTZXJpAANlcwER/+htbv5An3anAAABAREAAQ==",  # climate.capnp:Dataset.closestTimeSeriesAt$Results
    "ECRQBgb/f12horBn+NkAERYBAAAFAQcAATEVUgEAAREhPwAB/2NsaW1hdGUuBGNhcG5wOkRhdGFzZXQudGltZVNlcmllc0F0JFBhcmFtAXNRBAMEAAAEAQAAEQ1aAABRDAMBURgCAf9sb2NhdGlvbgADSWQBDAACAQwAAQ==",  # climate.capnp:Dataset.timeSeriesAt$Params
    "ECRQBgb/XHPCW25GDOMAERYBAAAFAQcAATEVWgEAAREhPwAB/2NsaW1hdGUuBGNhcG5wOkRhdGFzZXQudGltZVNlcmllc0F0JFJlc3VsA3RzUQQDBAAABAEAABENWgAAUQwDAVEYAgH/dGltZVNlcmkAA2VzARH/6G1u/kCfdqcAAAEBEQAB",  # climate.capnp:Dataset.timeSeriesAt$Results
    "EBJQBgb/utQobIUuoNIAERYBAAAEBwABMRU6AQAE/2NsaW1hdGUuA2NhcG5wOkRhdGFzZXQubG9jYXRpb25zJD9QYXJhbXM=",  # climate.capnp:Dataset.locations$Params
    "ECdQBgb/3V8dQNz8jKoAERYBAAAFAQcAATEVQgEAAREdPwAB/2NsaW1hdGUuBGNhcG5wOkRhdGFzZXQubG9jYXRpb25zJFJlc3VsdHMAUQQDBAAABAEAABENUgAAUQwDAVEoAgH/bG9jYXRpb24AAXMBDgABUAMBARD/Gf4T84VzuoUAAAEBDgAB",  # climate.capnp:Dataset.locations$Results
    "ECVQBgb/BkW2MfTwo/wAERYBAAAFAQcAATEVagEAAREhPwAB/2NsaW1hdGUuBGNhcG5wOkRhdGFzZXQuc3RyZWFtTG9jYXRpb25zJFBhD3JhbXNRBAMEAAAEAQAAEQ2qAABREAMBURwCAf9zdGFydEFmdAFlckxvY2F0aQ9vbklkAQwAAgEMAAE=",  # climate.capnp:Dataset.streamLocations$Params
    "ECVQBgb/Bvp5i1fbup4AERYBAAAFAQcAATEVcgEAAREhPwAB/2NsaW1hdGUuBGNhcG5wOkRhdGFzZXQuc3RyZWFtTG9jYXRpb25zJFJlH3N1bHRzUQQDBAAABAEAABENkgAAURADAVEcAgH/bG9jYXRpb24Bc0NhbGxiYWMBawER/3XhT/FDoBvWAAABAREAAQ==",  # climate.capnp:Dataset.streamLocations$Results
    "EDFQBgb/oOUiX+x/ptcAEQ4B/xhF6xDkOh2gAAUCBwAAM9wUHBURFdoRIQcAABEddwAB/2NsaW1hdGUuAmNhcG5wOk1ldGFQbHVzRGEDdGFQAQFRCAMEAAAEAQAAESkqAABRJAMBUTACAREBARQBAQAAES0qAABRKAMBUTQCAQ9tZXRhARD/sG1VZunSNvsAAAEBEAABD2RhdGEBEf/wYFnw0f019gAAAQERAAE=",  # climate.capnp:MetaPlusData
    "EHxQBgb/T5bGm/XMwfEAUQ4BAf8YResQ5DodoAAFBAcAADO2IqkkERXqESEHAAAxHVcBAAH/Y2xpbWF0ZS4CY2FwbnA6VGltZVNlcmllcw9EYXRhUAEBURgDBAAABAEAABGZKgAAUZQDAVHAAgEBARQBAQAAEb1qAABRvAMBUcgCARECARQBAgAAEcU6AABRwAMBUdwCAREDAhQBAwAAEdlSAABR2AMBUeQCAREEAxQBBAAAEeFCAABR3AMBUegCAREFARQBBQEBEeVaAABR5AMBUfACAQ9kYXRhAQ4AAVADAQEOAAFQAwEBCgACAQ4AAf9pc1RyYW5zcAAPb3NlZAEBAAIBAQABP2hlYWRlcgEOAAFQAwEBD/9ktVrbtGBX4wAAAQEOAAH/c3RhcnREYXQAAWUBEP+NESIDrP7mlwAAAQEQAAF/ZW5kRGF0ZQEQ/40RIgOs/uaXAAABARAAAf9yZXNvbHV0aQADb24BD//CA+xjz8pmtAAAAQEPAAE=",  # climate.capnp:TimeSeriesData
    "EC5QBgb/XwwrNdQIff4AEQ4D/xhF6xDkOh2gAAABM6skfCYRFbIRHQcAABEZhxF1JwAA/2NsaW1hdGUuAWNhcG5wOlNlH3J2aWNlUAEBUQgDBQAA/1HUBZRIykyAAejGNZSFgGiRETGqAAIRLQcBAf/b5qPdgx99nQGw6rB0kfeVzREhegACERkH/2dldEF2YWlsAWFibGVEYXRhD3NldHNAAf9nZXREYXRhcwA/ZXRzRm9yQAFRCAEB/9VInFnL0a+yAAAA/2XLNtyg2qfBAAAA",  # climate.capnp:Service
    "EBRQBgb/UdQFlEjKTIAAERYBAAAEBwABMRWSAQAE/2NsaW1hdGUuBWNhcG5wOlNlcnZpY2UuZ2V0QXZhaWxhYmxlRGF0YXNldHMkUGFyYW0Bcw==",  # climate.capnp:Service.getAvailableDatasets$Params
    "EClQBgb/6MY1lIWAaJEAERYBAAAFAQcAATEVmgEAARElPwAB/2NsaW1hdGUuBWNhcG5wOlNlcnZpY2UuZ2V0QXZhaWxhYmxlRGF0YXNldHMkUmVzdWwDdHNRBAMEAAAEAQAAEQ1KAABRDAMBUSgCAf9kYXRhc2V0cwAAAAEOAAFQAwEBEP+g5SJf7H+m1wAAAQEOAAE=",  # climate.capnp:Service.getAvailableDatasets$Results
    "ECRQBgb/2+aj3YMffZ0AERYBAAAFAQcAATEVYgEAAREhPwAB/2NsaW1hdGUuBGNhcG5wOlNlcnZpY2UuZ2V0RGF0YXNldHNGb3IkUGFyB2Ftc1EEAwQAAAQBAAARDUoAAFEMAwFRGAIB/3RlbXBsYXRlAAAAARD/sG1VZunSNvsAAAEBEAAB",  # climate.capnp:Service.getDatasetsFor$Params
    "EChQBgb/sOqwdJH3lc0AERYBAAAFAQcAATEVagEAAREhPwAB/2NsaW1hdGUuBGNhcG5wOlNlcnZpY2UuZ2V0RGF0YXNldHNGb3IkUmVzD3VsdHNRBAMEAAAEAQAAEQ1KAABRDAMBUSgCAf9kYXRhc2V0cwAAAAEOAAFQAwEBEf/wYFnw0f019gAAAQEOAAE=",  # climate.capnp:Service.getDatasetsFor$Results
    "ECVQBgb/2SmZxWzCGKQAEQ4D/xhF6xDkOh2gAAABM34mgikxFRoBESUXAAARMUcRWRcAAP9jbGltYXRlLgNjYXBucDpDU1ZUaW1lU2VyaWVzRmFjdG8DcnlRBAEB/7iQZvSpHKjrABEBUv9DU1ZDb25maQABZ1EEAwUAAP9HBXUBJo2qzwE0Va7I66/v7xEROgACEQUHP2NyZWF0ZUABUQQBAf/VSJxZy9GvsgAAAA==",  # climate.capnp:CSVTimeSeriesFactory
    "EG5QBgb/uJBm9KkcqOsAUSMBAf/ZKZnFbMIYpAAFAgcAADPsJu4oMRVqAREpBwAAESXnAAH/Y2xpbWF0ZS4EY2FwbnA6Q1NWVGltZVNlcmllc0ZhY3RvcnkuQ1NWQ28PbmZpZ1ABAVEQAwQAAAQBAQERYSIAAFFcAwFRaAIBEQEBFAEBAAARaVIAAFFoAwFRzAIBAQIUAQIBARHJkgAAUcwDAVHYAgERAwEUAQMBARHV0gAAUdwDAVHoAgEHc2VwAQwAAgEMAAARARIBLP9oZWFkZXJNYQABcAEOAAFQAwEBEP8zRxclR4bUuQAAAEABEQEfUQQCAf8zRxclR4bUuQAAABEBJ1EIAQEBAVEIAwEBAVEQAwEBDAACAQwAAgEOAAH/c2tpcExpbmUBc1RvSGVhZGUBcgEDAAIBAwAB/3NraXBMaW5lAnNGcm9tSGVhZGVyVG9EYXQBYQEDAAIFAwEAAQ==",  # climate.capnp:CSVTimeSeriesFactory.CSVConfig
    "EDNQBgb/RwV1ASaNqs8AESMBAAAFAgcAATEVigEAAREldwAB/2NsaW1hdGUuBWNhcG5wOkNTVlRpbWVTZXJpZXNGYWN0b3J5LmNyZWF0ZSRQYXJhbXMAAFEIAwQAAAQBAAARKUIAAFEkAwFRMAIBEQEBFAEBAAARLToAAFEoAwFRNAIBf2NzdkRhdGEBDAACAQwAAT9jb25maWcBEP+4kGb0qRyo6wAAAQEQAAE=",  # climate.capnp:CSVTimeSeriesFactory.create$Params
    "EDRQBgb/NFWuyOuv7+8AESMBAAAFAgcAATEVkgEAAREldwAB/2NsaW1hdGUuBWNhcG5wOkNTVlRpbWVTZXJpZXNGYWN0b3J5LmNyZWF0ZSRSZXN1bHQBc1EIAwQAAAQBAAARKVoAAFEoAwFRNAIBEQEBFAEBAAARMTIAAFEsAwFROAIB/3RpbWVzZXJpAANlcwER/+htbv5An3anAAABAREAAR9lcnJvcgEMAAIBDAAB",  # climate.capnp:CSVTimeSeriesFactory.create$Results
    "EFZQBgb/soSXl++A9OEAEQ4D/xhF6xDkOh2gAAABM4QpDi0xFSoBESUnAAAxPUcBEx0BFwAA/2NsaW1hdGUuA2NhcG5wOkFsdGVyVGltZVNlcmllc1dyYQ9wcGVyUQgBAf/FvpDzurmF0AARCUL/yljDB1F43bUAEQVSf0FsdGVyZWT/QWx0ZXJUeXAAAWVRFAMFAAD/qTb72e4mH+MBqveQj7XdLvsRkZIAAhGNBwEB/56GQdoMIqDLAWYXcby1dVvdEYGCAAIReQcBAv/k5ikpnB5r0wEchL6AYuyhxBFtMgACEWEHAQP/U/9FTf78e9sBOwATMLKASfQRVToAAhFJBwEE/2hQfr0tFgiPAbuUzYJ+eAqLET3KAAIRPQf/d3JhcHBlZFQBaW1lU2VyaWUBc0AB/2FsdGVyZWRFAWxlbWVudHMAQAEfYWx0ZXJAAT9yZW1vdmVAAf9yZXBsYWNlVwJyYXBwZWRUaW1lU2VyaWVzAABAAVEEAQH/6G1u/kCfdqcAAAA=",  # climate.capnp:AlterTimeSeriesWrapper
    "EEJQBgb/xb6Q87q5hdAAUSUBAf+yhJeX74D04QAEBwAAM4Iq3ioxFWoBESkHAAARJa8AAf9jbGltYXRlLgRjYXBucDpBbHRlclRpbWVTZXJpZXNXcmFwcGVyLkFsdA9lcmVkUAEBUQwDBAAABAEAABFFQgAAUUADAVFMAgERAQEUAQEAABFJMgAAUUQDAVFQAgERAgEUAQIAABFNKgAAUUgDAVFUAgF/ZWxlbWVudAEP/2S1Wtu0YFfjAAABAQ8AAR92YWx1ZQEKAAIBCgABD3R5cGUBD//KWMMHUXjdtQAAAQEPAAE=",  # climate.capnp:AlterTimeSeriesWrapper.Altered
    "EB1QBgb/yljDB1F43bUAESUC/7KEl5fvgPThAAABM0MrbysxFXoBESkHAAARJTcAAf9jbGltYXRlLgRjYXBucDpBbHRlclRpbWVTZXJpZXNXcmFwcGVyLkFsdD9lclR5cGVQAQFRCAECAAARESIAAAEBEQkiAAAHYWRkB211bA==",  # climate.capnp:AlterTimeSeriesWrapper.AlterType
    "EBVQBgb/qTb72e4mH+MAESUBAAAEBwABMRXyAQAE/2NsaW1hdGUuBmNhcG5wOkFsdGVyVGltZVNlcmllc1dyYXBwZXIud3JhcHBlZFRpbWVTZXJpZXMkUB9hcmFtcw==",  # climate.capnp:AlterTimeSeriesWrapper.wrappedTimeSeries$Params
    "ECZQBgb/qveQj7XdLvsAESUBAAAFAQcAATEV+gEAAREpPwAB/2NsaW1hdGUuBmNhcG5wOkFsdGVyVGltZVNlcmllc1dyYXBwZXIud3JhcHBlZFRpbWVTZXJpZXMkUj9lc3VsdHNRBAMEAAAEAQAAEQ1aAABRDAMBURgCAf90aW1lU2VyaQADZXMBEf/obW7+QJ92pwAAAQERAAE=",  # climate.capnp:AlterTimeSeriesWrapper.wrappedTimeSeries$Results
    "EBVQBgb/noZB2gwioMsAESUBAAAEBwABMRXiAQAE/2NsaW1hdGUuBmNhcG5wOkFsdGVyVGltZVNlcmllc1dyYXBwZXIuYWx0ZXJlZEVsZW1lbnRzJFBhcgdhbXM=",  # climate.capnp:AlterTimeSeriesWrapper.alteredElements$Params
    "EClQBgb/ZhdxvLV1W90AESUBAAAFAQcAATEV6gEAAREpPwAB/2NsaW1hdGUuBmNhcG5wOkFsdGVyVGltZVNlcmllc1dyYXBwZXIuYWx0ZXJlZEVsZW1lbnRzJFJlcw91bHRzUQQDBAAABAEAABENKgAAUQgDAVEkAgEPbGlzdAEOAAFQAwEBEP/FvpDzurmF0AAAAQEOAAE=",  # climate.capnp:AlterTimeSeriesWrapper.alteredElements$Results
    "EDRQBgb/5OYpKZwea9MAUSUBAQAABQEHAAExFZIBAAERJXcAAf9jbGltYXRlLgVjYXBucDpBbHRlclRpbWVTZXJpZXNXcmFwcGVyLmFsdGVyJFBhcmFtAXNRCAMEAAAEAQAAESkqAABRJAMBUTACAQEBFAEBAQERLYIAAFEsAwFROAIBD2Rlc2MBEP/FvpDzurmF0AAAAQEQAAH/YXNOZXdUaW0BZVNlcmllcwABAQACAQEAAQ==",  # climate.capnp:AlterTimeSeriesWrapper.alter$Params
    "ECVQBgb/HIS+gGLsocQAESUBAAAFAQcAATEVmgEAARElPwAB/2NsaW1hdGUuBWNhcG5wOkFsdGVyVGltZVNlcmllc1dyYXBwZXIuYWx0ZXIkUmVzdWwDdHNRBAMEAAAEAQAAEQ1aAABRDAMBURgCAf90aW1lU2VyaQADZXMBEf/obW7+QJ92pwAAAQERAAE=",  # climate.capnp:AlterTimeSeriesWrapper.alter$Results
    "ECVQBgb/U/9FTf78e9sAUSUBAQAABAcAATEVmgEAARElPwAB/2NsaW1hdGUuBWNhcG5wOkFsdGVyVGltZVNlcmllc1dyYXBwZXIucmVtb3ZlJFBhcmEDbXNRBAMEAAAEAQAAEQ16AABRDAMBURgCAf9hbHRlcmVkRQA/bGVtZW50AQ//ZLVa27RgV+MAAAEBDwAB",  # climate.capnp:AlterTimeSeriesWrapper.remove$Params
    "EBRQBgb9OxMwsoBJ9BElAQAABAcAATEVogEABP9jbGltYXRlLgVjYXBucDpBbHRlclRpbWVTZXJpZXNXcmFwcGVyLnJlbW92ZSRSZXN1B2x0cw==",  # climate.capnp:AlterTimeSeriesWrapper.remove$Results
    "ECdQBgb/aFB+vS0WCI8AESUBAAAFAQcAATEVKgIAAREtPwAB/2NsaW1hdGUuB2NhcG5wOkFsdGVyVGltZVNlcmllc1dyYXBwZXIucmVwbGFjZVdyYXBwZWRUaW1lU2VyaWVzJFBhD3JhbXNRBAMEAAAEAQAAEQ1aAABRDAMBURgCAf90aW1lU2VyaQADZXMBEf/obW7+QJ92pwAAAQERAAE=",  # climate.capnp:AlterTimeSeriesWrapper.replaceWrappedTimeSeries$Params
    "EBZQBgb/u5TNgn54CosAESUBAAAEBwABMRUyAgAE/2NsaW1hdGUuB2NhcG5wOkFsdGVyVGltZVNlcmllc1dyYXBwZXIucmVwbGFjZVdyYXBwZWRUaW1lU2VyaWVzJFJlH3N1bHRz",  # climate.capnp:AlterTimeSeriesWrapper.replaceWrappedTimeSeries$Results
    "ECJQBgb/RCelovAt8cUAEQ4D/xhF6xDkOh2gAAABMxAtLS4xFWIBESkHAAARJUcRTRcAAP9jbGltYXRlLgRjYXBucDpBbHRlclRpbWVTZXJpZXNXcmFwcGVyRmFjdAdvcnlQAQFRBAMFAAD//osB3AZIBpUBEV3Nm6yCibQRESoAAhEFBw93cmFwQAFRBAEB/9VInFnL0a+yAAAA",  # climate.capnp:AlterTimeSeriesWrapperFactory
    "ECVQBgb//osB3AZIBpUAESwBAAAFAQcAATEVwgEAARElPwAB/2NsaW1hdGUuBmNhcG5wOkFsdGVyVGltZVNlcmllc1dyYXBwZXJGYWN0b3J5LndyYXAkUGFyYW1zAFEEAwQAAAQBAAARDVoAAFEMAwFRGAIB/3RpbWVTZXJpAANlcwER/+htbv5An3anAAABAREAAQ==",  # climate.capnp:AlterTimeSeriesWrapperFactory.wrap$Params
    "ECVQBgb/EV3Nm6yCibQAESwBAAAFAQcAATEVygEAAREpPwAB/2NsaW1hdGUuBmNhcG5wOkFsdGVyVGltZVNlcmllc1dyYXBwZXJGYWN0b3J5LndyYXAkUmVzdWx0cwAAUQQDBAAABAEAABENQgAAUQgDAVEUAgF/d3JhcHBlcgER/7KEl5fvgPThAAABAREAAQ==",  # climate.capnp:AlterTimeSeriesWrapperFactory.wrap$Results
]

# Load schemas and build module structure
_loader = capnp.SchemaLoader()
for _schema_b64 in _SCHEMA_NODES:
    _schema_data = base64.b64decode(_schema_b64)
    _node_reader = schema_capnp.Node.from_bytes_packed(_schema_data)
    _loader.load_dynamic(_node_reader)

# Build module structure inline
GCM = _EnumModule(_loader.get(0xCE396869EEDE9F10).as_enum(), "GCM")
RCM = _EnumModule(_loader.get(0x8671DEC53083E351).as_enum(), "RCM")
SSP = _EnumModule(_loader.get(0xD3780AE416347AEE).as_enum(), "SSP")
RCP = _EnumModule(_loader.get(0x8EF30778310C94CC).as_enum(), "RCP")
EnsembleMember = _StructModule(
    _loader.get(0xC8CAACD1CD5DA434).as_struct(),
    "EnsembleMember",
)
Metadata = _StructModule(_loader.get(0xFB36D2E966556DB0).as_struct(), "Metadata")
Metadata.Supported = _InterfaceModule(
    _loader.get(0xAB06444B30722E01).as_interface(),
    "Supported",
)
Metadata.Value = _StructModule(_loader.get(0xC48E24C968A234DB).as_struct(), "Value")
Metadata.Entry = _StructModule(_loader.get(0x85AF7FEA06D0820C).as_struct(), "Entry")
Metadata.Information = _InterfaceModule(
    _loader.get(0xC781EDEAB8160CB7).as_interface(),
    "Information",
)
Dataset = _InterfaceModule(_loader.get(0xF635FDD1F05960F0).as_interface(), "Dataset")
Dataset.GetLocationsCallback = _InterfaceModule(
    _loader.get(0xD61BA043F14FE175).as_interface(),
    "GetLocationsCallback",
)
MetaPlusData = _StructModule(
    _loader.get(0xD7A67FEC5F22E5A0).as_struct(),
    "MetaPlusData",
)
Element = _EnumModule(_loader.get(0xE35760B4DB5AB564).as_enum(), "Element")
Location = _StructModule(_loader.get(0x85BA7385F313FE19).as_struct(), "Location")
Location.KV = _StructModule(_loader.get(0xC5FD13A53AE6D46A).as_struct(), "KV")
TimeSeries = _InterfaceModule(
    _loader.get(0xA7769F40FE6E6DE8).as_interface(),
    "TimeSeries",
)
TimeSeries.Resolution = _EnumModule(
    _loader.get(0xB466CACF63EC03C2).as_enum(),
    "Resolution",
)
TimeSeriesData = _StructModule(
    _loader.get(0xF1C1CCF59BC6964F).as_struct(),
    "TimeSeriesData",
)
Service = _InterfaceModule(_loader.get(0xFE7D08D4352B0C5F).as_interface(), "Service")
CSVTimeSeriesFactory = _InterfaceModule(
    _loader.get(0xA418C26CC59929D9).as_interface(),
    "CSVTimeSeriesFactory",
)
CSVTimeSeriesFactory.CSVConfig = _StructModule(
    _loader.get(0xEBA81CA9F46690B8).as_struct(),
    "CSVConfig",
)
AlterTimeSeriesWrapper = _InterfaceModule(
    _loader.get(0xE1F480EF979784B2).as_interface(),
    "AlterTimeSeriesWrapper",
)
AlterTimeSeriesWrapper.Altered = _StructModule(
    _loader.get(0xD085B9BAF390BEC5).as_struct(),
    "Altered",
)
AlterTimeSeriesWrapper.AlterType = _EnumModule(
    _loader.get(0xB5DD785107C358CA).as_enum(),
    "AlterType",
)
AlterTimeSeriesWrapperFactory = _InterfaceModule(
    _loader.get(0xC5F12DF0A2A52744).as_interface(),
    "AlterTimeSeriesWrapperFactory",
)

AlterTimeSeriesWrapperFactory.Server.WrapResultTuple = NamedTuple(
    "WrapResultTuple",
    [("wrapper", object)],
)
AlterTimeSeriesWrapper.Server.AlterResultTuple = NamedTuple(
    "AlterResultTuple",
    [("timeSeries", object)],
)
AlterTimeSeriesWrapper.Server.AlteredelementsResultTuple = NamedTuple(
    "AlteredelementsResultTuple",
    [("list", object)],
)
AlterTimeSeriesWrapper.Server.WrappedtimeseriesResultTuple = NamedTuple(
    "WrappedtimeseriesResultTuple",
    [("timeSeries", object)],
)
CSVTimeSeriesFactory.Server.CreateResultTuple = NamedTuple(
    "CreateResultTuple",
    [("timeseries", object), ("error", object)],
)
Dataset.Server.ClosesttimeseriesatResultTuple = NamedTuple(
    "ClosesttimeseriesatResultTuple",
    [("timeSeries", object)],
)
Dataset.Server.LocationsResultTuple = NamedTuple(
    "LocationsResultTuple",
    [("locations", object)],
)
Dataset.Server.MetadataResultTuple = NamedTuple(
    "MetadataResultTuple",
    [("entries", object), ("info", object)],
)
Dataset.Server.StreamlocationsResultTuple = NamedTuple(
    "StreamlocationsResultTuple",
    [("locationsCallback", object)],
)
Dataset.Server.TimeseriesatResultTuple = NamedTuple(
    "TimeseriesatResultTuple",
    [("timeSeries", object)],
)
Dataset.GetLocationsCallback.Server.NextlocationsResultTuple = NamedTuple(
    "NextlocationsResultTuple",
    [("locations", object)],
)
Metadata.Information.Server.ForallResultTuple = NamedTuple(
    "ForallResultTuple",
    [("all", object)],
)
Metadata.Information.Server.ForoneResultTuple = NamedTuple(
    "ForoneResultTuple",
    [("id", object), ("name", object), ("description", object)],
)
Metadata.Supported.Server.CategoriesResultTuple = NamedTuple(
    "CategoriesResultTuple",
    [("types", object)],
)
Metadata.Supported.Server.SupportedvaluesResultTuple = NamedTuple(
    "SupportedvaluesResultTuple",
    [("values", object)],
)
Service.Server.GetavailabledatasetsResultTuple = NamedTuple(
    "GetavailabledatasetsResultTuple",
    [("datasets", object)],
)
Service.Server.GetdatasetsforResultTuple = NamedTuple(
    "GetdatasetsforResultTuple",
    [("datasets", object)],
)
TimeSeries.Server.DataResultTuple = NamedTuple("DataResultTuple", [("data", object)])
TimeSeries.Server.DatatResultTuple = NamedTuple("DatatResultTuple", [("data", object)])
TimeSeries.Server.HeaderResultTuple = NamedTuple(
    "HeaderResultTuple",
    [("header", object)],
)
TimeSeries.Server.LocationResultTuple = NamedTuple(
    "LocationResultTuple",
    [
        ("id", object),
        ("heightNN", object),
        ("latlon", object),
        ("timeSeries", object),
        ("customData", object),
    ],
)
TimeSeries.Server.MetadataResultTuple = NamedTuple(
    "MetadataResultTuple",
    [("entries", object), ("info", object)],
)
TimeSeries.Server.RangeResultTuple = NamedTuple(
    "RangeResultTuple",
    [("startDate", object), ("endDate", object)],
)
TimeSeries.Server.ResolutionResultTuple = NamedTuple(
    "ResolutionResultTuple",
    [("resolution", object)],
)
TimeSeries.Server.SubheaderResultTuple = NamedTuple(
    "SubheaderResultTuple",
    [("timeSeries", object)],
)
TimeSeries.Server.SubrangeResultTuple = NamedTuple(
    "SubrangeResultTuple",
    [("timeSeries", object)],
)
