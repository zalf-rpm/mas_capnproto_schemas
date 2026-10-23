"""List helper types for `grid.capnp`."""

from collections.abc import Iterator
from typing import Any, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
)

from mas.schema.grid.grid_capnp.types import builders as builders
from mas.schema.grid.grid_capnp.types import readers as readers

class _LocationList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> readers.LocationReader: ...
        def __iter__(self) -> Iterator[readers.LocationReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.LocationBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.LocationReader | builders.LocationBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[builders.LocationBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.LocationBuilder: ...

class _AggregationPartList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> readers.AggregationPartReader: ...
        def __iter__(self) -> Iterator[readers.AggregationPartReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.AggregationPartBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.AggregationPartReader
            | builders.AggregationPartBuilder
            | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[builders.AggregationPartBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.AggregationPartBuilder: ...
