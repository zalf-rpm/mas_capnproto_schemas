"""Client helper types for `soil.capnp`."""

from collections.abc import Sequence
from typing import Any

from capnp.lib.capnp import (
    _DynamicCapabilityClient,
)

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.geo.geo_capnp.types.builders import LatLonCoordBuilder
from mas.schema.geo.geo_capnp.types.readers import LatLonCoordReader
from mas.schema.persistence.persistence_capnp.types.clients import PersistentClient
from mas.schema.soil.soil_capnp.types import builders as builders
from mas.schema.soil.soil_capnp.types import readers as readers
from mas.schema.soil.soil_capnp.types import requests as requests
from mas.schema.soil.soil_capnp.types.results import client as results_client

class ProfileClient(IdentifiableClient, PersistentClient):
    def data(self) -> results_client.DataResult: ...
    def geoLocation(self) -> results_client.GeolocationResult: ...
    def data_request(self) -> requests.DataRequest: ...
    def geoLocation_request(self) -> requests.GeolocationRequest: ...

class StreamClient(_DynamicCapabilityClient):
    def nextProfiles(
        self,
        maxCount: int | None = None,
    ) -> results_client.NextprofilesResult: ...
    def nextProfiles_request(
        self,
        maxCount: int | None = None,
    ) -> requests.NextprofilesRequest: ...

class ServiceClient(IdentifiableClient, PersistentClient):
    def checkAvailableParameters(
        self,
        mandatory: builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any]
        | None = None,
        optional: builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any]
        | None = None,
        onlyRawData: bool | None = None,
    ) -> results_client.CheckavailableparametersResult: ...
    def getAllAvailableParameters(
        self,
        onlyRawData: bool | None = None,
    ) -> results_client.GetallavailableparametersResult: ...
    def closestProfilesAt(
        self,
        coord: LatLonCoordBuilder | LatLonCoordReader | dict[str, Any] | None = None,
        query: builders.QueryBuilder
        | readers.QueryReader
        | dict[str, Any]
        | None = None,
    ) -> results_client.ClosestprofilesatResult: ...
    def streamAllProfiles(
        self,
        mandatory: builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any]
        | None = None,
        optional: builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any]
        | None = None,
        onlyRawData: bool | None = None,
    ) -> results_client.StreamallprofilesResult: ...
    def checkAvailableParameters_request(
        self,
        mandatory: builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any]
        | None = None,
        optional: builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any]
        | None = None,
        onlyRawData: bool | None = None,
    ) -> requests.CheckavailableparametersRequest: ...
    def getAllAvailableParameters_request(
        self,
        onlyRawData: bool | None = None,
    ) -> requests.GetallavailableparametersRequest: ...
    def closestProfilesAt_request(
        self,
        coord: LatLonCoordBuilder | None = None,
        query: builders.QueryBuilder | None = None,
    ) -> requests.ClosestprofilesatRequest: ...
    def streamAllProfiles_request(
        self,
        mandatory: builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any]
        | None = None,
        optional: builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any]
        | None = None,
        onlyRawData: bool | None = None,
    ) -> requests.StreamallprofilesRequest: ...
