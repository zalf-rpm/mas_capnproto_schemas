"""Client helper types for `modam.capnp`."""

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.dakis.modam.modam_capnp.types import requests as requests
from mas.schema.dakis.modam.modam_capnp.types.results import client as results_client

class ModamWrapperServiceClient(_DynamicCapabilityClient):
    def runAemModel(
        self,
        input: str | None = None,
    ) -> results_client.RunaemmodelResult: ...
    def runFieldModel(
        self,
        input: str | None = None,
    ) -> results_client.RunfieldmodelResult: ...
    def runAemModel_request(
        self,
        input: str | None = None,
    ) -> requests.RunaemmodelRequest: ...
    def runFieldModel_request(
        self,
        input: str | None = None,
    ) -> requests.RunfieldmodelRequest: ...
