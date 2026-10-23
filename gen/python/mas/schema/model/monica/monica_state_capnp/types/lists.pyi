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
        def __getitem__(self, index: int) -> YieldComponentReader: ...
        def __iter__(self) -> Iterator[YieldComponentReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> YieldComponentBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: YieldComponentReader | YieldComponentBuilder | dict[str, Any],
        ) -> None: ...
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
            index: int,
        ) -> readers.DelayedNMinApplicationParamsReader: ...
        def __iter__(self) -> Iterator[readers.DelayedNMinApplicationParamsReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(
            self,
            index: int,
        ) -> builders.DelayedNMinApplicationParamsBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.DelayedNMinApplicationParamsReader
            | builders.DelayedNMinApplicationParamsBuilder
            | dict[str, Any],
        ) -> None: ...
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
        def __getitem__(self, index: int) -> readers.AOMPropertiesReader: ...
        def __iter__(self) -> Iterator[readers.AOMPropertiesReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.AOMPropertiesBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.AOMPropertiesReader
            | builders.AOMPropertiesBuilder
            | dict[str, Any],
        ) -> None: ...
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
        def __getitem__(self, index: int) -> readers.SoilLayerStateReader: ...
        def __iter__(self) -> Iterator[readers.SoilLayerStateReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.SoilLayerStateBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.SoilLayerStateReader
            | builders.SoilLayerStateBuilder
            | dict[str, Any],
        ) -> None: ...
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
        def __getitem__(self, index: int) -> readers.ACDToValueReader: ...
        def __iter__(self) -> Iterator[readers.ACDToValueReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.ACDToValueBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.ACDToValueReader
            | builders.ACDToValueBuilder
            | dict[str, Any],
        ) -> None: ...
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
        def __getitem__(self, index: int) -> readers.ACDToValueListReader: ...
        def __iter__(self) -> Iterator[readers.ACDToValueListReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> builders.ACDToValueListBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: readers.ACDToValueListReader
            | builders.ACDToValueListBuilder
            | Sequence[
                readers.ACDToValueReader | builders.ACDToValueBuilder | dict[str, Any]
            ],
        ) -> None: ...
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
        def __getitem__(self, index: int) -> str: ...
        def __iter__(self) -> Iterator[str]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> str: ...
        @override
        def __setitem__(self, index: int, value: str) -> None: ...
        def __iter__(self) -> Iterator[str]: ...

class _DateList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> DateReader: ...
        def __iter__(self) -> Iterator[DateReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, index: int) -> DateBuilder: ...
        @override
        def __setitem__(
            self,
            index: int,
            value: DateReader | DateBuilder | dict[str, Any],
        ) -> None: ...
        def __iter__(self) -> Iterator[DateBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> DateBuilder: ...
