import asyncio
import contextlib
import enum
from collections.abc import Awaitable, Callable, Iterator, Sequence
from types import ModuleType
from typing import IO, Any, Literal, overload

from mas.schema.climate import climate_capnp
from mas.schema.cluster import cluster_admin_service_capnp
from mas.schema.common import common_capnp, date_capnp
from mas.schema.config import config_capnp
from mas.schema.crop import crop_capnp
from mas.schema.dakis.modam import modam_capnp
from mas.schema.data import field_exp_data_capnp
from mas.schema.fbp import fbp_capnp
from mas.schema.geo import geo_capnp
from mas.schema.grid import grid_capnp
from mas.schema.jobs import jobs_capnp
from mas.schema.management import management_capnp
from mas.schema.model import model_capnp
from mas.schema.model.agmip import agmip_capnp
from mas.schema.model.monica import (
    monica_management_capnp,
    monica_params_capnp,
    monica_state_capnp,
    sim_setup_capnp,
)
from mas.schema.model.weberest import web_berest_data_import_capnp
from mas.schema.model.yieldstat import yieldstat_capnp
from mas.schema.persistence import persistence_capnp
from mas.schema.registry import registry_capnp
from mas.schema.service import service_capnp
from mas.schema.soil import soil_capnp, soil_params_capnp
from mas.schema.storage import storage_capnp

# Generated imports for project-specific types
from mas.schema.test import a_capnp, x_capnp

class KjException(Exception):
    """KjException is a wrapper of the internal C++ exception type.

    There is an enum named `Type` listed below, and a bunch of fields.
    """

    class Type:
        FAILED: str
        OVERLOADED: str
        DISCONNECTED: str
        UNIMPLEMENTED: str
        OTHER: str
        reverse_mapping: dict[str, str]

    message: str | None
    nature: str | None
    durability: str | None
    wrapper: Any

    def __init__(
        self,
        message: str | None = None,
        nature: str | None = None,
        durability: str | None = None,
        wrapper: Any = None,
        type: str | None = None,
    ) -> None: ...
    @property
    def file(self) -> str: ...
    @property
    def line(self) -> int: ...
    @property
    def type(self) -> str | None: ...
    @property
    def description(self) -> str: ...
    def _to_python(self) -> Exception: ...

class _NestedNodeReader:
    @property
    def name(self) -> str: ...
    @property
    def id(self) -> int: ...

class _List_NestedNode_Reader:
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> _NestedNodeReader: ...

class _NodeReader:
    @property
    def displayName(self) -> str: ...
    @property
    def scopeId(self) -> int: ...
    @property
    def id(self) -> int: ...
    @property
    def nestedNodes(self) -> _List_NestedNode_Reader: ...
    @property
    def isStruct(self) -> bool: ...
    @property
    def isConst(self) -> bool: ...
    @property
    def isInterface(self) -> bool: ...
    @property
    def isEnum(self) -> bool: ...
    @property
    def node(self) -> _DynamicStructReader: ...

class _Schema:
    @property
    def node(self) -> _DynamicStructReader: ...
    def as_const_value(self) -> Any: ...
    def as_struct(self) -> _StructSchema: ...
    def as_interface(self) -> _InterfaceSchema: ...
    def as_enum(self) -> _EnumSchema: ...
    def get_proto(self) -> _NodeReader: ...

class _ParsedSchema(_Schema):
    def get_nested(self, name: str) -> _ParsedSchema: ...

class _StructSchema(_Schema):
    @property
    def fieldnames(self) -> tuple[str, ...]: ...
    @property
    def union_fields(self) -> tuple[str, ...]: ...
    @property
    def non_union_fields(self) -> tuple[str, ...]: ...
    @property
    def fields(self) -> dict[str, _StructSchemaField]: ...
    @property
    def fields_list(self) -> list[_StructSchemaField]: ...
    @property
    def node(self) -> _DynamicStructReader: ...

class _StructSchemaField:
    @property
    def proto(self) -> _DynamicStructReader: ...
    @property
    def schema(
        self,
    ) -> _StructSchema | _EnumSchema | _InterfaceSchema | _ListSchema: ...

class _InterfaceMethod:
    @property
    def param_type(self) -> _StructSchema: ...
    @property
    def result_type(self) -> _StructSchema: ...

class _EnumSchema:
    @property
    def enumerants(self) -> dict[str, int]: ...
    @property
    def node(self) -> _DynamicStructReader: ...

class _InterfaceSchema:
    @property
    def method_names(self) -> tuple[str, ...]: ...
    @property
    def method_names_inherited(self) -> set[str]: ...
    @property
    def methods(self) -> dict[str, _InterfaceMethod]: ...
    @property
    def methods_inherited(self) -> dict[str, _InterfaceMethod]: ...
    @property
    def superclasses(self) -> list[_InterfaceSchema]: ...
    @property
    def node(self) -> _DynamicStructReader: ...

class _SchemaType: ...

class _StructModuleWhich(enum.Enum):
    def __eq__(self, other: object) -> bool: ...
    __hash__: None  # pyright: ignore[reportIncompatibleMethodOverride]

class _ListSchema:
    def __init__(
        self,
        schema: _StructSchema
        | _EnumSchema
        | _InterfaceSchema
        | _ListSchema
        | _SchemaType
        | None = None,
    ) -> None: ...
    @property
    def elementType(
        self,
    ) -> _StructSchema | _EnumSchema | _InterfaceSchema | _ListSchema: ...

