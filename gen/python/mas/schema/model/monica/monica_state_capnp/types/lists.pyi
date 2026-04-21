"""List helper types for `monica_state.capnp`."""

from collections.abc import Iterator, Sequence
from typing import Any, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
)

from mas.schema.common.date_capnp.types.builders import DateBuilder
from mas.schema.common.date_capnp.types.readers import DateReader
from mas.schema.model.monica.monica_params_capnp.types.builders import (
    YieldComponentBuilder,
)
from mas.schema.model.monica.monica_params_capnp.types.readers import (
    YieldComponentReader,
)
from mas.schema.model.monica.monica_state_capnp.types import builders as builders
from mas.schema.model.monica.monica_state_capnp.types import readers as readers

class _BoolList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> bool: ...
        @override
        def __iter__(self) -> Iterator[bool]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> bool: ...
        @override
        def __setitem__(self, key: int, value: bool) -> None: ...
        @override
        def __iter__(self) -> Iterator[bool]: ...

class _Float64List:
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

class _Float64ListList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.Float64ListReader: ...
        @override
        def __iter__(self) -> Iterator[readers.Float64ListReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.Float64ListBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.Float64ListReader
            | builders.Float64ListBuilder
            | Sequence[Any],
        ) -> None: ...
        @override
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
        def __getitem__(self, key: int) -> YieldComponentReader: ...
        @override
        def __iter__(self) -> Iterator[YieldComponentReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> YieldComponentBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: YieldComponentReader | YieldComponentBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[YieldComponentBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> YieldComponentBuilder: ...

class _DelayedNMinApplicationParamsList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(
            self,
            key: int,
        ) -> readers.DelayedNMinApplicationParamsReader: ...
        @override
        def __iter__(self) -> Iterator[readers.DelayedNMinApplicationParamsReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(
            self,
            key: int,
        ) -> builders.DelayedNMinApplicationParamsBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.DelayedNMinApplicationParamsReader
            | builders.DelayedNMinApplicationParamsBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(
            self,
        ) -> Iterator[builders.DelayedNMinApplicationParamsBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.DelayedNMinApplicationParamsBuilder: ...

class _AOMPropertiesList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.AOMPropertiesReader: ...
        @override
        def __iter__(self) -> Iterator[readers.AOMPropertiesReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.AOMPropertiesBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.AOMPropertiesReader
            | builders.AOMPropertiesBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.AOMPropertiesBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.AOMPropertiesBuilder: ...

class _SoilLayerStateList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.SoilLayerStateReader: ...
        @override
        def __iter__(self) -> Iterator[readers.SoilLayerStateReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.SoilLayerStateBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.SoilLayerStateReader
            | builders.SoilLayerStateBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.SoilLayerStateBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.SoilLayerStateBuilder: ...

class _ACDToValueList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.ACDToValueReader: ...
        @override
        def __iter__(self) -> Iterator[readers.ACDToValueReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.ACDToValueBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.ACDToValueReader
            | builders.ACDToValueBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.ACDToValueBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.ACDToValueBuilder: ...

class _ACDToValueListList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.ACDToValueListReader: ...
        @override
        def __iter__(self) -> Iterator[readers.ACDToValueListReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.ACDToValueListBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.ACDToValueListReader
            | builders.ACDToValueListBuilder
            | Sequence[Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.ACDToValueListBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.ACDToValueListBuilder: ...

class _TextList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> str: ...
        @override
        def __iter__(self) -> Iterator[str]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> str: ...
        @override
        def __setitem__(self, key: int, value: str) -> None: ...
        @override
        def __iter__(self) -> Iterator[str]: ...

class _DateList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> DateReader: ...
        @override
        def __iter__(self) -> Iterator[DateReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> DateBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: DateReader | DateBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[DateBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> DateBuilder: ...
