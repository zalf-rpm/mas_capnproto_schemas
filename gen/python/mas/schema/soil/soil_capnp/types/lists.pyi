"""List helper types for `soil.capnp`."""

from collections.abc import Iterator
from typing import Any, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
)

from mas.schema.soil.soil_capnp.types import builders as builders
from mas.schema.soil.soil_capnp.types import clients as clients
from mas.schema.soil.soil_capnp.types import enums as enums
from mas.schema.soil.soil_capnp.types import modules as modules
from mas.schema.soil.soil_capnp.types import readers as readers

class _PropertyList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.PropertyReader: ...
        @override
        def __iter__(self) -> Iterator[readers.PropertyReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.PropertyBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.PropertyReader | builders.PropertyBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.PropertyBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.PropertyBuilder: ...

class _PropertyNameEnumList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> enums.PropertyNameEnum: ...
        @override
        def __iter__(self) -> Iterator[enums.PropertyNameEnum]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> enums.PropertyNameEnum: ...
        @override
        def __setitem__(self, key: int, value: enums.PropertyNameEnum) -> None: ...
        @override
        def __iter__(self) -> Iterator[enums.PropertyNameEnum]: ...

class _LayerList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.LayerReader: ...
        @override
        def __iter__(self) -> Iterator[readers.LayerReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.LayerBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.LayerReader | builders.LayerBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.LayerBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.LayerBuilder: ...

class _ProfileClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> clients.ProfileClient: ...
        @override
        def __iter__(self) -> Iterator[clients.ProfileClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> clients.ProfileClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: clients.ProfileClient | modules._ProfileInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[clients.ProfileClient]: ...