class _StructModule:
    schema: _StructSchema

    def __init__(self, schema: _StructSchema, name: str) -> None: ...
    def __call__(
        self,
        num_first_segment_words: int | None = None,
        **kwargs: Any,
    ) -> _DynamicStructBuilder: ...
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
        **kwargs: Any,
    ) -> _DynamicStructBuilder:
        """Returns a newly allocated builder message.

        :type num_first_segment_words: int
        :param num_first_segment_words: Size of the first segment to allocate (in words ie. 8 byte increments)

        :type allocate_seg_callable: Callable[[int], bytearray]
        :param allocate_seg_callable: A python callable object that takes the minimum number of 8-byte
        words to allocate (as an `int`) and returns a `bytearray`. This is used to customize the memory
        allocation strategy.

        :type kwargs: dict
        :param kwargs: A list of fields and their values to initialize in the struct.

        Note, kwargs is not an actual argument, but refers to Python's ability to pass keyword arguments.
        ie. new_message(my_field=100)

        :rtype: :class:`_DynamicStructBuilder`
        """
    def read(
        self,
        file: IO[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader:
        """Returns a Reader for the unpacked object read from file.

        :type file: file
        :param file: A python file-like object. It must be a "real" file, with a `fileno()` method.

        :type traversal_limit_in_words: int
        :param traversal_limit_in_words: Limits how many total words of data are allowed to be traversed.
                                         Is actually a uint64_t, and values can be up to 2^64-1. Default is 8*1024*1024.

        :type nesting_limit: int
        :param nesting_limit: Limits how many total words of data are allowed to be traversed. Default is 64.

        :rtype: :class:`_DynamicStructReader`
        """
    async def read_async(
        self,
        stream: _AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader | None:
        """Async version of read(). Returns either a message, or None in case of EOF.

        :type file: AsyncIoStream
        :param file: A AsyncIoStream

        :type traversal_limit_in_words: int
        :param traversal_limit_in_words: Limits how many total words of data are allowed to be traversed.
                                         Is actually a uint64_t, and values can be up to 2^64-1. Default is 8*1024*1024.

        :type nesting_limit: int
        :param nesting_limit: Limits how many total words of data are allowed to be traversed. Default is 64.

        :rtype: :class:`_DynamicStructReader`
        """
    def read_multiple(
        self,
        file: IO[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[_DynamicStructReader]:
        """Returns an iterable, that when traversed will return Readers for messages.

        :type file: file
        :param file: A python file-like object. It must be a "real" file, with a `fileno()` method.

        :type traversal_limit_in_words: int
        :param traversal_limit_in_words: Limits how many total words of data are allowed to be traversed.
                                         Is actually a uint64_t, and values can be up to 2^64-1. Default is 8*1024*1024.

        :type nesting_limit: int
        :param nesting_limit: Limits how many total words of data are allowed to be traversed. Default is 64.

        :type skip_copy: bool
        :param skip_copy: By default, each message is copied because the file needs to advance, even if the message is
                          never read completely. Skip this only if you know what you're doing.

        :rtype: Iterable with elements of :class:`_DynamicStructReader`
        """
    def read_packed(
        self,
        file: IO[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader:
        """Returns a Reader for the packed object read from file.

        :type file: file
        :param file: A python file-like object. It must be a "real" file, with a `fileno()` method.

        :type traversal_limit_in_words: int
        :param traversal_limit_in_words: Limits how many total words of data are allowed to be traversed.
                                         Is actually a uint64_t, and values can be up to 2^64-1. Default is 8*1024*1024.

        :type nesting_limit: int
        :param nesting_limit: Limits how many total words of data are allowed to be traversed. Default is 64.

        :rtype: :class:`_DynamicStructReader`
        """
    def read_multiple_packed(
        self,
        file: IO[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[_DynamicStructReader]:
        """Returns an iterable, that when traversed will return Readers for messages.

        :type file: file
        :param file: A python file-like object. It must be a "real" file, with a `fileno()` method.

        :type traversal_limit_in_words: int
        :param traversal_limit_in_words: Limits how many total words of data are allowed to be traversed.
                                         Is actually a uint64_t, and values can be up to 2^64-1. Default is 8*1024*1024.

        :type nesting_limit: int
        :param nesting_limit: Limits how many total words of data are allowed to be traversed. Default is 64.

        :type skip_copy: bool
        :param skip_copy: By default, each message is copied because the file needs to advance, even if the message is
                          never read completely. Skip this only if you know what you're doing.

        :rtype: Iterable with elements of :class:`_DynamicStructReader`
        """
    def read_multiple_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[_DynamicStructReader]:
        """Returns an iterable, that when traversed will return Readers for messages.

        :type buf: buffer
        :param buf: Any Python object that supports the buffer interface.

        :type traversal_limit_in_words: int
        :param traversal_limit_in_words: Limits how many total words of data are allowed to be traversed.
                                         Is actually a uint64_t, and values can be up to 2^64-1. Default is 8*1024*1024.

        :type nesting_limit: int
        :param nesting_limit: Limits how many total words of data are allowed to be traversed. Default is 64.

        :rtype: Iterable with elements of :class:`_DynamicStructReader`
        """
    def read_multiple_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[_DynamicStructReader]:
        """Returns an iterable, that when traversed will return Readers for messages.

        :type buf: buffer
        :param buf: Any Python object that supports the buffer interface.

        :type traversal_limit_in_words: int
        :param traversal_limit_in_words: Limits how many total words of data are allowed to be traversed.
                                         Is actually a uint64_t, and values can be up to 2^64-1. Default is 8*1024*1024.

        :type nesting_limit: int
        :param nesting_limit: Limits how many total words of data are allowed to be traversed. Default is 64.

        :rtype: Iterable with elements of :class:`_DynamicStructReader`
        """
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> contextlib.AbstractContextManager[_DynamicStructReader]:
        """Returns a Reader for the unpacked object in buf.

        :type buf: buffer
        :param buf: Any Python object that supports the buffer interface.

        :type traversal_limit_in_words: int
        :param traversal_limit_in_words: Limits how many total words of data are allowed to be traversed.
                                         Is actually a uint64_t, and values can be up to 2^64-1. Default is 8*1024*1024.

        :type nesting_limit: int
        :param nesting_limit: Limits how many total words of data are allowed to be traversed. Default is 64.

        :type builder: bool
        :param builder: If true, return a builder object.

        Enabling `builder` will allow you to change the contents of `buf`, so do this with care.

        :rtype: :class:`_DynamicStructReader` or :class:`_DynamicStructBuilder`
        """
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        builder: Literal[False] = False,
    ) -> contextlib.AbstractContextManager[_DynamicStructReader]:
        """Returns a Reader for the unpacked object in buf.

        :type buf: buffer
        :param buf: Any Python object that supports the buffer interface.

        :type traversal_limit_in_words: int
        :param traversal_limit_in_words: Limits how many total words of data are allowed to be traversed.
                                         Is actually a uint64_t, and values can be up to 2^64-1. Default is 8*1024*1024.

        :type nesting_limit: int
        :param nesting_limit: Limits how many total words of data are allowed to be traversed. Default is 64.

        :type builder: bool
        :param builder: If true, return a builder object.

        Enabling `builder` will allow you to change the contents of `buf`, so do this with care.

        :rtype: :class:`_DynamicStructReader` or :class:`_DynamicStructBuilder`
        """
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> contextlib.AbstractContextManager[_DynamicStructBuilder]:
        """Returns a Reader for the unpacked object in buf.

        :type buf: buffer
        :param buf: Any Python object that supports the buffer interface.

        :type traversal_limit_in_words: int
        :param traversal_limit_in_words: Limits how many total words of data are allowed to be traversed.
                                         Is actually a uint64_t, and values can be up to 2^64-1. Default is 8*1024*1024.

        :type nesting_limit: int
        :param nesting_limit: Limits how many total words of data are allowed to be traversed. Default is 64.

        :type builder: bool
        :param builder: If true, return a builder object.

        Enabling `builder` will allow you to change the contents of `buf`, so do this with care.

        :rtype: :class:`_DynamicStructReader` or :class:`_DynamicStructBuilder`
        """
    @overload
    def from_bytes(
        self,
        buf: Any,
        traversal_limit_in_words: int | None,
        nesting_limit: int | None,
        builder: Literal[True],
    ) -> contextlib.AbstractContextManager[_DynamicStructBuilder]:
        """Returns a Reader for the unpacked object in buf.

        :type buf: buffer
        :param buf: Any Python object that supports the buffer interface.

        :type traversal_limit_in_words: int
        :param traversal_limit_in_words: Limits how many total words of data are allowed to be traversed.
                                         Is actually a uint64_t, and values can be up to 2^64-1. Default is 8*1024*1024.

        :type nesting_limit: int
        :param nesting_limit: Limits how many total words of data are allowed to be traversed. Default is 64.

        :type builder: bool
        :param builder: If true, return a builder object.

        Enabling `builder` will allow you to change the contents of `buf`, so do this with care.

        :rtype: :class:`_DynamicStructReader` or :class:`_DynamicStructBuilder`
        """
    def from_segments(
        self,
        segments: Sequence[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader:
        """Returns a Reader for a list of segment bytes.

        This avoids making copies.

        NB: This is not currently supported on PyPy.

        :rtype: list
        """
    def from_bytes_packed(
        self,
        buf: Any,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader:
        """Returns a Reader for the packed object in buf.

        :type buf: buffer
        :param buf: Any Python object that supports the readable buffer interface.

        :type traversal_limit_in_words: int
        :param traversal_limit_in_words: Limits how many total words of data are allowed to be traversed.
                                         Is actually a uint64_t, and values can be up to 2^64-1. Default is 8*1024*1024.

        :type nesting_limit: int
        :param nesting_limit: Limits how many total words of data are allowed to be traversed. Default is 64.

        :rtype: :class:`_DynamicStructReader`
        """

class _EnumModule:
    schema: _EnumSchema

    def __init__(self, schema: _EnumSchema, name: str) -> None: ...

class _InterfaceModule:
    schema: _InterfaceSchema

    def __init__(self, schema: _InterfaceSchema, name: str) -> None: ...
    def _new_client(
        self,
        server: _DynamicCapabilityServer,
    ) -> _DynamicCapabilityClient: ...

class _DynamicEnum:
    _parent: Any

    @property
    def raw(self) -> int: ...
    def _as_str(self) -> str: ...
    def __str__(self) -> str: ...  # noqa: PYI029

class _DynamicEnumField:
    @property
    def raw(self) -> int: ...
    def _str(self) -> str: ...
    def __call__(self) -> str: ...

class _DynamicObjectReader:
    _parent: Any
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._AutomaticSowingStructModule._AvgSoilTempStructModule,
    ) -> monica_management_capnp.types.readers.AvgSoilTempReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._CuttingStructModule._SpecStructModule,
    ) -> monica_management_capnp.types.readers.SpecReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._DailyWeatherStructModule._KVStructModule,
    ) -> monica_management_capnp.types.readers.KVReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._HarvestStructModule._OptCarbonMgmtDataStructModule,
    ) -> monica_management_capnp.types.readers.OptCarbonMgmtDataReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._IrrigationStructModule._ParametersStructModule,
    ) -> monica_management_capnp.types.readers.ParamsIrrigationParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule,
    ) -> (
        monica_management_capnp.types.readers.ParamsMineralFertilizationParametersReader
    ): ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._OrganicFertilizationStructModule._OrganicMatterParametersStructModule,
    ) -> monica_management_capnp.types.readers.OrganicMatterParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._OrganicFertilizationStructModule._ParametersStructModule,
    ) -> (
        monica_management_capnp.types.readers.ParamsOrganicFertilizationParametersReader
    ): ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._EmissionsStructModule._SpeciesIdToEmissionStructModule,
    ) -> monica_params_capnp.types.readers.SpeciesIdToEmissionReader: ...
    @overload
    def as_struct(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule,
    ) -> storage_capnp.types.readers.ValueReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ObserverInterfaceModule._EventStructModule,
    ) -> fbp_capnp.types.readers.EventReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ObserverInterfaceModule._ParamsStructModule,
    ) -> fbp_capnp.types.readers.ChannelObserverParamsReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._StatsStructModule,
    ) -> fbp_capnp.types.readers.StatsReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._IPStructModule._SysAttributesStructModule._SysAttributesBracketTypeStructModule,
    ) -> fbp_capnp.types.readers.SysAttributesBracketTypeReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._AutomaticSowingStructModule._AvgSoilTempStructModule,
    ) -> management_capnp.types.readers.AvgSoilTempReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._CuttingStructModule._SpecStructModule,
    ) -> management_capnp.types.readers.SpecReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._HarvestStructModule._OptCarbonMgmtDataStructModule,
    ) -> management_capnp.types.readers.OptCarbonMgmtDataReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._EventStructModule._EventAfterStructModule,
    ) -> monica_management_capnp.types.readers.EventAfterReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._EventStructModule._EventAtStructModule,
    ) -> monica_management_capnp.types.readers.EventAtReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._EventStructModule._EventBetweenStructModule,
    ) -> monica_management_capnp.types.readers.EventBetweenReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._EventStructModule._TypeStructModule,
    ) -> monica_management_capnp.types.readers.TypeReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._AutomaticHarvestStructModule,
    ) -> monica_management_capnp.types.readers.AutomaticHarvestReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._AutomaticSowingStructModule,
    ) -> monica_management_capnp.types.readers.AutomaticSowingReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._CuttingStructModule,
    ) -> monica_management_capnp.types.readers.CuttingReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._DailyWeatherStructModule,
    ) -> monica_management_capnp.types.readers.DailyWeatherReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._HarvestStructModule,
    ) -> monica_management_capnp.types.readers.HarvestReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._IrrigationStructModule,
    ) -> monica_management_capnp.types.readers.IrrigationReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._MineralFertilizationStructModule,
    ) -> monica_management_capnp.types.readers.MineralFertilizationReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._NDemandFertilizationStructModule,
    ) -> monica_management_capnp.types.readers.NDemandFertilizationReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._OrganicFertilizationStructModule,
    ) -> monica_management_capnp.types.readers.OrganicFertilizationReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._SaveStateStructModule,
    ) -> monica_management_capnp.types.readers.SaveStateReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._SowingStructModule,
    ) -> monica_management_capnp.types.readers.SowingReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._TillageStructModule,
    ) -> monica_management_capnp.types.readers.TillageReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._EnvironmentParametersStructModule._YearToValueStructModule,
    ) -> monica_params_capnp.types.readers.YearToValueReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._MeasuredGroundwaterTableInformationStructModule._DateToValueStructModule,
    ) -> monica_params_capnp.types.readers.DateToValueReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._CPDataStructModule,
    ) -> monica_params_capnp.types.readers.CPDataReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._EmissionsStructModule,
    ) -> monica_params_capnp.types.readers.EmissionsReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._EnzymeActivityTStructModule,
    ) -> monica_params_capnp.types.readers.EnzymeActivityTReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._FoliageTStructModule,
    ) -> monica_params_capnp.types.readers.FoliageTReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._LeafEmissionTStructModule,
    ) -> monica_params_capnp.types.readers.LeafEmissionTReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._LeafEmissionsStructModule,
    ) -> monica_params_capnp.types.readers.LeafEmissionsReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._MicroClimateDataStructModule,
    ) -> monica_params_capnp.types.readers.MicroClimateDataReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._PhotosynthTStructModule,
    ) -> monica_params_capnp.types.readers.PhotosynthTReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._SpeciesDataStructModule,
    ) -> monica_params_capnp.types.readers.SpeciesDataReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._MonicaModelStateStructModule._ACDToValueStructModule,
    ) -> monica_state_capnp.types.readers.ACDToValueReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilColumnStateStructModule._DelayedNMinApplicationParamsStructModule,
    ) -> monica_state_capnp.types.readers.DelayedNMinApplicationParamsReader: ...
    @overload
    def as_struct(
        self,
        schema: yieldstat_capnp.types.modules._OutputStructModule._YearToResultStructModule,
    ) -> yieldstat_capnp.types.readers.YearToResultReader: ...
    @overload
    def as_struct(
        self,
        schema: yieldstat_capnp.types.modules._ResultStructModule._ResultToValueStructModule,
    ) -> yieldstat_capnp.types.readers.ResultToValueReader: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._HostPortResolverInterfaceModule._RegistrarInterfaceModule._RegisterParamsStructModule,
    ) -> persistence_capnp.types.readers.RegisterParamsReader: ...
    @overload
    def as_struct(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ContainerInterfaceModule._KeyAndEntryStructModule,
    ) -> storage_capnp.types.readers.KeyAndEntryReader: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._AlterTimeSeriesWrapperInterfaceModule._AlteredStructModule,
    ) -> climate_capnp.types.readers.AlteredReader: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._CSVTimeSeriesFactoryInterfaceModule._CSVConfigStructModule,
    ) -> climate_capnp.types.readers.CSVConfigReader: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._LocationStructModule._KVStructModule,
    ) -> climate_capnp.types.readers.KVReader: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule._EntryStructModule,
    ) -> climate_capnp.types.readers.EntryReader: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule._ValueStructModule,
    ) -> climate_capnp.types.readers.ValueReader: ...
    @overload
    def as_struct(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._ZmqPipelineAddressesStructModule,
    ) -> cluster_admin_service_capnp.types.readers.ZmqPipelineAddressesReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._MsgStructModule,
    ) -> fbp_capnp.types.readers.MsgReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StartupInfoStructModule,
    ) -> fbp_capnp.types.readers.StartupInfoReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ComponentStructModule._ComponentFactoryStructModule,
    ) -> fbp_capnp.types.readers.ComponentFactoryReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ComponentStructModule._PortStructModule,
    ) -> fbp_capnp.types.readers.PortReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._IPStructModule._ChunkedDataStructModule,
    ) -> fbp_capnp.types.readers.ChunkedDataReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._IPStructModule._KVStructModule,
    ) -> fbp_capnp.types.readers.KVReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._IPStructModule._SysAttributesStructModule,
    ) -> fbp_capnp.types.readers.SysAttributesReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._PortInfosStructModule._NameAndSRStructModule,
    ) -> fbp_capnp.types.readers.NameAndSRReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._ActivityInfoStructModule,
    ) -> fbp_capnp.types.readers.ActivityInfoReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._ConfigEntryStructModule,
    ) -> fbp_capnp.types.readers.ConfigEntryReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._RunInfoStructModule,
    ) -> fbp_capnp.types.readers.RunInfoReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._StartChannelsServiceInterfaceModule._ParamsStructModule,
    ) -> fbp_capnp.types.readers.StartChannelsServiceParamsReader: ...
    @overload
    def as_struct(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._AggregationPartStructModule,
    ) -> grid_capnp.types.readers.AggregationPartReader: ...
    @overload
    def as_struct(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._LocationStructModule,
    ) -> grid_capnp.types.readers.LocationReader: ...
    @overload
    def as_struct(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._ResolutionStructModule,
    ) -> grid_capnp.types.readers.ResolutionReader: ...
    @overload
    def as_struct(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._RowColStructModule,
    ) -> grid_capnp.types.readers.RowColReader: ...
    @overload
    def as_struct(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._ValueStructModule,
    ) -> grid_capnp.types.readers.ValueReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._EventStructModule._EventAfterStructModule,
    ) -> management_capnp.types.readers.EventAfterReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._EventStructModule._EventAtStructModule,
    ) -> management_capnp.types.readers.EventAtReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._EventStructModule._EventBetweenStructModule,
    ) -> management_capnp.types.readers.EventBetweenReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._EventStructModule._TypeStructModule,
    ) -> management_capnp.types.readers.TypeReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._AutomaticHarvestStructModule,
    ) -> management_capnp.types.readers.AutomaticHarvestReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._AutomaticSowingStructModule,
    ) -> management_capnp.types.readers.AutomaticSowingReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._CuttingStructModule,
    ) -> management_capnp.types.readers.CuttingReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._HarvestStructModule,
    ) -> management_capnp.types.readers.HarvestReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._IrrigationStructModule,
    ) -> management_capnp.types.readers.IrrigationReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._MineralFertilizationStructModule,
    ) -> management_capnp.types.readers.MineralFertilizationReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._NDemandFertilizationStructModule,
    ) -> management_capnp.types.readers.NDemandFertilizationReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._OrganicFertilizationStructModule,
    ) -> management_capnp.types.readers.OrganicFertilizationReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._SowingStructModule,
    ) -> management_capnp.types.readers.SowingReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._TillageStructModule,
    ) -> management_capnp.types.readers.TillageReader: ...
    @overload
    def as_struct(
        self,
        schema: agmip_capnp.types.modules._FieldExperimentDataTemplateStructModule,
    ) -> agmip_capnp.types.readers.FieldExperimentDataTemplateReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._EventStructModule,
    ) -> monica_management_capnp.types.readers.EventReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ILRDatesStructModule,
    ) -> monica_management_capnp.types.readers.ILRDatesReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule,
    ) -> monica_management_capnp.types.readers.ParamsReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._AutomaticHarvestParametersStructModule,
    ) -> monica_params_capnp.types.readers.AutomaticHarvestParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._AutomaticIrrigationParametersStructModule,
    ) -> monica_params_capnp.types.readers.AutomaticIrrigationParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._CropModuleParametersStructModule,
    ) -> monica_params_capnp.types.readers.CropModuleParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._CropParametersStructModule,
    ) -> monica_params_capnp.types.readers.CropParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._CropResidueParametersStructModule,
    ) -> monica_params_capnp.types.readers.CropResidueParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._CropSpecStructModule,
    ) -> monica_params_capnp.types.readers.CropSpecReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._CultivarParametersStructModule,
    ) -> monica_params_capnp.types.readers.CultivarParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._EnvironmentParametersStructModule,
    ) -> monica_params_capnp.types.readers.EnvironmentParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._MeasuredGroundwaterTableInformationStructModule,
    ) -> (
        monica_params_capnp.types.readers.MeasuredGroundwaterTableInformationReader
    ): ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._NMinApplicationParametersStructModule,
    ) -> monica_params_capnp.types.readers.NMinApplicationParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._NMinCropParametersStructModule,
    ) -> monica_params_capnp.types.readers.NMinCropParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SimulationParametersStructModule,
    ) -> monica_params_capnp.types.readers.SimulationParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SiteParametersStructModule,
    ) -> monica_params_capnp.types.readers.SiteParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SoilMoistureModuleParametersStructModule,
    ) -> monica_params_capnp.types.readers.SoilMoistureModuleParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SoilOrganicModuleParametersStructModule,
    ) -> monica_params_capnp.types.readers.SoilOrganicModuleParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SoilParametersStructModule,
    ) -> monica_params_capnp.types.readers.SoilParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SoilTemperatureModuleParametersStructModule,
    ) -> monica_params_capnp.types.readers.SoilTemperatureModuleParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SoilTransportModuleParametersStructModule,
    ) -> monica_params_capnp.types.readers.SoilTransportModuleParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SpeciesParametersStructModule,
    ) -> monica_params_capnp.types.readers.SpeciesParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SticsParametersStructModule,
    ) -> monica_params_capnp.types.readers.SticsParametersReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule,
    ) -> monica_params_capnp.types.readers.VocReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._YieldComponentStructModule,
    ) -> monica_params_capnp.types.readers.YieldComponentReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._AOMPropertiesStructModule,
    ) -> monica_state_capnp.types.readers.AOMPropertiesReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._CropModuleStateStructModule,
    ) -> monica_state_capnp.types.readers.CropModuleStateReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._CropStateStructModule,
    ) -> monica_state_capnp.types.readers.CropStateReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._FrostModuleStateStructModule,
    ) -> monica_state_capnp.types.readers.FrostModuleStateReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._ICDataStructModule,
    ) -> monica_state_capnp.types.readers.ICDataReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._MaybeBoolStructModule,
    ) -> monica_state_capnp.types.readers.MaybeBoolReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._MonicaModelStateStructModule,
    ) -> monica_state_capnp.types.readers.MonicaModelStateReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._RuntimeStateStructModule,
    ) -> monica_state_capnp.types.readers.RuntimeStateReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SnowModuleStateStructModule,
    ) -> monica_state_capnp.types.readers.SnowModuleStateReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilColumnStateStructModule,
    ) -> monica_state_capnp.types.readers.SoilColumnStateReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilLayerStateStructModule,
    ) -> monica_state_capnp.types.readers.SoilLayerStateReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilMoistureModuleStateStructModule,
    ) -> monica_state_capnp.types.readers.SoilMoistureModuleStateReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilOrganicModuleStateStructModule,
    ) -> monica_state_capnp.types.readers.SoilOrganicModuleStateReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilTemperatureModuleStateStructModule,
    ) -> monica_state_capnp.types.readers.SoilTemperatureModuleStateReader: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilTransportModuleStateStructModule,
    ) -> monica_state_capnp.types.readers.SoilTransportModuleStateReader: ...
    @overload
    def as_struct(
        self,
        schema: sim_setup_capnp.types.modules._SetupStructModule,
    ) -> sim_setup_capnp.types.readers.SetupReader: ...
    @overload
    def as_struct(
        self,
        schema: yieldstat_capnp.types.modules._OutputStructModule,
    ) -> yieldstat_capnp.types.readers.OutputReader: ...
    @overload
    def as_struct(
        self,
        schema: yieldstat_capnp.types.modules._RestInputStructModule,
    ) -> yieldstat_capnp.types.readers.RestInputReader: ...
    @overload
    def as_struct(
        self,
        schema: yieldstat_capnp.types.modules._ResultStructModule,
    ) -> yieldstat_capnp.types.readers.ResultReader: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._AddressStructModule._AddressIp6StructModule,
    ) -> persistence_capnp.types.readers.AddressIp6Reader: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._GatewayInterfaceModule._RegResultsStructModule,
    ) -> persistence_capnp.types.readers.RegResultsReader: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._PersistentInterfaceModule._SaveParamsStructModule,
    ) -> persistence_capnp.types.readers.SaveParamsReader: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._PersistentInterfaceModule._SaveResultsStructModule,
    ) -> persistence_capnp.types.readers.SaveResultsReader: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._RestorerInterfaceModule._RestoreParamsStructModule,
    ) -> persistence_capnp.types.readers.RestoreParamsReader: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._SturdyRefStructModule._OwnerStructModule,
    ) -> persistence_capnp.types.readers.OwnerReader: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._SturdyRefStructModule._TokenStructModule,
    ) -> persistence_capnp.types.readers.TokenReader: ...
    @overload
    def as_struct(
        self,
        schema: registry_capnp.types.modules._RegistrarInterfaceModule._CrossDomainRestoreStructModule,
    ) -> registry_capnp.types.readers.CrossDomainRestoreReader: ...
    @overload
    def as_struct(
        self,
        schema: registry_capnp.types.modules._RegistrarInterfaceModule._RegParamsStructModule,
    ) -> registry_capnp.types.readers.RegParamsReader: ...
    @overload
    def as_struct(
        self,
        schema: registry_capnp.types.modules._RegistryInterfaceModule._EntryStructModule,
    ) -> registry_capnp.types.readers.EntryReader: ...
    @overload
    def as_struct(
        self,
        schema: service_capnp.types.modules._FactoryInterfaceModule._AccessInfoStructModule,
    ) -> service_capnp.types.readers.AccessInfoReader: ...
    @overload
    def as_struct(
        self,
        schema: service_capnp.types.modules._FactoryInterfaceModule._CreateParamsStructModule,
    ) -> service_capnp.types.readers.CreateParamsReader: ...
    @overload
    def as_struct(
        self,
        schema: soil_capnp.types.modules._LayerStructModule._PropertyStructModule,
    ) -> soil_capnp.types.readers.PropertyReader: ...
    @overload
    def as_struct(
        self,
        schema: soil_capnp.types.modules._QueryStructModule._ResultStructModule,
    ) -> soil_capnp.types.readers.ResultReader: ...
    @overload
    def as_struct(
        self,
        schema: soil_params_capnp.types.modules._CapillaryRiseRateStructModule._DataStructModule,
    ) -> soil_params_capnp.types.readers.CapillaryRiseRateDataReader: ...
    @overload
    def as_struct(
        self,
        schema: soil_params_capnp.types.modules._SoilCharacteristicDataStructModule._DataStructModule,
    ) -> soil_params_capnp.types.readers.SoilCharacteristicDataDataReader: ...
    @overload
    def as_struct(
        self,
        schema: soil_params_capnp.types.modules._SoilCharacteristicModifierStructModule._DataStructModule,
    ) -> soil_params_capnp.types.readers.SoilCharacteristicModifierDataReader: ...
    @overload
    def as_struct(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ImportExportDataStructModule,
    ) -> storage_capnp.types.readers.ImportExportDataReader: ...
    @overload
    def as_struct(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._InfoAndContainerStructModule,
    ) -> storage_capnp.types.readers.InfoAndContainerReader: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._EnsembleMemberStructModule,
    ) -> climate_capnp.types.readers.EnsembleMemberReader: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._LocationStructModule,
    ) -> climate_capnp.types.readers.LocationReader: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._MetaPlusDataStructModule,
    ) -> climate_capnp.types.readers.MetaPlusDataReader: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule,
    ) -> climate_capnp.types.readers.MetadataReader: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._TimeSeriesDataStructModule,
    ) -> climate_capnp.types.readers.TimeSeriesDataReader: ...
    @overload
    def as_struct(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule,
    ) -> cluster_admin_service_capnp.types.readers.ClusterReader: ...
    @overload
    def as_struct(
        self,
        schema: common_capnp.types.modules._BlobStructModule,
    ) -> common_capnp.types.readers.BlobReader: ...
    @overload
    def as_struct(
        self,
        schema: common_capnp.types.modules._IdInformationStructModule,
    ) -> common_capnp.types.readers.IdInformationReader: ...
    @overload
    def as_struct(
        self,
        schema: common_capnp.types.modules._MimeTypesStructModule,
    ) -> common_capnp.types.readers.MimeTypesReader: ...
    @overload
    def as_struct(
        self,
        schema: common_capnp.types.modules._PairStructModule,
    ) -> common_capnp.types.readers.PairReader: ...
    @overload
    def as_struct(
        self,
        schema: common_capnp.types.modules._StructuredTextStructModule,
    ) -> common_capnp.types.readers.StructuredTextReader: ...
    @overload
    def as_struct(
        self,
        schema: common_capnp.types.modules._ValueStructModule,
    ) -> common_capnp.types.readers.ValueReader: ...
    @overload
    def as_struct(
        self,
        schema: date_capnp.types.modules._DateStructModule,
    ) -> date_capnp.types.readers.DateReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._CultivarStructModule,
    ) -> field_exp_data_capnp.types.readers.CultivarReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._EnvironmentModificationStructModule,
    ) -> field_exp_data_capnp.types.readers.EnvironmentModificationReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._ExperimentDescriptionStructModule,
    ) -> field_exp_data_capnp.types.readers.ExperimentDescriptionReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._FertilizerEventStructModule,
    ) -> field_exp_data_capnp.types.readers.FertilizerEventReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._FieldStructModule,
    ) -> field_exp_data_capnp.types.readers.FieldReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._HarvestEventStructModule,
    ) -> field_exp_data_capnp.types.readers.HarvestEventReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._InitialConditionsLayerStructModule,
    ) -> field_exp_data_capnp.types.readers.InitialConditionsLayerReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._IrrigationEventStructModule,
    ) -> field_exp_data_capnp.types.readers.IrrigationEventReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._MixedTypeStructModule,
    ) -> field_exp_data_capnp.types.readers.MixedTypeReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._PlantingEventStructModule,
    ) -> field_exp_data_capnp.types.readers.PlantingEventReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._PlotStructModule,
    ) -> field_exp_data_capnp.types.readers.PlotReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._ResidueStructModule,
    ) -> field_exp_data_capnp.types.readers.ResidueReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._SoilMetadataStructModule,
    ) -> field_exp_data_capnp.types.readers.SoilMetadataReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._TreatmentStructModule,
    ) -> field_exp_data_capnp.types.readers.TreatmentReader: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._WeatherStationStructModule,
    ) -> field_exp_data_capnp.types.readers.WeatherStationReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ComponentStructModule,
    ) -> fbp_capnp.types.readers.ComponentReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._IIPStructModule,
    ) -> fbp_capnp.types.readers.IIPReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._IPStructModule,
    ) -> fbp_capnp.types.readers.IPReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._LogMessageStructModule,
    ) -> fbp_capnp.types.readers.LogMessageReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._PortInfosStructModule,
    ) -> fbp_capnp.types.readers.PortInfosReader: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._CoordStructModule,
    ) -> geo_capnp.types.readers.CoordReader: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._EPSGStructModule,
    ) -> geo_capnp.types.readers.EPSGReader: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._GKCoordStructModule,
    ) -> geo_capnp.types.readers.GKCoordReader: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._LatLonCoordStructModule,
    ) -> geo_capnp.types.readers.LatLonCoordReader: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._Point2DStructModule,
    ) -> geo_capnp.types.readers.Point2DReader: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._RectBoundsStructModule,
    ) -> geo_capnp.types.readers.RectBoundsReader: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._RowColStructModule,
    ) -> geo_capnp.types.readers.RowColReader: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._UTMCoordStructModule,
    ) -> geo_capnp.types.readers.UTMCoordReader: ...
    @overload
    def as_struct(
        self,
        schema: jobs_capnp.types.modules._JobStructModule,
    ) -> jobs_capnp.types.readers.JobReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._EventStructModule,
    ) -> management_capnp.types.readers.EventReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._NutrientStructModule,
    ) -> management_capnp.types.readers.NutrientReader: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule,
    ) -> management_capnp.types.readers.ParamsReader: ...
    @overload
    def as_struct(
        self,
        schema: model_capnp.types.modules._EnvStructModule,
    ) -> model_capnp.types.readers.EnvReader: ...
    @overload
    def as_struct(
        self,
        schema: model_capnp.types.modules._StatStructModule,
    ) -> model_capnp.types.readers.StatReader: ...
    @overload
    def as_struct(
        self,
        schema: model_capnp.types.modules._XYPlusResultStructModule,
    ) -> model_capnp.types.readers.XYPlusResultReader: ...
    @overload
    def as_struct(
        self,
        schema: model_capnp.types.modules._XYResultStructModule,
    ) -> model_capnp.types.readers.XYResultReader: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._AddressStructModule,
    ) -> persistence_capnp.types.readers.AddressReader: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._SturdyRefStructModule,
    ) -> persistence_capnp.types.readers.SturdyRefReader: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._VatIdStructModule,
    ) -> persistence_capnp.types.readers.VatIdReader: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._VatPathStructModule,
    ) -> persistence_capnp.types.readers.VatPathReader: ...
    @overload
    def as_struct(
        self,
        schema: soil_capnp.types.modules._LayerStructModule,
    ) -> soil_capnp.types.readers.LayerReader: ...
    @overload
    def as_struct(
        self,
        schema: soil_capnp.types.modules._ProfileDataStructModule,
    ) -> soil_capnp.types.readers.ProfileDataReader: ...
    @overload
    def as_struct(
        self,
        schema: soil_capnp.types.modules._QueryStructModule,
    ) -> soil_capnp.types.readers.QueryReader: ...
    @overload
    def as_struct(
        self,
        schema: soil_params_capnp.types.modules._CapillaryRiseRateStructModule,
    ) -> soil_params_capnp.types.readers.CapillaryRiseRateReader: ...
    @overload
    def as_struct(
        self,
        schema: soil_params_capnp.types.modules._SoilCharacteristicDataStructModule,
    ) -> soil_params_capnp.types.readers.SoilCharacteristicDataReader: ...
    @overload
    def as_struct(
        self,
        schema: soil_params_capnp.types.modules._SoilCharacteristicModifierStructModule,
    ) -> soil_params_capnp.types.readers.SoilCharacteristicModifierReader: ...
    @overload
    def as_struct(
        self,
        schema: x_capnp.types.modules._SStructModule,
    ) -> x_capnp.types.readers.SReader: ...
    @overload
    def as_struct(
        self,
        schema: _StructSchema | _StructModule,
    ) -> _DynamicStructReader: ...
    def as_struct(
        self,
        schema: _StructSchema | _StructModule,
    ) -> _DynamicStructReader: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._AlterTimeSeriesWrapperInterfaceModule,
    ) -> climate_capnp.types.clients.AlterTimeSeriesWrapperClient: ...
    @overload
    def as_interface(
        self,
        schema: model_capnp.types.modules._EnvInstanceProxyInterfaceModule,
    ) -> model_capnp.types.clients.EnvInstanceProxyClient: ...
    @overload
    def as_interface(
        self,
        schema: model_capnp.types.modules._EnvInstanceInterfaceModule,
    ) -> model_capnp.types.clients.EnvInstanceClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._DatasetInterfaceModule,
    ) -> climate_capnp.types.clients.DatasetClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._ServiceInterfaceModule,
    ) -> climate_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._TimeSeriesInterfaceModule,
    ) -> climate_capnp.types.clients.TimeSeriesClient: ...
    @overload
    def as_interface(
        self,
        schema: common_capnp.types.modules._IdentifiableHolderInterfaceModule,
    ) -> common_capnp.types.clients.IdentifiableHolderClient: ...
    @overload
    def as_interface(
        self,
        schema: crop_capnp.types.modules._CropInterfaceModule,
    ) -> crop_capnp.types.clients.CropClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule,
    ) -> fbp_capnp.types.clients.ChannelClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ReaderInterfaceModule,
    ) -> fbp_capnp.types.clients.ReaderClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._WriterInterfaceModule,
    ) -> fbp_capnp.types.clients.WriterClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule,
    ) -> fbp_capnp.types.clients.ProcessClient: ...
    @overload
    def as_interface(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule,
    ) -> grid_capnp.types.clients.GridClient: ...
    @overload
    def as_interface(
        self,
        schema: jobs_capnp.types.modules._ServiceInterfaceModule,
    ) -> jobs_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: management_capnp.types.modules._FertilizerInterfaceModule,
    ) -> management_capnp.types.clients.FertilizerClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._GatewayInterfaceModule,
    ) -> persistence_capnp.types.clients.GatewayClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._HostPortResolverInterfaceModule,
    ) -> persistence_capnp.types.clients.HostPortResolverClient: ...
    @overload
    def as_interface(
        self,
        schema: soil_capnp.types.modules._ProfileInterfaceModule,
    ) -> soil_capnp.types.clients.ProfileClient: ...
    @overload
    def as_interface(
        self,
        schema: soil_capnp.types.modules._ServiceInterfaceModule,
    ) -> soil_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule,
    ) -> storage_capnp.types.clients.StoreClient: ...
    @overload
    def as_interface(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ContainerInterfaceModule,
    ) -> storage_capnp.types.clients.ContainerClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._AlterTimeSeriesWrapperFactoryInterfaceModule,
    ) -> climate_capnp.types.clients.AlterTimeSeriesWrapperFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._CSVTimeSeriesFactoryInterfaceModule,
    ) -> climate_capnp.types.clients.CSVTimeSeriesFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._AdminMasterInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.AdminMasterClient: ...
    @overload
    def as_interface(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._ModelInstanceFactoryInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.ModelInstanceFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._RuntimeInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.RuntimeClient: ...
    @overload
    def as_interface(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._UserMasterInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.UserMasterClient: ...
    @overload
    def as_interface(
        self,
        schema: common_capnp.types.modules._FactoryInterfaceModule,
    ) -> common_capnp.types.clients.FactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: common_capnp.types.modules._IOFactoryInterfaceModule,
    ) -> common_capnp.types.clients.IOFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: crop_capnp.types.modules._ServiceInterfaceModule,
    ) -> crop_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._FactoryInterfaceModule,
    ) -> fbp_capnp.types.clients.ProcessFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._RunnableInterfaceModule,
    ) -> fbp_capnp.types.clients.RunnableClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._RunnableInterfaceModule._FactoryInterfaceModule,
    ) -> fbp_capnp.types.clients.RunnableFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._StartChannelsServiceInterfaceModule,
    ) -> fbp_capnp.types.clients.StartChannelsServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: management_capnp.types.modules._FertilizerServiceInterfaceModule,
    ) -> management_capnp.types.clients.FertilizerServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: management_capnp.types.modules._ServiceInterfaceModule,
    ) -> management_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: model_capnp.types.modules._ClimateInstanceInterfaceModule,
    ) -> model_capnp.types.clients.ClimateInstanceClient: ...
    @overload
    def as_interface(
        self,
        schema: model_capnp.types.modules._InstanceFactoryInterfaceModule,
    ) -> model_capnp.types.clients.InstanceFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: monica_management_capnp.types.modules._ServiceInterfaceModule,
    ) -> monica_management_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: registry_capnp.types.modules._AdminInterfaceModule,
    ) -> registry_capnp.types.clients.AdminClient: ...
    @overload
    def as_interface(
        self,
        schema: registry_capnp.types.modules._RegistrarInterfaceModule,
    ) -> registry_capnp.types.clients.RegistrarClient: ...
    @overload
    def as_interface(
        self,
        schema: registry_capnp.types.modules._RegistryInterfaceModule,
    ) -> registry_capnp.types.clients.RegistryClient: ...
    @overload
    def as_interface(
        self,
        schema: service_capnp.types.modules._AdminInterfaceModule,
    ) -> service_capnp.types.clients.AdminClient: ...
    @overload
    def as_interface(
        self,
        schema: service_capnp.types.modules._FactoryInterfaceModule,
    ) -> service_capnp.types.clients.FactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: service_capnp.types.modules._SimpleFactoryInterfaceModule,
    ) -> service_capnp.types.clients.SimpleFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._DatasetInterfaceModule._GetLocationsCallbackInterfaceModule,
    ) -> climate_capnp.types.clients.GetLocationsCallbackClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule._InformationInterfaceModule,
    ) -> climate_capnp.types.clients.InformationClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule._SupportedInterfaceModule,
    ) -> climate_capnp.types.clients.SupportedClient: ...
    @overload
    def as_interface(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._UnregisterInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.UnregisterClient: ...
    @overload
    def as_interface(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._ValueHolderInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.ValueHolderClient: ...
    @overload
    def as_interface(
        self,
        schema: common_capnp.types.modules._HolderInterfaceModule,
    ) -> common_capnp.types.clients.HolderClient: ...
    @overload
    def as_interface(
        self,
        schema: common_capnp.types.modules._IdentifiableInterfaceModule,
    ) -> common_capnp.types.clients.IdentifiableClient: ...
    @overload
    def as_interface(
        self,
        schema: config_capnp.types.modules._ServiceInterfaceModule,
    ) -> config_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: modam_capnp.types.modules._ModamWrapperServiceInterfaceModule,
    ) -> modam_capnp.types.clients.ModamWrapperServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ObserverInterfaceModule,
    ) -> fbp_capnp.types.clients.ObserverClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ObserverInterfaceModule._UnregisterInterfaceModule,
    ) -> fbp_capnp.types.clients.ChannelObserverUnregisterClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ReaderInterfaceModule._LeaseInterfaceModule,
    ) -> fbp_capnp.types.clients.LeaseClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule,
    ) -> fbp_capnp.types.clients.StatsCallbackClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule,
    ) -> fbp_capnp.types.clients.ChannelStatsCallbackUnregisterClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._ActivityTransitionInterfaceModule,
    ) -> fbp_capnp.types.clients.ActivityTransitionClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._DisconnectInterfaceModule,
    ) -> fbp_capnp.types.clients.DisconnectClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._ProcessHandleInterfaceModule,
    ) -> fbp_capnp.types.clients.ProcessHandleClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._StateTransitionInterfaceModule,
    ) -> fbp_capnp.types.clients.StateTransitionClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._RunnableInterfaceModule._StoppedCallbackInterfaceModule,
    ) -> fbp_capnp.types.clients.StoppedCallbackClient: ...
    @overload
    def as_interface(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._CallbackInterfaceModule,
    ) -> grid_capnp.types.clients.CallbackClient: ...
    @overload
    def as_interface(
        self,
        schema: model_capnp.types.modules._EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule,
    ) -> model_capnp.types.clients.UnregisterClient: ...
    @overload
    def as_interface(
        self,
        schema: web_berest_data_import_capnp.types.modules._DWLABImportInterfaceModule,
    ) -> web_berest_data_import_capnp.types.clients.DWLABImportClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._GatewayRegistrableInterfaceModule,
    ) -> persistence_capnp.types.clients.GatewayRegistrableClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._HeartbeatInterfaceModule,
    ) -> persistence_capnp.types.clients.HeartbeatClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._HostPortResolverInterfaceModule._RegistrarInterfaceModule,
    ) -> persistence_capnp.types.clients.RegistrarClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._PersistentInterfaceModule,
    ) -> persistence_capnp.types.clients.PersistentClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule,
    ) -> persistence_capnp.types.clients.ReleaseSturdyRefClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._RestorerInterfaceModule,
    ) -> persistence_capnp.types.clients.RestorerClient: ...
    @overload
    def as_interface(
        self,
        schema: registry_capnp.types.modules._RegistrarInterfaceModule._UnregisterInterfaceModule,
    ) -> registry_capnp.types.clients.UnregisterClient: ...
    @overload
    def as_interface(
        self,
        schema: service_capnp.types.modules._StoppableInterfaceModule,
    ) -> service_capnp.types.clients.StoppableClient: ...
    @overload
    def as_interface(
        self,
        schema: soil_capnp.types.modules._ServiceInterfaceModule._StreamInterfaceModule,
    ) -> soil_capnp.types.clients.StreamClient: ...
    @overload
    def as_interface(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule,
    ) -> storage_capnp.types.clients.EntryClient: ...
    @overload
    def as_interface(
        self,
        schema: a_capnp.types.modules._AInterfaceModule,
    ) -> a_capnp.types.clients.AClient: ...
    @overload
    def as_interface(
        self,
        schema: x_capnp.types.modules._XInterfaceModule,
    ) -> x_capnp.types.clients.XClient: ...
    @overload
    def as_interface(
        self,
        schema: x_capnp.types.modules._YInterfaceModule,
    ) -> x_capnp.types.clients.YClient: ...
    @overload
    def as_interface(
        self,
        schema: x_capnp.types.modules._ZInterfaceModule,
    ) -> x_capnp.types.clients.ZClient: ...
    @overload
    def as_interface(
        self,
        schema: _InterfaceSchema | _InterfaceModule,
    ) -> _DynamicCapabilityClient: ...
    def as_interface(
        self,
        schema: _InterfaceSchema | _InterfaceModule,
    ) -> _DynamicCapabilityClient: ...
    @overload
    def as_list(
        self,
        schema: type[monica_management_capnp.types.lists._EventList],
    ) -> monica_management_capnp.types.readers.EventListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_management_capnp.types.lists._KVList],
    ) -> monica_management_capnp.types.readers.KVListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_management_capnp.types.lists._SpecList],
    ) -> monica_management_capnp.types.readers.SpecListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._BoolList],
    ) -> monica_params_capnp.types.readers.BoolListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._DateToValueList],
    ) -> monica_params_capnp.types.readers.DateToValueListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._Float64List],
    ) -> monica_params_capnp.types.readers.Float64ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._Float64ListList],
    ) -> monica_params_capnp.types.readers.Float64ListListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._SoilParametersList],
    ) -> monica_params_capnp.types.readers.SoilParametersListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._SpeciesIdToEmissionList],
    ) -> monica_params_capnp.types.readers.SpeciesIdToEmissionListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._YearToValueList],
    ) -> monica_params_capnp.types.readers.YearToValueListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._YieldComponentList],
    ) -> monica_params_capnp.types.readers.YieldComponentListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._ACDToValueList],
    ) -> monica_state_capnp.types.readers.ACDToValueListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._ACDToValueListList],
    ) -> monica_state_capnp.types.readers.ACDToValueListListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._AOMPropertiesList],
    ) -> monica_state_capnp.types.readers.AOMPropertiesListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._BoolList],
    ) -> monica_state_capnp.types.readers.BoolListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._DateList],
    ) -> monica_state_capnp.types.readers.DateListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._DelayedNMinApplicationParamsList],
    ) -> monica_state_capnp.types.readers.DelayedNMinApplicationParamsListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._Float64List],
    ) -> monica_state_capnp.types.readers.Float64ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._Float64ListList],
    ) -> monica_state_capnp.types.readers.Float64ListListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._SoilLayerStateList],
    ) -> monica_state_capnp.types.readers.SoilLayerStateListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._TextList],
    ) -> monica_state_capnp.types.readers.TextListReader: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._YieldComponentList],
    ) -> monica_state_capnp.types.readers.YieldComponentListReader: ...
    @overload
    def as_list(
        self,
        schema: type[yieldstat_capnp.types.lists._ResultToValueList],
    ) -> yieldstat_capnp.types.readers.ResultToValueListReader: ...
    @overload
    def as_list(
        self,
        schema: type[yieldstat_capnp.types.lists._YearToResultList],
    ) -> yieldstat_capnp.types.readers.YearToResultListReader: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._AlteredList],
    ) -> climate_capnp.types.readers.AlteredListReader: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._DatasetClientList],
    ) -> climate_capnp.types.readers.DatasetClientListReader: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._ElementEnumList],
    ) -> climate_capnp.types.readers.ElementEnumListReader: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._EntryList],
    ) -> climate_capnp.types.readers.EntryListReader: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._Float32List],
    ) -> climate_capnp.types.readers.Float32ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._Float32ListList],
    ) -> climate_capnp.types.readers.Float32ListListReader: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._IdInformationList],
    ) -> climate_capnp.types.readers.IdInformationListReader: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._KVList],
    ) -> climate_capnp.types.readers.KVListReader: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._LocationList],
    ) -> climate_capnp.types.readers.LocationListReader: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._MetaPlusDataList],
    ) -> climate_capnp.types.readers.MetaPlusDataListReader: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._PairList],
    ) -> climate_capnp.types.readers.PairListReader: ...
    @overload
    def as_list(
        self,
        schema: type[
            cluster_admin_service_capnp.types.lists._ModelInstanceFactoryClientList
        ],
    ) -> (
        cluster_admin_service_capnp.types.readers.ModelInstanceFactoryClientListReader
    ): ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._AnyPointerList],
    ) -> common_capnp.types.readers.AnyPointerListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._BoolList],
    ) -> common_capnp.types.readers.BoolListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._DataList],
    ) -> common_capnp.types.readers.DataListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Float32List],
    ) -> common_capnp.types.readers.Float32ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Float64List],
    ) -> common_capnp.types.readers.Float64ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Int16List],
    ) -> common_capnp.types.readers.Int16ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Int32List],
    ) -> common_capnp.types.readers.Int32ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Int64List],
    ) -> common_capnp.types.readers.Int64ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Int8List],
    ) -> common_capnp.types.readers.Int8ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._PairList],
    ) -> common_capnp.types.readers.PairListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._TextList],
    ) -> common_capnp.types.readers.TextListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Uint16List],
    ) -> common_capnp.types.readers.Uint16ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Uint32List],
    ) -> common_capnp.types.readers.Uint32ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Uint64List],
    ) -> common_capnp.types.readers.Uint64ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Uint8List],
    ) -> common_capnp.types.readers.Uint8ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._ValueList],
    ) -> common_capnp.types.readers.ValueListReader: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._EnvironmentModificationList],
    ) -> field_exp_data_capnp.types.readers.EnvironmentModificationListReader: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._FertilizerEventList],
    ) -> field_exp_data_capnp.types.readers.FertilizerEventListReader: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._HarvestEventList],
    ) -> field_exp_data_capnp.types.readers.HarvestEventListReader: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._InitialConditionsLayerList],
    ) -> field_exp_data_capnp.types.readers.InitialConditionsLayerListReader: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._IrrigationEventList],
    ) -> field_exp_data_capnp.types.readers.IrrigationEventListReader: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._PlantingEventList],
    ) -> field_exp_data_capnp.types.readers.PlantingEventListReader: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._PlotList],
    ) -> field_exp_data_capnp.types.readers.PlotListReader: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._TreatmentList],
    ) -> field_exp_data_capnp.types.readers.TreatmentListReader: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._ConfigEntryList],
    ) -> fbp_capnp.types.readers.ConfigEntryListReader: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._KVList],
    ) -> fbp_capnp.types.readers.KVListReader: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._NameAndSRList],
    ) -> fbp_capnp.types.readers.NameAndSRListReader: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._PortList],
    ) -> fbp_capnp.types.readers.PortListReader: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._ReaderClientList],
    ) -> fbp_capnp.types.readers.ReaderClientListReader: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._StartupInfoList],
    ) -> fbp_capnp.types.readers.StartupInfoListReader: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._SturdyRefList],
    ) -> fbp_capnp.types.readers.SturdyRefListReader: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._TextList],
    ) -> fbp_capnp.types.readers.TextListReader: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._WriterClientList],
    ) -> fbp_capnp.types.readers.WriterClientListReader: ...
    @overload
    def as_list(
        self,
        schema: type[grid_capnp.types.lists._AggregationPartList],
    ) -> grid_capnp.types.readers.AggregationPartListReader: ...
    @overload
    def as_list(
        self,
        schema: type[grid_capnp.types.lists._LocationList],
    ) -> grid_capnp.types.readers.LocationListReader: ...
    @overload
    def as_list(
        self,
        schema: type[management_capnp.types.lists._EventList],
    ) -> management_capnp.types.readers.EventListReader: ...
    @overload
    def as_list(
        self,
        schema: type[management_capnp.types.lists._NutrientList],
    ) -> management_capnp.types.readers.NutrientListReader: ...
    @overload
    def as_list(
        self,
        schema: type[management_capnp.types.lists._SpecList],
    ) -> management_capnp.types.readers.SpecListReader: ...
    @overload
    def as_list(
        self,
        schema: type[model_capnp.types.lists._EventList],
    ) -> model_capnp.types.readers.EventListReader: ...
    @overload
    def as_list(
        self,
        schema: type[model_capnp.types.lists._Float64List],
    ) -> model_capnp.types.readers.Float64ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[model_capnp.types.lists._IdentifiableClientList],
    ) -> model_capnp.types.readers.IdentifiableClientListReader: ...
    @overload
    def as_list(
        self,
        schema: type[model_capnp.types.lists._StatList],
    ) -> model_capnp.types.readers.StatListReader: ...
    @overload
    def as_list(
        self,
        schema: type[model_capnp.types.lists._TimeSeriesClientList],
    ) -> model_capnp.types.readers.TimeSeriesClientListReader: ...
    @overload
    def as_list(
        self,
        schema: type[registry_capnp.types.lists._EntryList],
    ) -> registry_capnp.types.readers.EntryListReader: ...
    @overload
    def as_list(
        self,
        schema: type[registry_capnp.types.lists._IdInformationList],
    ) -> registry_capnp.types.readers.IdInformationListReader: ...
    @overload
    def as_list(
        self,
        schema: type[registry_capnp.types.lists._IdentifiableClientList],
    ) -> registry_capnp.types.readers.IdentifiableClientListReader: ...
    @overload
    def as_list(
        self,
        schema: type[registry_capnp.types.lists._TextList],
    ) -> registry_capnp.types.readers.TextListReader: ...
    @overload
    def as_list(
        self,
        schema: type[service_capnp.types.lists._IdInformationList],
    ) -> service_capnp.types.readers.IdInformationListReader: ...
    @overload
    def as_list(
        self,
        schema: type[service_capnp.types.lists._IdentifiableClientList],
    ) -> service_capnp.types.readers.IdentifiableClientListReader: ...
    @overload
    def as_list(
        self,
        schema: type[service_capnp.types.lists._PairList],
    ) -> service_capnp.types.readers.PairListReader: ...
    @overload
    def as_list(
        self,
        schema: type[service_capnp.types.lists._TextList],
    ) -> service_capnp.types.readers.TextListReader: ...
    @overload
    def as_list(
        self,
        schema: type[soil_capnp.types.lists._LayerList],
    ) -> soil_capnp.types.readers.LayerListReader: ...
    @overload
    def as_list(
        self,
        schema: type[soil_capnp.types.lists._ProfileClientList],
    ) -> soil_capnp.types.readers.ProfileClientListReader: ...
    @overload
    def as_list(
        self,
        schema: type[soil_capnp.types.lists._PropertyList],
    ) -> soil_capnp.types.readers.PropertyListReader: ...
    @overload
    def as_list(
        self,
        schema: type[soil_capnp.types.lists._PropertyNameEnumList],
    ) -> soil_capnp.types.readers.PropertyNameEnumListReader: ...
    @overload
    def as_list(
        self,
        schema: type[soil_params_capnp.types.lists._DataList],
    ) -> soil_params_capnp.types.readers.DataListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._BoolList],
    ) -> storage_capnp.types.readers.BoolListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._DataList],
    ) -> storage_capnp.types.readers.DataListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Float32List],
    ) -> storage_capnp.types.readers.Float32ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Float64List],
    ) -> storage_capnp.types.readers.Float64ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._InfoAndContainerList],
    ) -> storage_capnp.types.readers.InfoAndContainerListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Int16List],
    ) -> storage_capnp.types.readers.Int16ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Int32List],
    ) -> storage_capnp.types.readers.Int32ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Int64List],
    ) -> storage_capnp.types.readers.Int64ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Int8List],
    ) -> storage_capnp.types.readers.Int8ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._KeyAndEntryList],
    ) -> storage_capnp.types.readers.KeyAndEntryListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._PairList],
    ) -> storage_capnp.types.readers.PairListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._TextList],
    ) -> storage_capnp.types.readers.TextListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Uint16List],
    ) -> storage_capnp.types.readers.Uint16ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Uint32List],
    ) -> storage_capnp.types.readers.Uint32ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Uint64List],
    ) -> storage_capnp.types.readers.Uint64ListReader: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Uint8List],
    ) -> storage_capnp.types.readers.Uint8ListReader: ...
    def as_list(self, schema: _ListSchema) -> _DynamicListReader: ...
    def as_text(self) -> str: ...

