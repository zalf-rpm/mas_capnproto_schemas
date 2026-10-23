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
        def __getitem__(self, index: int) -> readers.PropertyReader: ...
        def __iter__(self) -> Iterator[readers.PropertyReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.PropertyBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.PropertyReader | builders.PropertyBuilder | dict[str, Any],
        ) -> None: ...
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
        def __getitem__(self, index: int) -> enums.PropertyNameValue: ...
        def __iter__(self) -> Iterator[enums.PropertyNameValue]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> enums.PropertyNameValue: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: enums.PropertyNameValue | enums.PropertyNameEnum,
        ) -> None: ...
        def __iter__(self) -> Iterator[enums.PropertyNameValue]: ...

class _LayerList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> readers.LayerReader: ...
        def __iter__(self) -> Iterator[readers.LayerReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.LayerBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.LayerReader | builders.LayerBuilder | dict[str, Any],
        ) -> None: ...
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
        def __getitem__(self, index: int) -> clients.ProfileClient: ...
        def __iter__(self) -> Iterator[clients.ProfileClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> clients.ProfileClient: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: clients.ProfileClient | modules._ProfileInterfaceModule.Server,
        ) -> None: ...
        def __iter__(self) -> Iterator[clients.ProfileClient]: ...
