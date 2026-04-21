"""Builder helper types for `fbp.capnp`."""

from typing import Any, Literal, overload, override

from capnp.lib.capnp import (
    _DynamicObjectBuilder,
    _DynamicObjectReader,
    _DynamicStructBuilder,
)

from mas.schema.common.common_capnp.types.builders import (
    IdInformationBuilder,
    StructuredTextBuilder,
    ValueBuilder,
)
from mas.schema.common.common_capnp.types.readers import (
    IdInformationReader,
    StructuredTextReader,
    ValueReader,
)
from mas.schema.fbp.fbp_capnp.types import clients as clients
from mas.schema.fbp.fbp_capnp.types import common as common
from mas.schema.fbp.fbp_capnp.types import enums as enums
from mas.schema.fbp.fbp_capnp.types import lists as lists
from mas.schema.fbp.fbp_capnp.types import modules as modules
from mas.schema.fbp.fbp_capnp.types import readers as readers
from mas.schema.persistence.persistence_capnp.types.builders import SturdyRefBuilder
from mas.schema.persistence.persistence_capnp.types.readers import SturdyRefReader

class KVBuilder(_DynamicStructBuilder):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str) -> None: ...
    @property
    def desc(self) -> str: ...
    @desc.setter
    def desc(self, value: str) -> None: ...
    @property
    def value(self) -> _DynamicObjectBuilder: ...
    @value.setter
    def value(self, value: common.AnyPointer) -> None: ...
    @override
    def as_reader(self) -> readers.KVReader: ...

class IPBuilder(_DynamicStructBuilder):
    @property
    def attributes(self) -> KVListBuilder: ...
    @attributes.setter
    def attributes(
        self,
        value: KVListBuilder | readers.KVListReader | dict[str, Any],
    ) -> None: ...
    @property
    def content(self) -> _DynamicObjectBuilder: ...
    @content.setter
    def content(self, value: common.AnyPointer) -> None: ...
    @property
    def type(self) -> enums.IPTypeEnum: ...
    @type.setter
    def type(self, value: enums.IPTypeEnum) -> None: ...
    @override
    def init(
        self,
        field: Literal["attributes"],
        size: int | None = None,
    ) -> KVListBuilder: ...
    @override
    def as_reader(self) -> readers.IPReader: ...

class IIPBuilder(_DynamicStructBuilder):
    @property
    def content(self) -> _DynamicObjectBuilder: ...
    @content.setter
    def content(self, value: common.AnyPointer) -> None: ...
    @override
    def as_reader(self) -> readers.IIPReader: ...

class MsgBuilder(_DynamicStructBuilder):
    @property
    def value(self) -> _DynamicObjectReader: ...
    @value.setter
    def value(self, value: common.AnyPointer) -> None: ...
    @property
    def done(self) -> None: ...
    @done.setter
    def done(self, value: None) -> None: ...
    @property
    def noMsg(self) -> None: ...
    @noMsg.setter
    def noMsg(self, value: None) -> None: ...
    @override
    def which(self) -> Literal["value", "done", "noMsg"]: ...
    @override
    def as_reader(self) -> readers.MsgReader: ...

class StartupInfoBuilder(_DynamicStructBuilder):
    @property
    def bufferSize(self) -> int: ...
    @bufferSize.setter
    def bufferSize(self, value: int) -> None: ...
    @property
    def closeSemantics(self) -> enums.ChannelCloseSemanticsEnum: ...
    @closeSemantics.setter
    def closeSemantics(self, value: enums.ChannelCloseSemanticsEnum) -> None: ...
    @property
    def channelSR(self) -> SturdyRefBuilder: ...
    @channelSR.setter
    def channelSR(
        self,
        value: SturdyRefBuilder | SturdyRefReader | dict[str, Any],
    ) -> None: ...
    @property
    def readerSRs(self) -> SturdyRefListBuilder: ...
    @readerSRs.setter
    def readerSRs(
        self,
        value: SturdyRefListBuilder | readers.SturdyRefListReader | dict[str, Any],
    ) -> None: ...
    @property
    def writerSRs(self) -> SturdyRefListBuilder: ...
    @writerSRs.setter
    def writerSRs(
        self,
        value: SturdyRefListBuilder | readers.SturdyRefListReader | dict[str, Any],
    ) -> None: ...
    @property
    def channel(self) -> clients.ChannelClient: ...
    @channel.setter
    def channel(
        self,
        value: clients.ChannelClient | modules._ChannelInterfaceModule.Server,
    ) -> None: ...
    @property
    def readers(self) -> ReaderClientListBuilder: ...
    @readers.setter
    def readers(
        self,
        value: ReaderClientListBuilder
        | readers.ReaderClientListReader
        | dict[str, Any],
    ) -> None: ...
    @property
    def writers(self) -> WriterClientListBuilder: ...
    @writers.setter
    def writers(
        self,
        value: WriterClientListBuilder
        | readers.WriterClientListReader
        | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["channelSR"],
        size: int | None = None,
    ) -> SturdyRefBuilder: ...
    @overload
    def init(
        self,
        field: Literal["readerSRs"],
        size: int | None = None,
    ) -> SturdyRefListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["writerSRs"],
        size: int | None = None,
    ) -> SturdyRefListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["readers"],
        size: int | None = None,
    ) -> ReaderClientListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["writers"],
        size: int | None = None,
    ) -> WriterClientListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.StartupInfoReader: ...

