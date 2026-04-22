"""Reader helper types for `registry.capnp`."""

from collections.abc import Callable
from typing import override

from capnp.lib.capnp import (
    _DynamicStructReader,
)

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.persistence.persistence_capnp.types.clients import RestorerClient
from mas.schema.persistence.persistence_capnp.types.readers import (
    VatIdReader,
)
from mas.schema.registry.registry_capnp.types import builders as builders
from mas.schema.registry.registry_capnp.types import lists as lists

class EntryReader(_DynamicStructReader):
    @property
    def categoryId(self) -> str: ...
    @property
    def ref(self) -> IdentifiableClient: ...
    @property
    def name(self) -> str: ...
    @property
    def id(self) -> str: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.EntryBuilder: ...

class CrossDomainRestoreReader(_DynamicStructReader):
    @property
    def vatId(self) -> VatIdReader: ...
    @property
    def restorer(self) -> RestorerClient: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.CrossDomainRestoreBuilder: ...

class RegParamsReader(_DynamicStructReader):
    @property
    def cap(self) -> IdentifiableClient: ...
    @property
    def regName(self) -> str: ...
    @property
    def categoryId(self) -> str: ...
    @property
    def xDomain(self) -> CrossDomainRestoreReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.RegParamsBuilder: ...

type EntryListReader = lists._EntryList.Reader

type IdInformationListReader = lists._IdInformationList.Reader

type IdentifiableClientListReader = lists._IdentifiableClientList.Reader

type TextListReader = lists._TextList.Reader
