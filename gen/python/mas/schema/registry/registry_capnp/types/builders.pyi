"""Builder helper types for `registry.capnp`."""

from typing import Any, Literal, override

from capnp.lib.capnp import (
    _DynamicStructBuilder,
)

from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.persistence.persistence_capnp.types.builders import VatIdBuilder
from mas.schema.persistence.persistence_capnp.types.clients import RestorerClient
from mas.schema.persistence.persistence_capnp.types.modules import (
    _RestorerInterfaceModule,
)
from mas.schema.persistence.persistence_capnp.types.readers import VatIdReader
from mas.schema.registry.registry_capnp.types import lists as lists
from mas.schema.registry.registry_capnp.types import readers as readers

class EntryBuilder(_DynamicStructBuilder):
    @property
    def categoryId(self) -> str: ...
    @categoryId.setter
    def categoryId(self, value: str) -> None: ...
    @property
    def ref(self) -> IdentifiableClient: ...
    @ref.setter
    def ref(
        self,
        value: IdentifiableClient | _IdentifiableInterfaceModule.Server,
    ) -> None: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> None: ...
    @override
    def as_reader(self) -> readers.EntryReader: ...

class CrossDomainRestoreBuilder(_DynamicStructBuilder):
    @property
    def vatId(self) -> VatIdBuilder: ...
    @vatId.setter
    def vatId(self, value: VatIdBuilder | VatIdReader | dict[str, Any]) -> None: ...
    @property
    def restorer(self) -> RestorerClient: ...
    @restorer.setter
    def restorer(
        self,
        value: RestorerClient | _RestorerInterfaceModule.Server,
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["vatId"],
        size: int | None = None,
    ) -> VatIdBuilder: ...
    @override
    def as_reader(self) -> readers.CrossDomainRestoreReader: ...

class RegParamsBuilder(_DynamicStructBuilder):
    @property
    def cap(self) -> IdentifiableClient: ...
    @cap.setter
    def cap(
        self,
        value: IdentifiableClient | _IdentifiableInterfaceModule.Server,
    ) -> None: ...
    @property
    def regName(self) -> str: ...
    @regName.setter
    def regName(self, value: str) -> None: ...
    @property
    def categoryId(self) -> str: ...
    @categoryId.setter
    def categoryId(self, value: str) -> None: ...
    @property
    def xDomain(self) -> CrossDomainRestoreBuilder: ...
    @xDomain.setter
    def xDomain(
        self,
        value: CrossDomainRestoreBuilder
        | readers.CrossDomainRestoreReader
        | dict[str, Any],
    ) -> None: ...
    @override
    def init(
        self,
        field: Literal["xDomain"],
        size: int | None = None,
    ) -> CrossDomainRestoreBuilder: ...
    @override
    def as_reader(self) -> readers.RegParamsReader: ...

type EntryListBuilder = lists._EntryList.Builder

type IdInformationListBuilder = lists._IdInformationList.Builder

type IdentifiableClientListBuilder = lists._IdentifiableClientList.Builder

type TextListBuilder = lists._TextList.Builder