class StatsBuilder(_DynamicStructBuilder):
    @property
    def noOfWaitingWriters(self) -> int: ...
    @noOfWaitingWriters.setter
    def noOfWaitingWriters(self, value: int) -> None: ...
    @property
    def noOfWaitingReaders(self) -> int: ...
    @noOfWaitingReaders.setter
    def noOfWaitingReaders(self, value: int) -> None: ...
    @property
    def noOfIpsInQueue(self) -> int: ...
    @noOfIpsInQueue.setter
    def noOfIpsInQueue(self, value: int) -> None: ...
    @property
    def totalNoOfIpsReceived(self) -> int: ...
    @totalNoOfIpsReceived.setter
    def totalNoOfIpsReceived(self, value: int) -> None: ...
    @property
    def timestamp(self) -> str: ...
    @timestamp.setter
    def timestamp(self, value: str) -> None: ...
    @property
    def updateIntervalInMs(self) -> int: ...
    @updateIntervalInMs.setter
    def updateIntervalInMs(self, value: int) -> None: ...
    @override
    def as_reader(self) -> readers.StatsReader: ...

class ParamsBuilder(_DynamicStructBuilder):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def noOfChannels(self) -> int: ...
    @noOfChannels.setter
    def noOfChannels(self, value: int) -> None: ...
    @property
    def noOfReaders(self) -> int: ...
    @noOfReaders.setter
    def noOfReaders(self, value: int) -> None: ...
    @property
    def noOfWriters(self) -> int: ...
    @noOfWriters.setter
    def noOfWriters(self, value: int) -> None: ...
    @property
    def readerSrts(self) -> TextListBuilder: ...
    @readerSrts.setter
    def readerSrts(
        self,
        value: TextListBuilder | readers.TextListReader | dict[str, Any],
    ) -> None: ...
    @property
    def writerSrts(self) -> TextListBuilder: ...
    @writerSrts.setter
    def writerSrts(
        self,
        value: TextListBuilder | readers.TextListReader | dict[str, Any],
    ) -> None: ...
    @property
    def bufferSize(self) -> int: ...
    @bufferSize.setter
    def bufferSize(self, value: int) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["readerSrts"],
        size: int | None = None,
    ) -> TextListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["writerSrts"],
        size: int | None = None,
    ) -> TextListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.ParamsReader: ...

class NameAndSRBuilder(_DynamicStructBuilder):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def sr(self) -> SturdyRefBuilder: ...
    @sr.setter
    def sr(
        self,
        value: SturdyRefBuilder | SturdyRefReader | dict[str, Any],
    ) -> None: ...
    @property
    def srs(self) -> SturdyRefListBuilder: ...
    @srs.setter
    def srs(
        self,
        value: SturdyRefListBuilder | readers.SturdyRefListReader | dict[str, Any],
    ) -> None: ...
    @override
    def which(self) -> Literal["sr", "srs"]: ...
    @override
    @overload
    def init(
        self,
        field: Literal["sr"],
        size: int | None = None,
    ) -> SturdyRefBuilder: ...
    @overload
    def init(
        self,
        field: Literal["srs"],
        size: int | None = None,
    ) -> SturdyRefListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.NameAndSRReader: ...

class PortInfosBuilder(_DynamicStructBuilder):
    @property
    def inPorts(self) -> NameAndSRListBuilder: ...
    @inPorts.setter
    def inPorts(
        self,
        value: NameAndSRListBuilder | readers.NameAndSRListReader | dict[str, Any],
    ) -> None: ...
    @property
    def outPorts(self) -> NameAndSRListBuilder: ...
    @outPorts.setter
    def outPorts(
        self,
        value: NameAndSRListBuilder | readers.NameAndSRListReader | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["inPorts"],
        size: int | None = None,
    ) -> NameAndSRListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["outPorts"],
        size: int | None = None,
    ) -> NameAndSRListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.PortInfosReader: ...

