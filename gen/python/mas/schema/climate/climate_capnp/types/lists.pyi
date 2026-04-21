"""List helper types for `climate.capnp`."""

from collections.abc import Iterator, Sequence
from typing import Any, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
)

from mas.schema.climate.climate_capnp.types import builders as builders
from mas.schema.climate.climate_capnp.types import clients as clients
from mas.schema.climate.climate_capnp.types import enums as enums
from mas.schema.climate.climate_capnp.types import modules as modules
from mas.schema.climate.climate_capnp.types import readers as readers
from mas.schema.common.common_capnp.types.builders import (
    IdInformationBuilder,
    PairBuilder,
)
from mas.schema.common.common_capnp.types.readers import IdInformationReader, PairReader

class _IdInformationList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdInformationReader: ...
        @override
        def __iter__(self) -> Iterator[IdInformationReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> IdInformationBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: IdInformationReader | IdInformationBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[IdInformationBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> IdInformationBuilder: ...

class _PairList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> PairReader: ...
        @override
        def __iter__(self) -> Iterator[PairReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> PairBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: PairReader | PairBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[PairBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> PairBuilder: ...

class _EntryList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.EntryReader: ...
        @override
        def __iter__(self) -> Iterator[readers.EntryReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.EntryBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.EntryReader | builders.EntryBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.EntryBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.EntryBuilder: ...

class _ElementEnumList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> enums.ElementEnum: ...
        @override
        def __iter__(self) -> Iterator[enums.ElementEnum]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> enums.ElementEnum: ...
        @override
        def __setitem__(self, key: int, value: enums.ElementEnum) -> None: ...
        @override
        def __iter__(self) -> Iterator[enums.ElementEnum]: ...

class _Float32List:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> float: ...
        @override
        def __iter__(self) -> Iterator[float]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> float: ...
        @override
        def __setitem__(self, key: int, value: float) -> None: ...
        @override
        def __iter__(self) -> Iterator[float]: ...

class _Float32ListList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.Float32ListReader: ...
        @override
        def __iter__(self) -> Iterator[readers.Float32ListReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.Float32ListBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.Float32ListReader
            | builders.Float32ListBuilder
            | Sequence[Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.Float32ListBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.Float32ListBuilder: ...

class _KVList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.KVReader: ...
        @override
        def __iter__(self) -> Iterator[readers.KVReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.KVBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.KVReader | builders.KVBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.KVBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> builders.KVBuilder: ...

class _LocationList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.LocationReader: ...
        @override
        def __iter__(self) -> Iterator[readers.LocationReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.LocationBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.LocationReader | builders.LocationBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.LocationBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.LocationBuilder: ...

class _MetaPlusDataList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.MetaPlusDataReader: ...
        @override
        def __iter__(self) -> Iterator[readers.MetaPlusDataReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.MetaPlusDataBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.MetaPlusDataReader
            | builders.MetaPlusDataBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.MetaPlusDataBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.MetaPlusDataBuilder: ...

class _DatasetClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> clients.DatasetClient: ...
        @override
        def __iter__(self) -> Iterator[clients.DatasetClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> clients.DatasetClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: clients.DatasetClient | modules._DatasetInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[clients.DatasetClient]: ...

class _AlteredList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.AlteredReader: ...
        @override
        def __iter__(self) -> Iterator[readers.AlteredReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.AlteredBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.AlteredReader | builders.AlteredBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.AlteredBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.AlteredBuilder: ...