class _DynamicObjectBuilder:
    _parent: Any
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._AutomaticSowingStructModule._AvgSoilTempStructModule,
    ) -> monica_management_capnp.types.builders.AvgSoilTempBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._CuttingStructModule._SpecStructModule,
    ) -> monica_management_capnp.types.builders.SpecBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._DailyWeatherStructModule._KVStructModule,
    ) -> monica_management_capnp.types.builders.KVBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._HarvestStructModule._OptCarbonMgmtDataStructModule,
    ) -> monica_management_capnp.types.builders.OptCarbonMgmtDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._IrrigationStructModule._ParametersStructModule,
    ) -> monica_management_capnp.types.builders.ParamsIrrigationParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._MineralFertilizationStructModule._ParametersStructModule,
    ) -> monica_management_capnp.types.builders.ParamsMineralFertilizationParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._OrganicFertilizationStructModule._OrganicMatterParametersStructModule,
    ) -> monica_management_capnp.types.builders.OrganicMatterParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._OrganicFertilizationStructModule._ParametersStructModule,
    ) -> monica_management_capnp.types.builders.ParamsOrganicFertilizationParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._EmissionsStructModule._SpeciesIdToEmissionStructModule,
    ) -> monica_params_capnp.types.builders.SpeciesIdToEmissionBuilder: ...
    @overload
    def as_struct(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule._ValueStructModule,
    ) -> storage_capnp.types.builders.ValueBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ObserverInterfaceModule._EventStructModule,
    ) -> fbp_capnp.types.builders.EventBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ObserverInterfaceModule._ParamsStructModule,
    ) -> fbp_capnp.types.builders.ChannelObserverParamsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._StatsStructModule,
    ) -> fbp_capnp.types.builders.StatsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._IPStructModule._SysAttributesStructModule._SysAttributesBracketTypeStructModule,
    ) -> fbp_capnp.types.builders.SysAttributesBracketTypeBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._AutomaticSowingStructModule._AvgSoilTempStructModule,
    ) -> management_capnp.types.builders.AvgSoilTempBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._CuttingStructModule._SpecStructModule,
    ) -> management_capnp.types.builders.SpecBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._HarvestStructModule._OptCarbonMgmtDataStructModule,
    ) -> management_capnp.types.builders.OptCarbonMgmtDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._EventStructModule._EventAfterStructModule,
    ) -> monica_management_capnp.types.builders.EventAfterBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._EventStructModule._EventAtStructModule,
    ) -> monica_management_capnp.types.builders.EventAtBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._EventStructModule._EventBetweenStructModule,
    ) -> monica_management_capnp.types.builders.EventBetweenBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._EventStructModule._TypeStructModule,
    ) -> monica_management_capnp.types.builders.TypeBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._AutomaticHarvestStructModule,
    ) -> monica_management_capnp.types.builders.AutomaticHarvestBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._AutomaticSowingStructModule,
    ) -> monica_management_capnp.types.builders.AutomaticSowingBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._CuttingStructModule,
    ) -> monica_management_capnp.types.builders.CuttingBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._DailyWeatherStructModule,
    ) -> monica_management_capnp.types.builders.DailyWeatherBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._HarvestStructModule,
    ) -> monica_management_capnp.types.builders.HarvestBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._IrrigationStructModule,
    ) -> monica_management_capnp.types.builders.IrrigationBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._MineralFertilizationStructModule,
    ) -> monica_management_capnp.types.builders.MineralFertilizationBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._NDemandFertilizationStructModule,
    ) -> monica_management_capnp.types.builders.NDemandFertilizationBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._OrganicFertilizationStructModule,
    ) -> monica_management_capnp.types.builders.OrganicFertilizationBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._SaveStateStructModule,
    ) -> monica_management_capnp.types.builders.SaveStateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._SowingStructModule,
    ) -> monica_management_capnp.types.builders.SowingBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule._TillageStructModule,
    ) -> monica_management_capnp.types.builders.TillageBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._EnvironmentParametersStructModule._YearToValueStructModule,
    ) -> monica_params_capnp.types.builders.YearToValueBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._MeasuredGroundwaterTableInformationStructModule._DateToValueStructModule,
    ) -> monica_params_capnp.types.builders.DateToValueBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._CPDataStructModule,
    ) -> monica_params_capnp.types.builders.CPDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._EmissionsStructModule,
    ) -> monica_params_capnp.types.builders.EmissionsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._EnzymeActivityTStructModule,
    ) -> monica_params_capnp.types.builders.EnzymeActivityTBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._FoliageTStructModule,
    ) -> monica_params_capnp.types.builders.FoliageTBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._LeafEmissionTStructModule,
    ) -> monica_params_capnp.types.builders.LeafEmissionTBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._LeafEmissionsStructModule,
    ) -> monica_params_capnp.types.builders.LeafEmissionsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._MicroClimateDataStructModule,
    ) -> monica_params_capnp.types.builders.MicroClimateDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._PhotosynthTStructModule,
    ) -> monica_params_capnp.types.builders.PhotosynthTBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule._SpeciesDataStructModule,
    ) -> monica_params_capnp.types.builders.SpeciesDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._MonicaModelStateStructModule._ACDToValueStructModule,
    ) -> monica_state_capnp.types.builders.ACDToValueBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilColumnStateStructModule._DelayedNMinApplicationParamsStructModule,
    ) -> monica_state_capnp.types.builders.DelayedNMinApplicationParamsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: yieldstat_capnp.types.modules._OutputStructModule._YearToResultStructModule,
    ) -> yieldstat_capnp.types.builders.YearToResultBuilder: ...
    @overload
    def as_struct(
        self,
        schema: yieldstat_capnp.types.modules._ResultStructModule._ResultToValueStructModule,
    ) -> yieldstat_capnp.types.builders.ResultToValueBuilder: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._HostPortResolverInterfaceModule._RegistrarInterfaceModule._RegisterParamsStructModule,
    ) -> persistence_capnp.types.builders.RegisterParamsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ContainerInterfaceModule._KeyAndEntryStructModule,
    ) -> storage_capnp.types.builders.KeyAndEntryBuilder: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._AlterTimeSeriesWrapperInterfaceModule._AlteredStructModule,
    ) -> climate_capnp.types.builders.AlteredBuilder: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._CSVTimeSeriesFactoryInterfaceModule._CSVConfigStructModule,
    ) -> climate_capnp.types.builders.CSVConfigBuilder: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._LocationStructModule._KVStructModule,
    ) -> climate_capnp.types.builders.KVBuilder: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule._EntryStructModule,
    ) -> climate_capnp.types.builders.EntryBuilder: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule._ValueStructModule,
    ) -> climate_capnp.types.builders.ValueBuilder: ...
    @overload
    def as_struct(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._ZmqPipelineAddressesStructModule,
    ) -> cluster_admin_service_capnp.types.builders.ZmqPipelineAddressesBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._MsgStructModule,
    ) -> fbp_capnp.types.builders.MsgBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StartupInfoStructModule,
    ) -> fbp_capnp.types.builders.StartupInfoBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ComponentStructModule._ComponentFactoryStructModule,
    ) -> fbp_capnp.types.builders.ComponentFactoryBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ComponentStructModule._PortStructModule,
    ) -> fbp_capnp.types.builders.PortBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._IPStructModule._ChunkedDataStructModule,
    ) -> fbp_capnp.types.builders.ChunkedDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._IPStructModule._KVStructModule,
    ) -> fbp_capnp.types.builders.KVBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._IPStructModule._SysAttributesStructModule,
    ) -> fbp_capnp.types.builders.SysAttributesBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._PortInfosStructModule._NameAndSRStructModule,
    ) -> fbp_capnp.types.builders.NameAndSRBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._ActivityInfoStructModule,
    ) -> fbp_capnp.types.builders.ActivityInfoBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._ConfigEntryStructModule,
    ) -> fbp_capnp.types.builders.ConfigEntryBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._RunInfoStructModule,
    ) -> fbp_capnp.types.builders.RunInfoBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._StartChannelsServiceInterfaceModule._ParamsStructModule,
    ) -> fbp_capnp.types.builders.StartChannelsServiceParamsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._AggregationPartStructModule,
    ) -> grid_capnp.types.builders.AggregationPartBuilder: ...
    @overload
    def as_struct(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._LocationStructModule,
    ) -> grid_capnp.types.builders.LocationBuilder: ...
    @overload
    def as_struct(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._ResolutionStructModule,
    ) -> grid_capnp.types.builders.ResolutionBuilder: ...
    @overload
    def as_struct(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._RowColStructModule,
    ) -> grid_capnp.types.builders.RowColBuilder: ...
    @overload
    def as_struct(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._ValueStructModule,
    ) -> grid_capnp.types.builders.ValueBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._EventStructModule._EventAfterStructModule,
    ) -> management_capnp.types.builders.EventAfterBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._EventStructModule._EventAtStructModule,
    ) -> management_capnp.types.builders.EventAtBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._EventStructModule._EventBetweenStructModule,
    ) -> management_capnp.types.builders.EventBetweenBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._EventStructModule._TypeStructModule,
    ) -> management_capnp.types.builders.TypeBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._AutomaticHarvestStructModule,
    ) -> management_capnp.types.builders.AutomaticHarvestBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._AutomaticSowingStructModule,
    ) -> management_capnp.types.builders.AutomaticSowingBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._CuttingStructModule,
    ) -> management_capnp.types.builders.CuttingBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._HarvestStructModule,
    ) -> management_capnp.types.builders.HarvestBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._IrrigationStructModule,
    ) -> management_capnp.types.builders.IrrigationBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._MineralFertilizationStructModule,
    ) -> management_capnp.types.builders.MineralFertilizationBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._NDemandFertilizationStructModule,
    ) -> management_capnp.types.builders.NDemandFertilizationBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._OrganicFertilizationStructModule,
    ) -> management_capnp.types.builders.OrganicFertilizationBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._SowingStructModule,
    ) -> management_capnp.types.builders.SowingBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule._TillageStructModule,
    ) -> management_capnp.types.builders.TillageBuilder: ...
    @overload
    def as_struct(
        self,
        schema: agmip_capnp.types.modules._FieldExperimentDataTemplateStructModule,
    ) -> agmip_capnp.types.builders.FieldExperimentDataTemplateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._EventStructModule,
    ) -> monica_management_capnp.types.builders.EventBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ILRDatesStructModule,
    ) -> monica_management_capnp.types.builders.ILRDatesBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_management_capnp.types.modules._ParamsStructModule,
    ) -> monica_management_capnp.types.builders.ParamsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._AutomaticHarvestParametersStructModule,
    ) -> monica_params_capnp.types.builders.AutomaticHarvestParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._AutomaticIrrigationParametersStructModule,
    ) -> monica_params_capnp.types.builders.AutomaticIrrigationParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._CropModuleParametersStructModule,
    ) -> monica_params_capnp.types.builders.CropModuleParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._CropParametersStructModule,
    ) -> monica_params_capnp.types.builders.CropParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._CropResidueParametersStructModule,
    ) -> monica_params_capnp.types.builders.CropResidueParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._CropSpecStructModule,
    ) -> monica_params_capnp.types.builders.CropSpecBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._CultivarParametersStructModule,
    ) -> monica_params_capnp.types.builders.CultivarParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._EnvironmentParametersStructModule,
    ) -> monica_params_capnp.types.builders.EnvironmentParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._MeasuredGroundwaterTableInformationStructModule,
    ) -> (
        monica_params_capnp.types.builders.MeasuredGroundwaterTableInformationBuilder
    ): ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._NMinApplicationParametersStructModule,
    ) -> monica_params_capnp.types.builders.NMinApplicationParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._NMinCropParametersStructModule,
    ) -> monica_params_capnp.types.builders.NMinCropParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SimulationParametersStructModule,
    ) -> monica_params_capnp.types.builders.SimulationParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SiteParametersStructModule,
    ) -> monica_params_capnp.types.builders.SiteParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SoilMoistureModuleParametersStructModule,
    ) -> monica_params_capnp.types.builders.SoilMoistureModuleParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SoilOrganicModuleParametersStructModule,
    ) -> monica_params_capnp.types.builders.SoilOrganicModuleParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SoilParametersStructModule,
    ) -> monica_params_capnp.types.builders.SoilParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SoilTemperatureModuleParametersStructModule,
    ) -> monica_params_capnp.types.builders.SoilTemperatureModuleParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SoilTransportModuleParametersStructModule,
    ) -> monica_params_capnp.types.builders.SoilTransportModuleParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SpeciesParametersStructModule,
    ) -> monica_params_capnp.types.builders.SpeciesParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._SticsParametersStructModule,
    ) -> monica_params_capnp.types.builders.SticsParametersBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._VocStructModule,
    ) -> monica_params_capnp.types.builders.VocBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_params_capnp.types.modules._YieldComponentStructModule,
    ) -> monica_params_capnp.types.builders.YieldComponentBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._AOMPropertiesStructModule,
    ) -> monica_state_capnp.types.builders.AOMPropertiesBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._CropModuleStateStructModule,
    ) -> monica_state_capnp.types.builders.CropModuleStateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._CropStateStructModule,
    ) -> monica_state_capnp.types.builders.CropStateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._FrostModuleStateStructModule,
    ) -> monica_state_capnp.types.builders.FrostModuleStateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._ICDataStructModule,
    ) -> monica_state_capnp.types.builders.ICDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._MaybeBoolStructModule,
    ) -> monica_state_capnp.types.builders.MaybeBoolBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._MonicaModelStateStructModule,
    ) -> monica_state_capnp.types.builders.MonicaModelStateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._RuntimeStateStructModule,
    ) -> monica_state_capnp.types.builders.RuntimeStateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SnowModuleStateStructModule,
    ) -> monica_state_capnp.types.builders.SnowModuleStateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilColumnStateStructModule,
    ) -> monica_state_capnp.types.builders.SoilColumnStateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilLayerStateStructModule,
    ) -> monica_state_capnp.types.builders.SoilLayerStateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilMoistureModuleStateStructModule,
    ) -> monica_state_capnp.types.builders.SoilMoistureModuleStateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilOrganicModuleStateStructModule,
    ) -> monica_state_capnp.types.builders.SoilOrganicModuleStateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilTemperatureModuleStateStructModule,
    ) -> monica_state_capnp.types.builders.SoilTemperatureModuleStateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: monica_state_capnp.types.modules._SoilTransportModuleStateStructModule,
    ) -> monica_state_capnp.types.builders.SoilTransportModuleStateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: sim_setup_capnp.types.modules._SetupStructModule,
    ) -> sim_setup_capnp.types.builders.SetupBuilder: ...
    @overload
    def as_struct(
        self,
        schema: yieldstat_capnp.types.modules._OutputStructModule,
    ) -> yieldstat_capnp.types.builders.OutputBuilder: ...
    @overload
    def as_struct(
        self,
        schema: yieldstat_capnp.types.modules._RestInputStructModule,
    ) -> yieldstat_capnp.types.builders.RestInputBuilder: ...
    @overload
    def as_struct(
        self,
        schema: yieldstat_capnp.types.modules._ResultStructModule,
    ) -> yieldstat_capnp.types.builders.ResultBuilder: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._AddressStructModule._AddressIp6StructModule,
    ) -> persistence_capnp.types.builders.AddressIp6Builder: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._GatewayInterfaceModule._RegResultsStructModule,
    ) -> persistence_capnp.types.builders.RegResultsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._PersistentInterfaceModule._SaveParamsStructModule,
    ) -> persistence_capnp.types.builders.SaveParamsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._PersistentInterfaceModule._SaveResultsStructModule,
    ) -> persistence_capnp.types.builders.SaveResultsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._RestorerInterfaceModule._RestoreParamsStructModule,
    ) -> persistence_capnp.types.builders.RestoreParamsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._SturdyRefStructModule._OwnerStructModule,
    ) -> persistence_capnp.types.builders.OwnerBuilder: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._SturdyRefStructModule._TokenStructModule,
    ) -> persistence_capnp.types.builders.TokenBuilder: ...
    @overload
    def as_struct(
        self,
        schema: registry_capnp.types.modules._RegistrarInterfaceModule._CrossDomainRestoreStructModule,
    ) -> registry_capnp.types.builders.CrossDomainRestoreBuilder: ...
    @overload
    def as_struct(
        self,
        schema: registry_capnp.types.modules._RegistrarInterfaceModule._RegParamsStructModule,
    ) -> registry_capnp.types.builders.RegParamsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: registry_capnp.types.modules._RegistryInterfaceModule._EntryStructModule,
    ) -> registry_capnp.types.builders.EntryBuilder: ...
    @overload
    def as_struct(
        self,
        schema: service_capnp.types.modules._FactoryInterfaceModule._AccessInfoStructModule,
    ) -> service_capnp.types.builders.AccessInfoBuilder: ...
    @overload
    def as_struct(
        self,
        schema: service_capnp.types.modules._FactoryInterfaceModule._CreateParamsStructModule,
    ) -> service_capnp.types.builders.CreateParamsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: soil_capnp.types.modules._LayerStructModule._PropertyStructModule,
    ) -> soil_capnp.types.builders.PropertyBuilder: ...
    @overload
    def as_struct(
        self,
        schema: soil_capnp.types.modules._QueryStructModule._ResultStructModule,
    ) -> soil_capnp.types.builders.ResultBuilder: ...
    @overload
    def as_struct(
        self,
        schema: soil_params_capnp.types.modules._CapillaryRiseRateStructModule._DataStructModule,
    ) -> soil_params_capnp.types.builders.CapillaryRiseRateDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: soil_params_capnp.types.modules._SoilCharacteristicDataStructModule._DataStructModule,
    ) -> soil_params_capnp.types.builders.SoilCharacteristicDataDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: soil_params_capnp.types.modules._SoilCharacteristicModifierStructModule._DataStructModule,
    ) -> soil_params_capnp.types.builders.SoilCharacteristicModifierDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ImportExportDataStructModule,
    ) -> storage_capnp.types.builders.ImportExportDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._InfoAndContainerStructModule,
    ) -> storage_capnp.types.builders.InfoAndContainerBuilder: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._EnsembleMemberStructModule,
    ) -> climate_capnp.types.builders.EnsembleMemberBuilder: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._LocationStructModule,
    ) -> climate_capnp.types.builders.LocationBuilder: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._MetaPlusDataStructModule,
    ) -> climate_capnp.types.builders.MetaPlusDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule,
    ) -> climate_capnp.types.builders.MetadataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: climate_capnp.types.modules._TimeSeriesDataStructModule,
    ) -> climate_capnp.types.builders.TimeSeriesDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule,
    ) -> cluster_admin_service_capnp.types.builders.ClusterBuilder: ...
    @overload
    def as_struct(
        self,
        schema: common_capnp.types.modules._BlobStructModule,
    ) -> common_capnp.types.builders.BlobBuilder: ...
    @overload
    def as_struct(
        self,
        schema: common_capnp.types.modules._IdInformationStructModule,
    ) -> common_capnp.types.builders.IdInformationBuilder: ...
    @overload
    def as_struct(
        self,
        schema: common_capnp.types.modules._MimeTypesStructModule,
    ) -> common_capnp.types.builders.MimeTypesBuilder: ...
    @overload
    def as_struct(
        self,
        schema: common_capnp.types.modules._PairStructModule,
    ) -> common_capnp.types.builders.PairBuilder: ...
    @overload
    def as_struct(
        self,
        schema: common_capnp.types.modules._StructuredTextStructModule,
    ) -> common_capnp.types.builders.StructuredTextBuilder: ...
    @overload
    def as_struct(
        self,
        schema: common_capnp.types.modules._ValueStructModule,
    ) -> common_capnp.types.builders.ValueBuilder: ...
    @overload
    def as_struct(
        self,
        schema: date_capnp.types.modules._DateStructModule,
    ) -> date_capnp.types.builders.DateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._CultivarStructModule,
    ) -> field_exp_data_capnp.types.builders.CultivarBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._EnvironmentModificationStructModule,
    ) -> field_exp_data_capnp.types.builders.EnvironmentModificationBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._ExperimentDescriptionStructModule,
    ) -> field_exp_data_capnp.types.builders.ExperimentDescriptionBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._FertilizerEventStructModule,
    ) -> field_exp_data_capnp.types.builders.FertilizerEventBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._FieldStructModule,
    ) -> field_exp_data_capnp.types.builders.FieldBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._HarvestEventStructModule,
    ) -> field_exp_data_capnp.types.builders.HarvestEventBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._InitialConditionsLayerStructModule,
    ) -> field_exp_data_capnp.types.builders.InitialConditionsLayerBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._IrrigationEventStructModule,
    ) -> field_exp_data_capnp.types.builders.IrrigationEventBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._MixedTypeStructModule,
    ) -> field_exp_data_capnp.types.builders.MixedTypeBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._PlantingEventStructModule,
    ) -> field_exp_data_capnp.types.builders.PlantingEventBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._PlotStructModule,
    ) -> field_exp_data_capnp.types.builders.PlotBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._ResidueStructModule,
    ) -> field_exp_data_capnp.types.builders.ResidueBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._SoilMetadataStructModule,
    ) -> field_exp_data_capnp.types.builders.SoilMetadataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._TreatmentStructModule,
    ) -> field_exp_data_capnp.types.builders.TreatmentBuilder: ...
    @overload
    def as_struct(
        self,
        schema: field_exp_data_capnp.types.modules._WeatherStationStructModule,
    ) -> field_exp_data_capnp.types.builders.WeatherStationBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ComponentStructModule,
    ) -> fbp_capnp.types.builders.ComponentBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._IIPStructModule,
    ) -> fbp_capnp.types.builders.IIPBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._IPStructModule,
    ) -> fbp_capnp.types.builders.IPBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._LogMessageStructModule,
    ) -> fbp_capnp.types.builders.LogMessageBuilder: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._PortInfosStructModule,
    ) -> fbp_capnp.types.builders.PortInfosBuilder: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._CoordStructModule,
    ) -> geo_capnp.types.builders.CoordBuilder: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._EPSGStructModule,
    ) -> geo_capnp.types.builders.EPSGBuilder: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._GKCoordStructModule,
    ) -> geo_capnp.types.builders.GKCoordBuilder: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._LatLonCoordStructModule,
    ) -> geo_capnp.types.builders.LatLonCoordBuilder: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._Point2DStructModule,
    ) -> geo_capnp.types.builders.Point2DBuilder: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._RectBoundsStructModule,
    ) -> geo_capnp.types.builders.RectBoundsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._RowColStructModule,
    ) -> geo_capnp.types.builders.RowColBuilder: ...
    @overload
    def as_struct(
        self,
        schema: geo_capnp.types.modules._UTMCoordStructModule,
    ) -> geo_capnp.types.builders.UTMCoordBuilder: ...
    @overload
    def as_struct(
        self,
        schema: jobs_capnp.types.modules._JobStructModule,
    ) -> jobs_capnp.types.builders.JobBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._EventStructModule,
    ) -> management_capnp.types.builders.EventBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._NutrientStructModule,
    ) -> management_capnp.types.builders.NutrientBuilder: ...
    @overload
    def as_struct(
        self,
        schema: management_capnp.types.modules._ParamsStructModule,
    ) -> management_capnp.types.builders.ParamsBuilder: ...
    @overload
    def as_struct(
        self,
        schema: model_capnp.types.modules._EnvStructModule,
    ) -> model_capnp.types.builders.EnvBuilder: ...
    @overload
    def as_struct(
        self,
        schema: model_capnp.types.modules._StatStructModule,
    ) -> model_capnp.types.builders.StatBuilder: ...
    @overload
    def as_struct(
        self,
        schema: model_capnp.types.modules._XYPlusResultStructModule,
    ) -> model_capnp.types.builders.XYPlusResultBuilder: ...
    @overload
    def as_struct(
        self,
        schema: model_capnp.types.modules._XYResultStructModule,
    ) -> model_capnp.types.builders.XYResultBuilder: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._AddressStructModule,
    ) -> persistence_capnp.types.builders.AddressBuilder: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._SturdyRefStructModule,
    ) -> persistence_capnp.types.builders.SturdyRefBuilder: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._VatIdStructModule,
    ) -> persistence_capnp.types.builders.VatIdBuilder: ...
    @overload
    def as_struct(
        self,
        schema: persistence_capnp.types.modules._VatPathStructModule,
    ) -> persistence_capnp.types.builders.VatPathBuilder: ...
    @overload
    def as_struct(
        self,
        schema: soil_capnp.types.modules._LayerStructModule,
    ) -> soil_capnp.types.builders.LayerBuilder: ...
    @overload
    def as_struct(
        self,
        schema: soil_capnp.types.modules._ProfileDataStructModule,
    ) -> soil_capnp.types.builders.ProfileDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: soil_capnp.types.modules._QueryStructModule,
    ) -> soil_capnp.types.builders.QueryBuilder: ...
    @overload
    def as_struct(
        self,
        schema: soil_params_capnp.types.modules._CapillaryRiseRateStructModule,
    ) -> soil_params_capnp.types.builders.CapillaryRiseRateBuilder: ...
    @overload
    def as_struct(
        self,
        schema: soil_params_capnp.types.modules._SoilCharacteristicDataStructModule,
    ) -> soil_params_capnp.types.builders.SoilCharacteristicDataBuilder: ...
    @overload
    def as_struct(
        self,
        schema: soil_params_capnp.types.modules._SoilCharacteristicModifierStructModule,
    ) -> soil_params_capnp.types.builders.SoilCharacteristicModifierBuilder: ...
    @overload
    def as_struct(
        self,
        schema: x_capnp.types.modules._SStructModule,
    ) -> x_capnp.types.builders.SBuilder: ...
    @overload
    def as_struct(
        self,
        schema: _StructSchema | _StructModule,
    ) -> _DynamicStructBuilder: ...
    def as_struct(
        self,
        schema: _StructSchema | _StructModule,
    ) -> _DynamicStructBuilder: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._AlterTimeSeriesWrapperInterfaceModule,
    ) -> climate_capnp.types.clients.AlterTimeSeriesWrapperClient: ...
    @overload
    def as_interface(
        self,
        schema: model_capnp.types.modules._EnvInstanceProxyInterfaceModule,
    ) -> model_capnp.types.clients.EnvInstanceProxyClient: ...
    @overload
    def as_interface(
        self,
        schema: model_capnp.types.modules._EnvInstanceInterfaceModule,
    ) -> model_capnp.types.clients.EnvInstanceClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._DatasetInterfaceModule,
    ) -> climate_capnp.types.clients.DatasetClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._ServiceInterfaceModule,
    ) -> climate_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._TimeSeriesInterfaceModule,
    ) -> climate_capnp.types.clients.TimeSeriesClient: ...
    @overload
    def as_interface(
        self,
        schema: common_capnp.types.modules._IdentifiableHolderInterfaceModule,
    ) -> common_capnp.types.clients.IdentifiableHolderClient: ...
    @overload
    def as_interface(
        self,
        schema: crop_capnp.types.modules._CropInterfaceModule,
    ) -> crop_capnp.types.clients.CropClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule,
    ) -> fbp_capnp.types.clients.ChannelClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ReaderInterfaceModule,
    ) -> fbp_capnp.types.clients.ReaderClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._WriterInterfaceModule,
    ) -> fbp_capnp.types.clients.WriterClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule,
    ) -> fbp_capnp.types.clients.ProcessClient: ...
    @overload
    def as_interface(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule,
    ) -> grid_capnp.types.clients.GridClient: ...
    @overload
    def as_interface(
        self,
        schema: jobs_capnp.types.modules._ServiceInterfaceModule,
    ) -> jobs_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: management_capnp.types.modules._FertilizerInterfaceModule,
    ) -> management_capnp.types.clients.FertilizerClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._GatewayInterfaceModule,
    ) -> persistence_capnp.types.clients.GatewayClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._HostPortResolverInterfaceModule,
    ) -> persistence_capnp.types.clients.HostPortResolverClient: ...
    @overload
    def as_interface(
        self,
        schema: soil_capnp.types.modules._ProfileInterfaceModule,
    ) -> soil_capnp.types.clients.ProfileClient: ...
    @overload
    def as_interface(
        self,
        schema: soil_capnp.types.modules._ServiceInterfaceModule,
    ) -> soil_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule,
    ) -> storage_capnp.types.clients.StoreClient: ...
    @overload
    def as_interface(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ContainerInterfaceModule,
    ) -> storage_capnp.types.clients.ContainerClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._AlterTimeSeriesWrapperFactoryInterfaceModule,
    ) -> climate_capnp.types.clients.AlterTimeSeriesWrapperFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._CSVTimeSeriesFactoryInterfaceModule,
    ) -> climate_capnp.types.clients.CSVTimeSeriesFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._AdminMasterInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.AdminMasterClient: ...
    @overload
    def as_interface(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._ModelInstanceFactoryInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.ModelInstanceFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._RuntimeInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.RuntimeClient: ...
    @overload
    def as_interface(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._UserMasterInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.UserMasterClient: ...
    @overload
    def as_interface(
        self,
        schema: common_capnp.types.modules._FactoryInterfaceModule,
    ) -> common_capnp.types.clients.FactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: common_capnp.types.modules._IOFactoryInterfaceModule,
    ) -> common_capnp.types.clients.IOFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: crop_capnp.types.modules._ServiceInterfaceModule,
    ) -> crop_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._FactoryInterfaceModule,
    ) -> fbp_capnp.types.clients.ProcessFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._RunnableInterfaceModule,
    ) -> fbp_capnp.types.clients.RunnableClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._RunnableInterfaceModule._FactoryInterfaceModule,
    ) -> fbp_capnp.types.clients.RunnableFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._StartChannelsServiceInterfaceModule,
    ) -> fbp_capnp.types.clients.StartChannelsServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: management_capnp.types.modules._FertilizerServiceInterfaceModule,
    ) -> management_capnp.types.clients.FertilizerServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: management_capnp.types.modules._ServiceInterfaceModule,
    ) -> management_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: model_capnp.types.modules._ClimateInstanceInterfaceModule,
    ) -> model_capnp.types.clients.ClimateInstanceClient: ...
    @overload
    def as_interface(
        self,
        schema: model_capnp.types.modules._InstanceFactoryInterfaceModule,
    ) -> model_capnp.types.clients.InstanceFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: monica_management_capnp.types.modules._ServiceInterfaceModule,
    ) -> monica_management_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: registry_capnp.types.modules._AdminInterfaceModule,
    ) -> registry_capnp.types.clients.AdminClient: ...
    @overload
    def as_interface(
        self,
        schema: registry_capnp.types.modules._RegistrarInterfaceModule,
    ) -> registry_capnp.types.clients.RegistrarClient: ...
    @overload
    def as_interface(
        self,
        schema: registry_capnp.types.modules._RegistryInterfaceModule,
    ) -> registry_capnp.types.clients.RegistryClient: ...
    @overload
    def as_interface(
        self,
        schema: service_capnp.types.modules._AdminInterfaceModule,
    ) -> service_capnp.types.clients.AdminClient: ...
    @overload
    def as_interface(
        self,
        schema: service_capnp.types.modules._FactoryInterfaceModule,
    ) -> service_capnp.types.clients.FactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: service_capnp.types.modules._SimpleFactoryInterfaceModule,
    ) -> service_capnp.types.clients.SimpleFactoryClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._DatasetInterfaceModule._GetLocationsCallbackInterfaceModule,
    ) -> climate_capnp.types.clients.GetLocationsCallbackClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule._InformationInterfaceModule,
    ) -> climate_capnp.types.clients.InformationClient: ...
    @overload
    def as_interface(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule._SupportedInterfaceModule,
    ) -> climate_capnp.types.clients.SupportedClient: ...
    @overload
    def as_interface(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._UnregisterInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.UnregisterClient: ...
    @overload
    def as_interface(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._ValueHolderInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.ValueHolderClient: ...
    @overload
    def as_interface(
        self,
        schema: common_capnp.types.modules._HolderInterfaceModule,
    ) -> common_capnp.types.clients.HolderClient: ...
    @overload
    def as_interface(
        self,
        schema: common_capnp.types.modules._IdentifiableInterfaceModule,
    ) -> common_capnp.types.clients.IdentifiableClient: ...
    @overload
    def as_interface(
        self,
        schema: config_capnp.types.modules._ServiceInterfaceModule,
    ) -> config_capnp.types.clients.ServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: modam_capnp.types.modules._ModamWrapperServiceInterfaceModule,
    ) -> modam_capnp.types.clients.ModamWrapperServiceClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ObserverInterfaceModule,
    ) -> fbp_capnp.types.clients.ObserverClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ObserverInterfaceModule._UnregisterInterfaceModule,
    ) -> fbp_capnp.types.clients.ChannelObserverUnregisterClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ReaderInterfaceModule._LeaseInterfaceModule,
    ) -> fbp_capnp.types.clients.LeaseClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule,
    ) -> fbp_capnp.types.clients.StatsCallbackClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule,
    ) -> fbp_capnp.types.clients.ChannelStatsCallbackUnregisterClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._ActivityTransitionInterfaceModule,
    ) -> fbp_capnp.types.clients.ActivityTransitionClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._DisconnectInterfaceModule,
    ) -> fbp_capnp.types.clients.DisconnectClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._ProcessHandleInterfaceModule,
    ) -> fbp_capnp.types.clients.ProcessHandleClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._StateTransitionInterfaceModule,
    ) -> fbp_capnp.types.clients.StateTransitionClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._RunnableInterfaceModule._StoppedCallbackInterfaceModule,
    ) -> fbp_capnp.types.clients.StoppedCallbackClient: ...
    @overload
    def as_interface(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._CallbackInterfaceModule,
    ) -> grid_capnp.types.clients.CallbackClient: ...
    @overload
    def as_interface(
        self,
        schema: model_capnp.types.modules._EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule,
    ) -> model_capnp.types.clients.UnregisterClient: ...
    @overload
    def as_interface(
        self,
        schema: web_berest_data_import_capnp.types.modules._DWLABImportInterfaceModule,
    ) -> web_berest_data_import_capnp.types.clients.DWLABImportClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._GatewayRegistrableInterfaceModule,
    ) -> persistence_capnp.types.clients.GatewayRegistrableClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._HeartbeatInterfaceModule,
    ) -> persistence_capnp.types.clients.HeartbeatClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._HostPortResolverInterfaceModule._RegistrarInterfaceModule,
    ) -> persistence_capnp.types.clients.RegistrarClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._PersistentInterfaceModule,
    ) -> persistence_capnp.types.clients.PersistentClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule,
    ) -> persistence_capnp.types.clients.ReleaseSturdyRefClient: ...
    @overload
    def as_interface(
        self,
        schema: persistence_capnp.types.modules._RestorerInterfaceModule,
    ) -> persistence_capnp.types.clients.RestorerClient: ...
    @overload
    def as_interface(
        self,
        schema: registry_capnp.types.modules._RegistrarInterfaceModule._UnregisterInterfaceModule,
    ) -> registry_capnp.types.clients.UnregisterClient: ...
    @overload
    def as_interface(
        self,
        schema: service_capnp.types.modules._StoppableInterfaceModule,
    ) -> service_capnp.types.clients.StoppableClient: ...
    @overload
    def as_interface(
        self,
        schema: soil_capnp.types.modules._ServiceInterfaceModule._StreamInterfaceModule,
    ) -> soil_capnp.types.clients.StreamClient: ...
    @overload
    def as_interface(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule,
    ) -> storage_capnp.types.clients.EntryClient: ...
    @overload
    def as_interface(
        self,
        schema: a_capnp.types.modules._AInterfaceModule,
    ) -> a_capnp.types.clients.AClient: ...
    @overload
    def as_interface(
        self,
        schema: x_capnp.types.modules._XInterfaceModule,
    ) -> x_capnp.types.clients.XClient: ...
    @overload
    def as_interface(
        self,
        schema: x_capnp.types.modules._YInterfaceModule,
    ) -> x_capnp.types.clients.YClient: ...
    @overload
    def as_interface(
        self,
        schema: x_capnp.types.modules._ZInterfaceModule,
    ) -> x_capnp.types.clients.ZClient: ...
    @overload
    def as_interface(
        self,
        schema: _InterfaceSchema | _InterfaceModule,
    ) -> _DynamicCapabilityClient: ...
    def as_interface(
        self,
        schema: _InterfaceSchema | _InterfaceModule,
    ) -> _DynamicCapabilityClient: ...
    @overload
    def as_list(
        self,
        schema: type[monica_management_capnp.types.lists._EventList],
    ) -> monica_management_capnp.types.builders.EventListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_management_capnp.types.lists._KVList],
    ) -> monica_management_capnp.types.builders.KVListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_management_capnp.types.lists._SpecList],
    ) -> monica_management_capnp.types.builders.SpecListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._BoolList],
    ) -> monica_params_capnp.types.builders.BoolListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._DateToValueList],
    ) -> monica_params_capnp.types.builders.DateToValueListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._Float64List],
    ) -> monica_params_capnp.types.builders.Float64ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._Float64ListList],
    ) -> monica_params_capnp.types.builders.Float64ListListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._SoilParametersList],
    ) -> monica_params_capnp.types.builders.SoilParametersListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._SpeciesIdToEmissionList],
    ) -> monica_params_capnp.types.builders.SpeciesIdToEmissionListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._YearToValueList],
    ) -> monica_params_capnp.types.builders.YearToValueListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_params_capnp.types.lists._YieldComponentList],
    ) -> monica_params_capnp.types.builders.YieldComponentListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._ACDToValueList],
    ) -> monica_state_capnp.types.builders.ACDToValueListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._ACDToValueListList],
    ) -> monica_state_capnp.types.builders.ACDToValueListListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._AOMPropertiesList],
    ) -> monica_state_capnp.types.builders.AOMPropertiesListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._BoolList],
    ) -> monica_state_capnp.types.builders.BoolListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._DateList],
    ) -> monica_state_capnp.types.builders.DateListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._DelayedNMinApplicationParamsList],
    ) -> monica_state_capnp.types.builders.DelayedNMinApplicationParamsListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._Float64List],
    ) -> monica_state_capnp.types.builders.Float64ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._Float64ListList],
    ) -> monica_state_capnp.types.builders.Float64ListListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._SoilLayerStateList],
    ) -> monica_state_capnp.types.builders.SoilLayerStateListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._TextList],
    ) -> monica_state_capnp.types.builders.TextListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[monica_state_capnp.types.lists._YieldComponentList],
    ) -> monica_state_capnp.types.builders.YieldComponentListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[yieldstat_capnp.types.lists._ResultToValueList],
    ) -> yieldstat_capnp.types.builders.ResultToValueListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[yieldstat_capnp.types.lists._YearToResultList],
    ) -> yieldstat_capnp.types.builders.YearToResultListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._AlteredList],
    ) -> climate_capnp.types.builders.AlteredListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._DatasetClientList],
    ) -> climate_capnp.types.builders.DatasetClientListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._ElementEnumList],
    ) -> climate_capnp.types.builders.ElementEnumListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._EntryList],
    ) -> climate_capnp.types.builders.EntryListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._Float32List],
    ) -> climate_capnp.types.builders.Float32ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._Float32ListList],
    ) -> climate_capnp.types.builders.Float32ListListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._IdInformationList],
    ) -> climate_capnp.types.builders.IdInformationListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._KVList],
    ) -> climate_capnp.types.builders.KVListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._LocationList],
    ) -> climate_capnp.types.builders.LocationListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._MetaPlusDataList],
    ) -> climate_capnp.types.builders.MetaPlusDataListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[climate_capnp.types.lists._PairList],
    ) -> climate_capnp.types.builders.PairListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[
            cluster_admin_service_capnp.types.lists._ModelInstanceFactoryClientList
        ],
    ) -> (
        cluster_admin_service_capnp.types.builders.ModelInstanceFactoryClientListBuilder
    ): ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._AnyPointerList],
    ) -> common_capnp.types.builders.AnyPointerListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._BoolList],
    ) -> common_capnp.types.builders.BoolListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._DataList],
    ) -> common_capnp.types.builders.DataListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Float32List],
    ) -> common_capnp.types.builders.Float32ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Float64List],
    ) -> common_capnp.types.builders.Float64ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Int16List],
    ) -> common_capnp.types.builders.Int16ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Int32List],
    ) -> common_capnp.types.builders.Int32ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Int64List],
    ) -> common_capnp.types.builders.Int64ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Int8List],
    ) -> common_capnp.types.builders.Int8ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._PairList],
    ) -> common_capnp.types.builders.PairListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._TextList],
    ) -> common_capnp.types.builders.TextListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Uint16List],
    ) -> common_capnp.types.builders.Uint16ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Uint32List],
    ) -> common_capnp.types.builders.Uint32ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Uint64List],
    ) -> common_capnp.types.builders.Uint64ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._Uint8List],
    ) -> common_capnp.types.builders.Uint8ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[common_capnp.types.lists._ValueList],
    ) -> common_capnp.types.builders.ValueListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._EnvironmentModificationList],
    ) -> field_exp_data_capnp.types.builders.EnvironmentModificationListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._FertilizerEventList],
    ) -> field_exp_data_capnp.types.builders.FertilizerEventListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._HarvestEventList],
    ) -> field_exp_data_capnp.types.builders.HarvestEventListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._InitialConditionsLayerList],
    ) -> field_exp_data_capnp.types.builders.InitialConditionsLayerListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._IrrigationEventList],
    ) -> field_exp_data_capnp.types.builders.IrrigationEventListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._PlantingEventList],
    ) -> field_exp_data_capnp.types.builders.PlantingEventListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._PlotList],
    ) -> field_exp_data_capnp.types.builders.PlotListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[field_exp_data_capnp.types.lists._TreatmentList],
    ) -> field_exp_data_capnp.types.builders.TreatmentListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._ConfigEntryList],
    ) -> fbp_capnp.types.builders.ConfigEntryListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._KVList],
    ) -> fbp_capnp.types.builders.KVListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._NameAndSRList],
    ) -> fbp_capnp.types.builders.NameAndSRListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._PortList],
    ) -> fbp_capnp.types.builders.PortListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._ReaderClientList],
    ) -> fbp_capnp.types.builders.ReaderClientListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._StartupInfoList],
    ) -> fbp_capnp.types.builders.StartupInfoListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._SturdyRefList],
    ) -> fbp_capnp.types.builders.SturdyRefListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._TextList],
    ) -> fbp_capnp.types.builders.TextListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[fbp_capnp.types.lists._WriterClientList],
    ) -> fbp_capnp.types.builders.WriterClientListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[grid_capnp.types.lists._AggregationPartList],
    ) -> grid_capnp.types.builders.AggregationPartListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[grid_capnp.types.lists._LocationList],
    ) -> grid_capnp.types.builders.LocationListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[management_capnp.types.lists._EventList],
    ) -> management_capnp.types.builders.EventListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[management_capnp.types.lists._NutrientList],
    ) -> management_capnp.types.builders.NutrientListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[management_capnp.types.lists._SpecList],
    ) -> management_capnp.types.builders.SpecListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[model_capnp.types.lists._EventList],
    ) -> model_capnp.types.builders.EventListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[model_capnp.types.lists._Float64List],
    ) -> model_capnp.types.builders.Float64ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[model_capnp.types.lists._IdentifiableClientList],
    ) -> model_capnp.types.builders.IdentifiableClientListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[model_capnp.types.lists._StatList],
    ) -> model_capnp.types.builders.StatListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[model_capnp.types.lists._TimeSeriesClientList],
    ) -> model_capnp.types.builders.TimeSeriesClientListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[registry_capnp.types.lists._EntryList],
    ) -> registry_capnp.types.builders.EntryListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[registry_capnp.types.lists._IdInformationList],
    ) -> registry_capnp.types.builders.IdInformationListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[registry_capnp.types.lists._IdentifiableClientList],
    ) -> registry_capnp.types.builders.IdentifiableClientListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[registry_capnp.types.lists._TextList],
    ) -> registry_capnp.types.builders.TextListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[service_capnp.types.lists._IdInformationList],
    ) -> service_capnp.types.builders.IdInformationListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[service_capnp.types.lists._IdentifiableClientList],
    ) -> service_capnp.types.builders.IdentifiableClientListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[service_capnp.types.lists._PairList],
    ) -> service_capnp.types.builders.PairListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[service_capnp.types.lists._TextList],
    ) -> service_capnp.types.builders.TextListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[soil_capnp.types.lists._LayerList],
    ) -> soil_capnp.types.builders.LayerListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[soil_capnp.types.lists._ProfileClientList],
    ) -> soil_capnp.types.builders.ProfileClientListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[soil_capnp.types.lists._PropertyList],
    ) -> soil_capnp.types.builders.PropertyListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[soil_capnp.types.lists._PropertyNameEnumList],
    ) -> soil_capnp.types.builders.PropertyNameEnumListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[soil_params_capnp.types.lists._DataList],
    ) -> soil_params_capnp.types.builders.DataListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._BoolList],
    ) -> storage_capnp.types.builders.BoolListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._DataList],
    ) -> storage_capnp.types.builders.DataListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Float32List],
    ) -> storage_capnp.types.builders.Float32ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Float64List],
    ) -> storage_capnp.types.builders.Float64ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._InfoAndContainerList],
    ) -> storage_capnp.types.builders.InfoAndContainerListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Int16List],
    ) -> storage_capnp.types.builders.Int16ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Int32List],
    ) -> storage_capnp.types.builders.Int32ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Int64List],
    ) -> storage_capnp.types.builders.Int64ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Int8List],
    ) -> storage_capnp.types.builders.Int8ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._KeyAndEntryList],
    ) -> storage_capnp.types.builders.KeyAndEntryListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._PairList],
    ) -> storage_capnp.types.builders.PairListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._TextList],
    ) -> storage_capnp.types.builders.TextListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Uint16List],
    ) -> storage_capnp.types.builders.Uint16ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Uint32List],
    ) -> storage_capnp.types.builders.Uint32ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Uint64List],
    ) -> storage_capnp.types.builders.Uint64ListBuilder: ...
    @overload
    def as_list(
        self,
        schema: type[storage_capnp.types.lists._Uint8List],
    ) -> storage_capnp.types.builders.Uint8ListBuilder: ...
    @overload
    def as_list(self, schema: _ListSchema) -> _DynamicListBuilder: ...
    def as_list(self, schema: _ListSchema) -> _DynamicListBuilder: ...
    def set(self, other: Any) -> None:
        """Set value of this object with the value of another AnyPointer::Reader. Don't use this for structs"""
    def set_as_text(self, text: str) -> None: ...
    def init_as_list(self, schema: _ListSchema, size: int) -> _DynamicListBuilder: ...
    def as_text(self) -> str: ...
    def as_reader(self) -> _DynamicObjectReader: ...

