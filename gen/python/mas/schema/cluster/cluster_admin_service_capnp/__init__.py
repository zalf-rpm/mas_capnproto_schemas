"""This is an automatically generated stub for `cluster_admin_service.capnp`."""

import base64
from typing import NamedTuple

import capnp
import schema_capnp
from capnp.lib.capnp import _InterfaceModule, _StructModule

capnp.remove_import_hook()

# Embedded compiled schemas (base64-encoded)
_SCHEMA_NODES = [
    "EEJQBgb/+tCpbX2ywfMAARYAAxEV4hEhFxEtZwAC/2NsdXN0ZXJfAmFkbWluX3NlcnZpY2UuY2EHcG5wUQQBAf99DvLWVl1I9wARAUJ/Q2x1c3RlclEQAQL/LF+Av575xrkAUSgCAUE8Af9s+bDj/qNejABROAIBQUwB/+AreSMQf6m+AFFIAgFBVAH/tUQOJgG2MOEAUVACAUF8AQEMAAARAar/bWFzOjpzY2gBZW1hOjpjbHUPc3RlcgAAAQwAABEBmv9tYXMuc2NoZQFtYS5jbHVzdANlcgAAAQwAABEBQn9jbHVzdGVyAAABDAAAMQFCAv9naXRodWIuYwhvbS96YWxmLXJwbS9tYXMtaW5mcmFzdHJ1Y3R1cmUvY2FwbnByb3RvX3NjaGVtYXMvZ2VuL2dvL2NsdXN0ZXIAAAA=",  # cluster_admin_service.capnp
    "EDBQBgb/fQ7y1lZdSPcAERwB//rQqW19ssHzAAQHAAAzrQGMEDEVIgERJXcAA/9jbHVzdGVyXwNhZG1pbl9zZXJ2aWNlLmNhcG5wOkNsdXMHdGVyURwBAf++G2WSofex6AARMVr/zjP2ZYwnJL8AETFi/2BLNSjfxkLsABExWv92R1zqj4RJ+AARMUL/ZCrMvqJLA8kAES2q/8i08tyA8KzWABExYv++Dp+PmVmZ/QARMar/VW5yZWdpc3QAA2Vy/0FkbWluTWFzAAd0ZXL/VXNlck1hc3QAA2Vyf1J1bnRpbWX/Wm1xUGlwZWwBaW5lQWRkcmUPc3Nlc/9WYWx1ZUhvbAAHZGVy/01vZGVsSW5zAXRhbmNlRmFjD3Rvcnk=",  # cluster_admin_service.capnp:Cluster
    "ECFQBgb/vhtlkqH3segAESQD/30O8tZWXUj3AAABM8EBBAIxFXoBESkHAAARJUcRUQcAAP9jbHVzdGVyXwRhZG1pbl9zZXJ2aWNlLmNhcG5wOkNsdXN0ZXIuVW5yZT9naXN0ZXJQAQFRBAMFAAD/o673qTKJt+EBjzNPcfNuqbsREVoAAhEJB/91bnJlZ2lzdAADZXJAAVABAQ==",  # cluster_admin_service.capnp:Cluster.Unregister
    "EBZQBgb/o673qTKJt+EAES8BAAAEBwABMRUKAgAE/2NsdXN0ZXJfB2FkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5VbnJlZ2lzdGVyLnVucmVnaXN0ZXIkUGFyYW1zAAA=",  # cluster_admin_service.capnp:Cluster.Unregister.unregister$Params
    "ECZQBgb/jzNPcfNuqbsAUS8BAQAABAcAATEVEgIAAREtPwAB/2NsdXN0ZXJfB2FkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5VbnJlZ2lzdGVyLnVucmVnaXN0ZXIkUmVzdWx0AXNRBAMEAAAEAQAAEQ1CAABRCAMBURQCAX9zdWNjZXNzAQEAAgEBAAE=",  # cluster_admin_service.capnp:Cluster.Unregister.unregister$Results
    "EDBQBgb/zjP2ZYwnJL8AESQD/30O8tZWXUj3AAABMwgC8wMxFYIBESkHAAARJYcRhRcAAP9jbHVzdGVyXwVhZG1pbl9zZXJ2aWNlLmNhcG5wOkNsdXN0ZXIuQWRtaW5NYXN0ZXIAUAEBUQgDBQAA/xDmTW/uVDuUAd7jseKBT0PnETHqAAIRMQcBAf+OzKZrZZtmoAGPAMSnAc6+1BElggACER0H/3JlZ2lzdGVyAk1vZGVsSW5zdGFuY2VGYWMPdG9yeUAB/2F2YWlsYWJsAWVNb2RlbHMAQAFRBAEB/9VInFnL0a+yAAAA",  # cluster_admin_service.capnp:Cluster.AdminMaster
    "EDlQBgb/EOZNb+5UO5QAETABAAAFAgcAATEVogIAARE1dwAB/2NsdXN0ZXJfCWFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5BZG1pbk1hc3Rlci5yZWdpc3Rlck1vZGVsSW5zdGFuY2VGYWN0b3J5JFBhcgdhbXNRCAMEAAAEAQAAESlKAABRKAMBUTQCAREBARQBAQAAETFKAABRMAMBUTwCAf9hTW9kZWxJZAAAAAEMAAIBDAAB/2FGYWN0b3J5AAAAARH/vg6fj5lZmf0AAAEBEQAB",  # cluster_admin_service.capnp:Cluster.AdminMaster.registerModelInstanceFactory$Params
    "EGtQBgb/vg6fj5lZmf0AESQD/30O8tZWXUj3AAABM9QKihAxFcoBETEHAAAxLccBE3EBFwAA/2NsdXN0ZXJfBmFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeQAAUAEBURwDBQEC/3QS8dJkEviLARyEX1HcsWj0EdFiAAIRyQcBA/8E4tfiooNdmAGToQ3n3fasvBG9agACEbUHAQT/FsNXz1GCXYsBXJlNHcZTEKgRqfIAAhGpBwEF/yF2tpj5w6T+ARkwZ/Whefm6EZ2KAAIRmQcBAf/YdMT7K+q25AHa5gPnQFrP4xGNQgACEYEHAAD/xAHBh0QdpL4BCF9uwaSyj8oRdbIAAhFxBwEG/3284sx4P4rYAf1cLEbw+83lEWWKAAIRYQf/bmV3SW5zdGEAB25jZUAB/25ld0luc3RhAA9uY2VzQAH/bmV3Q2xvdWQCVmlhWm1xUGlwZWxpbmVQch9veGllc0AB/25ld0Nsb3VkAVZpYVByb3h5AABAAX9tb2RlbElkQAH/cmVnaXN0ZXIBTW9kZWxJbnMfdGFuY2VAAf9yZXN0b3JlUwF0dXJkeVJlZgAAQAFRBAEB/9VInFnL0a+yAAAA",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory
    "EBdQBgb/dBLx0mQS+IsAETkBAAAEBwABMRViAgAE/2NsdXN0ZXJfCGFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5uZXdJbnN0YW5jZSRQYXIHYW1z",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.newInstance$Params
    "EChQBgb/HIRfUdyxaPQAETkBAAAFAQcAATEVagIAARExPwAB/2NsdXN0ZXJfCGFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5uZXdJbnN0YW5jZSRSZXMPdWx0c1EEAwQAAAQBAAARDUoAAFEMAwFRGAIB/2luc3RhbmNlAAAAARH/yLTy3IDwrNYAAAEBEQAB",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.newInstance$Results
    "EEtQBgb/yLTy3IDwrNYAESQD/30O8tZWXUj3AAAAEAEz1AnQCjEVggERKQcAABElhxHtBxHtD/9jbHVzdGVyXwVhZG1pbl9zZXJ2aWNlLmNhcG5wOkNsdXN0ZXIuVmFsdWVIb2xkZXIAUAEBUQgDBQAA/0/oAcqcVqaLAWza8Xj3iV6BETEyAABBLAFBPAERTQcBAf+WiCcKsMhnqQHF4DtZGJq93RFBQhFBH0FkAUF0ARGFBx92YWx1ZREBH1EEAgH/yLTy3IDwrNYAAQEAABEBH1EEAgH/yLTy3IDwrNYAAQEAAEABf3JlbGVhc2VRBAEC//GNLxcSYLnCAFEEAgFBFAEBDAAAEQFq/3JlbGVhc2VWAA9hbHVlAAARAR9RBAIB/8i08tyA8KzWAAEBAAARAR9RBAIB/8i08tyA8KzWAAEBAABAAVABAUEEAREBEgFU",  # cluster_admin_service.capnp:Cluster.ValueHolder
    "EBVQBgb/T+gBypxWposAETABAAAEBxABAAAxFeoBAAT/Y2x1c3Rlcl8GYWRtaW5fc2VydmljZS5jYXBucDpDbHVzdGVyLlZhbHVlSG9sZGVyLnZhbHVlJFBhD3JhbXM=",  # cluster_admin_service.capnp:Cluster.ValueHolder.value$Params
    "ECVQBgb/bNrxePeJXoEAETABAAAFAQcQAQAAMRXyAQABESk/AAH/Y2x1c3Rlcl8GYWRtaW5fc2VydmljZS5jYXBucDpDbHVzdGVyLlZhbHVlSG9sZGVyLnZhbHVlJFJlH3N1bHRzUQQDBAAABAEAABENIgAAUQgDAVEUAgEHdmFsARIBAf/ItPLcgPCs1gAAAAESAAE=",  # cluster_admin_service.capnp:Cluster.ValueHolder.value$Results
    "EBVQBgb/lognCrDIZ6kAETABAAAEBxABAAAxFfoBAAT/Y2x1c3Rlcl8GYWRtaW5fc2VydmljZS5jYXBucDpDbHVzdGVyLlZhbHVlSG9sZGVyLnJlbGVhc2UkP1BhcmFtcw==",  # cluster_admin_service.capnp:Cluster.ValueHolder.release$Params
    "EBVQBgb/xeA7WRiavd0AETABAAAEBxABAAAxFQICAAT/Y2x1c3Rlcl8HYWRtaW5fc2VydmljZS5jYXBucDpDbHVzdGVyLlZhbHVlSG9sZGVyLnJlbGVhc2UkUmVzdWx0cwA=",  # cluster_admin_service.capnp:Cluster.ValueHolder.release$Results
    "EClQBgb/BOLX4qKDXZgAUTkBAQAABAcAATEVagIAARExPwAB/2NsdXN0ZXJfCGFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5uZXdJbnN0YW5jZXMkUGEPcmFtc1EEAwQAAAQBAAARDZIAAFEQAwFRHAIB/251bWJlck9mAUluc3RhbmNlAXMBAwACAQMAAQ==",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.newInstances$Params
    "EDhQBgb/k6EN5932rLwAETkBAAAFAQcAATEVcgIAARExPwAB/2NsdXN0ZXJfCGFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5uZXdJbnN0YW5jZXMkUmUfc3VsdHNRBAMEAAAEAQAAEQ1SAABRDAMBUVgCAf9pbnN0YW5jZQABcwER/8i08tyA8KzWAAAAQAERAR9RBAIB/8i08tyA8KzWAAAAEQEXUQQBAQEBUAMBAQ4AAVADAQER/8i08tyA8KzWAAABAREAAQ==",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.newInstances$Results
    "ECtQBgb/FsNXz1GCXYsAUTkBAQAABAcAATEV8gIAARE5PwAB/2NsdXN0ZXJfCmFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5uZXdDbG91ZFZpYVptcVBpcGVsaW5lUHJveGllcyRQH2FyYW1zUQQDBAAABAEAABENkgAAURADAVEcAgH/bnVtYmVyT2YBSW5zdGFuY2UBcwEDAAIBAwAB",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.newCloudViaZmqPipelineProxies$Params
    "EDZQBgb/XJlNHcZTEKgAETkBAAAFAQcAATEV+gIAARE5PwAB/2NsdXN0ZXJfCmFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5uZXdDbG91ZFZpYVptcVBpcGVsaW5lUHJveGllcyRSP2VzdWx0c1EEAwQAAAQBAAARDXoAAFEMAwFRSAIB/3Byb3h5QWRkAD9yZXNzZXMBEf/ItPLcgPCs1gAAAEABEQEfUQQCAf/ItPLcgPCs1gAAABEBF1EEAQEBAVADAQEQ/2QqzL6iSwPJAAABAREAAQ==",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.newCloudViaZmqPipelineProxies$Results
    "ECpQBgb/IXa2mPnDpP4AUTkBAQAABAcAATEVigIAARE1PwAB/2NsdXN0ZXJfCWFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5uZXdDbG91ZFZpYVByb3h5JFBhcmFtcwAAUQQDBAAABAEAABENkgAAURADAVEcAgH/bnVtYmVyT2YBSW5zdGFuY2UBcwEDAAIBAwAB",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.newCloudViaProxy$Params
    "EChQBgb/GTBn9aF5+boAETkBAAAFAQcAATEVkgIAARE1PwAB/2NsdXN0ZXJfCWFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5uZXdDbG91ZFZpYVByb3h5JFJlc3VsdAFzUQQDBAAABAEAABENMgAAUQgDAVEUAgEfcHJveHkBEf/ItPLcgPCs1gAAAQERAAE=",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.newCloudViaProxy$Results
    "EBZQBgb/2HTE+yvqtuQAETkBAAAEBwABMRVCAgAE/2NsdXN0ZXJfCGFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5tb2RlbElkJFBhcmFtcwA=",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.modelId$Params
    "ECdQBgb/2uYD50Baz+MAETkBAAAFAQcAATEVSgIAARExPwAB/2NsdXN0ZXJfCGFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5tb2RlbElkJFJlc3VsdHMAAFEEAwQAAAQBAAARDRoAAFEIAwFRFAIBA2lkAQwAAgEMAAE=",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.modelId$Results
    "EDtQBgb/xAHBh0QdpL4AETkBAAAFAgcAATEVsgIAARE1dwAB/2NsdXN0ZXJfCWFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5yZWdpc3Rlck1vZGVsSW5zdGFuY2UkUB9hcmFtc1EIAwQAAAQBAAARKUoAAFEoAwFRNAIBEQEBFAEBAQERMZIAAFE0AwFRQAIB/2luc3RhbmNlAAAAARIEAwABARIAAf9yZWdpc3RyYQF0aW9uVG9rZQFuAQwAAgEMAAARAQoAAA==",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.registerModelInstance$Params
    "EClQBgb/CF9uwaSyj8oAETkBAAAFAQcAATEVugIAARE1PwAB/2NsdXN0ZXJfCWFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5yZWdpc3Rlck1vZGVsSW5zdGFuY2UkUj9lc3VsdHNRBAMEAAAEAQAAEQ1aAABRDAMBURgCAf91bnJlZ2lzdAADZXIBEf++G2WSofex6AAAAQERAAE=",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.registerModelInstance$Results
    "EClQBgb/fbzizHg/itgAETkBAAAFAQcAATEVigIAARE1PwAB/2NsdXN0ZXJfCWFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5yZXN0b3JlU3R1cmR5UmVmJFBhcmFtcwAAUQQDBAAABAEAABENUgAAUQwDAVEYAgH/c3R1cmR5UmUAAWYBDAACAQwAAQ==",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.restoreSturdyRef$Params
    "EChQBgb//VwsRvD7zeUAETkBAAAFAQcAATEVkgIAARE1PwAB/2NsdXN0ZXJfCWFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Nb2RlbEluc3RhbmNlRmFjdG9yeS5yZXN0b3JlU3R1cmR5UmVmJFJlc3VsdAFzUQQDBAAABAEAABENIgAAUQgDAVEUAgEHY2FwARH/yLTy3IDwrNYAAAEBEQAB",  # cluster_admin_service.capnp:Cluster.ModelInstanceFactory.restoreSturdyRef$Results
    "EClQBgb/3uOx4oFPQ+cAETABAAAFAQcAATEVqgIAARE1PwAB/2NsdXN0ZXJfCWFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5BZG1pbk1hc3Rlci5yZWdpc3Rlck1vZGVsSW5zdGFuY2VGYWN0b3J5JFJlcw91bHRzUQQDBAAABAEAABENWgAAUQwDAVEYAgH/dW5yZWdpc3QAA2VyARH/vhtlkqH3segAAAEBEQAB",  # cluster_admin_service.capnp:Cluster.AdminMaster.registerModelInstanceFactory$Results
    "EBZQBgb/jsyma2WbZqAAETABAAAEBwABMRU6AgAE/2NsdXN0ZXJfB2FkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5BZG1pbk1hc3Rlci5hdmFpbGFibGVNb2RlbHMkP1BhcmFtcw==",  # cluster_admin_service.capnp:Cluster.AdminMaster.availableModels$Params
    "ECtQBgb9j8SnAc6+1BEwAQAABQEHAAExFUICAAERLT8AAf9jbHVzdGVyXwhhZG1pbl9zZXJ2aWNlLmNhcG5wOkNsdXN0ZXIuQWRtaW5NYXN0ZXIuYXZhaWxhYmxlTW9kZWxzJFJlc3VsdHMAUQQDBAAABAEAABENUgAAUQwDAVEoAgH/ZmFjdG9yaWUAAXMBDgABUAMBARH/vg6fj5lZmf0AAAEBDgAB",  # cluster_admin_service.capnp:Cluster.AdminMaster.availableModels$Results
    "ECNQBgb/YEs1KN/GQuwAESQD/30O8tZWXUj3AAABM/cDGwUxFXoBESkHAAARJUcRURcAAP9jbHVzdGVyXwRhZG1pbl9zZXJ2aWNlLmNhcG5wOkNsdXN0ZXIuVXNlcj9NYXN0ZXJQAQFRBAMFAAD/ZeDqhcDvgJoB2hsI9/vkR7EREYIAAhEJB/9hdmFpbGFibAFlTW9kZWxzAEABUQQBAf/VSJxZy9GvsgAAAA==",  # cluster_admin_service.capnp:Cluster.UserMaster
    "EBZQBgb/ZeDqhcDvgJoAES8BAAAEBwABMRUyAgAE/2NsdXN0ZXJfB2FkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Vc2VyTWFzdGVyLmF2YWlsYWJsZU1vZGVscyRQH2FyYW1z",  # cluster_admin_service.capnp:Cluster.UserMaster.availableModels$Params
    "ECtQBgb/2hsI9/vkR7EAES8BAAAFAQcAATEVOgIAAREtPwAB/2NsdXN0ZXJfB2FkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5Vc2VyTWFzdGVyLmF2YWlsYWJsZU1vZGVscyRSP2VzdWx0c1EEAwQAAAQBAAARDVIAAFEMAwFRKAIB/2ZhY3RvcmllAAFzAQ4AAVADAQER/74On4+ZWZn9AAABAQ4AAQ==",  # cluster_admin_service.capnp:Cluster.UserMaster.availableModels$Results
    "EFNQBgb/dkdc6o+ESfgAESQD/30O8tZWXUj3AAABMx8FggkxFWIBESkHAAAxJUcBExEBFwAA/2NsdXN0ZXJfBGFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5SdW50B2ltZVABAVEUAwUAAP+IzkZ5j4pmwwHUS2aIe6vfqBGR6gACEZEHAQH/Gt0aEr6qNf4BKc3utvWzvZMRhYIAAhF9BwEC/2x2VFAMLD2bAX8NJZqfWLLmEXFyAAIRaQcBA/9Otolg/7ckwgHGciEwMq4E8BFdkgACEVkHAQT/6Z0RKjAL0LQBu0xi6ozd2LwRTaoAAhFJB/9yZWdpc3RlcgJNb2RlbEluc3RhbmNlRmFjD3RvcnlAAf9hdmFpbGFibAFlTW9kZWxzAEAB/251bWJlck9mAB9Db3Jlc0AB/2ZyZWVOdW1iAWVyT2ZDb3JlAXNAAf9yZXNlcnZlTgF1bWJlck9mQw9vcmVzQAFRBAEB/9VInFnL0a+yAAAA",  # cluster_admin_service.capnp:Cluster.Runtime
    "EDhQBgb/iM5GeY+KZsMAESwBAAAFAgcAATEVggIAARExdwAB/2NsdXN0ZXJfCWFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5SdW50aW1lLnJlZ2lzdGVyTW9kZWxJbnN0YW5jZUZhY3RvcnkkUGFyYW1zAFEIAwQAAAQBAAARKUoAAFEoAwFRNAIBEQEBFAEBAAARMUoAAFEwAwFRPAIB/2FNb2RlbElkAAAAAQwAAgEMAAH/YUZhY3RvcnkAAAABEf++Dp+PmVmZ/QAAAQERAAE=",  # cluster_admin_service.capnp:Cluster.Runtime.registerModelInstanceFactory$Params
    "EClQBgb/1EtmiHur36gAESwBAAAFAQcAATEVigIAARE1PwAB/2NsdXN0ZXJfCWFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5SdW50aW1lLnJlZ2lzdGVyTW9kZWxJbnN0YW5jZUZhY3RvcnkkUmVzdWx0cwAAUQQDBAAABAEAABENWgAAUQwDAVEYAgH/dW5yZWdpc3QAA2VyARH/vhtlkqH3segAAAEBEQAB",  # cluster_admin_service.capnp:Cluster.Runtime.registerModelInstanceFactory$Results
    "EBZQBgb/Gt0aEr6qNf4AESwBAAAEBwABMRUaAgAE/2NsdXN0ZXJfB2FkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5SdW50aW1lLmF2YWlsYWJsZU1vZGVscyRQYXJhA21z",  # cluster_admin_service.capnp:Cluster.Runtime.availableModels$Params
    "ECtQBgb/Kc3utvWzvZMAESwBAAAFAQcAATEVIgIAAREtPwAB/2NsdXN0ZXJfB2FkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5SdW50aW1lLmF2YWlsYWJsZU1vZGVscyRSZXN1B2x0c1EEAwQAAAQBAAARDVIAAFEMAwFRKAIB/2ZhY3RvcmllAAFzAQ4AAVADAQER/74On4+ZWZn9AAABAQ4AAQ==",  # cluster_admin_service.capnp:Cluster.Runtime.availableModels$Results
    "EBZQBgb/bHZUUAwsPZsAESwBAAAEBwABMRUKAgAE/2NsdXN0ZXJfB2FkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5SdW50aW1lLm51bWJlck9mQ29yZXMkUGFyYW1zAAA=",  # cluster_admin_service.capnp:Cluster.Runtime.numberOfCores$Params
    "ECZQBgb/fw0lmp9YsuYAUSwBAQAABAcAATEVEgIAAREtPwAB/2NsdXN0ZXJfB2FkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5SdW50aW1lLm51bWJlck9mQ29yZXMkUmVzdWx0AXNRBAMEAAAEAQAAEQ0yAABRCAMBURQCAR9jb3JlcwEDAAIBAwAB",  # cluster_admin_service.capnp:Cluster.Runtime.numberOfCores$Results
    "EBZQBgb/TraJYP+3JMIAESwBAAAEBwABMRUqAgAE/2NsdXN0ZXJfB2FkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5SdW50aW1lLmZyZWVOdW1iZXJPZkNvcmVzJFBhD3JhbXM=",  # cluster_admin_service.capnp:Cluster.Runtime.freeNumberOfCores$Params
    "ECZQBgb/xnIhMDKuBPAAUSwBAQAABAcAATEVMgIAAREtPwAB/2NsdXN0ZXJfB2FkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5SdW50aW1lLmZyZWVOdW1iZXJPZkNvcmVzJFJlH3N1bHRzUQQDBAAABAEAABENMgAAUQgDAVEUAgEfY29yZXMBAwACAQMAAQ==",  # cluster_admin_service.capnp:Cluster.Runtime.freeNumberOfCores$Results
    "EDdQBgb/6Z0RKjAL0LQAUSwBAQAABQEHAAExFUICAAERLXcAAf9jbHVzdGVyXwhhZG1pbl9zZXJ2aWNlLmNhcG5wOkNsdXN0ZXIuUnVudGltZS5yZXNlcnZlTnVtYmVyT2ZDb3JlcyRQYXJhbXMAUQgDBAAABAEAABEpagAAUSgDAVE0AgEBARQBAQAAETFKAABRMAMBUTwCAf9yZXNlcnZlQwAPb3JlcwEDAAIBAwAB/2FNb2RlbElkAAAAAQwAAgEMAAE=",  # cluster_admin_service.capnp:Cluster.Runtime.reserveNumberOfCores$Params
    "EChQBgb/u0xi6ozd2LwAUSwBAQAABAcAATEVSgIAARExPwAB/2NsdXN0ZXJfCGFkbWluX3NlcnZpY2UuY2FwbnA6Q2x1c3Rlci5SdW50aW1lLnJlc2VydmVOdW1iZXJPZkNvcmVzJFJlc3VsdHMAAFEEAwQAAAQBAAARDXIAAFEMAwFRGAIB/3Jlc2VydmVkAB9Db3JlcwEDAAIBAwAB",  # cluster_admin_service.capnp:Cluster.Runtime.reserveNumberOfCores$Results
    "EDVQBgb/ZCrMvqJLA8kAESQB/30O8tZWXUj3AAUCBwAAM4YJ0AkxFcoBETEHAAARLXcAAf9jbHVzdGVyXwZhZG1pbl9zZXJ2aWNlLmNhcG5wOkNsdXN0ZXIuWm1xUGlwZWxpbmVBZGRyZXNzZXMAAFABAVEIAwQAAAQBAAARKTIAAFEkAwFRMAIBEQEBFAEBAAARLToAAFEoAwFRNAIBH2lucHV0AQwAAgEMAAE/b3V0cHV0AQwAAgEMAAE=",  # cluster_admin_service.capnp:Cluster.ZmqPipelineAddresses
]

