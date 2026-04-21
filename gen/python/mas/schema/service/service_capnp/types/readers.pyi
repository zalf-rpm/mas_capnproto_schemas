"""Reader helper types for `service.capnp`."""

from collections.abc import Callable
from typing import override

from capnp.lib.capnp import (
    _DynamicObjectReader,
    _DynamicStructReader,
)

from mas.schema.service.service_capnp.types import builders as builders
from mas.schema.service.service_capnp.types import lists as lists

class CreateParamsReader(_DynamicStructReader):
    @property
    def timeoutSeconds(self) -> int: ...
    @property
    def interfaceNameToRegistrySR(self) -> PairListReader: ...
    @property
    def msgPayload(self) -> _DynamicObjectReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.CreateParamsBuilder: ...

class AccessInfoReader(_DynamicStructReader):
    @property
    def adminCap(self) -> _DynamicObjectReader: ...
    @property
    def serviceCaps(self) -> IdentifiableClientListReader: ...
    @property
    def error(self) -> str: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.AccessInfoBuilder: ...

type IdInformationListReader = lists._IdInformationList.Reader

type IdentifiableClientListReader = lists._IdentifiableClientList.Reader

type PairListReader = lists._PairList.Reader

type TextListReader = lists._TextList.Reader