class _MessageSize:
    word_count: int
    cap_count: int

    def __init__(self, word_count: int, cap_count: int) -> None: ...

class _DynamicStructReader:
    """Reads Cap'n Proto structs

    This class is almost a 1 for 1 wrapping of the Cap'n Proto C++ DynamicStruct::Reader.
    The only difference is that instead of a `get` method, __getattr__ is overloaded and the field name
    is passed onto the C++ equivalent `get`. This means you just use . syntax to access any field.
    For field names that don't follow valid python naming convention for fields, use the global function
    :py:func:`getattr`::

        person = addressbook.Person.read(file) # This returns a _DynamicStructReader
        print person.name # using . syntax
        print getattr(person, 'field-with-hyphens') # for names that are invalid for python, use getattr
    """

    _parent: Any
    is_root: bool

    def __getattr__(self, field: str) -> Any: ...
    @property
    def which(self) -> _DynamicEnumField:
        """Returns the enum corresponding to the union in this struct

        :rtype: :class:`_DynamicEnumField`
        :return: A string/enum corresponding to what field is set in the union

        :Raises: :exc:`KjException` if this struct doesn't contain a union
        """
    @property
    def schema(self) -> _StructSchema: ...
    @property
    def total_size(self) -> _MessageSize: ...
    def _get(self, field: str) -> Any: ...
    def _get_by_field(self, field: _StructSchemaField) -> Any: ...
    def _has(self, field: str) -> bool: ...
    def _has_by_field(self, field: _StructSchemaField) -> bool: ...
    def get_data_as_view(self, field: str) -> memoryview:
        """Efficiently get a read-only memoryview for a DATA field without copying."""
    def _which_str(self) -> str: ...
    def _which(self) -> _DynamicEnumField:
        """Returns the enum corresponding to the union in this struct

        :rtype: :class:`_DynamicEnumField`
        :return: A string/enum corresponding to what field is set in the union

        :Raises: :exc:`KjException` if this struct doesn't contain a union
        """
    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
    ) -> _DynamicStructBuilder:
        """A method for casting this Reader to a Builder

        This is a copying operation with respect to the message's buffer.
        Changes in the new builder will not reflect in the original reader.

        :type num_first_segment_words: int
        :param num_first_segment_words: Size of the first segment to allocate (in words ie. 8 byte increments)

        :type allocate_seg_callable: Callable[[int], Buffer]
        :param allocate_seg_callable: A python callable object that takes the minimum number of 8-byte
        words to allocate (as an `int`) and returns any object supporting the writable buffer protocol
        (e.g., `bytearray`, `memoryview`, `numpy.ndarray`). This enables custom memory allocation
        strategies including shared memory.

        :rtype: :class:`_DynamicStructBuilder`
        """
    def to_dict(
        self,
        verbose: bool = False,
        ordered: bool = False,
        encode_bytes_as_base64: bool = False,
    ) -> dict[str, Any]: ...

