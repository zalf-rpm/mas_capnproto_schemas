"""List helper types for `soil_params.capnp`."""

from collections.abc import Iterator
from typing import Any, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
)

from mas.schema.soil.soil_params_capnp.types import modules as modules

class _DataList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(
            self,
            key: int,
        ) -> modules._SoilCharacteristicDataStructModule._DataStructModule.Reader: ...
        @override
        def __iter__(
            self,
        ) -> Iterator[
            modules._SoilCharacteristicDataStructModule._DataStructModule.Reader
        ]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(
            self,
            key: int,
        ) -> modules._SoilCharacteristicDataStructModule._DataStructModule.Builder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: modules._SoilCharacteristicDataStructModule._DataStructModule.Reader
            | modules._SoilCharacteristicDataStructModule._DataStructModule.Builder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(
            self,
        ) -> Iterator[
            modules._SoilCharacteristicDataStructModule._DataStructModule.Builder
        ]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> modules._SoilCharacteristicDataStructModule._DataStructModule.Builder: ...
