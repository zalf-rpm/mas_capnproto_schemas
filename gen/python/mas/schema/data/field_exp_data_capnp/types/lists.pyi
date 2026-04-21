"""List helper types for `field_exp_data.capnp`."""

from collections.abc import Iterator
from typing import Any, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
)

from mas.schema.data.field_exp_data_capnp.types import builders as builders
from mas.schema.data.field_exp_data_capnp.types import readers as readers

class _PlotList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.PlotReader: ...
        @override
        def __iter__(self) -> Iterator[readers.PlotReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.PlotBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.PlotReader | builders.PlotBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.PlotBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> builders.PlotBuilder: ...

class _InitialConditionsLayerList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.InitialConditionsLayerReader: ...
        @override
        def __iter__(self) -> Iterator[readers.InitialConditionsLayerReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.InitialConditionsLayerBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.InitialConditionsLayerReader
            | builders.InitialConditionsLayerBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.InitialConditionsLayerBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.InitialConditionsLayerBuilder: ...

class _PlantingEventList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.PlantingEventReader: ...
        @override
        def __iter__(self) -> Iterator[readers.PlantingEventReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.PlantingEventBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.PlantingEventReader
            | builders.PlantingEventBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.PlantingEventBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.PlantingEventBuilder: ...

class _HarvestEventList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.HarvestEventReader: ...
        @override
        def __iter__(self) -> Iterator[readers.HarvestEventReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.HarvestEventBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.HarvestEventReader
            | builders.HarvestEventBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.HarvestEventBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.HarvestEventBuilder: ...

class _IrrigationEventList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.IrrigationEventReader: ...
        @override
        def __iter__(self) -> Iterator[readers.IrrigationEventReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.IrrigationEventBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.IrrigationEventReader
            | builders.IrrigationEventBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.IrrigationEventBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.IrrigationEventBuilder: ...

class _FertilizerEventList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.FertilizerEventReader: ...
        @override
        def __iter__(self) -> Iterator[readers.FertilizerEventReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.FertilizerEventBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.FertilizerEventReader
            | builders.FertilizerEventBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.FertilizerEventBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.FertilizerEventBuilder: ...

class _EnvironmentModificationList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.EnvironmentModificationReader: ...
        @override
        def __iter__(self) -> Iterator[readers.EnvironmentModificationReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.EnvironmentModificationBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.EnvironmentModificationReader
            | builders.EnvironmentModificationBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.EnvironmentModificationBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.EnvironmentModificationBuilder: ...

class _TreatmentList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.TreatmentReader: ...
        @override
        def __iter__(self) -> Iterator[readers.TreatmentReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.TreatmentBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.TreatmentReader | builders.TreatmentBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.TreatmentBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.TreatmentBuilder: ...