class _DynamicStructBuilder:
    """Builds Cap'n Proto structs

    This class is almost a 1 for 1 wrapping of the Cap'n Proto C++ DynamicStruct::Builder.
    The only difference is that instead of a `get`/`set` method, __getattr__/__setattr__ is overloaded
    and the field name is passed onto the C++ equivalent function.

    This means you just use . syntax to access or set any field. For field names that don't follow valid
    python naming convention for fields, use the global functions :py:func:`getattr`/:py:func:`setattr`::

        person = addressbook.Person.new_message() # This returns a _DynamicStructBuilder

        person.name = 'foo' # using . syntax
        print person.name # using . syntax

        setattr(person, 'field-with-hyphens', 'foo') # for names that are invalid for python, use setattr
        print getattr(person, 'field-with-hyphens') # for names that are invalid for python, use getattr
    """

    _parent: Any
    is_root: bool
    _is_written: bool

    def __getattr__(self, field: str) -> Any: ...
    def __setattr__(self, field: str, value: Any) -> None: ...
    @property
    def which(self) -> _DynamicEnumField:
        """Returns the enum corresponding to the union in this struct

        :rtype: :class:`_DynamicEnumField`
        :return: A string/enum corresponding to what field is set in the union

        :Raises: :exc:`KjException` if this struct doesn't contain a union
        """
    @property
    def schema(self) -> _StructSchema: ...
    @property
    def total_size(self) -> _MessageSize: ...
    def _get(self, field: str) -> Any: ...
    def _get_by_field(self, field: _StructSchemaField) -> Any: ...
    def _set(self, field: str, value: Any) -> None: ...
    def _set_by_field(self, field: _StructSchemaField, value: Any) -> None: ...
    def _has(self, field: str) -> bool: ...
    def _has_by_field(self, field: _StructSchemaField) -> bool: ...
    def init(self, field: str, size: int | None = None) -> Any:
        """Method for initializing fields that are of type union/struct/list

        Typically, you don't have to worry about initializing structs/unions, so this method is mainly for lists.

        :type field: str
        :param field: The field name to initialize

        :type size: int
        :param size: The size of the list to initiialize. This should be None for struct/union initialization.

        :rtype: :class:`_DynamicStructBuilder` or :class:`_DynamicListBuilder`

        :Raises: :exc:`KjException` if the field isn't in this struct
        """
    def _init_by_field(self, field: _StructSchemaField, size: int | None = None) -> Any:
        """Method for initializing fields that are of type union/struct/list

        Typically, you don't have to worry about initializing structs/unions, so this method is mainly for lists.

        :type field: str
        :param field: The field name to initialize

        :type size: int
        :param size: The size of the list to initiialize. This should be None for struct/union initialization.

        :rtype: :class:`_DynamicStructBuilder` or :class:`_DynamicListBuilder`

        :Raises: :exc:`KjException` if the field isn't in this struct
        """
    def init_resizable_list(self, field: str) -> _DynamicResizableListBuilder:
        """Method for initializing fields that are of type list (of structs)

        This version of init returns a :class:`_DynamicResizableListBuilder` that allows
        you to add members one at a time (ie. if you don't know the size for sure).
        This is only meant for lists of Cap'n Proto objects, since for primitive types
        you can just define a normal python list and fill it yourself.

        .. warning::
            You need to call :meth:`_DynamicResizableListBuilder.finish` on the
            list object before serializing the Cap'n Proto message. Failure to do
            so will cause your objects not to be written out as well as leaking
            orphan structs into your message.

        :type field: str
        :param field: The field name to initialize

        :rtype: :class:`_DynamicResizableListBuilder`

        :Raises: :exc:`KjException` if the field isn't in this struct
        """
    def _which_str(self) -> str: ...
    def _which(self) -> _DynamicEnumField:
        """Returns the enum corresponding to the union in this struct

        :rtype: :class:`_DynamicEnumField`
        :return: A string/enum corresponding to what field is set in the union

        :Raises: :exc:`KjException` if this struct doesn't contain a union
        """
    def adopt(self, field: str, orphan: _DynamicOrphan) -> None:
        """A method for adopting Cap'n Proto orphans

        Don't use this method unless you know what you're doing.
        Orphans are useful for dynamically allocating objects for an unknown sized list.

        :type field: str
        :param field: The field name in the struct

        :type orphan: :class:`_DynamicOrphan`
        :param orphan: A Cap'n proto orphan to adopt. It will be unusable after this operation.

        :rtype: void
        """
    def disown(self, field: str) -> _DynamicOrphan:
        """A method for disowning Cap'n Proto orphans

        Don't use this method unless you know what you're doing.

        :type field: str
        :param field: The field name in the struct

        :rtype: :class:`_DynamicOrphan`
        """
    def get_data_as_view(self, field: str) -> memoryview:
        """Efficiently get a writable memoryview for a DATA field without copying.

        This allows in-place modification of the underlying buffer:
        msg.get_data_as_view('myField')[0] = 0xFF
        """
    def as_reader(self) -> _DynamicStructReader:
        """A method for casting this Builder to a Reader

        This is a non-copying operation with respect to the message's buffer.
        This means changes to the fields in the original struct will carry over to the new reader.

        :rtype: :class:`_DynamicStructReader`
        """
    def copy(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], Any] | None = None,
    ) -> _DynamicStructBuilder:
        """A method for copying this Builder

        This is a copying operation with respect to the message's buffer.
        Changes in the new builder will not reflect in the original reader.

        :type num_first_segment_words: int
        :param num_first_segment_words: Size of the first segment to allocate (in words ie. 8 byte increments)

        :type allocate_seg_callable: Callable[[int], Buffer]
        :param allocate_seg_callable: A python callable object that takes the minimum number of 8-byte
        words to allocate (as an `int`) and returns any object supporting the writable buffer protocol
        (e.g., `bytearray`, `memoryview`, `numpy.ndarray`). This enables custom memory allocation
        strategies including shared memory.

        :rtype: :class:`_DynamicStructBuilder`
        """
    def to_dict(
        self,
        verbose: bool = False,
        ordered: bool = False,
        encode_bytes_as_base64: bool = False,
    ) -> dict[str, Any]: ...
    def from_dict(self, d: dict[str, Any]) -> None: ...
    def clear_write_flag(self) -> None:
        """A method used to clear the _is_written flag.

        This allows you to write the struct more than once without seeing any warnings.
        """
    def to_bytes(self) -> bytes:
        """Returns the struct's containing message as a Python bytes object in the unpacked binary format.

        This is inefficient; it makes several copies.

        :rtype: bytes

        :Raises: :exc:`KjException` if this isn't the message's root struct.
        """
    def to_segments(self) -> list[bytes]:
        """Returns the struct's containing message as a Python list of Python bytes objects.

        This avoids making copies.

        NB: This is not currently supported on PyPy.

        :rtype: list
        """
    def _to_bytes_packed_helper(self, word_count: int) -> bytes: ...
    def to_bytes_packed(self) -> bytes: ...
    def write(self, file: IO[Any]) -> None:
        """Writes the struct's containing message to the given file object in unpacked binary format.

        This is a shortcut for calling capnp._write_message_to_fd().  This can only be called on the
        message's root struct.

        :type file: file
        :param file: A file or socket object (or anything with a fileno() method), open for write.

        :rtype: void

        :Raises: :exc:`KjException` if this isn't the message's root struct.
        """
    async def write_async(self, stream: _AsyncIoStream) -> None:
        """Async version of of write().

        This is a shortcut for calling capnp._write_message_to_fd().  This can only be called on the
        message's root struct.

        :type file: AsyncIoStream
        :param file: The AsyncIoStream to write the message to

        :rtype: void

        :Raises: :exc:`KjException` if this isn't the message's root struct.
        """
    def write_packed(self, file: IO[Any]) -> None:
        """Writes the struct's containing message to the given file object in packed binary format.

        This is a shortcut for calling capnp._write_packed_message_to_fd().  This can only be called on
        the message's root struct.

        :type file: file
        :param file: A file or socket object (or anything with a fileno() method), open for write.

        :rtype: void

        :Raises: :exc:`KjException` if this isn't the message's root struct.
        """

