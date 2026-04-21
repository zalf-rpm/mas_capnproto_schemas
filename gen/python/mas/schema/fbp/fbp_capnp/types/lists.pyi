"""List helper types for `fbp.capnp`."""

from collections.abc import Iterator
from typing import Any, override

from capnp.lib.capnp import (
    _DynamicListBuilder,
    _DynamicListReader,
)

from mas.schema.fbp.fbp_capnp.types import builders as builders
from mas.schema.fbp.fbp_capnp.types import clients as clients
from mas.schema.fbp.fbp_capnp.types import modules as modules
from mas.schema.fbp.fbp_capnp.types import readers as readers
from mas.schema.persistence.persistence_capnp.types.builders import SturdyRefBuilder
from mas.schema.persistence.persistence_capnp.types.readers import SturdyRefReader

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

class _SturdyRefList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> SturdyRefReader: ...
        @override
        def __iter__(self) -> Iterator[SturdyRefReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> SturdyRefBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: SturdyRefReader | SturdyRefBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[SturdyRefBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> SturdyRefBuilder: ...

class _ReaderClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> clients.ReaderClient: ...
        @override
        def __iter__(self) -> Iterator[clients.ReaderClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> clients.ReaderClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: clients.ReaderClient
            | modules._ChannelInterfaceModule._ReaderInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[clients.ReaderClient]: ...

class _WriterClientList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> clients.WriterClient: ...
        @override
        def __iter__(self) -> Iterator[clients.WriterClient]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> clients.WriterClient: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: clients.WriterClient
            | modules._ChannelInterfaceModule._WriterInterfaceModule.Server,
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[clients.WriterClient]: ...

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

class _StartupInfoList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.StartupInfoReader: ...
        @override
        def __iter__(self) -> Iterator[readers.StartupInfoReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.StartupInfoBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.StartupInfoReader
            | builders.StartupInfoBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.StartupInfoBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.StartupInfoBuilder: ...

class _NameAndSRList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.NameAndSRReader: ...
        @override
        def __iter__(self) -> Iterator[readers.NameAndSRReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.NameAndSRBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.NameAndSRReader | builders.NameAndSRBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.NameAndSRBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.NameAndSRBuilder: ...

class _PortList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.PortReader: ...
        @override
        def __iter__(self) -> Iterator[readers.PortReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.PortBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.PortReader | builders.PortBuilder | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.PortBuilder]: ...
        @override
        def init(self, index: int, size: int | None = None) -> builders.PortBuilder: ...

class _ConfigEntryList:
    class Reader(_DynamicListReader):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> readers.ConfigEntryReader: ...
        @override
        def __iter__(self) -> Iterator[readers.ConfigEntryReader]: ...

    class Builder(_DynamicListBuilder):
        @override
        def __len__(self) -> int: ...
        @override
        def __getitem__(self, key: int) -> builders.ConfigEntryBuilder: ...
        @override
        def __setitem__(
            self,
            key: int,
            value: readers.ConfigEntryReader
            | builders.ConfigEntryBuilder
            | dict[str, Any],
        ) -> None: ...
        @override
        def __iter__(self) -> Iterator[builders.ConfigEntryBuilder]: ...
        @override
        def init(
            self,
            index: int,
            size: int | None = None,
        ) -> builders.ConfigEntryBuilder: ...
