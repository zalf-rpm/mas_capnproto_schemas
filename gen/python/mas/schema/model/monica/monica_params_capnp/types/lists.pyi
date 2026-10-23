"""List helper types for `monica_params.capnp`."""

from collections.abc import Iterator, Sequence
from typing import Any, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
)

from mas.schema.model.monica.monica_params_capnp.types import builders as builders
from mas.schema.model.monica.monica_params_capnp.types import readers as readers

class _Float64List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> float: ...
        def __iter__(self) -> Iterator[float]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> float: ...
        @override
        def __setitem__(self, index: int, value: float) -> None: ...
        def __iter__(self) -> Iterator[float]: ...

class _BoolList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> bool: ...
        def __iter__(self) -> Iterator[bool]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> bool: ...
        @override
        def __setitem__(self, index: int, value: bool) -> None: ...
        def __iter__(self) -> Iterator[bool]: ...

class _Float64ListList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> readers.Float64ListReader: ...
        def __iter__(self) -> Iterator[readers.Float64ListReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.Float64ListBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.Float64ListReader
            | builders.Float64ListBuilder
            | Sequence[float],
        ) -> None: ...
        def __iter__(self) -> Iterator[builders.Float64ListBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.Float64ListBuilder: ...

class _YieldComponentList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> readers.YieldComponentReader: ...
        def __iter__(self) -> Iterator[readers.YieldComponentReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.YieldComponentBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.YieldComponentReader
            | builders.YieldComponentBuilder
            | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[builders.YieldComponentBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.YieldComponentBuilder: ...

class _SoilParametersList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> readers.SoilParametersReader: ...
        def __iter__(self) -> Iterator[readers.SoilParametersReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.SoilParametersBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.SoilParametersReader
            | builders.SoilParametersBuilder
            | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[builders.SoilParametersBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.SoilParametersBuilder: ...

class _YearToValueList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> readers.YearToValueReader: ...
        def __iter__(self) -> Iterator[readers.YearToValueReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.YearToValueBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.YearToValueReader
            | builders.YearToValueBuilder
            | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[builders.YearToValueBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.YearToValueBuilder: ...

class _DateToValueList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> readers.DateToValueReader: ...
        def __iter__(self) -> Iterator[readers.DateToValueReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.DateToValueBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.DateToValueReader
            | builders.DateToValueBuilder
            | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[builders.DateToValueBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.DateToValueBuilder: ...

class _SpeciesIdToEmissionList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> readers.SpeciesIdToEmissionReader: ...
        def __iter__(self) -> Iterator[readers.SpeciesIdToEmissionReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.SpeciesIdToEmissionBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.SpeciesIdToEmissionReader
            | builders.SpeciesIdToEmissionBuilder
            | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[builders.SpeciesIdToEmissionBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.SpeciesIdToEmissionBuilder: ...