class _Request(_DynamicStructBuilder):
    is_consumed: bool

    def send(self) -> _RemotePromise: ...

class _Response(_DynamicStructReader): ...

class _CallContext:
    @property
    def params(self) -> _DynamicStructReader: ...
    @property
    def results(self) -> _DynamicStructBuilder: ...
    def _get_results(self, word_count: int = 0) -> _DynamicStructBuilder: ...
    def release_params(self) -> None: ...
    def tail_call(self, tailRequest: _Request) -> _Promise: ...

class _DynamicCapabilityClient:
    _parent: Any
    _cached_schema: _InterfaceSchema | None

    def __getattr__(self, name: str) -> Any: ...
    @property
    def schema(self) -> _InterfaceSchema: ...
    def _find_method_args(self, method_name: str) -> Any: ...
    def _send_helper(
        self,
        name: str,
        word_count: int | None,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
    ) -> _RemotePromise: ...
    def _request_helper(
        self,
        name: str,
        firstSegmentWordSize: int | None,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
    ) -> _Request: ...
    def _request(
        self,
        name: str,
        *args: Any,
        word_count: int | None = None,
        **kwargs: Any,
    ) -> _Request: ...
    def _send(
        self,
        name: str,
        *args: Any,
        word_count: int | None = None,
        **kwargs: Any,
    ) -> _RemotePromise: ...
    def upcast(
        self,
        schema: _InterfaceSchema | _InterfaceModule,
    ) -> _DynamicCapabilityClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._AlterTimeSeriesWrapperInterfaceModule,
    ) -> climate_capnp.types.clients.AlterTimeSeriesWrapperClient: ...
    @overload
    def cast_as(
        self,
        schema: model_capnp.types.modules._EnvInstanceProxyInterfaceModule,
    ) -> model_capnp.types.clients.EnvInstanceProxyClient: ...
    @overload
    def cast_as(
        self,
        schema: model_capnp.types.modules._EnvInstanceInterfaceModule,
    ) -> model_capnp.types.clients.EnvInstanceClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._DatasetInterfaceModule,
    ) -> climate_capnp.types.clients.DatasetClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._ServiceInterfaceModule,
    ) -> climate_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._TimeSeriesInterfaceModule,
    ) -> climate_capnp.types.clients.TimeSeriesClient: ...
    @overload
    def cast_as(
        self,
        schema: common_capnp.types.modules._IdentifiableHolderInterfaceModule,
    ) -> common_capnp.types.clients.IdentifiableHolderClient: ...
    @overload
    def cast_as(
        self,
        schema: crop_capnp.types.modules._CropInterfaceModule,
    ) -> crop_capnp.types.clients.CropClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule,
    ) -> fbp_capnp.types.clients.ChannelClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ReaderInterfaceModule,
    ) -> fbp_capnp.types.clients.ReaderClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._WriterInterfaceModule,
    ) -> fbp_capnp.types.clients.WriterClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule,
    ) -> fbp_capnp.types.clients.ProcessClient: ...
    @overload
    def cast_as(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule,
    ) -> grid_capnp.types.clients.GridClient: ...
    @overload
    def cast_as(
        self,
        schema: jobs_capnp.types.modules._ServiceInterfaceModule,
    ) -> jobs_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: management_capnp.types.modules._FertilizerInterfaceModule,
    ) -> management_capnp.types.clients.FertilizerClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._GatewayInterfaceModule,
    ) -> persistence_capnp.types.clients.GatewayClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._HostPortResolverInterfaceModule,
    ) -> persistence_capnp.types.clients.HostPortResolverClient: ...
    @overload
    def cast_as(
        self,
        schema: soil_capnp.types.modules._ProfileInterfaceModule,
    ) -> soil_capnp.types.clients.ProfileClient: ...
    @overload
    def cast_as(
        self,
        schema: soil_capnp.types.modules._ServiceInterfaceModule,
    ) -> soil_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule,
    ) -> storage_capnp.types.clients.StoreClient: ...
    @overload
    def cast_as(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ContainerInterfaceModule,
    ) -> storage_capnp.types.clients.ContainerClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._AlterTimeSeriesWrapperFactoryInterfaceModule,
    ) -> climate_capnp.types.clients.AlterTimeSeriesWrapperFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._CSVTimeSeriesFactoryInterfaceModule,
    ) -> climate_capnp.types.clients.CSVTimeSeriesFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._AdminMasterInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.AdminMasterClient: ...
    @overload
    def cast_as(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._ModelInstanceFactoryInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.ModelInstanceFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._RuntimeInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.RuntimeClient: ...
    @overload
    def cast_as(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._UserMasterInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.UserMasterClient: ...
    @overload
    def cast_as(
        self,
        schema: common_capnp.types.modules._FactoryInterfaceModule,
    ) -> common_capnp.types.clients.FactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: common_capnp.types.modules._IOFactoryInterfaceModule,
    ) -> common_capnp.types.clients.IOFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: crop_capnp.types.modules._ServiceInterfaceModule,
    ) -> crop_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._FactoryInterfaceModule,
    ) -> fbp_capnp.types.clients.ProcessFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._RunnableInterfaceModule,
    ) -> fbp_capnp.types.clients.RunnableClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._RunnableInterfaceModule._FactoryInterfaceModule,
    ) -> fbp_capnp.types.clients.RunnableFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._StartChannelsServiceInterfaceModule,
    ) -> fbp_capnp.types.clients.StartChannelsServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: management_capnp.types.modules._FertilizerServiceInterfaceModule,
    ) -> management_capnp.types.clients.FertilizerServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: management_capnp.types.modules._ServiceInterfaceModule,
    ) -> management_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: model_capnp.types.modules._ClimateInstanceInterfaceModule,
    ) -> model_capnp.types.clients.ClimateInstanceClient: ...
    @overload
    def cast_as(
        self,
        schema: model_capnp.types.modules._InstanceFactoryInterfaceModule,
    ) -> model_capnp.types.clients.InstanceFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: monica_management_capnp.types.modules._ServiceInterfaceModule,
    ) -> monica_management_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: registry_capnp.types.modules._AdminInterfaceModule,
    ) -> registry_capnp.types.clients.AdminClient: ...
    @overload
    def cast_as(
        self,
        schema: registry_capnp.types.modules._RegistrarInterfaceModule,
    ) -> registry_capnp.types.clients.RegistrarClient: ...
    @overload
    def cast_as(
        self,
        schema: registry_capnp.types.modules._RegistryInterfaceModule,
    ) -> registry_capnp.types.clients.RegistryClient: ...
    @overload
    def cast_as(
        self,
        schema: service_capnp.types.modules._AdminInterfaceModule,
    ) -> service_capnp.types.clients.AdminClient: ...
    @overload
    def cast_as(
        self,
        schema: service_capnp.types.modules._FactoryInterfaceModule,
    ) -> service_capnp.types.clients.FactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: service_capnp.types.modules._SimpleFactoryInterfaceModule,
    ) -> service_capnp.types.clients.SimpleFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._DatasetInterfaceModule._GetLocationsCallbackInterfaceModule,
    ) -> climate_capnp.types.clients.GetLocationsCallbackClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule._InformationInterfaceModule,
    ) -> climate_capnp.types.clients.InformationClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule._SupportedInterfaceModule,
    ) -> climate_capnp.types.clients.SupportedClient: ...
    @overload
    def cast_as(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._UnregisterInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.UnregisterClient: ...
    @overload
    def cast_as(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._ValueHolderInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.ValueHolderClient: ...
    @overload
    def cast_as(
        self,
        schema: common_capnp.types.modules._HolderInterfaceModule,
    ) -> common_capnp.types.clients.HolderClient: ...
    @overload
    def cast_as(
        self,
        schema: common_capnp.types.modules._IdentifiableInterfaceModule,
    ) -> common_capnp.types.clients.IdentifiableClient: ...
    @overload
    def cast_as(
        self,
        schema: config_capnp.types.modules._ServiceInterfaceModule,
    ) -> config_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: modam_capnp.types.modules._ModamWrapperServiceInterfaceModule,
    ) -> modam_capnp.types.clients.ModamWrapperServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ObserverInterfaceModule,
    ) -> fbp_capnp.types.clients.ObserverClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ObserverInterfaceModule._UnregisterInterfaceModule,
    ) -> fbp_capnp.types.clients.ChannelObserverUnregisterClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ReaderInterfaceModule._LeaseInterfaceModule,
    ) -> fbp_capnp.types.clients.LeaseClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule,
    ) -> fbp_capnp.types.clients.StatsCallbackClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule,
    ) -> fbp_capnp.types.clients.ChannelStatsCallbackUnregisterClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._ActivityTransitionInterfaceModule,
    ) -> fbp_capnp.types.clients.ActivityTransitionClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._DisconnectInterfaceModule,
    ) -> fbp_capnp.types.clients.DisconnectClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._ProcessHandleInterfaceModule,
    ) -> fbp_capnp.types.clients.ProcessHandleClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._StateTransitionInterfaceModule,
    ) -> fbp_capnp.types.clients.StateTransitionClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._RunnableInterfaceModule._StoppedCallbackInterfaceModule,
    ) -> fbp_capnp.types.clients.StoppedCallbackClient: ...
    @overload
    def cast_as(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._CallbackInterfaceModule,
    ) -> grid_capnp.types.clients.CallbackClient: ...
    @overload
    def cast_as(
        self,
        schema: model_capnp.types.modules._EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule,
    ) -> model_capnp.types.clients.UnregisterClient: ...
    @overload
    def cast_as(
        self,
        schema: web_berest_data_import_capnp.types.modules._DWLABImportInterfaceModule,
    ) -> web_berest_data_import_capnp.types.clients.DWLABImportClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._GatewayRegistrableInterfaceModule,
    ) -> persistence_capnp.types.clients.GatewayRegistrableClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._HeartbeatInterfaceModule,
    ) -> persistence_capnp.types.clients.HeartbeatClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._HostPortResolverInterfaceModule._RegistrarInterfaceModule,
    ) -> persistence_capnp.types.clients.RegistrarClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._PersistentInterfaceModule,
    ) -> persistence_capnp.types.clients.PersistentClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule,
    ) -> persistence_capnp.types.clients.ReleaseSturdyRefClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._RestorerInterfaceModule,
    ) -> persistence_capnp.types.clients.RestorerClient: ...
    @overload
    def cast_as(
        self,
        schema: registry_capnp.types.modules._RegistrarInterfaceModule._UnregisterInterfaceModule,
    ) -> registry_capnp.types.clients.UnregisterClient: ...
    @overload
    def cast_as(
        self,
        schema: service_capnp.types.modules._StoppableInterfaceModule,
    ) -> service_capnp.types.clients.StoppableClient: ...
    @overload
    def cast_as(
        self,
        schema: soil_capnp.types.modules._ServiceInterfaceModule._StreamInterfaceModule,
    ) -> soil_capnp.types.clients.StreamClient: ...
    @overload
    def cast_as(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule,
    ) -> storage_capnp.types.clients.EntryClient: ...
    @overload
    def cast_as(
        self,
        schema: a_capnp.types.modules._AInterfaceModule,
    ) -> a_capnp.types.clients.AClient: ...
    @overload
    def cast_as(
        self,
        schema: x_capnp.types.modules._XInterfaceModule,
    ) -> x_capnp.types.clients.XClient: ...
    @overload
    def cast_as(
        self,
        schema: x_capnp.types.modules._YInterfaceModule,
    ) -> x_capnp.types.clients.YClient: ...
    @overload
    def cast_as(
        self,
        schema: x_capnp.types.modules._ZInterfaceModule,
    ) -> x_capnp.types.clients.ZClient: ...
    @overload
    def cast_as(
        self,
        schema: _InterfaceSchema | _InterfaceModule,
    ) -> _DynamicCapabilityClient: ...
    def cast_as(
        self,
        schema: _InterfaceSchema | _InterfaceModule,
    ) -> _DynamicCapabilityClient: ...

