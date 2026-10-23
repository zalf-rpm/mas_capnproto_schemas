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
        def __getitem__(self, index: int) -> readers.ResultToValueReader: ...
        def __iter__(self) -> Iterator[readers.ResultToValueReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.ResultToValueBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.ResultToValueReader
            | builders.ResultToValueBuilder
            | dict[str, Any],
        ) -> None: ...
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
        def __getitem__(self, index: int) -> readers.YearToResultReader: ...
        def __iter__(self) -> Iterator[readers.YearToResultReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.YearToResultBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.YearToResultReader
            | builders.YearToResultBuilder
            | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[builders.YearToResultBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.YearToResultBuilder: ...