# Load schemas and build module structure
_loader = capnp.SchemaLoader()
for _schema_b64 in _SCHEMA_NODES:
    _schema_data = base64.b64decode(_schema_b64)
    _node_reader = schema_capnp.Node.from_bytes_packed(_schema_data)
    _loader.load_dynamic(_node_reader)

# Build module structure inline
Cluster = _StructModule(_loader.get(0xF7485D56D6F20E7D).as_struct(), "Cluster")
Cluster.Unregister = _InterfaceModule(
    _loader.get(0xE8B1F7A192651BBE).as_interface(),
    "Unregister",
)
Cluster.AdminMaster = _InterfaceModule(
    _loader.get(0xBF24278C65F633CE).as_interface(),
    "AdminMaster",
)
Cluster.UserMaster = _InterfaceModule(
    _loader.get(0xEC42C6DF28354B60).as_interface(),
    "UserMaster",
)
Cluster.Runtime = _InterfaceModule(
    _loader.get(0xF849848FEA5C4776).as_interface(),
    "Runtime",
)
Cluster.ZmqPipelineAddresses = _StructModule(
    _loader.get(0xC9034BA2BECC2A64).as_struct(),
    "ZmqPipelineAddresses",
)
Cluster.ValueHolder = _InterfaceModule(
    _loader.get(0xD6ACF080DCF2B4C8).as_interface(),
    "ValueHolder",
)
Cluster.ModelInstanceFactory = _InterfaceModule(
    _loader.get(0xFD9959998F9F0EBE).as_interface(),
    "ModelInstanceFactory",
)

