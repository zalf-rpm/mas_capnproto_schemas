"""Server result helper types for `soil.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.soil.soil_capnp.types import builders as builders
from mas.schema.soil.soil_capnp.types import clients as clients
from mas.schema.soil.soil_capnp.types import modules as modules
from mas.schema.soil.soil_capnp.types import readers as readers

class NextprofilesServerResult(_DynamicStructBuilder):
    @property
    def profiles(self) -> builders.ProfileClientListBuilder: ...
    @profiles.setter
    def profiles(
        self,
        value: builders.ProfileClientListBuilder
        | readers.ProfileClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["profiles"],
        size: int | None = None,
    ) -> builders.ProfileClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class GetallavailableparametersServerResult(_DynamicStructBuilder):
    @property
    def mandatory(self) -> builders.PropertyNameEnumListBuilder: ...
    @mandatory.setter
    def mandatory(
        self,
        value: builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any],
    ) -> None: ...
    @property
    def optional(self) -> builders.PropertyNameEnumListBuilder: ...
    @optional.setter
    def optional(
        self,
        value: builders.PropertyNameEnumListBuilder
        | readers.PropertyNameEnumListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["mandatory"],
        size: int | None = None,
    ) -> builders.PropertyNameEnumListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["optional"],
        size: int | None = None,
    ) -> builders.PropertyNameEnumListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ClosestprofilesatServerResult(_DynamicStructBuilder):
    @property
    def profiles(self) -> builders.ProfileClientListBuilder: ...
    @profiles.setter
    def profiles(
        self,
        value: builders.ProfileClientListBuilder
        | readers.ProfileClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["profiles"],
        size: int | None = None,
    ) -> builders.ProfileClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class StreamallprofilesServerResult(_DynamicStructBuilder):
    @property
    def allProfiles(
        self,
    ) -> (
        modules._ServiceInterfaceModule._StreamInterfaceModule.Server
        | clients.StreamClient
    ): ...
    @allProfiles.setter
    def allProfiles(
        self,
        value: modules._ServiceInterfaceModule._StreamInterfaceModule.Server
        | clients.StreamClient,
    ) -> None: ...