class PortBuilder(_DynamicStructBuilder):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def contentType(self) -> str: ...
    @contentType.setter
    def contentType(self, value: str) -> None: ...
    @property
    def type(self) -> enums.ComponentPortPortTypeEnum: ...
    @type.setter
    def type(self, value: enums.ComponentPortPortTypeEnum) -> None: ...
    @property
    def desc(self) -> str: ...
    @desc.setter
    def desc(self, value: str) -> None: ...
    @override
    def as_reader(self) -> readers.PortReader: ...

class ConfigEntryBuilder(_DynamicStructBuilder):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def val(self) -> ValueBuilder: ...
    @val.setter
    def val(self, value: ValueBuilder | ValueReader | dict[str, Any]) -> None: ...
    @override
    def init(self, field: Literal["val"], size: int | None = None) -> ValueBuilder: ...
    @override
    def as_reader(self) -> readers.ConfigEntryReader: ...

class ComponentFactoryBuilder(_DynamicStructBuilder):
    @property
    def none(self) -> None: ...
    @none.setter
    def none(self, value: None) -> None: ...
    @property
    def runnable(self) -> clients.RunnableFactoryClient: ...
    @runnable.setter
    def runnable(
        self,
        value: clients.RunnableFactoryClient
        | modules._RunnableInterfaceModule._FactoryInterfaceModule.Server,
    ) -> None: ...
    @property
    def process(self) -> clients.ProcessFactoryClient: ...
    @process.setter
    def process(
        self,
        value: clients.ProcessFactoryClient
        | modules._ProcessInterfaceModule._FactoryInterfaceModule.Server,
    ) -> None: ...
    @override
    def which(self) -> Literal["none", "runnable", "process"]: ...
    @override
    def as_reader(self) -> readers.ComponentFactoryReader: ...

class ComponentBuilder(_DynamicStructBuilder):
    @property
    def info(self) -> IdInformationBuilder: ...
    @info.setter
    def info(
        self,
        value: IdInformationBuilder | IdInformationReader | dict[str, Any],
    ) -> None: ...
    @property
    def type(self) -> enums.ComponentComponentTypeEnum: ...
    @type.setter
    def type(self, value: enums.ComponentComponentTypeEnum) -> None: ...
    @property
    def inPorts(self) -> PortListBuilder: ...
    @inPorts.setter
    def inPorts(
        self,
        value: PortListBuilder | readers.PortListReader | dict[str, Any],
    ) -> None: ...
    @property
    def outPorts(self) -> PortListBuilder: ...
    @outPorts.setter
    def outPorts(
        self,
        value: PortListBuilder | readers.PortListReader | dict[str, Any],
    ) -> None: ...
    @property
    def defaultConfig(self) -> StructuredTextBuilder: ...
    @defaultConfig.setter
    def defaultConfig(
        self,
        value: StructuredTextBuilder | StructuredTextReader | dict[str, Any],
    ) -> None: ...
    @property
    def factory(self) -> ComponentFactoryBuilder: ...
    @factory.setter
    def factory(
        self,
        value: ComponentFactoryBuilder
        | readers.ComponentFactoryReader
        | dict[str, Any],
    ) -> None: ...
    @override
    @overload
    def init(
        self,
        field: Literal["info"],
        size: int | None = None,
    ) -> IdInformationBuilder: ...
    @overload
    def init(
        self,
        field: Literal["defaultConfig"],
        size: int | None = None,
    ) -> StructuredTextBuilder: ...
    @overload
    def init(
        self,
        field: Literal["factory"],
        size: int | None = None,
    ) -> ComponentFactoryBuilder: ...
    @overload
    def init(
        self,
        field: Literal["inPorts"],
        size: int | None = None,
    ) -> PortListBuilder: ...
    @overload
    def init(
        self,
        field: Literal["outPorts"],
        size: int | None = None,
    ) -> PortListBuilder: ...
    @overload
    def init(self, field: str, size: int | None = None) -> Any: ...
    @override
    def as_reader(self) -> readers.ComponentReader: ...

type ConfigEntryListBuilder = lists._ConfigEntryList.Builder

type KVListBuilder = lists._KVList.Builder

type NameAndSRListBuilder = lists._NameAndSRList.Builder

type PortListBuilder = lists._PortList.Builder

type ReaderClientListBuilder = lists._ReaderClientList.Builder

type StartupInfoListBuilder = lists._StartupInfoList.Builder

type SturdyRefListBuilder = lists._SturdyRefList.Builder

type TextListBuilder = lists._TextList.Builder

type WriterClientListBuilder = lists._WriterClientList.Builder
