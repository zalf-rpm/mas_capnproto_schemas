# pyright: reportAttributeAccessIssue=false, reportArgumentType=false, reportUnknownMemberType=false
"""This is an automatically generated stub for `common.capnp`."""

from __future__ import annotations

import base64

import capnp
import schema_capnp
from capnp.lib.capnp import _EnumModule, _InterfaceModule, _StructModule

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EGRQBgb/yYqodafJ8ZkAAQ4AAxEVohEdtxG9ZwAC/2NvbW1vbi9jAW9tbW9uLmNhB3BucFEsAQH/09oD/st+y9QAEVFy/9VInFnL0a+yABFRav9U1Mpniwls7QARUXr/C4bNJsi+sqIAEVFS/xejF/UuDhjHABFRKv9GsnNTM5J14QARTTL/2W5YjAv1aagAEUlC/2h7osa15XGXABFFUv8zRxclR4bUuQARRSr/xWoLu8xFMMgAEUE6//ZWXTB8PVTuABE9mv9JZEluZm9ybQAfYXRpb27/SWRlbnRpZmkAD2FibGX/U3RydWN0dXIAP2VkVGV4dP9NaW1lVHlwZQABcw9CbG9iH1ZhbHVlf0ZhY3Rvcnn/SU9GYWN0b3IAAXkPUGFpcj9Ib2xkZXL/SWRlbnRpZmkBYWJsZUhvbGQDZXJREAEC/yxfgL+e+ca5AFEoAgFBPAH/bPmw4/6jXowAUTgCAUFMAf/gK3kjEH+pvgBRSAIBQVQB/7VEDiYBtjDhAFFQAgFBdAEBDAAAEQGi/21hczo6c2NoAWVtYTo6Y29tB21vbgAAAQwAABEBkv9tYXMuc2NoZQFtYS5jb21tbwFuAAABDAAAEQE6P2NvbW1vbgAAAQwAADEBwgH/Z2l0aHViLmMGb20vemFsZi1ycG0vbWFzX2NhcG5wcm90b19zY2hlbWFzL2dlbi9nby9jb21tb24AAAA=",  # common/common.capnp
    "EEJQBgb/09oD/st+y9QAERQB/8mKqHWnyfGZAAUDBwAAMzwBnwExFRIBESUHAAARIa8AAf9jb21tb24vYwNvbW1vbi5jYXBucDpJZEluZm9ybWF0aW8BblABAVEMAwQAAAQBAAARRRoAAFFAAwFRTAIBEQEBFAEBAAARSSoAAFFEAwFRUAIBEQICFAECAAARTWIAAFFMAwFRWAIBA2lkAQwAAgEMAAEPbmFtZQEMAAIBDAAB/2Rlc2NyaXB0AAdpb24BDAACAQwAAQ==",  # common/common.capnp:IdInformation
    "EB9QBgb/1UicWcvRr7IAERQD/8mKqHWnyfGZAAABM6EBEgIxFQoBESUHAAARIUcRSQcAAP9jb21tb24vYwNvbW1vbi5jYXBucDpJZGVudGlmaWFibGUAAFABAVEEAwUAAP+x3kkez6GKnQHT2gP+y37L1BERKgACEQUHD2luZm9AAVABAQ==",  # common/common.capnp:Identifiable
    "EBNQBgb/sd5JHs+hip0AESEBAAAEBwABMRVqAQAE/2NvbW1vbi9jBG9tbW9uLmNhcG5wOklkZW50aWZpYWJsZS5pbmZvJFBhD3JhbXM=",  # common/common.capnp:Identifiable.info$Params
    "EDVQBgb/VNTKZ4sJbO0AURQBAf/Jiqh1p8nxmQAFAQcAADMUAkUDMRUaARElFwAAES13AAH/Y29tbW9uL2MDb21tb24uY2FwbnA6U3RydWN0dXJlZFRlA3h0UQQBAf9Pl7UXPsTrngARASoPVHlwZVEIAwQAAAQBAAARKTIAAFEkAwFRMAIBAQEUAQEBAREtKgAAUSgDAVE0AgEfdmFsdWUBDAACAQwAAQ90eXBlAQ//T5e1Fz7E654AAAEBDwAB",  # common/common.capnp:StructuredText
    "EC5QBgb/T5e1Fz7E654AESMC/1TUymeLCWztAAABM4QCIwMxFUIBESUHAAARIZcAAf9jb21tb24vYwRvbW1vbi5jYXBucDpTdHJ1Y3R1cmVkVGV4dC5UeXBlAFABAVEYAQIAABFBagAAAQERPSoAAAECETUiAAABAxEtKgAAAQQRJVIAAAEFESEiAAD/dW5zdHJ1Y3QAD3VyZWQPanNvbgd4bWwPdG9tbP9zdHVyZHlSZQABZgdjc3Y=",  # common/common.capnp:StructuredText.Type
    "EMZQBgb/C4bNJsi+sqIAERQB/8mKqHWnyfGZAAQHAAAzRwOPCxEV8jEhtwIAA/9jb21tb24vYwJvbW1vbi5jYXBucDpNaW1lH1R5cGVzUawBAf8Cgkln9WP7oQATUQFS/xUMof83ob7qABNRAUr/fF+GEvpdXMMAE1EBQv8kxa/qXoM82wATTQFC/139DzFh9nC3ABNJAXr/uJUzYhNEjfUAE0kBav8Kw9suBYQPmwATSQFC/y1s4jfQ4CenABNFAYL/MPI29XpLkIkAE0UBev/4Mp90uHsG4gATRQF6/8e4ZXfHFaW9ABNFAXr/ddK0HlG67PsAE0UBgv9dBHEGmm01tgATRQG6/6qxfsKy8v+kABNJAbL/7nHiFqvTlfkAE00B6v+17J5ugCJ05gATVQGS/1Uk6JnrpsyVABNZAeL/565Sfl99TZUAE2EBSv8qUn/KtTq7owATYQFS/zFOq9lu6jfkABNhAUr/g7Zt90fWRpQAE2EBUv/kspJ9V/MZ/QATYQFi/2uULc2gRoOHABNhAUr/HsA5tmwIaaoAE2EBUv9pxvWen98VgQATYQFa//xizqHxpGy1ABNhAeL//WCWbYzRb4UAM2kBUgH/5EqoQ64rWLkAE3kBUv+hv94qKo8mowATeQFK/9mPJz1y6vbfABN5AUr/EopS54F09oMAE3kBSv/FYIKLXdu3/wATeQFS/1UNJ8SpvdeTABN5AUr/Qvr9/HOHEokAE3kBSv+GagcI6QJW1AATeQFS/9hSyJHhvdbFABN5AUr/qarXFRtNA+kAE3kBUv8QWahGq6IrzgATeQF6/53uMA3aaTrUABN5AXL/HApbXP2Xn8oAE3kBQv/p63tSjpAZ/QATdQFC/xCH771auQ+kABNxAUr/3hRnsQubmvYAE3EBUv90ZXh0UGxhaQABbv90ZXh0SHRtbAAAAH90ZXh0Q3Nzf3RleHRDc3b/dGV4dEphdmEAP3NjcmlwdP90ZXh0TWFyawAPZG93bn90ZXh0WG1s/2FwcGxpY2F0Amlvbkpzb24AYXBwbGljYXQ/aW9uWG1s/2FwcGxpY2F0AD9pb25QZGb/YXBwbGljYXQAP2lvblppcP9hcHBsaWNhdANpb25HemlwAGFwcGxpY2F0aW9uT2N0ZXQ/U3RyZWFt/2FwcGxpY2F0AWlvbkphdmFzH2NyaXB0/2FwcGxpY2F0Amlvbld3d0Zvcm1VcmxlbmMPb2RlZP9tdWx0aXBhcgF0Rm9ybURhdAFh/2FwcGxpY2F0AmlvblZuZEFwYWNoZVBhcnEHdWV0/2ltYWdlUG5nAAAA/2ltYWdlSnBlAAFn/2ltYWdlR2lmAAAA/2ltYWdlV2ViAAFw/2ltYWdlU3ZnAAdYbWz/aW1hZ2VCbXAAAAD/aW1hZ2VUaWYAAWb/aW1hZ2VYSWMAA29u/2ltYWdlVGlmAmZBcHBsaWNhdGlvbkdlb3QHaWZm/2ltYWdlVGlmBGZBcHBsaWNhdGlvbkdlb3RpZmZDbG91ZE9wdGltaXplAWT/YXVkaW9NcGUAAWf/YXVkaW9NcDQAAAD/YXVkaW9PZ2cAAAD/YXVkaW9XYXYAAAD/YXVkaW9XZWIAAW3/YXVkaW9BYWMAAAD/dmlkZW9NcDQAAAD/dmlkZW9NcGUAAWf/dmlkZW9PZ2cAAAD/dmlkZW9XZWIAAW3/dmlkZW9RdWkAP2NrdGltZf92aWRlb1hNcwAfVmlkZW9/Zm9udFR0Zn9mb250T3Rm/2ZvbnRXb2ZmAAAA/2ZvbnRXb2ZmAAEy",  # common/common.capnp:MimeTypes
    "EBxQBgb/AoJJZ/Vj+6EAER4E/wuGzSbIvrKiAAABM1wDgQMxFUIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy50ZXh0UGxhaW4AUAEBAQwAAgEMAAARAVr/dGV4dC9wbGEAA2lu",  # common/common.capnp:MimeTypes.textPlain
    "EBxQBgb/FQyh/zehvuoAER4E/wuGzSbIvrKiAAABM4QDpwMxFToBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy50ZT94dEh0bWxQAQEBDAACAQwAABEBUv90ZXh0L2h0bQABbA==",  # common/common.capnp:MimeTypes.textHtml
    "EBxQBgb/fF+GEvpdXMMAER4E/wuGzSbIvrKiAAABM6oDywMxFTIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy50ZR94dENzc1ABAQEMAAIBDAAAEQFK/3RleHQvY3NzAAAA",  # common/common.capnp:MimeTypes.textCss
    "EBxQBgb/JMWv6l6DPNsAER4E/wuGzSbIvrKiAAABM84D7wMxFTIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy50ZR94dENzdlABAQEMAAIBDAAAEQFK/3RleHQvY3N2AAAA",  # common/common.capnp:MimeTypes.textCsv
    "EB1QBgb/Xf0PMWH2cLcAER4E/wuGzSbIvrKiAAABM/IDIQQxFWoBESkHAABRJAMBUTACAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy50ZXh0SmF2YXNjD3JpcHRQAQEBDAACAQwAABEBgv90ZXh0L2phdgFhc2NyaXB0AA==",  # common/common.capnp:MimeTypes.textJavascript
    "EB1QBgb/uJUzYhNEjfUAER4E/wuGzSbIvrKiAAABMyQETwQxFVoBESkHAABRJAMBUTACAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy50ZXh0TWFya2RvA3duUAEBAQwAAgEMAAARAXL/dGV4dC9tYXIAH2tkb3du",  # common/common.capnp:MimeTypes.textMarkdown
    "EBxQBgb/CsPbLgWED5sAER4E/wuGzSbIvrKiAAABM1IEcwQxFTIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy50ZR94dFhtbFABAQEMAAIBDAAAEQFK/3RleHQveG1sAAAA",  # common/common.capnp:MimeTypes.textXml
    "EB5QBgb/LWziN9DgJ6cAER4E/wuGzSbIvrKiAAABM3cEqAQxFXIBESkHAABRJAMBUTACAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5hcHBsaWNhdGlvH25Kc29uUAEBAQwAAgEMAAARAYr/YXBwbGljYXQBaW9uL2pzb24AAA==",  # common/common.capnp:MimeTypes.applicationJson
    "EB1QBgb/MPI29XpLkIkAER4E/wuGzSbIvrKiAAABM6sE2gQxFWoBESkHAABRJAMBUTACAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5hcHBsaWNhdGlvD25YbWxQAQEBDAACAQwAABEBgv9hcHBsaWNhdAFpb24veG1sAA==",  # common/common.capnp:MimeTypes.applicationXml
    "EB1QBgb/+DKfdLh7BuIAER4E/wuGzSbIvrKiAAABM90EDAUxFWoBESkHAABRJAMBUTACAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5hcHBsaWNhdGlvD25QZGZQAQEBDAACAQwAABEBgv9hcHBsaWNhdAFpb24vcGRmAA==",  # common/common.capnp:MimeTypes.applicationPdf
    "EB1QBgb/x7hld8cVpb0AER4E/wuGzSbIvrKiAAABMw8FPgUxFWoBESkHAABRJAMBUTACAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5hcHBsaWNhdGlvD25aaXBQAQEBDAACAQwAABEBgv9hcHBsaWNhdAFpb24vemlwAA==",  # common/common.capnp:MimeTypes.applicationZip
    "EB5QBgb/ddK0HlG67PsAER4E/wuGzSbIvrKiAAABM0EFcgUxFXIBESkHAABRJAMBUTACAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5hcHBsaWNhdGlvH25HemlwUAEBAQwAAgEMAAARAYr/YXBwbGljYXQBaW9uL2d6aXAAAA==",  # common/common.capnp:MimeTypes.applicationGzip
    "ECBQBgb/XQRxBpptNbYAER4E/wuGzSbIvrKiAAABM3UFtQUxFaoBES0HAABRKAMBUTQCAQAA/2NvbW1vbi9jBW9tbW9uLmNhcG5wOk1pbWVUeXBlcy5hcHBsaWNhdGlvbk9jdGV0U3QPcmVhbVABAQEMAAIBDAAAEQHK/2FwcGxpY2F0Amlvbi9vY3RldC1zdHJlYW0AAA==",  # common/common.capnp:MimeTypes.applicationOctetStream
    "EB9QBgb/qrF+wrLy/6QAER4E/wuGzSbIvrKiAAABM7gF9QUxFaIBES0HAABRKAMBUTQCAQAA/2NvbW1vbi9jBW9tbW9uLmNhcG5wOk1pbWVUeXBlcy5hcHBsaWNhdGlvbkphdmFzY3IHaXB0UAEBAQwAAgEMAAARAbr/YXBwbGljYXQBaW9uL2phdmE/c2NyaXB0",  # common/common.capnp:MimeTypes.applicationJavascript
    "ECJQBgb/7nHiFqvTlfkAER4E/wuGzSbIvrKiAAABM/gFRwYxFdoBETEHAABRLAMBUTgCAQAA/2NvbW1vbi9jBm9tbW9uLmNhcG5wOk1pbWVUeXBlcy5hcHBsaWNhdGlvbld3d0Zvcm1VcmxlbmNvZANlZFABAQEMAAIBDAAAMQESAf9hcHBsaWNhdANpb24veC13d3ctZm9ybS11cmxlbmNvZGUBZA==",  # common/common.capnp:MimeTypes.applicationWwwFormUrlencoded
    "EB5QBgb/teyeboAidOYAER4E/wuGzSbIvrKiAAABM0oGgAYxFYIBESkHAABRJAMBUTACAQAA/2NvbW1vbi9jBW9tbW9uLmNhcG5wOk1pbWVUeXBlcy5tdWx0aXBhcnRGb3JtRGF0YQBQAQEBDAACAQwAABEBov9tdWx0aXBhcgF0L2Zvcm0tZAdhdGE=",  # common/common.capnp:MimeTypes.multipartFormData
    "ECFQBgb/VSTomeumzJUAER4E/wuGzSbIvrKiAAABM4QGzwYxFdIBETEHAABRLAMBUTgCAQAA/2NvbW1vbi9jBm9tbW9uLmNhcG5wOk1pbWVUeXBlcy5hcHBsaWNhdGlvblZuZEFwYWNoZVBhcnF1ZQF0UAEBAQwAAgEMAAARAfr/YXBwbGljYXQCaW9uL3ZuZC5hcGFjaGUucD9hcnF1ZXQ=",  # common/common.capnp:MimeTypes.applicationVndApacheParquet
    "EBxQBgb/565Sfl99TZUAER4E/wuGzSbIvrKiAAABM9MG9gYxFToBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy5pbT9hZ2VQbmdQAQEBDAACAQwAABEBUv9pbWFnZS9wbgABZw==",  # common/common.capnp:MimeTypes.imagePng
    "EBxQBgb/KlJ/yrU6u6MAER4E/wuGzSbIvrKiAAABM/kGHgcxFUIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5pbWFnZUpwZWcAUAEBAQwAAgEMAAARAVr/aW1hZ2UvanAAA2Vn",  # common/common.capnp:MimeTypes.imageJpeg
    "EBxQBgb/MU6r2W7qN+QAER4E/wuGzSbIvrKiAAABMyEHRAcxFToBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy5pbT9hZ2VHaWZQAQEBDAACAQwAABEBUv9pbWFnZS9naQABZg==",  # common/common.capnp:MimeTypes.imageGif
    "EBxQBgb/g7Zt90fWRpQAER4E/wuGzSbIvrKiAAABM0cHbAcxFUIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5pbWFnZVdlYnAAUAEBAQwAAgEMAAARAVr/aW1hZ2Uvd2UAA2Jw",  # common/common.capnp:MimeTypes.imageWebp
    "EB1QBgb/5LKSfVfzGf0AER4E/wuGzSbIvrKiAAABM28HmQcxFVIBESkHAABRJAMBUTACAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5pbWFnZVN2Z1htAWxQAQEBDAACAQwAABEBcv9pbWFnZS9zdgAfZyt4bWw=",  # common/common.capnp:MimeTypes.imageSvgXml
    "EBxQBgb/a5QtzaBGg4cAER4E/wuGzSbIvrKiAAABM5wHvwcxFToBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy5pbT9hZ2VCbXBQAQEBDAACAQwAABEBUv9pbWFnZS9ibQABcA==",  # common/common.capnp:MimeTypes.imageBmp
    "EBxQBgb/HsA5tmwIaaoAER4E/wuGzSbIvrKiAAABM8IH5wcxFUIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5pbWFnZVRpZmYAUAEBAQwAAgEMAAARAVr/aW1hZ2UvdGkAA2Zm",  # common/common.capnp:MimeTypes.imageTiff
    "EB1QBgb/acb1np/fFYEAER4E/wuGzSbIvrKiAAABM+oHEggxFUoBESkHAABRJAMBUTACAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5pbWFnZVhJY29uAABQAQEBDAACAQwAABEBav9pbWFnZS94LQAPaWNvbg==",  # common/common.capnp:MimeTypes.imageXIcon
    "ECFQBgb//GLOofGkbLUAER4E/wuGzSbIvrKiAAABMz4IkAgxFdIBETEHAABRLAMBUTgCAQAA/2NvbW1vbi9jBm9tbW9uLmNhcG5wOk1pbWVUeXBlcy5pbWFnZVRpZmZBcHBsaWNhdGlvbkdlb3RpZgFmUAEBAQwAAgEMAAAxAQIB/2ltYWdlL3RpA2ZmOyBhcHBsaWNhdGlvbj1nZW90aWZmAA==",  # common/common.capnp:MimeTypes.imageTiffApplicationGeotiff
    "ECZQBgb//WCWbYzRb4UAER4E/wuGzSbIvrKiAAABM5QIDQkxFUICETUHAABRMAMBUTwCAQAA/2NvbW1vbi9jCG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5pbWFnZVRpZmZBcHBsaWNhdGlvbkdlb3RpZmZDbG91ZE9wdGltaXplZABQAQEBDAACAQwAADEBygH/aW1hZ2UvdGkGZmY7IGFwcGxpY2F0aW9uPWdlb3RpZmY7IHByb2ZpbGU9Y2xvdWQtb3B0aW1pemVkAAA=",  # common/common.capnp:MimeTypes.imageTiffApplicationGeotiffCloudOptimized
    "EBxQBgb/5EqoQ64rWLkAER4E/wuGzSbIvrKiAAABMxEJNgkxFUIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5hdWRpb01wZWcAUAEBAQwAAgEMAAARAVr/YXVkaW8vbXAAA2Vn",  # common/common.capnp:MimeTypes.audioMpeg
    "EBxQBgb/ob/eKiqPJqMAER4E/wuGzSbIvrKiAAABMzkJXAkxFToBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy5hdT9kaW9NcDRQAQEBDAACAQwAABEBUv9hdWRpby9tcAABNA==",  # common/common.capnp:MimeTypes.audioMp4
    "EBxQBgb/2Y8nPXLq9t8AER4E/wuGzSbIvrKiAAABM18JggkxFToBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy5hdT9kaW9PZ2dQAQEBDAACAQwAABEBUv9hdWRpby9vZwABZw==",  # common/common.capnp:MimeTypes.audioOgg
    "EBxQBgb/EopS54F09oMAER4E/wuGzSbIvrKiAAABM4UJqAkxFToBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy5hdT9kaW9XYXZQAQEBDAACAQwAABEBUv9hdWRpby93YQABdg==",  # common/common.capnp:MimeTypes.audioWav
    "EBxQBgb/xWCCi13bt/8AER4E/wuGzSbIvrKiAAABM6sJ0AkxFUIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5hdWRpb1dlYm0AUAEBAQwAAgEMAAARAVr/YXVkaW8vd2UAA2Jt",  # common/common.capnp:MimeTypes.audioWebm
    "EBxQBgb/VQ0nxKm915MAER4E/wuGzSbIvrKiAAABM9MJ9gkxFToBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy5hdT9kaW9BYWNQAQEBDAACAQwAABEBUv9hdWRpby9hYQABYw==",  # common/common.capnp:MimeTypes.audioAac
    "EBxQBgb/Qvr9/HOHEokAER4E/wuGzSbIvrKiAAABM/oJHQoxFToBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy52aT9kZW9NcDRQAQEBDAACAQwAABEBUv92aWRlby9tcAABNA==",  # common/common.capnp:MimeTypes.videoMp4
    "EBxQBgb/hmoHCOkCVtQAER4E/wuGzSbIvrKiAAABMyAKRQoxFUIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy52aWRlb01wZWcAUAEBAQwAAgEMAAARAVr/dmlkZW8vbXAAA2Vn",  # common/common.capnp:MimeTypes.videoMpeg
    "EBxQBgb/2FLIkeG91sUAER4E/wuGzSbIvrKiAAABM0gKawoxFToBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy52aT9kZW9PZ2dQAQEBDAACAQwAABEBUv92aWRlby9vZwABZw==",  # common/common.capnp:MimeTypes.videoOgg
    "EBxQBgb/qarXFRtNA+kAER4E/wuGzSbIvrKiAAABM24KkwoxFUIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy52aWRlb1dlYm0AUAEBAQwAAgEMAAARAVr/dmlkZW8vd2UAA2Jt",  # common/common.capnp:MimeTypes.videoWebm
    "EB1QBgb/EFmoRquiK84AER4E/wuGzSbIvrKiAAABM5YKxQoxFWoBESkHAABRJAMBUTACAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy52aWRlb1F1aWNrD3RpbWVQAQEBDAACAQwAABEBgv92aWRlby9xdQFpY2t0aW1lAA==",  # common/common.capnp:MimeTypes.videoQuicktime
    "EB1QBgb/ne4wDdppOtQAER4E/wuGzSbIvrKiAAABM8gK9goxFWIBESkHAABRJAMBUTACAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy52aWRlb1hNc1ZpB2Rlb1ABAQEMAAIBDAAAEQGC/3ZpZGVvL3gtAW1zdmlkZW8A",  # common/common.capnp:MimeTypes.videoXMsVideo
    "EBxQBgb/HApbXP2Xn8oAER4E/wuGzSbIvrKiAAABM/oKGwsxFTIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy5mbx9udFR0ZlABAQEMAAIBDAAAEQFK/2ZvbnQvdHRmAAAA",  # common/common.capnp:MimeTypes.fontTtf
    "EBxQBgb/6et7Uo6QGf0AER4E/wuGzSbIvrKiAAABMx4LPwsxFTIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy5mbx9udE90ZlABAQEMAAIBDAAAEQFK/2ZvbnQvb3RmAAAA",  # common/common.capnp:MimeTypes.fontOtf
    "EBxQBgb/EIfvvVq5D6QAER4E/wuGzSbIvrKiAAABM0ILZQsxFToBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jA29tbW9uLmNhcG5wOk1pbWVUeXBlcy5mbz9udFdvZmZQAQEBDAACAQwAABEBUv9mb250L3dvZgABZg==",  # common/common.capnp:MimeTypes.fontWoff
    "EBxQBgb/3hRnsQubmvYAER4E/wuGzSbIvrKiAAABM2gLjQsxFUIBESUHAABRIAMBUSwCAQAA/2NvbW1vbi9jBG9tbW9uLmNhcG5wOk1pbWVUeXBlcy5mb250V29mZjIAUAEBAQwAAgEMAAARAVr/Zm9udC93b2YAA2Yy",  # common/common.capnp:MimeTypes.fontWoff2
    "EDJQBgb/F6MX9S4OGMcAERQB/8mKqHWnyfGZAAUCBwAAM5ELxwsRFcoRIQcAABEddwAB/2NvbW1vbi9jAm9tbW9uLmNhcG5wOkJsb2IAAFABAVEIAwQAAAQBAAARKWIAAFEoAwFRNAIBEQEBFAEBAAARMSoAAFEsAwFROAIB/2NvbnRlbnRUAAd5cGUBDAACAQwAAQ9kYXRhAQ0AAgENAAE=",  # common/common.capnp:Blob
    "MCQCUAYG/0ayc1MzknXhAFEUAQL/yYqodafJ8ZkARQEHHwEEM8kLQw8RFdIRIQcAADEdzwYAAf9jb21tb24vYwJvbW1vbi5jYXBucDpWYWx1AWVQAQFRfAMEDP//BAEAABNVAyIAAFNQAwMBU1wDAgENAf7/FAEBAAATWQMiAABTVAMDAVNgAwIBDQL9/xQBAgAAE10DIgAAU1gDAwFTZAMCAQ0D/P8UAQMAABNhAyIAAFNcAwMBU2gDAgENBPv/FAEEAAATZQMiAABTYAMDAVNsAwIBDQX6/xQBBQAAE2kDGgAAU2QDAwFTcAMCAQ0G+f8UAQYAABNtAyoAAFNoAwMBU3QDAgENB/j/FAEHAAATcQMqAABTbAMDAVN4AwIBDQj3/xQBCAAAE3UDKgAAU3ADAwFTfAMCAQ0J9v8UAQkAABN5AyIAAFN0AwMBU4ADAgENCvX/FAEKAAATfQMSAABTeAMDAVOEAwIBDQv0/xQBCwAAE4EDEgAAU3wDAwFTiAMCAQ0M8/8UAQwAABOFAxIAAFOAAwMBU4wDAgENDfL/FAENAAATiQMSAABThAMDAVOQAwIBDQ7x/xQBDgAAE40DIgAAU4gDAwFTlAMCAQ0P8P8UAQ8AABORAyoAAFOMAwMBU6gDAgENEO//FAEQAAATpQMqAABToAMDAVO8AwIBDRHu/xQBEQAAE7kDKgAAU7QDAwFT0AMCAQ0S7f8UARIAABPNAyoAAFPIAwMBU+QDAgENE+z/FAETAAAT4QMqAABT3AMDAVP4AwIBDRTr/xQBFAAAE/UDIgAAU/ADAwFTDAQCAQ0V6v8UARUAABMJBDIAAFMEBAMBUyAEAgENFun/FAEWAAATHQQyAABTGAQDAVM0BAIBDRfo/xQBFwAAEzEEMgAAUywEAwFTSAQCAQ0Y5/8UARgAABNFBCoAAFNABAMBU1wEAgENGeb/FAEZAAATWQQaAABTVAQDAVNwBAIBDRrl/xQBGgAAE20EGgAAU2gEAwFThAQCAQ0b5P8UARsAABOBBBoAAFN8BAMBU5gEAgENHOP/FAEcAAATlQQqAABTkAQDAVOsBAIBDR3i/xQBHQAAE6kEMgAAU6QEAwFTwAQCAQ0e4f8UAR4AABO9BBoAAFO4BAMBU9QEAgEHZjY0AQsAAgELAAEHZjMyAQoAAgEKAAEHaTY0AQUAAgEFAAEHaTMyAQQAAgEEAAEHaTE2AQMAAgEDAAEDaTgBAgACAQIAAQ91aTY0AQkAAgEJAAEPdWkzMgEIAAIBCAABD3VpMTYBBwACAQcAAQd1aTgBBgACAQYAAQFiAQEAAgEBAAEBdAEMAAIBDAABAWQBDQACAQ0AAQFwARIAAgESAAEHY2FwARIEAwABARIAAQ9sZjY0AQ4AAVADAQELAAIBDgABD2xmMzIBDgABUAMBAQoAAgEOAAEPbGk2NAEOAAFQAwEBBQACAQ4AAQ9saTMyAQ4AAVADAQEEAAIBDgABD2xpMTYBDgABUAMBAQMAAgEOAAEHbGk4AQ4AAVADAQECAAIBDgABH2x1aTY0AQ4AAVADAQEJAAIBDgABH2x1aTMyAQ4AAVADAQEIAAIBDgABH2x1aTE2AQ4AAVADAQEHAAIBDgABD2x1aTgBDgABUAMBAQYAAgEOAAEDbGIBDgABUAMBAQEAAgEOAAEDbHQBDgABUAMBAQwAAgEOAAEDbGQBDgABUAMBAQ0AAgEOAAEPbGNhcAEOAAFQAwEBEgQDAAEBDgABH2xwYWlyAQ4AAVADAQEQ/zNHFyVHhtS5AAABAQ4AAQNsdgEOAAFQAwEBEP9GsnNTM5J14QAAAQEOAAE=",  # common/common.capnp:Value
    "EDZQBgb/M0cXJUeG1LkAERQB/8mKqHWnyfGZAAUCBxABM2sQmhARFcoRIQcAABEddwAAEZEX/2NvbW1vbi9jAm9tbW9uLmNhcG5wOlBhaXIAAFABAVEIAwQAAAQBAAARKSIAAFEkAwFRMAIBEQEBFAEBAAARLSIAAFEoAwFRNAIBB2ZzdAESAQH/M0cXJUeG1LkAAAABEgABB3NuZAESBQEB/zNHFyVHhtS5AAAAARIAAUEIAREFEhEFEgFGAVM=",  # common/common.capnp:Pair
    "EC1QBgb/2W5YjAv1aagAERQD/8mKqHWnyfGZAAAAEAEzRQ/HDxEV4hEhBwAAER1HEW0XEXUP/2NvbW1vbi9jAm9tbW9uLmNhcG5wOkZhY3QHb3J5UAEBUQQDBQAA/80IlR+9iwX9ASIF3xt/9xDQERE6AABBDAFBHAERLQc/Y3JlYXRlEQEfUQQCAf/ZbliMC/VpqAABAQAAEQEfUQQCAf/ZbliMC/VpqAABAQAAQAFRBAEB/9VInFnL0a+yAAAAQQQBEQE6P091dHB1dA==",  # common/common.capnp:Factory
    "EBNQBgb/zQiVH72LBf0AERwBAAAEBxABAAAxFVIBAAT/Y29tbW9uL2MEb21tb24uY2FwbnA6RmFjdG9yeS5jcmVhdGUkUGFyYW0Bcw==",  # common/common.capnp:Factory.create$Params
    "ECNQBgb/IgXfG3/3ENAAERwBAAAFAQcQAQAAMRVaAQABESE/AAH/Y29tbW9uL2MEb21tb24uY2FwbnA6RmFjdG9yeS5jcmVhdGUkUmVzdWwDdHNRBAMEAAAEAQAAEQ0iAABRCAMBURQCAQdvdXQBEgEB/9luWIwL9WmoAAAAARIAAQ==",  # common/common.capnp:Factory.create$Results
    "EC9QBgb/aHuixrXlcZcAERQD/8mKqHWnyfGZAAAAEAEzyQ9pEBEV8hEhBwAAER1HEW0XEXUX/2NvbW1vbi9jAm9tbW9uLmNhcG5wOklPRmEfY3RvcnlQAQFRBAMFAAD/XVZbzvSyOJsB8EcAYHn0F4QREUIAAEEMAUEcAREtB39wcm9kdWNlEQEfUQQCAf9oe6LGteVxlwABAQAAEQEfUQQCAf9oe6LGteVxlwABAQAAQAFRBAEB/9VInFnL0a+yAAAAQQgBEQUyEQU6H0lucHV0P091dHB1dA==",  # common/common.capnp:IOFactory
    "ECNQBgb/XVZbzvSyOJsAER4BAAAFAQcQAQAAMRVqAQABESE/AAH/Y29tbW9uL2MEb21tb24uY2FwbnA6SU9GYWN0b3J5LnByb2R1Y2UkUGEPcmFtc1EEAwQAAAQBAAARDRoAAFEIAwFRFAIBA2luARIBAf9oe6LGteVxlwAAAAESAAE=",  # common/common.capnp:IOFactory.produce$Params
    "ECNQBgb78EdgefQXhBEeAQAABQEHEAEAADEVcgEAAREhPwAB/2NvbW1vbi9jBG9tbW9uLmNhcG5wOklPRmFjdG9yeS5wcm9kdWNlJFJlH3N1bHRzUQQDBAAABAEAABENIgAAUQgDAVEUAgEHb3V0ARIFAQH/aHuixrXlcZcAAAABEgAB",  # common/common.capnp:IOFactory.produce$Results
    "ECtQBgb/xWoLu8xFMMgAERQD/8mKqHWnyfGZAAAAEAEzdBHnEREV2hEhBwAAER1HEW0HEW0P/2NvbW1vbi9jAm9tbW9uLmNhcG5wOkhvbGQDZXJQAQFRBAMFAAD/jVdfz0oFbZYBicwy7krTi6ERETIAAEEMAUEcAREtBx92YWx1ZREBH1EEAgH/xWoLu8xFMMgAAQEAABEBH1EEAgH/xWoLu8xFMMgAAQEAAEABUAEBQQQBEQESAVQ=",  # common/common.capnp:Holder
    "EBJQBgb/jVdfz0oFbZYAERsBAAAEBxABAAAxFUIBAAT/Y29tbW9uL2MEb21tb24uY2FwbnA6SG9sZGVyLnZhbHVlJFBhcmFtcwA=",  # common/common.capnp:Holder.value$Params
    "ECNQBgb/icwy7krTi6EAERsBAAAFAQcQAQAAMRVKAQABESE/AAH/Y29tbW9uL2MEb21tb24uY2FwbnA6SG9sZGVyLnZhbHVlJFJlc3VsdHMAAFEEAwQAAAQBAAARDTIAAFEIAwFRFAIBH3ZhbHVlARIBAf/Fagu7zEUwyAAAAAESAAE=",  # common/common.capnp:Holder.value$Results
    "EChQBgb/9lZdMHw9VO4AERQD/8mKqHWnyfGZAAAAEAEz6REsEjEVOgERJQcAABEhBxEhJxFhD/9jb21tb24vYwNvbW1vbi5jYXBucDpJZGVudGlmaWFibGU/SG9sZGVyUAEBUAMFUQgBAf/VSJxZy9GvsgAAAP/Fagu7zEUwyABAAREBH1EEAgH/xWoLu8xFMMgAAAARARdRBAEBAQFQAwEBEgEB//ZWXTB8PVTuAAAAQQQBEQESAVQ=",  # common/common.capnp:IdentifiableHolder
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

