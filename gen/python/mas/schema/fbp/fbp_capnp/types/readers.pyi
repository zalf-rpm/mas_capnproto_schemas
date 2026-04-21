"""Reader helper types for `fbp.capnp`."""

from collections.abc import Callable
from typing import Literal, override

from capnp.lib.capnp import (
    _DynamicObjectReader,
    _DynamicStructReader,
)

from mas.schema.common.common_capnp.types.readers import (
    IdInformationReader,
    StructuredTextReader,
    ValueReader,
)
from mas.schema.fbp.fbp_capnp.types import builders as builders
from mas.schema.fbp.fbp_capnp.types import clients as clients
from mas.schema.fbp.fbp_capnp.types import enums as enums
from mas.schema.fbp.fbp_capnp.types import lists as lists
from mas.schema.persistence.persistence_capnp.types.readers import SturdyRefReader

class KVReader(_DynamicStructReader):
    @property
    def key(self) -> str: ...
    @property
    def desc(self) -> str: ...
    @property
    def value(self) -> _DynamicObjectReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.KVBuilder: ...

class IPReader(_DynamicStructReader):
    @property
    def attributes(self) -> KVListReader: ...
    @property
    def content(self) -> _DynamicObjectReader: ...
    @property
    def type(self) -> enums.IPTypeEnum: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.IPBuilder: ...

class IIPReader(_DynamicStructReader):
    @property
    def content(self) -> _DynamicObjectReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.IIPBuilder: ...

class MsgReader(_DynamicStructReader):
    @property
    def value(self) -> _DynamicObjectReader: ...
    @property
    def done(self) -> None: ...
    @property
    def noMsg(self) -> None: ...
    @override
    def which(self) -> Literal["value", "done", "noMsg"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.MsgBuilder: ...

class StartupInfoReader(_DynamicStructReader):
    @property
    def bufferSize(self) -> int: ...
    @property
    def closeSemantics(self) -> enums.ChannelCloseSemanticsEnum: ...
    @property
    def channelSR(self) -> SturdyRefReader: ...
    @property
    def readerSRs(self) -> SturdyRefListReader: ...
    @property
    def writerSRs(self) -> SturdyRefListReader: ...
    @property
    def channel(self) -> clients.ChannelClient: ...
    @property
    def readers(self) -> ReaderClientListReader: ...
    @property
    def writers(self) -> WriterClientListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.StartupInfoBuilder: ...

class StatsReader(_DynamicStructReader):
    @property
    def noOfWaitingWriters(self) -> int: ...
    @property
    def noOfWaitingReaders(self) -> int: ...
    @property
    def noOfIpsInQueue(self) -> int: ...
    @property
    def totalNoOfIpsReceived(self) -> int: ...
    @property
    def timestamp(self) -> str: ...
    @property
    def updateIntervalInMs(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.StatsBuilder: ...

class ParamsReader(_DynamicStructReader):
    @property
    def name(self) -> str: ...
    @property
    def noOfChannels(self) -> int: ...
    @property
    def noOfReaders(self) -> int: ...
    @property
    def noOfWriters(self) -> int: ...
    @property
    def readerSrts(self) -> TextListReader: ...
    @property
    def writerSrts(self) -> TextListReader: ...
    @property
    def bufferSize(self) -> int: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ParamsBuilder: ...

class NameAndSRReader(_DynamicStructReader):
    @property
    def name(self) -> str: ...
    @property
    def sr(self) -> SturdyRefReader: ...
    @property
    def srs(self) -> SturdyRefListReader: ...
    @override
    def which(self) -> Literal["sr", "srs"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.NameAndSRBuilder: ...

class PortInfosReader(_DynamicStructReader):
    @property
    def inPorts(self) -> NameAndSRListReader: ...
    @property
    def outPorts(self) -> NameAndSRListReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.PortInfosBuilder: ...

class PortReader(_DynamicStructReader):
    @property
    def name(self) -> str: ...
    @property
    def contentType(self) -> str: ...
    @property
    def type(self) -> enums.ComponentPortPortTypeEnum: ...
    @property
    def desc(self) -> str: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.PortBuilder: ...

class ConfigEntryReader(_DynamicStructReader):
    @property
    def name(self) -> str: ...
    @property
    def val(self) -> ValueReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ConfigEntryBuilder: ...

class ComponentFactoryReader(_DynamicStructReader):
    @property
    def none(self) -> None: ...
    @property
    def runnable(self) -> clients.RunnableFactoryClient: ...
    @property
    def process(self) -> clients.ProcessFactoryClient: ...
    @override
    def which(self) -> Literal["none", "runnable", "process"]: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ComponentFactoryBuilder: ...

class ComponentReader(_DynamicStructReader):
    @property
    def info(self) -> IdInformationReader: ...
    @property
    def type(self) -> enums.ComponentComponentTypeEnum: ...
    @property
    def inPorts(self) -> PortListReader: ...
    @property
    def outPorts(self) -> PortListReader: ...
    @property
    def defaultConfig(self) -> StructuredTextReader: ...
    @property
    def factory(self) -> ComponentFactoryReader: ...
    @override
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
    ) -> builders.ComponentBuilder: ...

type ConfigEntryListReader = lists._ConfigEntryList.Reader

type KVListReader = lists._KVList.Reader

type NameAndSRListReader = lists._NameAndSRList.Reader

type PortListReader = lists._PortList.Reader

type ReaderClientListReader = lists._ReaderClientList.Reader

type StartupInfoListReader = lists._StartupInfoList.Reader

type SturdyRefListReader = lists._SturdyRefList.Reader

type TextListReader = lists._TextList.Reader

type WriterClientListReader = lists._WriterClientList.Reader