class _DynamicCapabilityServer: ...

class _CapabilityClient:
    _parent: Any
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._AlterTimeSeriesWrapperInterfaceModule,
    ) -> climate_capnp.types.clients.AlterTimeSeriesWrapperClient: ...
    @overload
    def cast_as(
        self,
        schema: model_capnp.types.modules._EnvInstanceProxyInterfaceModule,
    ) -> model_capnp.types.clients.EnvInstanceProxyClient: ...
    @overload
    def cast_as(
        self,
        schema: model_capnp.types.modules._EnvInstanceInterfaceModule,
    ) -> model_capnp.types.clients.EnvInstanceClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._DatasetInterfaceModule,
    ) -> climate_capnp.types.clients.DatasetClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._ServiceInterfaceModule,
    ) -> climate_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._TimeSeriesInterfaceModule,
    ) -> climate_capnp.types.clients.TimeSeriesClient: ...
    @overload
    def cast_as(
        self,
        schema: common_capnp.types.modules._IdentifiableHolderInterfaceModule,
    ) -> common_capnp.types.clients.IdentifiableHolderClient: ...
    @overload
    def cast_as(
        self,
        schema: crop_capnp.types.modules._CropInterfaceModule,
    ) -> crop_capnp.types.clients.CropClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule,
    ) -> fbp_capnp.types.clients.ChannelClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ReaderInterfaceModule,
    ) -> fbp_capnp.types.clients.ReaderClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._WriterInterfaceModule,
    ) -> fbp_capnp.types.clients.WriterClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule,
    ) -> fbp_capnp.types.clients.ProcessClient: ...
    @overload
    def cast_as(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule,
    ) -> grid_capnp.types.clients.GridClient: ...
    @overload
    def cast_as(
        self,
        schema: jobs_capnp.types.modules._ServiceInterfaceModule,
    ) -> jobs_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: management_capnp.types.modules._FertilizerInterfaceModule,
    ) -> management_capnp.types.clients.FertilizerClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._GatewayInterfaceModule,
    ) -> persistence_capnp.types.clients.GatewayClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._HostPortResolverInterfaceModule,
    ) -> persistence_capnp.types.clients.HostPortResolverClient: ...
    @overload
    def cast_as(
        self,
        schema: soil_capnp.types.modules._ProfileInterfaceModule,
    ) -> soil_capnp.types.clients.ProfileClient: ...
    @overload
    def cast_as(
        self,
        schema: soil_capnp.types.modules._ServiceInterfaceModule,
    ) -> soil_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule,
    ) -> storage_capnp.types.clients.StoreClient: ...
    @overload
    def cast_as(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ContainerInterfaceModule,
    ) -> storage_capnp.types.clients.ContainerClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._AlterTimeSeriesWrapperFactoryInterfaceModule,
    ) -> climate_capnp.types.clients.AlterTimeSeriesWrapperFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._CSVTimeSeriesFactoryInterfaceModule,
    ) -> climate_capnp.types.clients.CSVTimeSeriesFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._AdminMasterInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.AdminMasterClient: ...
    @overload
    def cast_as(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._ModelInstanceFactoryInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.ModelInstanceFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._RuntimeInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.RuntimeClient: ...
    @overload
    def cast_as(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._UserMasterInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.UserMasterClient: ...
    @overload
    def cast_as(
        self,
        schema: common_capnp.types.modules._FactoryInterfaceModule,
    ) -> common_capnp.types.clients.FactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: common_capnp.types.modules._IOFactoryInterfaceModule,
    ) -> common_capnp.types.clients.IOFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: crop_capnp.types.modules._ServiceInterfaceModule,
    ) -> crop_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._FactoryInterfaceModule,
    ) -> fbp_capnp.types.clients.ProcessFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._RunnableInterfaceModule,
    ) -> fbp_capnp.types.clients.RunnableClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._RunnableInterfaceModule._FactoryInterfaceModule,
    ) -> fbp_capnp.types.clients.RunnableFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._StartChannelsServiceInterfaceModule,
    ) -> fbp_capnp.types.clients.StartChannelsServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: management_capnp.types.modules._FertilizerServiceInterfaceModule,
    ) -> management_capnp.types.clients.FertilizerServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: management_capnp.types.modules._ServiceInterfaceModule,
    ) -> management_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: model_capnp.types.modules._ClimateInstanceInterfaceModule,
    ) -> model_capnp.types.clients.ClimateInstanceClient: ...
    @overload
    def cast_as(
        self,
        schema: model_capnp.types.modules._InstanceFactoryInterfaceModule,
    ) -> model_capnp.types.clients.InstanceFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: monica_management_capnp.types.modules._ServiceInterfaceModule,
    ) -> monica_management_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: registry_capnp.types.modules._AdminInterfaceModule,
    ) -> registry_capnp.types.clients.AdminClient: ...
    @overload
    def cast_as(
        self,
        schema: registry_capnp.types.modules._RegistrarInterfaceModule,
    ) -> registry_capnp.types.clients.RegistrarClient: ...
    @overload
    def cast_as(
        self,
        schema: registry_capnp.types.modules._RegistryInterfaceModule,
    ) -> registry_capnp.types.clients.RegistryClient: ...
    @overload
    def cast_as(
        self,
        schema: service_capnp.types.modules._AdminInterfaceModule,
    ) -> service_capnp.types.clients.AdminClient: ...
    @overload
    def cast_as(
        self,
        schema: service_capnp.types.modules._FactoryInterfaceModule,
    ) -> service_capnp.types.clients.FactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: service_capnp.types.modules._SimpleFactoryInterfaceModule,
    ) -> service_capnp.types.clients.SimpleFactoryClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._DatasetInterfaceModule._GetLocationsCallbackInterfaceModule,
    ) -> climate_capnp.types.clients.GetLocationsCallbackClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule._InformationInterfaceModule,
    ) -> climate_capnp.types.clients.InformationClient: ...
    @overload
    def cast_as(
        self,
        schema: climate_capnp.types.modules._MetadataStructModule._SupportedInterfaceModule,
    ) -> climate_capnp.types.clients.SupportedClient: ...
    @overload
    def cast_as(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._UnregisterInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.UnregisterClient: ...
    @overload
    def cast_as(
        self,
        schema: cluster_admin_service_capnp.types.modules._ClusterStructModule._ValueHolderInterfaceModule,
    ) -> cluster_admin_service_capnp.types.clients.ValueHolderClient: ...
    @overload
    def cast_as(
        self,
        schema: common_capnp.types.modules._HolderInterfaceModule,
    ) -> common_capnp.types.clients.HolderClient: ...
    @overload
    def cast_as(
        self,
        schema: common_capnp.types.modules._IdentifiableInterfaceModule,
    ) -> common_capnp.types.clients.IdentifiableClient: ...
    @overload
    def cast_as(
        self,
        schema: config_capnp.types.modules._ServiceInterfaceModule,
    ) -> config_capnp.types.clients.ServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: modam_capnp.types.modules._ModamWrapperServiceInterfaceModule,
    ) -> modam_capnp.types.clients.ModamWrapperServiceClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ObserverInterfaceModule,
    ) -> fbp_capnp.types.clients.ObserverClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ObserverInterfaceModule._UnregisterInterfaceModule,
    ) -> fbp_capnp.types.clients.ChannelObserverUnregisterClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._ReaderInterfaceModule._LeaseInterfaceModule,
    ) -> fbp_capnp.types.clients.LeaseClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule,
    ) -> fbp_capnp.types.clients.StatsCallbackClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule,
    ) -> fbp_capnp.types.clients.ChannelStatsCallbackUnregisterClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._ActivityTransitionInterfaceModule,
    ) -> fbp_capnp.types.clients.ActivityTransitionClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._DisconnectInterfaceModule,
    ) -> fbp_capnp.types.clients.DisconnectClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._ProcessHandleInterfaceModule,
    ) -> fbp_capnp.types.clients.ProcessHandleClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._StateTransitionInterfaceModule,
    ) -> fbp_capnp.types.clients.StateTransitionClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._RunnableInterfaceModule._StoppedCallbackInterfaceModule,
    ) -> fbp_capnp.types.clients.StoppedCallbackClient: ...
    @overload
    def cast_as(
        self,
        schema: grid_capnp.types.modules._GridInterfaceModule._CallbackInterfaceModule,
    ) -> grid_capnp.types.clients.CallbackClient: ...
    @overload
    def cast_as(
        self,
        schema: model_capnp.types.modules._EnvInstanceProxyInterfaceModule._UnregisterInterfaceModule,
    ) -> model_capnp.types.clients.UnregisterClient: ...
    @overload
    def cast_as(
        self,
        schema: web_berest_data_import_capnp.types.modules._DWLABImportInterfaceModule,
    ) -> web_berest_data_import_capnp.types.clients.DWLABImportClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._GatewayRegistrableInterfaceModule,
    ) -> persistence_capnp.types.clients.GatewayRegistrableClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._HeartbeatInterfaceModule,
    ) -> persistence_capnp.types.clients.HeartbeatClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._HostPortResolverInterfaceModule._RegistrarInterfaceModule,
    ) -> persistence_capnp.types.clients.RegistrarClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._PersistentInterfaceModule,
    ) -> persistence_capnp.types.clients.PersistentClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._PersistentInterfaceModule._ReleaseSturdyRefInterfaceModule,
    ) -> persistence_capnp.types.clients.ReleaseSturdyRefClient: ...
    @overload
    def cast_as(
        self,
        schema: persistence_capnp.types.modules._RestorerInterfaceModule,
    ) -> persistence_capnp.types.clients.RestorerClient: ...
    @overload
    def cast_as(
        self,
        schema: registry_capnp.types.modules._RegistrarInterfaceModule._UnregisterInterfaceModule,
    ) -> registry_capnp.types.clients.UnregisterClient: ...
    @overload
    def cast_as(
        self,
        schema: service_capnp.types.modules._StoppableInterfaceModule,
    ) -> service_capnp.types.clients.StoppableClient: ...
    @overload
    def cast_as(
        self,
        schema: soil_capnp.types.modules._ServiceInterfaceModule._StreamInterfaceModule,
    ) -> soil_capnp.types.clients.StreamClient: ...
    @overload
    def cast_as(
        self,
        schema: storage_capnp.types.modules._StoreInterfaceModule._ContainerInterfaceModule._EntryInterfaceModule,
    ) -> storage_capnp.types.clients.EntryClient: ...
    @overload
    def cast_as(
        self,
        schema: a_capnp.types.modules._AInterfaceModule,
    ) -> a_capnp.types.clients.AClient: ...
    @overload
    def cast_as(
        self,
        schema: x_capnp.types.modules._XInterfaceModule,
    ) -> x_capnp.types.clients.XClient: ...
    @overload
    def cast_as(
        self,
        schema: x_capnp.types.modules._YInterfaceModule,
    ) -> x_capnp.types.clients.YClient: ...
    @overload
    def cast_as(
        self,
        schema: x_capnp.types.modules._ZInterfaceModule,
    ) -> x_capnp.types.clients.ZClient: ...
    @overload
    def cast_as(
        self,
        schema: _InterfaceSchema | _InterfaceModule,
    ) -> _DynamicCapabilityClient: ...
    def cast_as(
        self,
        schema: _InterfaceSchema | _InterfaceModule,
    ) -> _DynamicCapabilityClient: ...

class _Promise:
    def cancel(self) -> None: ...

class _RemotePromise:
    def __getattr__(self, field: str) -> _DynamicStructPipeline: ...
    def __await__(self) -> Iterator[Any]: ...
    @property
    def schema(self) -> _StructSchema: ...
    def _get(self, field: str) -> _DynamicStructPipeline: ...
    def to_dict(
        self,
        verbose: bool = False,
        ordered: bool = False,
        encode_bytes_as_base64: bool = False,
    ) -> dict[str, Any]: ...
    def cancel(self) -> None: ...

class _DynamicStructPipeline:
    """Reads Cap'n Proto structs

    This class is almost a 1 for 1 wrapping of the Cap'n Proto C++ DynamicStruct::Pipeline.
    The only difference is that instead of a `get` method, __getattr__ is overloaded and the
    field name is passed onto the C++ equivalent `get`. This means you just use . syntax to
    access any field. For field names that don't follow valid python naming convention for fields,
    use the global function :py:func:`getattr`::
    """

    _parent: Any

    def __getattr__(self, field: str) -> Any: ...
    @property
    def schema(self) -> _StructSchema: ...
    def _get(self, field: str) -> Any: ...
    def to_dict(
        self,
        verbose: bool = False,
        ordered: bool = False,
        encode_bytes_as_base64: bool = False,
    ) -> dict[str, Any]: ...

class _MessageBuilder:
    """An abstract base class for building Cap'n Proto messages

    .. warning:: Don't ever instantiate this class directly. It is only used for inheritance.
    """

    def __init__(self) -> None: ...
    def init_root(self, schema: _StructModule) -> _DynamicStructBuilder:
        """A method for instantiating Cap'n Proto structs

        You will need to pass in a schema to specify which struct to
        instantiate. Schemas are available in a loaded Cap'n Proto module::

            addressbook = capnp.load('addressbook.capnp')
            ...
            person = message.init_root(addressbook.Person)

        :type schema: Schema
        :param schema: A Cap'n proto schema specifying which struct to instantiate

        :rtype: :class:`_DynamicStructBuilder`
        :return: An object where you will set all the members
        """
    def get_root(self, schema: _StructModule) -> _DynamicStructBuilder:
        """A method for instantiating Cap'n Proto structs, from an already pre-written buffer

        Don't use this method unless you know what you're doing. You probably
        want to use init_root instead::

            addressbook = capnp.load('addressbook.capnp')
            ...
            person = message.init_root(addressbook.Person)
            ...
            person = message.get_root(addressbook.Person)

        :type schema: Schema
        :param schema: A Cap'n proto schema specifying which struct to instantiate

        :rtype: :class:`_DynamicStructBuilder`
        :return: An object where you will set all the members
        """
    def get_root_as_any(self) -> _DynamicObjectBuilder:
        """A method for getting a Cap'n Proto AnyPointer, from an already pre-written buffer

        Don't use this method unless you know what you're doing.

        :rtype: :class:`_DynamicObjectBuilder`
        :return: An AnyPointer that you can set fields in
        """
    def set_root(self, value: Any) -> None:
        """A method for instantiating Cap'n Proto structs by copying from an existing struct

        :type value: :class:`_DynamicStructReader`
        :param value: A Cap'n Proto struct value to copy

        :rtype: void
        """
    def get_segments_for_output(self) -> list[bytes]: ...
    def new_orphan(self, schema: _StructModule) -> _DynamicOrphan:
        """A method for instantiating Cap'n Proto orphans

        Don't use this method unless you know what you're doing.
        Orphans are useful for dynamically allocating objects for an unknown sized list, ie::

            addressbook = capnp.load('addressbook.capnp')
            m = capnp._MallocMessageBuilder()
            alice = m.new_orphan(addressbook.Person)

        :type schema: Schema
        :param schema: A Cap'n proto schema specifying which struct to instantiate

        :rtype: :class:`_DynamicOrphan`
        :return: An orphan representing a :class:`_DynamicStructBuilder`
        """

