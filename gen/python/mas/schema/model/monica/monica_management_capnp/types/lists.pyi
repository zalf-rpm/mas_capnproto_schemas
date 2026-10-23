"""List helper types for `monica_management.capnp`."""

from collections.abc import Iterator
from typing import Any, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
)

from mas.schema.model.monica.monica_management_capnp.types import builders as builders
from mas.schema.model.monica.monica_management_capnp.types import readers as readers

class _KVList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> readers.KVReader: ...
        def __iter__(self) -> Iterator[readers.KVReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.KVBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.KVReader | builders.KVBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[builders.KVBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> builders.KVBuilder: ...

class _SpecList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> readers.SpecReader: ...
        def __iter__(self) -> Iterator[readers.SpecReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.SpecBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.SpecReader | builders.SpecBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[builders.SpecBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> builders.SpecBuilder: ...

class _EventList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> readers.EventReader: ...
        def __iter__(self) -> Iterator[readers.EventReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.EventBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.EventReader | builders.EventBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[builders.EventBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.EventBuilder: ...
