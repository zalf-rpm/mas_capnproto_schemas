"""List helper types for `yieldstat.capnp`."""

from collections.abc import Iterator
from typing import Any, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
)

from mas.schema.model.yieldstat.yieldstat_capnp.types import builders as builders
from mas.schema.model.yieldstat.yieldstat_capnp.types import readers as readers

class _ResultToValueList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.ResultToValueReader: ...
        @override
        def __iter__(self) -> Iterator[readers.ResultToValueReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.ResultToValueBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.ResultToValueReader
            | builders.ResultToValueBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.ResultToValueBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.ResultToValueBuilder: ...

class _YearToResultList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.YearToResultReader: ...
        @override
        def __iter__(self) -> Iterator[readers.YearToResultReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.YearToResultBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.YearToResultReader
            | builders.YearToResultBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.YearToResultBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.YearToResultBuilder: ...