IdInformation = _StructModule(
    _loader.get(0xD4CB7ECBFE03DAD3).as_struct(),
    "IdInformation",
)
Identifiable = _InterfaceModule(
    _loader.get(0xB2AFD1CB599C48D5).as_interface(),
    "Identifiable",
)
StructuredText = _StructModule(
    _loader.get(0xED6C098B67CAD454).as_struct(),
    "StructuredText",
)
StructuredText.Type = _EnumModule(
    StructuredText.schema.fields["type"].schema,
    "Type",
)
MimeTypes = _StructModule(
    _loader.get(0xA2B2BEC826CD860B).as_struct(),
    "MimeTypes",
)
MimeTypes.textPlain = _loader.get(0xA1FB63F567498202).as_const_value()
MimeTypes.textHtml = _loader.get(0xEABEA137FFA10C15).as_const_value()
MimeTypes.textCss = _loader.get(0xC35C5DFA12865F7C).as_const_value()
MimeTypes.textCsv = _loader.get(0xDB3C835EEAAFC524).as_const_value()
MimeTypes.textJavascript = _loader.get(0xB770F661310FFD5D).as_const_value()
MimeTypes.textMarkdown = _loader.get(0xF58D4413623395B8).as_const_value()
MimeTypes.textXml = _loader.get(0x9B0F84052EDBC30A).as_const_value()
MimeTypes.applicationJson = _loader.get(0xA727E0D037E26C2D).as_const_value()
MimeTypes.applicationXml = _loader.get(0x89904B7AF536F230).as_const_value()
MimeTypes.applicationPdf = _loader.get(0xE2067BB8749F32F8).as_const_value()
MimeTypes.applicationZip = _loader.get(0xBDA515C77765B8C7).as_const_value()
MimeTypes.applicationGzip = _loader.get(0xFBECBA511EB4D275).as_const_value()
MimeTypes.applicationOctetStream = _loader.get(0xB6356D9A0671045D).as_const_value()
MimeTypes.applicationJavascript = _loader.get(0xA4FFF2B2C27EB1AA).as_const_value()
MimeTypes.applicationWwwFormUrlencoded = _loader.get(
    0xF995D3AB16E271EE,
).as_const_value()
MimeTypes.multipartFormData = _loader.get(0xE67422806E9EECB5).as_const_value()
MimeTypes.applicationVndApacheParquet = _loader.get(0x95CCA6EB99E82455).as_const_value()
MimeTypes.imagePng = _loader.get(0x954D7D5F7E52AEE7).as_const_value()
MimeTypes.imageJpeg = _loader.get(0xA3BB3AB5CA7F522A).as_const_value()
MimeTypes.imageGif = _loader.get(0xE437EA6ED9AB4E31).as_const_value()
MimeTypes.imageWebp = _loader.get(0x9446D647F76DB683).as_const_value()
MimeTypes.imageSvgXml = _loader.get(0xFD19F3577D92B2E4).as_const_value()
MimeTypes.imageBmp = _loader.get(0x878346A0CD2D946B).as_const_value()
MimeTypes.imageTiff = _loader.get(0xAA69086CB639C01E).as_const_value()
MimeTypes.imageXIcon = _loader.get(0x8115DF9F9EF5C669).as_const_value()
MimeTypes.imageTiffApplicationGeotiff = _loader.get(0xB56CA4F1A1CE62FC).as_const_value()
MimeTypes.imageTiffApplicationGeotiffCloudOptimized = _loader.get(
    0x856FD18C6D9660FD,
).as_const_value()
MimeTypes.audioMpeg = _loader.get(0xB9582BAE43A84AE4).as_const_value()
MimeTypes.audioMp4 = _loader.get(0xA3268F2A2ADEBFA1).as_const_value()
MimeTypes.audioOgg = _loader.get(0xDFF6EA723D278FD9).as_const_value()
MimeTypes.audioWav = _loader.get(0x83F67481E7528A12).as_const_value()
MimeTypes.audioWebm = _loader.get(0xFFB7DB5D8B8260C5).as_const_value()
MimeTypes.audioAac = _loader.get(0x93D7BDA9C4270D55).as_const_value()
MimeTypes.videoMp4 = _loader.get(0x89128773FCFDFA42).as_const_value()
MimeTypes.videoMpeg = _loader.get(0xD45602E908076A86).as_const_value()
MimeTypes.videoOgg = _loader.get(0xC5D6BDE191C852D8).as_const_value()
MimeTypes.videoWebm = _loader.get(0xE9034D1B15D7AAA9).as_const_value()
MimeTypes.videoQuicktime = _loader.get(0xCE2BA2AB46A85910).as_const_value()
MimeTypes.videoXMsVideo = _loader.get(0xD43A69DA0D30EE9D).as_const_value()
MimeTypes.fontTtf = _loader.get(0xCA9F97FD5C5B0A1C).as_const_value()
MimeTypes.fontOtf = _loader.get(0xFD19908E527BEBE9).as_const_value()
MimeTypes.fontWoff = _loader.get(0xA40FB95ABDEF8710).as_const_value()
MimeTypes.fontWoff2 = _loader.get(0xF69A9B0BB16714DE).as_const_value()
Blob = _StructModule(
    _loader.get(0xC7180E2EF517A317).as_struct(),
    "Blob",
)
Value = _StructModule(
    _loader.get(0xE17592335373B246).as_struct(),
    "Value",
)
Factory = _InterfaceModule(
    _loader.get(0xA869F50B8C586ED9).as_interface(),
    "Factory",
)
IOFactory = _InterfaceModule(
    _loader.get(0x9771E5B5C6A27B68).as_interface(),
    "IOFactory",
)
Pair = _StructModule(
    _loader.get(0xB9D4864725174733).as_struct(),
    "Pair",
)
Holder = _InterfaceModule(
    _loader.get(0xC83045CCBB0B6AC5).as_interface(),
    "Holder",
)
IdentifiableHolder = _InterfaceModule(
    _loader.get(0xEE543D7C305D56F6).as_interface(),
    "IdentifiableHolder",
)