Cluster.AdminMaster.Server.AvailablemodelsResultTuple = NamedTuple(
    "AvailablemodelsResultTuple",
    [("factories", object)],
)
Cluster.AdminMaster.Server.RegistermodelinstancefactoryResultTuple = NamedTuple(
    "RegistermodelinstancefactoryResultTuple",
    [("unregister", object)],
)
Cluster.ModelInstanceFactory.Server.ModelidResultTuple = NamedTuple(
    "ModelidResultTuple",
    [("id", object)],
)
Cluster.ModelInstanceFactory.Server.NewcloudviaproxyResultTuple = NamedTuple(
    "NewcloudviaproxyResultTuple",
    [("proxy", object)],
)
Cluster.ModelInstanceFactory.Server.NewcloudviazmqpipelineproxiesResultTuple = (
    NamedTuple("NewcloudviazmqpipelineproxiesResultTuple", [("proxyAddresses", object)])
)
Cluster.ModelInstanceFactory.Server.NewinstanceResultTuple = NamedTuple(
    "NewinstanceResultTuple",
    [("instance", object)],
)
Cluster.ModelInstanceFactory.Server.NewinstancesResultTuple = NamedTuple(
    "NewinstancesResultTuple",
    [("instances", object)],
)
Cluster.ModelInstanceFactory.Server.RegistermodelinstanceResultTuple = NamedTuple(
    "RegistermodelinstanceResultTuple",
    [("unregister", object)],
)
Cluster.ModelInstanceFactory.Server.RestoresturdyrefResultTuple = NamedTuple(
    "RestoresturdyrefResultTuple",
    [("cap", object)],
)
Cluster.Runtime.Server.AvailablemodelsResultTuple = NamedTuple(
    "AvailablemodelsResultTuple",
    [("factories", object)],
)
Cluster.Runtime.Server.FreenumberofcoresResultTuple = NamedTuple(
    "FreenumberofcoresResultTuple",
    [("cores", object)],
)
Cluster.Runtime.Server.NumberofcoresResultTuple = NamedTuple(
    "NumberofcoresResultTuple",
    [("cores", object)],
)
Cluster.Runtime.Server.RegistermodelinstancefactoryResultTuple = NamedTuple(
    "RegistermodelinstancefactoryResultTuple",
    [("unregister", object)],
)
Cluster.Runtime.Server.ReservenumberofcoresResultTuple = NamedTuple(
    "ReservenumberofcoresResultTuple",
    [("reservedCores", object)],
)
Cluster.Unregister.Server.UnregisterResultTuple = NamedTuple(
    "UnregisterResultTuple",
    [("success", object)],
)
Cluster.UserMaster.Server.AvailablemodelsResultTuple = NamedTuple(
    "AvailablemodelsResultTuple",
    [("factories", object)],
)
Cluster.ValueHolder.Server.ValueResultTuple = NamedTuple(
    "ValueResultTuple",
    [("val", object)],
)
