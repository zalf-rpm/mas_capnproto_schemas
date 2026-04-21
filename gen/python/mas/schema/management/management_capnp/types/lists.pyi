"""List helper types for `management.capnp`."""

from collections.abc import Iterator
from typing import Any, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
)

from mas.schema.management.management_capnp.types import builders as builders
from mas.schema.management.management_capnp.types import readers as readers

class _SpecList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.SpecReader: ...
        @override
        def __iter__(self) -> Iterator[readers.SpecReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.SpecBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.SpecReader | builders.SpecBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.SpecBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> builders.SpecBuilder: ...

class _NutrientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.NutrientReader: ...
        @override
        def __iter__(self) -> Iterator[readers.NutrientReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.NutrientBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.NutrientReader | builders.NutrientBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.NutrientBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.NutrientBuilder: ...

class _EventList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.EventReader: ...
        @override
        def __iter__(self) -> Iterator[readers.EventReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.EventBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.EventReader | builders.EventBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.EventBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.EventBuilder: ...
