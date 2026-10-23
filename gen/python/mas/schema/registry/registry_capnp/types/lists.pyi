"""List helper types for `registry.capnp`."""

from collections.abc import Iterator
from typing import Any, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
)

from mas.schema.common.common_capnp.types.builders import IdInformationBuilder
from mas.schema.common.common_capnp.types.clients import IdentifiableClient
from mas.schema.common.common_capnp.types.modules import _IdentifiableInterfaceModule
from mas.schema.common.common_capnp.types.readers import IdInformationReader
from mas.schema.registry.registry_capnp.types import builders as builders
from mas.schema.registry.registry_capnp.types import readers as readers

class _IdentifiableClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> IdentifiableClient: ...
        def __iter__(self) -> Iterator[IdentifiableClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> IdentifiableClient: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: IdentifiableClient | _IdentifiableInterfaceModule.Server,
        ) -> None: ...
        def __iter__(self) -> Iterator[IdentifiableClient]: ...

class _TextList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> str: ...
        def __iter__(self) -> Iterator[str]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> str: ...
        @override
        def __setitem__(self, index: int, value: str) -> None: ...
        def __iter__(self) -> Iterator[str]: ...

class _IdInformationList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> IdInformationReader: ...
        def __iter__(self) -> Iterator[IdInformationReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> IdInformationBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: IdInformationReader | IdInformationBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[IdInformationBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> IdInformationBuilder: ...

class _EntryList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> readers.EntryReader: ...
        def __iter__(self) -> Iterator[readers.EntryReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.EntryBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.EntryReader | builders.EntryBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[builders.EntryBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.EntryBuilder: ...
