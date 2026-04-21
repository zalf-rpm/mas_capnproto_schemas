"""Runtime placeholder module for server helpers of `management.capnp`."""

# pyright: reportUnusedClass=none

from .. import Fertilizer, FertilizerService, Service

FertilizerServer = Fertilizer.Server
FertilizerServiceServer = FertilizerService.Server
ServiceServer = Service.Server
