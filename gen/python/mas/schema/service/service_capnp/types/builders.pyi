"""Builder helper types for `service.capnp`."""

from typing import Any, Literal, override

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
    _DynamicStructBuilder,
)

from mas.schema.service.service_capnp.types import common as common
from mas.schema.service.service_capnp.types import lists as lists
from mas.schema.service.service_capnp.types import readers as readers

class CreateParamsBuilder(_DynamicStructBuilder):
    @property
    def timeoutSeconds(self) -> int: ...
    @timeoutSeconds.setter
    def timeoutSeconds(self, value: int) -> None: ...
    @property
    def interfaceNameToRegistrySR(self) -> PairListBuilder: ...
    @interfaceNameToRegistrySR.setter
    def interfaceNameToRegistrySR(
        self,
        value: PairListBuilder | readers.PairListReader | dict[str, Any],
    ) -> None: ...
    @property
    def msgPayload(self) -> _DynamicObjectBuilder: ...
    @msgPayload.setter
    def msgPayload(self, value: common.AnyPointer) -> None: ...
    @override
    def init(
        self,
        field: Literal["interfaceNameToRegistrySR"],
        size: int | None = None,
    ) -> PairListBuilder: ...
    @override
    def as_reader(self) -> readers.CreateParamsReader: ...

class AccessInfoBuilder(_DynamicStructBuilder):
    @property
    def adminCap(self) -> _DynamicObjectBuilder: ...
    @adminCap.setter
    def adminCap(self, value: common.Capability) -> None: ...
    @property
    def serviceCaps(self) -> IdentifiableClientListBuilder: ...
    @serviceCaps.setter
    def serviceCaps(
        self,
        value: IdentifiableClientListBuilder
        | readers.IdentifiableClientListReader
        | dict[str, Any],
    ) -> None: ...
    @property
    def error(self) -> str: ...
    @error.setter
    def error(self, value: str) -> None: ...
    @override
    def init(
        self,
        field: Literal["serviceCaps"],
        size: int | None = None,
    ) -> IdentifiableClientListBuilder: ...
    @override
    def as_reader(self) -> readers.AccessInfoReader: ...

type IdInformationListBuilder = lists._IdInformationList.Builder

type IdentifiableClientListBuilder = lists._IdentifiableClientList.Builder

type PairListBuilder = lists._PairList.Builder

type TextListBuilder = lists._TextList.Builder