class _MallocMessageBuilder(_MessageBuilder):
    """The main class for building Cap'n Proto messages

    You will use this class to handle arena allocation of the Cap'n Proto
    messages. You also use this object when you're done assigning to Cap'n
    Proto objects, and wish to serialize them::

        addressbook = capnp.load('addressbook.capnp')
        message = capnp._MallocMessageBuilder()
        person = message.init_root(addressbook.Person)
        person.name = 'alice'
        ...
        f = open('out.txt', 'w')
        _write_message_to_fd(f.fileno(), message)
    """

    def __init__(self, size: int | None = None) -> None: ...

class _PyCustomMessageBuilder(_MessageBuilder):
    """The class for building Cap'n Proto messages,
    with customised memory allocation strategy

    You will use this class if you want to customise the allocateSegment method,
    and define your own memory allocation strategy.
    """

    def __init__(
        self,
        allocate_seg_callable: Callable[[int], Any],
        size: int | None = None,
    ) -> None:
        """The constructor requires you to provide a Python callable object as a parameter.
        This callable object will be invoked in the allocateSegment method of the MessageBuilder
        to allocate memory. The allocated memory will be managed within the MessageBuilder.

        :type allocate_seg_callable: Callable[[int], Buffer]
        :param allocate_seg_callable: A python callable object that takes the minimum number of 8-byte
        words to allocate (as an `int`) and returns any object supporting the writable buffer protocol
        (e.g., `bytearray`, `memoryview`, `numpy.ndarray`). This enables custom memory allocation
        strategies including shared memory.

        Required function signature is like this:
        def __call__(self, minimum_size: int) -> Buffer:

        Where `Buffer` is any object that:
          - Supports the Python buffer protocol (PyObject_GetBuffer)
          - Is writable
        Note that the unit of minimum_size is words, ie. 8 byte increments.

        The underlying memory must remain valid for the lifetime of the MessageBuilder.
        If returning a view (e.g., `memoryview`, `numpy.ndarray`) that wraps external memory,
        the allocator is responsible for properly managing the memory lifecycle。

        Examples:
            # Example 1: Simple bytearray allocator
            class Allocator:
                def __init__(self):
                    self.cur_size = 0
                def __call__(self, minimum_size: int) -> bytearray:
                    size = max(minimum_size, self.cur_size)
                    self.cur_size += size
                    WORD_SIZE = 8
                    byte_count = size * WORD_SIZE
                    return bytearray(byte_count)

            addressbook = capnp.load('addressbook.capnp')
            allocator = Allocator()
            message = capnp._PyCustomMessageBuilder(allocator)
            person = message.init_root(addressbook.Person)

            # Example 2: Shared memory allocator (zero-copy)
            import ctypes

            class ShmAllocator:
                def __init__(self, shm_pool):
                    self.shm = shm_pool
                    self.buffers = []

                def __call__(self, minimum_size: int) -> memoryview:
                    size = minimum_size * 8
                    ptr = self.shm.allocate(size)
                    buffer = (ctypes.c_uint8 * size).from_address(ptr)
                    self.buffers.append(buffer)
                    return memoryview(buffer)

                def release(self):
                    for buffer in self.buffers:
                        ptr = ctypes.addressof(buffer)
                        size = ctypes.sizeof(buffer)
                        self.shm.deallocate(ptr, size)
                    self.buffers.clear()

        :type size: int
        :param size: Size of the first segment to allocate (in words ie. 8 byte increments)

        """

class _MessageReader:
    """An abstract base class for reading Cap'n Proto messages

    .. warning:: Don't ever instantiate this class. It is only used for inheritance.
    """

    _parent: Any

    def __init__(self) -> None: ...
    def get_root(self, schema: _StructModule) -> _DynamicStructReader:
        """A method for instantiating Cap'n Proto structs

        You will need to pass in a schema to specify which struct to
        instantiate. Schemas are available in a loaded Cap'n Proto module::

            addressbook = capnp.load('addressbook.capnp')
            ...
            person = message.get_root(addressbook.Person)

        :type schema: Schema
        :param schema: A Cap'n proto schema specifying which struct to instantiate

        :rtype: :class:`_DynamicStructReader`
        :return: An object with all the data of the read Cap'n Proto message.
            Access members with . syntax.
        """
    def get_root_as_any(self) -> _DynamicObjectReader:
        """A method for getting a Cap'n Proto AnyPointer, from an already pre-written buffer

        Don't use this method unless you know what you're doing.

        :rtype: :class:`_DynamicObjectReader`
        :return: An AnyPointer that you can read from
        """

class _PackedFdMessageReader(_MessageReader):
    """Read a Cap'n Proto message from a file descriptor in a packed manner

    You use this class to for reading message(s) from a file. It's analagous to the inverse of
    :func:`_write_packed_message_to_fd` and :class:`_MessageBuilder`, but in one class.::

        f = open('out.txt')
        message = _PackedFdMessageReader(f)
        person = message.get_root(addressbook.Person)
        print person.name

    :Parameters: - fd (`int`) - A file descriptor
    """

    def __init__(
        self,
        file: IO[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> None: ...

class _StreamFdMessageReader(_MessageReader):
    """Read a Cap'n Proto message from a file descriptor

    You use this class to for reading message(s) from a file. It's analagous to the inverse of
    :func:`_write_message_to_fd` and :class:`_MessageBuilder`, but in one class::

        f = open('out.txt')
        message = _StreamFdMessageReader(f)
        person = message.get_root(addressbook.Person)
        print person.name

    :Parameters: - fd (`int`) - A file descriptor
    """

    def __init__(
        self,
        file: IO[Any],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> None: ...

class SchemaLoader:
    """Class which can be used to construct Schema objects from schema::Nodes as defined in
    schema.capnp.

    This class wraps capnproto/c++/src/capnp/schema-loader.h directly.
    """

    def load(self, reader: _NodeReader) -> _Schema:
        """Loads the given schema node.  Validates the node and throws an exception if invalid.  This
        makes a copy of the schema, so the object passed in can be destroyed after this returns.
        """
    def load_dynamic(self, reader: _DynamicStructReader) -> _Schema:
        """Loads the given schema node with self.load, but converts from a _DynamicStructReader
        first.
        """
    def get(self, id_: int) -> _Schema:
        """Gets the schema for the given ID, throwing an exception if it isn't present."""

class SchemaParser:
    """A class for loading Cap'n Proto schema files.

    Do not use this class unless you're sure you know what you're doing.
    Use the convenience method :func:`load` instead.
    """

    modules_by_id: dict[int, ModuleType]

    def load(
        self,
        file_name: str,
        display_name: str | None = None,
        imports: Sequence[str] = [],
    ) -> ModuleType:
        """Load a Cap'n Proto schema from a file

        You will have to load a schema before you can begin doing anything
        meaningful with this library. Loading a schema is much like loading
        a Python module (and load even returns a `ModuleType`). Once it's been
        loaded, you use it much like any other Module::

            parser = capnp.SchemaParser()
            addressbook = parser.load('addressbook.capnp')
            print addressbook.qux # qux is a top level constant
            # 123
            person = addressbook.Person.new_message()

        :type file_name: str
        :param file_name: A relative or absolute path to a Cap'n Proto schema

        :type display_name: str
        :param display_name: The name internally used by the Cap'n Proto library
            for the loaded schema. By default, it's just os.path.basename(file_name)

        :type imports: list
        :param imports: A list of str directories to add to the import path.

        :rtype: ModuleType
        :return: A module corresponding to the loaded schema. You can access
            parsed schemas and constants with . syntax

        :Raises:
            - :exc:`exceptions.IOError` if `file_name` doesn't exist
            - :exc:`KjException` if the Cap'n Proto C++ library has any problems loading the schema
        """
    def _parse_disk_file(
        self,
        displayName: str,
        diskPath: str,
        imports: Sequence[str],
    ) -> _ParsedSchema: ...

class _DynamicListBuilder:
    """Class for building Cap'n Proto Lists

    This class thinly wraps the C++ Cap'n Proto DynamicList::Bulder class. __getitem__, __setitem__, and __len__
    have been defined properly, so you can treat this class mostly like any other iterable class::

        ...
        person = addressbook.Person.new_message()

        phones = person.init('phones', 2) # This returns a _DynamicListBuilder

        phone = phones[0]
        phone.number = 'foo'
        phone = phones[1]
        phone.number = 'bar'

        for phone in phones:
            print phone.number
    """

    _parent: Any

    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> Any: ...
    def __setitem__(self, index: int, value: Any) -> None: ...
    def _get(self, index: int) -> Any: ...
    def _set(self, index: int, value: Any) -> None: ...
    def adopt(self, index: int, orphan: _DynamicOrphan) -> None:
        """A method for adopting Cap'n Proto orphans

        Don't use this method unless you know what you're doing.
        Orphans are useful for dynamically allocating objects for an unknown sized list.

        :type index: int
        :param index: The index of the element in the list to replace with the newly adopted object

        :type orphan: :class:`_DynamicOrphan`
        :param orphan: A Cap'n proto orphan to adopt. It will be unusable after this operation.

        :rtype: void
        """
    def disown(self, index: int) -> _DynamicOrphan:
        """A method for disowning Cap'n Proto orphans

        Don't use this method unless you know what you're doing.

        :type index: int
        :param index: The index of the element in the list to disown

        :rtype: :class:`_DynamicOrphan`
        """
    def init(self, index: int, size: int) -> Any:
        """A method for initializing an element in a list

        :type index: int
        :param index: The index of the element in the list

        :type size: int
        :param size: Size of the element to be initialized.
        """

class _DynamicListReader:
    """Class for reading Cap'n Proto Lists

    This class thinly wraps the C++ Cap'n Proto DynamicList::Reader class. __getitem__ and __len__
    have been defined properly, so you can treat this class mostly like any other iterable class::

        ...
        person = addressbook.Person.read(file)

        phones = person.phones # This returns a _DynamicListReader

        phone = phones[0]
        print phone.number

        for phone in phones:
            print phone.number
    """

    _parent: Any

    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> Any: ...
    def _get(self, index: int) -> Any: ...

class _DynamicOrphan:
    _parent: Any

    def get(self) -> Any:
        """Returns a python object corresponding to the DynamicValue owned by this orphan

        Use this DynamicValue to set fields inside the orphan
        """

class _DynamicResizableListBuilder:
    """Class for building growable Cap'n Proto Lists

    .. warning::
        You need to call :meth:`finish` on this object before serializing the
        Cap'n Proto message. Failure to do so will cause your objects not to be
        written out as well as leaking orphan structs into your message.

    This class works much like :class:`_DynamicListBuilder`, but it allows growing the list dynamically.
    It is meant for lists of structs, since for primitive types like int or float, you're much better off
    using a normal python list and then serializing straight to a Cap'n Proto list.
    It has __getitem__ and __len__ defined, but not __setitem__::

        ...
        person = addressbook.Person.new_message()

        phones = person.init_resizable_list('phones') # This returns a _DynamicResizableListBuilder

        phone = phones.add()
        phone.number = 'foo'
        phone = phones.add()
        phone.number = 'bar'

        phones.finish()

        f = open('example', 'w')
        person.write(f)
    """

    _parent: Any

    def __init__(
        self,
        parent: _DynamicStructBuilder,
        field: Any,
        schema: Any,
    ) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> Any: ...
    def _get(self, index: int) -> Any: ...
    def add(self) -> Any:
        """A method for adding a new struct to the list

        This will return a struct, in which you can set fields that will be reflected in the serialized
        Cap'n Proto message.

        :rtype: :class:`_DynamicStructBuilder`
        """
    def finish(self) -> None:
        """A method for closing this list and serializing all its members to the message

        If you don't call this method, the items you previously added from this object will leak into the message,
        ie. inaccessible but still taking up space.
        """

class _EventLoop: ...

class TwoPartyClient:
    """TwoPartyClient for RPC Communication

    :param socket: AsyncIoStream
    :param traversal_limit_in_words: Pointer derefence limit (see https://capnproto.org/cxx.html).
    :param nesting_limit: Recursive limit when reading types (see https://capnproto.org/cxx.html).
    """

    def __init__(
        self,
        socket: _AsyncIoStream | None = None,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> None: ...
    def close(self) -> None: ...
    def bootstrap(self) -> _CapabilityClient: ...
    def on_disconnect(self) -> Awaitable[None]: ...

class TwoPartyServer:
    """TwoPartyServer for RPC Communication

    :param socket: AsyncIoStream
    :param bootstrap: Class object defining the implementation of the Cap'n'proto interface.
    :param traversal_limit_in_words: Pointer derefence limit (see https://capnproto.org/cxx.html).
    :param nesting_limit: Recursive limit when reading types (see https://capnproto.org/cxx.html).
    """

    def __init__(
        self,
        socket: _AsyncIoStream | None = None,
        bootstrap: Any = None,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> None: ...
    def close(self) -> None: ...
    def bootstrap(self) -> _CapabilityClient: ...
    def on_disconnect(self) -> Awaitable[None]: ...

class _AsyncIoStream:
    def __init__(self) -> None: ...
    @staticmethod
    async def create_connection(
        host: str | None = None,
        port: int | None = None,
        **kwargs: Any,
    ) -> _AsyncIoStream:
        """Create a TCP connection.

        All parameters given to this function are passed to `asyncio.get_running_loop().create_connection()`.
        See that function for documentation on the possible arguments.
        """
    @staticmethod
    async def create_unix_connection(
        path: str | None = None,
        **kwargs: Any,
    ) -> _AsyncIoStream:
        """Create a Unix socket connection.

        All parameters given to this function are passed to `asyncio.get_running_loop().create_unix_connection()`.
        See that function for documentation on the possible arguments.
        """
    @staticmethod
    async def create_server(
        callback: Callable[[_AsyncIoStream], Awaitable[None]],
        host: str | None = None,
        port: int | None = None,
        **kwargs: Any,
    ) -> asyncio.Server:
        """Create a TCP connection server.

        The `callback` parameter will be called whenever a new connection is made. It receives a `AsyncIoStream`
        instance as its only argument. If the result of `callback` is a coroutine, it will be scheduled as a task.

        This function behaves similarly to `asyncio.get_running_loop().create_server()`. All arguments except
        for `callback` will be passed directly to that function, and the server returned is similar as well.
        See that function for documentation on the possible arguments.
        """
    @staticmethod
    async def create_unix_server(
        callback: Callable[[_AsyncIoStream], Awaitable[None]],
        path: str | None = None,
        **kwargs: Any,
    ) -> asyncio.Server:
        """Create a unix connection server.

        The `callback` parameter will be called whenever a new connection is made. It receives a `AsyncIoStream`
        instance as its only argument. If the result of `callback` is a coroutine, it will be scheduled as a task.

        This function behaves similarly to `asyncio.get_running_loop().create_server()`. All arguments except
        for `callback` will be passed directly to that function, and the server returned is similar as well.
        See that function for documentation on the possible arguments.
        """
    def close(self) -> None: ...
    async def wait_closed(self) -> None: ...

types: ModuleType
_global_schema_parser: SchemaParser | None

def register_type(id: int, klass: type[Any]) -> None: ...
def deregister_all_types() -> None: ...
def void_task_done_callback(method_name: str, fulfiller: Any, task: Any) -> None: ...
def fill_context(
    method_name: str,
    context: _CallContext,
    returned_data: Any,
) -> None: ...
def add_import_hook() -> None:
    """Add a hook to the python import system, so that Cap'n Proto modules are directly importable

    After calling this function, you can use the python import syntax to directly import capnproto schemas.
    This function is automatically called upon first import of `capnp`,
    so you will typically never need to use this function.::

        import capnp
        capnp.add_import_hook()

        import addressbook_capnp
        # equivalent to capnp.load('addressbook.capnp', 'addressbook', sys.path),
        # except it will search for 'addressbook.capnp' in all directories of sys.path
    """

def remove_import_hook() -> None:
    """Remove the import hook, and return python's import to normal"""

def load(
    file_name: str,
    display_name: str | None = None,
    imports: Sequence[str] = [],
) -> ModuleType:
    """Load a Cap'n Proto schema from a file

    You will have to load a schema before you can begin doing anything
    meaningful with this library. Loading a schema is much like loading
    a Python module (and load even returns a `ModuleType`). Once it's been
    loaded, you use it much like any other Module::

        addressbook = capnp.load('addressbook.capnp')
        print addressbook.qux # qux is a top level constant in the addressbook.capnp schema
        # 123
        person = addressbook.Person.new_message()

    :type file_name: str
    :param file_name: A relative or absolute path to a Cap'n Proto schema

    :type display_name: str
    :param display_name: The name internally used by the Cap'n Proto library
        for the loaded schema. By default, it's just os.path.basename(file_name)

    :type imports: list
    :param imports: A list of str directories to add to the import path.

    :rtype: ModuleType
    :return: A module corresponding to the loaded schema. You can access
        parsed schemas and constants with . syntax

    :Raises: :exc:`KjException` if `file_name` doesn't exist
    """

def cleanup_global_schema_parser() -> None:
    """Unloads all of the schema from the current context"""

def read_multiple_bytes_packed(
    buf: Any,
    traversal_limit_in_words: int | None = None,
    nesting_limit: int | None = None,
) -> Iterator[_DynamicStructReader]:
    """Returns an iterable, that when traversed will return Readers for AnyPointer messages.

    :type buf: buffer
    :param buf: Any Python object that supports the buffer interface.

    :type traversal_limit_in_words: int
    :param traversal_limit_in_words: Limits how many total words of data are allowed to be traversed.
                                        Is actually a uint64_t, and values can be up to 2^64-1. Default is 8*1024*1024.

    :type nesting_limit: int
    :param nesting_limit: Limits how many total words of data are allowed to be traversed. Default is 64.

    :rtype: Iterable with elements of :class:`_DynamicStructReader`
    """

def _write_message_to_fd(fd: int, message: _MessageBuilder) -> None:
    """Serialize a Cap'n Proto message to a file descriptor

    You use this method to serialize your message to a file. Please note that
    you must pass a file descriptor (ie. an int), not a file object. Make sure
    you use the proper reader to match this (ie. don't use _PackedFdMessageReader)::

        message = capnp._MallocMessageBuilder()
        ...
        f = open('out.txt', 'w')
        _write_message_to_fd(f.fileno(), message)
        ...
        f = open('out.txt')
        _StreamFdMessageReader(f)

    :type fd: int
    :param fd: A file descriptor

    :type message: :class:`_MessageBuilder`
    :param message: The Cap'n Proto message to serialize

    :rtype: void
    """

def _write_packed_message_to_fd(fd: int, message: _MessageBuilder) -> None:
    """Serialize a Cap'n Proto message to a file descriptor in a packed manner

    You use this method to serialize your message to a file. Please note that
    you must pass a file descriptor (ie. an int), not a file object. Also, note
    the difference in names with _write_message_to_fd. This method uses a different
    serialization specification, and your reader will need to match.::

        message = capnp._MallocMessageBuilder()
        ...
        f = open('out.txt', 'w')
        _write_packed_message_to_fd(f.fileno(), message)
        ...
        f = open('out.txt')
        _PackedFdMessageReader(f)

    :type fd: int
    :param fd: A file descriptor

    :type message: :class:`_MessageBuilder`
    :param message: The Cap'n Proto message to serialize

    :rtype: void
    """

async def run(coro: Awaitable[Any]) -> Any:
    """Ensure that the coroutine runs while the KJ event loop is running

    This is a shortcut for wrapping the coroutine in a :py:meth:`capnp.kj_loop` context manager.

    :param coro: Coroutine to run
    """

def kj_loop() -> contextlib.AbstractAsyncContextManager[None]:
    """Context manager for running the KJ event loop

    As long as the context manager is active it is guaranteed that the KJ event
    loop is running. When the context manager is exited, the KJ event loop is
    shut down properly and pending tasks are cancelled.

    :raises [RuntimeError]: If the KJ event loop is already running (on this thread).

    .. warning:: Every capnp rpc call required a running KJ event loop.
    """

def _init_capnp_api() -> None:
    """Initialize static function pointers for cdef api functions."""
