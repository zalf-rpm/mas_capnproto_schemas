"""Server result helper types for `service.capnp`."""

from collections.abc import Sequence
from typing import Any, Literal, overload

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.service.service_capnp.types import builders as builders
from mas.schema.service.service_capnp.types import readers as readers

class IdentitiesServerResult(_DynamicStructBuilder):
    @property
    def infos(self) -> builders.IdInformationListBuilder: ...
    @infos.setter
    def infos(
        self,
        value: builders.IdInformationListBuilder
        | readers.IdInformationListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["infos"],
        size: int | None = None,
    ) -> builders.IdInformationListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class SimpleFactoryCreateServerResult(_DynamicStructBuilder):
    @property
    def caps(self) -> builders.IdentifiableClientListBuilder: ...
    @caps.setter
    def caps(
        self,
        value: builders.IdentifiableClientListBuilder
        | readers.IdentifiableClientListReader
        | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["caps"],
        size: int | None = None,
    ) -> builders.IdentifiableClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class ServiceinterfacenamesServerResult(_DynamicStructBuilder):
    @property
    def names(self) -> builders.TextListBuilder: ...
    @names.setter
    def names(
        self,
        value: builders.TextListBuilder | readers.TextListReader | Sequence[Any],
    ) -> None: ...
    @overload
    def init(
        self,
        field: Literal["names"],
        size: int | None = None,
    ) -> builders.TextListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...

class StoppableStopServerResult(_DynamicStructBuilder):
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool) -> None: ...
