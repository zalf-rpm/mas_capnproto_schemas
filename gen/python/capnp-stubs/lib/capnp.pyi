from collections.abc import (
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    MutableMapping,
    Sequence,
)
from contextlib import AbstractContextManager, asynccontextmanager
from ssl import SSLContext
from typing import IO, Any, Literal, overload

# Type alias for anypointer to reflect what is really allowed for anypointer inputs
from capnp._internal import CapnpModule as _CapnpModule
from capnp._internal import CapnpTypesModule as _CapnpTypesModule
from capnp._internal import (
    Server as _Server,
)
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

# Import schema.capnp types for precise node property types
# These are _DynamicStructReader at runtime but typed more precisely
from schema_capnp import FieldReader as _SchemaFieldReader
from schema_capnp import NodeReader as _SchemaNodeReader

type AnyPointer = (
    str
    | bytes
    | _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicListBuilder
    | _DynamicListReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)
type Capability = (
    _DynamicCapabilityClient
    | _DynamicCapabilityServer
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)
type AnyStruct = (
    _DynamicStructBuilder
    | _DynamicStructReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)
type AnyList = (
    _DynamicListBuilder
    | _DynamicListReader
    | _DynamicObjectReader
    | _DynamicObjectBuilder
)
type _CapnpModuleType = _CapnpModule

types: _CapnpTypesModule

class KjException(Exception):
    """Exception raised by Cap'n Proto operations.

    KjException is a wrapper of the internal C++ exception type.
    It contains an enum named `Type` and several properties providing
    information about the exception.
    """

    class Type:
        """Exception type enumeration."""

        FAILED: str
        OVERLOADED: str
        DISCONNECTED: str
        UNIMPLEMENTED: str
        OTHER: str
        reverse_mapping: dict[int, str]

    message: str | None
    nature: str | None
    durability: str | None
    wrapper: Any

    def file(self) -> str:
        """Source file where the exception occurred."""

    def line(self) -> int:
        """Line number where the exception occurred."""

    def type(self) -> str | None:
        """Exception type (one of the Type enum values)."""

    def description(self) -> str:
        """Human-readable description of the exception."""

    def __init__(
        self,
        message: str | None = None,
        nature: str | None = None,
        durability: str | None = None,
        wrapper: Any = None,
        type: str | None = None,
    ) -> None: ...
    def _to_python(self) -> Exception:
        """Convert to a more specific Python exception if appropriate."""

class _NestedNodeReader:
    """pycapnp's internal representation of a nested node in a schema.

    This is distinct from schema_capnp.NestedNodeReader which is a _DynamicStructReader.
    This type is returned by _NodeReader.nestedNodes.
    """

    @property
    def id(self) -> int:
        """The ID of the nested node."""

    @property
    def name(self) -> str:
        """The name of the nested node."""

class _List_NestedNode_Reader:
    """pycapnp's internal list of nested nodes.

    This is distinct from schema_capnp list types which are _DynamicListReader.
    """

    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> _NestedNodeReader: ...
    def __iter__(self) -> Iterator[_NestedNodeReader]: ...

class _NodeReader:
    """pycapnp's internal representation of a schema node.

    This is distinct from schema_capnp.NodeReader which is a _DynamicStructReader.
    This type is returned by _Schema.get_proto() and can be passed to SchemaLoader.load().
    """

    @property
    def displayName(self) -> str:
        """The display name of the node."""

    @property
    def id(self) -> int:
        """The unique ID of the node."""

    @property
    def isConst(self) -> bool:
        """Whether this node is a constant."""

    @property
    def isEnum(self) -> bool:
        """Whether this node is an enum."""

    @property
    def isInterface(self) -> bool:
        """Whether this node is an interface."""

    @property
    def isStruct(self) -> bool:
        """Whether this node is a struct."""

    @property
    def nestedNodes(self) -> _List_NestedNode_Reader:
        """List of nested nodes."""

    @property
    def node(self) -> _SchemaNodeReader:
        """Access the underlying schema.capnp Node reader."""

    @property
    def scopeId(self) -> int:
        """The scope ID of this node."""

class _StructSchemaField:
    """pycapnp's internal representation of a field in a struct schema.

    This is distinct from schema_capnp.FieldReader which is a _DynamicStructReader.
    This type is returned by _StructSchema.fields and _StructSchema.fields_list.
    """

    @property
    def proto(self) -> _SchemaFieldReader:
        """The field's schema as a schema.capnp Field reader."""

    @property
    def schema(self) -> _StructSchema | _EnumSchema | _InterfaceSchema | _ListSchema:
        """The schema of the field's type.

        For list fields, this returns a _ListSchema whose elementType describes the list items.
        This property may raise for primitive/unknown types.
        """

class _InterfaceMethod:
    @property
    def param_type(self) -> _StructSchema: ...
    @property
    def result_type(self) -> _StructSchema: ...

class _Schema:
    """Base class for _StructSchema and _ParsedSchema."""

    def as_const_value(self) -> Any: ...
    @property
    def node(self) -> _SchemaNodeReader: ...
    def as_enum(self) -> _EnumSchema: ...
    def as_interface(self) -> _InterfaceSchema: ...
    def as_struct(self) -> _StructSchema: ...
    def get_proto(self) -> _NodeReader: ...

class _ParsedSchema(_Schema):
    def get_nested(self, name: str) -> _ParsedSchema: ...

class _StructSchema(_Schema):
    @property
    def fieldnames(self) -> tuple[str, ...]:
        """A tuple of the field names in the struct."""

    @property
    def union_fields(self) -> tuple[str, ...]:
        """A tuple of the field names in the struct."""

    @property
    def non_union_fields(self) -> tuple[str, ...]:
        """A tuple of the field names in the struct."""

    @property
    def fields(self) -> dict[str, _StructSchemaField]:
        """All of the _StructSchemaField in this schema as a dict."""

    @property
    def fields_list(self) -> list[_StructSchemaField]:
        """All of the _StructSchemaField in this schema as a list."""

class _EnumSchema:
    """Schema for enum types.

    Provides access to enum schema information.
    Only accessible from capnp.lib.capnp, not from capnp directly.
    """

    @property
    def enumerants(self) -> dict[str, int]:
        """The list of enumerants as a dictionary."""

    @property
    def node(self) -> _SchemaNodeReader:
        """The raw schema node."""

class _InterfaceSchema:
    """Schema for interface types.

    Provides access to interface schema information.
    Only accessible from capnp.lib.capnp, not from capnp directly.
    """

    @property
    def method_names(self) -> tuple[str, ...]:
        """A tuple of the function names in the interface."""

    @property
    def method_names_inherited(self) -> set[str]:
        """A set of the function names in the interface, including inherited methods."""

    @property
    def methods(self) -> dict[str, _InterfaceMethod]:
        """A mapping of method names to their respective _InterfaceMethod."""

    @property
    def methods_inherited(self) -> dict[str, _InterfaceMethod]:
        """A mapping of method names to their respective _InterfaceMethod, including inherited methods."""

    @property
    def superclasses(self) -> list[Any]:
        """A list of superclasses for this interface."""
    @property
    def node(self) -> _SchemaNodeReader:
        """The raw schema node."""

class _ListSchema:
    """Schema for list types.

    Can be instantiated to create list schemas for different element types.
    """

    def __init__(
        self,
        schema: (
            _StructSchema
            | _EnumSchema
            | _InterfaceSchema
            | _ListSchema
            | _SchemaType
            | None
        ) = None,
    ) -> None:
        """Create a list schema for the given element type.

        Args:
            schema: Element type schema. Can be:
                - A struct schema (_StructSchema or StructSchema)
                - An enum schema (_EnumSchema)
                - An interface schema (_InterfaceSchema)
                - Another list schema (_ListSchema) for nested lists
                - A primitive type (_SchemaType, e.g., capnp.types.Int8)
                - Any object with a .schema attribute
                - None (creates uninitialized schema)

        """
    @property
    def elementType(
        self,
    ) -> _StructSchema | _EnumSchema | _InterfaceSchema | _ListSchema:
        """The schema of the element type of this list.

        Returns:
            Schema of the list element type:
            - _StructSchema for struct elements
            - _EnumSchema for enum elements
            - _InterfaceSchema for interface elements
            - _ListSchema for nested list elements

        Raises:
            KjException: When the element type is a primitive type (Int32, Text, Bool, etc.)
                with message "Schema type is unknown"

        """

class _StructModule:
    """Module/class for a generated struct type.

    Instances of this class are what you get when you access a struct class from
    a loaded schema (e.g. `addressbook.Person`). The module exposes factory and
    I/O helpers for that struct type.

    Nested types (structs, enums, interfaces) are accessed as attributes, not methods.
    """

    def __init__(self, schema: _StructSchema, name: str) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    @property
    def schema(self) -> _StructSchema: ...
    def new_message(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[[int], bytearray] | None = None,
        **kwargs: Any,
    ) -> _DynamicStructBuilder:
        """Create a new in-memory message builder for this struct type.

        Args:
            num_first_segment_words: Initial size of the first segment in 8-byte words
            allocate_seg_callable: Custom allocator function that takes the minimum
                number of 8-byte words to allocate and returns a bytearray
            **kwargs: Additional keyword arguments

        Returns:
            A builder instance for this struct type

        """

    def read(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader:
        """Read a struct of this type from a file-like object and return a reader.

        Args:
            file: File-like object with a fileno() method (opened file, socket, etc.)
                  Does NOT accept BytesIO or other pure-Python file-like objects
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth

        Returns:
            A reader for this struct type

        """

    def read_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader:
        """Read a packed-format struct from a file-like object and return a reader.

        Args:
            file: File-like object with a fileno() method (opened file, socket, etc.)
                  Does NOT accept BytesIO or other pure-Python file-like objects
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth

        Returns:
            A reader for this struct type

        """

    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> AbstractContextManager[_DynamicStructReader]:
        """Create a reader for this struct type from a bytes buffer (unpacked).

        Returns a context manager that yields a reader. The context manager must be
        used to ensure proper memory management.

        Args:
            buf: Bytes buffer containing the serialized message
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth

        Returns:
            Context manager yielding a reader for this struct type

        Example:
            with Person.from_bytes(data) as reader:
                print(reader.name)

        """

    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[False],
    ) -> AbstractContextManager[_DynamicStructReader]:
        """Create a reader for this struct type from a bytes buffer (unpacked).

        Returns a context manager that yields a reader. The context manager must be
        used to ensure proper memory management.

        Args:
            buf: Bytes buffer containing the serialized message
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth
            builder: If False, returns a reader

        Returns:
            Context manager yielding a reader for this struct type

        Example:
            with Person.from_bytes(data, builder=False) as reader:
                print(reader.name)

        """

    @overload
    def from_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        *,
        builder: Literal[True],
    ) -> AbstractContextManager[_DynamicStructBuilder]:
        """Create a builder for this struct type from a bytes buffer (unpacked).

        Returns a context manager that yields a builder. The context manager must be
        used to ensure proper memory management.

        Args:
            buf: Bytes buffer containing the serialized message
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth
            builder: If True, returns a builder (mutable)

        Returns:
            Context manager yielding a builder for this struct type

        Example:
            with Person.from_bytes(data, builder=True) as builder:
                builder.name = "New Name"

        """

    def from_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader:
        """Create a reader for this struct type from a packed bytes buffer.

        Args:
            buf: Packed bytes buffer containing the serialized message
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth

        Returns:
            A reader for this struct type

        """

    def from_segments(
        self,
        segments: Sequence[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader:
        """Create a reader for this struct type from a list of segment bytes.

        Args:
            segments: List of byte arrays, one for each segment
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth

        Returns:
            A reader for this struct type

        """

    async def read_async(
        self,
        stream: AsyncIoStream,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> _DynamicStructReader:
        """Asynchronously read a struct of this type from an AsyncIoStream.

        Args:
            stream: AsyncIoStream to read from
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth

        Returns:
            A reader for this struct type

        """

    def read_multiple(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[_DynamicStructReader]:
        """Read multiple structs of this type from a file-like object.

        Args:
            file: File-like object with a fileno() method (opened file, socket, etc.)
                  Does NOT accept BytesIO or other pure-Python file-like objects
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth
            skip_copy: If True, skip copying data (use with caution)

        Returns:
            Iterator yielding readers for each message in the file

        """

    def read_multiple_bytes(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[_DynamicStructReader]:
        """Read multiple structs of this type from a bytes buffer.

        Args:
            buf: Bytes buffer containing multiple serialized messages
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth

        Returns:
            Iterator yielding readers for each message in the buffer

        """

    def read_multiple_bytes_packed(
        self,
        buf: bytes,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> Iterator[_DynamicStructReader]:
        """Read multiple packed structs of this type from a bytes buffer.

        Args:
            buf: Packed bytes buffer containing multiple serialized messages
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth

        Returns:
            Iterator yielding readers for each message in the buffer

        """

    def read_multiple_packed(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
        skip_copy: bool = False,
    ) -> Iterator[_DynamicStructReader]:
        """Read multiple packed structs of this type from a file-like object.

        Args:
            file: File-like object with a fileno() method (opened file, socket, etc.)
                  Does NOT accept BytesIO or other pure-Python file-like objects
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth
            skip_copy: If True, skip copying data (use with caution)

        Returns:
            Iterator yielding readers for each message in the file

        """

class _DynamicObjectReader:
    """Reader for Cap'n Proto AnyPointer type.

    This class wraps the Cap'n Proto C++ DynamicObject::Reader.
    AnyPointer can be cast to different pointer types (struct, list, text, interface).
    """

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
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule,
    ) -> fbp_capnp.types.clients.StatsCallbackClient: ...
    @overload
    def as_interface(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule,
    ) -> fbp_capnp.types.clients.UnregisterClient: ...
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
    ) -> _DynamicCapabilityClient:
        """Cast this AnyPointer to an interface capability.

        The return type reflects the provided interface schema when overloads are available.

        Args:
            schema: The interface schema to cast to (e.g., MyInterface.schema).

        Returns:
            A capability client of the interface type.

        Example:
            iface = anyptr.as_interface(MyInterface.schema)  # Returns MyInterface

        """
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
    def as_list(self, schema: _ListSchema) -> Any:
        """Cast this AnyPointer to a list.

        Args:
            schema: The list schema to cast to.

        Returns:
            A list reader.

        """
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
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._StatsStructModule,
    ) -> fbp_capnp.types.readers.StatsReader: ...
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
        schema: common_capnp.types.modules._StructuredTextStructModule._StructuredTextStructureStructModule,
    ) -> common_capnp.types.readers.StructuredTextStructureReader: ...
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
        schema: fbp_capnp.types.modules._IPStructModule._KVStructModule,
    ) -> fbp_capnp.types.readers.KVReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._PortInfosStructModule._NameAndSRStructModule,
    ) -> fbp_capnp.types.readers.NameAndSRReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._ProcessInterfaceModule._ConfigEntryStructModule,
    ) -> fbp_capnp.types.readers.ConfigEntryReader: ...
    @overload
    def as_struct(
        self,
        schema: fbp_capnp.types.modules._StartChannelsServiceInterfaceModule._ParamsStructModule,
    ) -> fbp_capnp.types.readers.ParamsReader: ...
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
        schema: common_capnp.types.modules._IdInformationStructModule,
    ) -> common_capnp.types.readers.IdInformationReader: ...
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
    def as_struct(self, schema: _StructSchema | _StructModule) -> _DynamicStructReader:
        """Cast this AnyPointer to a struct reader.

        The return type reflects the provided struct schema when overloads are available.
        Can accept either the .schema attribute or the struct class itself.

        Args:
            schema: The struct schema or class to cast to (e.g., MyStruct.schema or MyStruct).

        Returns:
            A struct reader of the appropriate type.

        Examples:
            reader = anyptr.as_struct(MyStruct.schema)  # Returns MyStructReader
            reader = anyptr.as_struct(MyStruct)         # Also returns MyStructReader

        """

    def as_text(self) -> str:
        """Cast this AnyPointer to Text (str).

        Returns:
            The text value as a Python string.

        """

class _DynamicObjectBuilder:
    """Builder for Cap'n Proto AnyPointer type.

    This class wraps the Cap'n Proto C++ DynamicObject::Builder.
    AnyPointer can be initialized or cast to different pointer types.
    """

    def as_interface(self, schema: _InterfaceSchema | _InterfaceModule) -> Any:
        """Cast this AnyPointer to an interface capability.

        The return type reflects the provided interface schema when overloads are available.

        Args:
            schema: The interface schema to cast to (e.g., MyInterface.schema).

        Returns:
            A capability client of the interface type.

        Example:
            iface = anyptr.as_interface(MyInterface.schema)  # Returns MyInterface

        """

    def as_list(self, schema: _ListSchema) -> Any:
        """Cast this AnyPointer to a list.

        Args:
            schema: The list schema to cast to.

        Returns:
            A list builder.

        """

    def as_reader(self) -> _DynamicObjectReader:
        """Get a reader view of this builder.

        Returns:
            A reader for this AnyPointer.

        """

    def as_struct(self, schema: _StructSchema | _StructModule) -> _DynamicStructBuilder:
        """Cast this AnyPointer to a struct builder.

        The return type reflects the provided struct schema when overloads are available.
        Can accept either the .schema attribute or the struct class itself.

        Args:
            schema: The struct schema or class to cast to (e.g., MyStruct.schema or MyStruct).

        Returns:
            A struct builder of the appropriate type.

        Examples:
            builder = anyptr.as_struct(MyStruct.schema)  # Returns MyStructBuilder
            builder = anyptr.as_struct(MyStruct)         # Also returns MyStructBuilder

        """

    def as_text(self) -> str:
        """Cast this AnyPointer to Text (str).

        Returns:
            The text value as a Python string.

        """

    def init_as_list(self, schema: _ListSchema, size: int) -> _DynamicListBuilder:
        """Initialize this AnyPointer as a list of the given size.

        Args:
            schema: The list schema.
            size: The number of elements in the list.

        Returns:
            A list builder for the newly initialized list.

        """

    def set(self, other: _DynamicObjectReader) -> None:
        """Set this AnyPointer to a copy of another AnyPointer.

        Note: Don't use this for structs.

        Args:
            other: The AnyPointer reader to copy from.

        """

    def set_as_text(self, text: str) -> None:
        """Set this AnyPointer to a Text value.

        Args:
            text: The text value to set.

        """

class _MessageSize:
    @property
    def cap_count(self) -> int: ...
    @property
    def word_count(self) -> int: ...

class _DynamicStructReader:
    """Reader for Cap'n Proto structs.

    This class is almost a 1:1 wrapping of the Cap'n Proto C++ DynamicStruct::Reader.
    The only difference is that instead of a `get` method, __getattr__ is overloaded and the field name
    is passed onto the C++ equivalent `get`. This means you just use . syntax to access any field.
    For field names that don't follow valid python naming convention for fields, use the global function
    getattr()::

        person = addressbook.Person.read(file)  # This returns a _DynamicStructReader
        print(person.name)  # using . syntax
        print(getattr(person, 'field-with-hyphens'))  # for names that are invalid for python
    """

    @property
    def schema(self) -> _StructSchema: ...
    @property
    def is_root(self) -> bool: ...
    @property
    def total_size(self) -> _MessageSize: ...
    def which(self) -> str:
        """Return the name of the currently set union field.

        Raises:
            KjException: if this struct doesn't contain a union

        """

    def _get(self, field: str) -> Any:
        """Low-level get method for accessing struct fields by name."""

    def __getattr__(self, field: str) -> Any:
        """Access struct fields by name."""

    def _has(self, field: str) -> bool:
        """Check if a field is set (mainly for unions and pointer fields)."""

    def _which(self) -> Any:
        """Return the enum corresponding to the union in this struct.

        Returns:
            A string/enum corresponding to what field is set in the union

        Raises:
            KjException: if this struct doesn't contain a union

        """

    def _which_str(self) -> str:
        """Return the union field name as a string."""

    def as_builder(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[..., Any] | None = None,
    ) -> _DynamicStructBuilder:
        """Convert this reader to a builder (creates a copy).

        Args:
            num_first_segment_words: Size of first segment
            allocate_seg_callable: Custom allocator function

        Returns:
            A builder containing a copy of this struct

        """

    def to_dict(
        self,
        verbose: bool = False,
        ordered: bool = False,
        encode_bytes_as_base64: bool = False,
    ) -> dict[str, Any]:
        """Convert the struct to a Python dictionary.

        Args:
            verbose: Include more details
            ordered: Use OrderedDict for output
            encode_bytes_as_base64: Encode bytes fields as base64 strings

        Returns:
            Dictionary representation of the struct

        """

class _DynamicStructBuilder:
    """Builder for Cap'n Proto structs.

    This class is almost a 1:1 wrapping of the Cap'n Proto C++ DynamicStruct::Builder.
    The only difference is that instead of `get`/`set` methods, __getattr__/__setattr__ is overloaded
    and the field name is passed onto the C++ equivalent function.

    This means you just use . syntax to access or set any field. For field names that don't follow valid
    python naming convention for fields, use the global functions getattr()/setattr()::

        person = addressbook.Person.new_message()  # This returns a _DynamicStructBuilder

        person.name = 'foo'  # using . syntax
        print(person.name)  # using . syntax

        setattr(person, 'field-with-hyphens', 'foo')  # for invalid python names
        print(getattr(person, 'field-with-hyphens'))
    """

    @property
    def schema(self) -> _StructSchema: ...
    @property
    def is_root(self) -> bool: ...
    @property
    def total_size(self) -> _MessageSize: ...
    def which(self) -> str:
        """Return the name of the currently set union field.

        Raises:
            KjException: if this struct doesn't contain a union

        """

    def _get(self, field: str) -> Any:
        """Low-level get method for accessing struct fields by name."""

    def _set(self, field: str, value: Any) -> None:
        """Low-level set method for setting struct fields by name."""

    def _has(self, field: str) -> bool:
        """Check if a field is set (mainly for unions and pointer fields)."""

    def _which(self) -> Any:
        """Return the enum corresponding to the union in this struct.

        Returns:
            A string/enum corresponding to what field is set in the union

        Raises:
            KjException: if this struct doesn't contain a union

        """

    def _which_str(self) -> str:
        """Return the union field name as a string."""

    def as_reader(self) -> _DynamicStructReader:
        """Convert this builder to a reader (read-only view).

        Returns:
            A reader view of this struct

        """

    def adopt(self, field: str, orphan: Any) -> None:
        """Adopt an orphaned message into a field.

        Args:
            field: Field name
            orphan: Orphaned message to adopt

        """

    def disown(self, field: str) -> Any:
        """Disown a field, returning an orphan.

        Args:
            field: Field name

        Returns:
            Orphaned message

        """

    def init(self, field: Any, size: int | None = None) -> Any:
        """Initialize a struct or list field.

        Args:
            field: Field name
            size: Size for list fields

        Returns:
            The initialized field (builder for structs, list builder for lists)

        """

    def init_resizable_list(self, field: Any) -> _DynamicListBuilder:
        """Initialize a resizable list field (for lists of structs).

        This version of init returns a _DynamicResizableListBuilder that allows
        you to add members one at a time (if you don't know the size for sure).
        This is only meant for lists of Cap'n Proto objects, since for primitive types
        you can just define a normal python list and fill it yourself.

        Warning:
            You need to call finish() on the list object before serializing the
            Cap'n Proto message. Failure to do so will cause your objects not to be
            written out as well as leaking orphan structs into your message.

        Args:
            field: Field name

        Returns:
            Resizable list builder

        Raises:
            KjException: if the field isn't in this struct

        """

    def from_dict(self, d: dict[str, Any]) -> None:
        """Populate the struct from a dictionary.

        Args:
            d: Dictionary with field values

        """

    def to_dict(
        self,
        verbose: bool = False,
        ordered: bool = False,
        encode_bytes_as_base64: bool = False,
    ) -> dict[str, Any]:
        """Convert the struct to a Python dictionary.

        Args:
            verbose: Include more details
            ordered: Use OrderedDict for output
            encode_bytes_as_base64: Encode bytes fields as base64 strings

        Returns:
            Dictionary representation of the struct

        """

    def copy(
        self,
        num_first_segment_words: int | None = None,
        allocate_seg_callable: Callable[..., Any] | None = None,
    ) -> _DynamicStructBuilder:
        """Create a deep copy of this struct.

        Args:
            num_first_segment_words: Size of first segment
            allocate_seg_callable: Custom allocator function

        Returns:
            A new builder containing a copy

        """

    def clear_write_flag(self) -> None:
        """Clear the write flag for this struct."""

    def to_bytes(self) -> bytes:
        """Serialize the struct to bytes.

        Returns:
            Serialized message bytes

        """

    def to_bytes_packed(self) -> bytes:
        """Serialize the struct to packed bytes.

        Returns:
            Serialized message bytes (packed format)

        """

    def to_segments(self) -> list[bytes]:
        """Serialize the struct to a list of segment bytes.

        Returns:
            List of segment byte arrays

        """

    def write(self, file: IO[str] | IO[bytes]) -> None:
        """Write the struct to a file.

        Args:
            file: File-like object with a fileno() method (opened file, socket, etc.)
                  Does NOT accept BytesIO or other pure-Python file-like objects

        """

    def write_packed(self, file: IO[str] | IO[bytes]) -> None:
        """Write the struct to a file in packed format.

        Args:
            file: File-like object with a fileno() method (opened file, socket, etc.)
                  Does NOT accept BytesIO or other pure-Python file-like objects

        """

    async def write_async(self, stream: AsyncIoStream) -> None:
        """Asynchronously write the struct to a stream.

        Args:
            stream: AsyncIoStream to write to

        """

# RPC Request/Response Types
class _Request(_DynamicStructBuilder):
    """RPC request builder.

    Extends DynamicStructBuilder with RPC-specific send() method.
    """

    def send(self) -> _Response:
        """Send the RPC request and return a promise for the response.

        Returns:
            Response promise

        """

    def is_consumed(self) -> bool:
        """Check if the request has been consumed (sent).

        Returns:
            True if the request has been sent

        """

class _Response(_DynamicStructReader):
    """RPC response reader.

    Extends DynamicStructReader for reading RPC responses.
    Response objects are also awaitable promises.
    """

class _CallContext:
    """Context for an RPC call on the server side.

    Provides methods for handling server-side RPC calls.

    """

    def params(self) -> _DynamicStructReader: ...
    def release_params(self) -> None:
        """Release the parameter struct.

        Call this when you're done reading the parameters to allow
        the message memory to be freed.
        """

    def tail_call(self, tailRequest: _Request) -> None:
        """Perform a tail call to another capability.

        Args:
            tailRequest: Request to tail call

        """

# Capability Types
class _DynamicCapabilityClient(_CapabilityClient):
    """Dynamic capability client.

    Represents a reference to a remote capability.
    This is the base class for all generated capability client classes.
    """

    @property
    def schema(self) -> _InterfaceSchema: ...
    def upcast(
        self,
        schema: _InterfaceSchema | _InterfaceModule,
    ) -> _DynamicCapabilityClient:
        """Upcast this capability to a parent interface type.

        Args:
            schema: Parent interface type

        Returns:
            Capability upcast to the parent interface

        """

class _DynamicCapabilityServer:
    """Dynamic capability server base class.

    Implement this to create server-side capability implementations.
    """

class _CapabilityClient:
    """Base class for capability clients.

    Wraps Cap'n Proto capability references.
    """

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
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule,
    ) -> fbp_capnp.types.clients.StatsCallbackClient: ...
    @overload
    def cast_as(
        self,
        schema: fbp_capnp.types.modules._ChannelInterfaceModule._StatsCallbackInterfaceModule._UnregisterInterfaceModule,
    ) -> fbp_capnp.types.clients.UnregisterClient: ...
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
    ) -> _DynamicCapabilityClient:
        """Cast this capability to a specific interface type.

        Args:
            schema: Interface schema or module to cast to

        Returns:
            Capability cast to the specified interface

        """

class _Promise:
    """Promise for asynchronous RPC results.

    Represents a promise for a future value in Cap'n Proto RPC.
    Can be awaited in async contexts.
    """

    def cancel(self) -> None:
        """Cancel the promise."""

class _RemotePromise(_Promise):
    """Remote promise for asynchronous RPC results.

    Extended promise type that provides additional methods for
    accessing pipelined capabilities.
    """

    def to_dict(
        self,
        verbose: bool = False,
        ordered: bool = False,
        encode_bytes_as_base64: bool = False,
    ) -> dict[str, Any]:
        """Convert the promise result to a dictionary.

        Args:
            verbose: Include more details
            ordered: Use OrderedDict for output
            encode_bytes_as_base64: Encode bytes fields as base64 strings

        Returns:
            Dictionary representation

        """

class _DynamicStructPipeline:
    """Pipeline for pipelined RPC calls on struct results.

    This class is almost a 1:1 wrapping of the Cap'n Proto C++ DynamicStruct::Pipeline.
    The only difference is that instead of a `get` method, __getattr__ is overloaded and the
    field name is passed onto the C++ equivalent `get`. This means you just use . syntax to
    access any field. For field names that don't follow valid python naming convention for fields,
    use the global function getattr()::

        # Pipeline calls allow you to call methods on results before they arrive
        result = remote_object.method()
        result.field.another_method()  # Pipelined call
    """

    def to_dict(
        self,
        verbose: bool = False,
        ordered: bool = False,
        encode_bytes_as_base64: bool = False,
    ) -> dict[str, Any]:
        """Convert to dictionary when the pipeline resolves.

        Args:
            verbose: Include more details
            ordered: Use OrderedDict for output
            encode_bytes_as_base64: Encode bytes fields as base64 strings

        Returns:
            Dictionary representation

        """

# Message Builder/Reader Types
class _MessageBuilder:
    """Abstract base class for building Cap'n Proto messages.

    Warning:
        Don't ever instantiate this class directly. It is only used for inheritance.

    """

    def init_root(self, schema: _StructSchema) -> Any:
        """Initialize the message root as a struct of the given type.

        Args:
            schema: The struct schema to use for the root

        Returns:
            A builder for the root struct

        """

    def get_root(self, schema: _StructSchema) -> Any:
        """Get the message root as a struct of the given type.

        Args:
            schema: The struct schema to use for the root

        Returns:
            A reader for the root struct

        """

    def get_root_as_any(self) -> _DynamicObjectBuilder:
        """Get the message root as an AnyPointer.

        Returns:
            An AnyPointer builder for the root

        """

    def set_root(self, value: _DynamicStructReader) -> None:
        """Set the message root by copying from a struct reader.

        Args:
            value: The struct reader to copy from

        """

    def new_orphan(self, schema: _StructSchema) -> Any:
        """Create a new orphaned struct.

        Don't use this method unless you know what you're doing.

        Args:
            schema: The struct schema for the orphan

        Returns:
            An orphaned struct

        """

    def get_segments_for_output(self) -> list[bytes]:
        """Get the message segments as a list of bytes.

        Returns:
            List of segment byte arrays

        """

class _MallocMessageBuilder(_MessageBuilder):
    """The main class for building Cap'n Proto messages.

    You will use this class to handle arena allocation of Cap'n Proto
    messages. You also use this object when you're done assigning to Cap'n
    Proto objects, and wish to serialize them::

        addressbook = capnp.load('addressbook.capnp')
        message = capnp._MallocMessageBuilder()
        person = message.init_root(addressbook.Person)
        person.name = 'alice'
        ...
        f = open('out.txt', 'w')
        capnp._write_message_to_fd(f.fileno(), message)
    """

    def __init__(self, size: int | None = None) -> None:
        """Create a new message builder.

        Args:
            size: Optional initial size for the first segment (in words)

        """

class _MessageReader:
    """Abstract base class for reading Cap'n Proto messages.

    Warning:
        Don't ever instantiate this class. It is only used for inheritance.

    """

    def get_root(self, schema: _StructSchema) -> Any:
        """Get the message root as a struct of the given type.

        Args:
            schema: The struct schema to use for the root

        Returns:
            A reader for the root struct

        """

    def get_root_as_any(self) -> _DynamicObjectReader:
        """Get the message root as an AnyPointer.

        Returns:
            An AnyPointer reader for the root

        """

class _PackedFdMessageReader(_MessageReader):
    """Read a Cap'n Proto message from a file descriptor in packed format.

    This class reads messages that were written with _write_packed_message_to_fd.
    """

    def __init__(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> None:
        """Create a reader from a file object.

        Args:
            file: File object with a fileno() method (opened file, socket, etc.)
                  Does NOT accept BytesIO or other pure-Python file-like objects
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth

        """

class _StreamFdMessageReader(_MessageReader):
    """Read a Cap'n Proto message from a file descriptor in stream format.

    This class reads messages that were written with _write_message_to_fd.
    """

    def __init__(
        self,
        file: IO[str] | IO[bytes],
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> None:
        """Create a reader from a file object.

        Args:
            file: File object with a fileno() method (opened file, socket, etc.)
                  Does NOT accept BytesIO or other pure-Python file-like objects
            traversal_limit_in_words: Optional limit on pointer dereferences
            nesting_limit: Optional limit on nesting depth

        """

class _PyCustomMessageBuilder(_MessageBuilder):
    """Custom message builder with user-provided segments.

    This allows building messages with custom memory management.
    """

    def __init__(self, allocate_seg_callable: Callable[[int], bytearray]) -> None:
        """Create a message builder with custom memory allocation.

        Args:
            allocate_seg_callable: A callable that takes the minimum number of 8-byte
                words to allocate (as an int) and returns a bytearray. This is used to
                customize the memory allocation strategy.

        """

class SchemaParser:
    """Parser for loading Cap'n Proto schema files.

    Do not use this class unless you're sure you know what you're doing.
    Use the convenience method :func:`load` instead.
    """

    modules_by_id: MutableMapping[int, Any]  # Maps ID to loaded module
    def load(
        self,
        file_name: str,
        display_name: str | None = None,
        imports: Sequence[str] = [],
    ) -> _CapnpModule:
        """Load a Cap'n Proto schema file.

        Args:
            file_name: Path to the .capnp file
            display_name: Optional display name for the module
            imports: List of import paths for resolving imports

        Returns:
            Loaded module (types.ModuleType with extra attributes like .schema)

        """
    def _parse_disk_file(
        self,
        display_name: str,
        file_name: str,
        imports: Sequence[str],
    ) -> _ParsedSchema: ...

class SchemaLoader:
    """Class for constructing Schema objects from schema::Nodes.

    Wraps capnproto/c++/src/capnp/schema-loader.h directly.
    """

    def get(self, id_: int) -> _Schema:
        """Get a schema by its ID.

        Args:
            id_: Schema node ID

        Returns:
            The schema with the given ID

        """
    def load(self, reader: _NodeReader) -> _Schema:
        """Load a schema from a reader.

        Args:
            reader: DynamicStructReader containing schema data

        Returns:
            Loaded schema

        """
    def load_dynamic(self, reader: _DynamicStructReader) -> _Schema:
        """Load a schema dynamically from a reader.

        Args:
            reader: DynamicStructReader containing schema data

        Returns:
            Loaded schema

        """

# Module loading and import hooks
def add_import_hook() -> None:
    """Add a hook to the Python import system.

    After calling this, Cap'n Proto modules can be directly imported
    like regular Python modules.
    """

def remove_import_hook() -> None:
    """Remove the import hook and return Python's import to normal."""

def load(
    file_name: str,
    display_name: str | None = None,
    imports: Sequence[str] = [],
) -> _CapnpModule:
    """Load a Cap'n Proto schema from a file.

    Args:
        file_name: Path to the .capnp file
        display_name: Optional display name for the module
        imports: List of import paths for resolving imports

    Returns:
        Loaded GeneratedModule with generated types

    """

def register_type(id: int, klass: type) -> None:
    """Register a type with the given schema ID.

    Args:
        id: Schema node ID
        klass: Python class to register

    """

def cleanup_global_schema_parser() -> None:
    """Unload all schemas from the current context."""

def deregister_all_types() -> None:
    """Deregister all registered types."""

def read_multiple_bytes_packed(
    buf: bytes,
    traversal_limit_in_words: int | None = None,
    nesting_limit: int | None = None,
) -> Iterator[_DynamicStructReader]:
    """Read multiple packed Cap'n Proto messages from a buffer.

    Returns an iterable that yields Readers for AnyPointer messages.

    Args:
        buf: Buffer containing packed messages
        traversal_limit_in_words: Optional limit on pointer dereferences
        nesting_limit: Optional limit on nesting depth

    Yields:
        DynamicStructReader for each message

    """

def _write_message_to_fd(fd: int, message: _MessageBuilder) -> None:
    """Write a Cap'n Proto message to a file descriptor.

    Writes the message in unpacked format with a segment table header.

    Args:
        fd: File descriptor to write to
        message: Message to write

    """

def _write_packed_message_to_fd(fd: int, message: _MessageBuilder) -> None:
    """Write a Cap'n Proto message to a file descriptor in packed format.

    Writes the message using Cap'n Proto's packing algorithm which compresses
    runs of zero bytes.

    Args:
        fd: File descriptor to write to
        message: Message to write

    """

def fill_context(method_name: str, context: _CallContext, returned_data: Any) -> None:
    """Internal helper for filling RPC call context with returned data.

    Args:
        method_name: Name of the RPC method
        context: Call context to fill
        returned_data: Data to return to the caller

    """

def void_task_done_callback(method_name: str, fulfiller: Any, task: Any) -> None:
    """Internal callback for void RPC methods when async task completes.

    Args:
        method_name: Name of the RPC method
        fulfiller: Promise fulfiller to complete
        task: Async task that completed

    """

# Internal/private module attributes
_global_schema_parser: SchemaParser | None
"""Global schema parser instance used by import hooks and pickling (may be None).

Note: This is actually defined in capnp.lib.capnp but referenced at module level
in some internal code like pickle_helper.py.
"""

class _SchemaType:
    """Internal schema type representation.

    This class represents Cap'n Proto primitive types.
    Instances are used for type comparisons and type checking.
    """

class _DynamicListBuilder:
    """List builder type returned by init() for list fields.

    This class wraps the Cap'n Proto C++ DynamicList::Builder.
    __getitem__, __setitem__, __len__ and __iter__ have been defined properly,
    so you can treat this class mostly like any other iterable class::

        person = addressbook.Person.new_message()

        phones = person.init('phones', 2)  # This returns a _DynamicListBuilder

        phones[0].number = '555-1234'
        phones[1].number = '555-5678'

        for phone in phones:
            print(phone.number)

    For struct element types, both element instances and dict[str, Any] are accepted
    for convenient initialization, e.g.:
        list_builder[0] = {"field": value}
    """

    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> Any: ...
    def __setitem__(self, index: int, value: Any) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    def adopt(self, index: int, orphan: Any) -> None:
        """Adopt an orphaned message at the given index.

        Don't use this method unless you know what you're doing.
        """
    def disown(self, index: int) -> Any:
        """Disown the element at the given index, returning an orphan.

        Don't use this method unless you know what you're doing.
        """
    def init(self, index: int, size: int) -> Any:
        """Initialize a struct or list element at the given index with the given size.

        Args:
            index: Index of the element to initialize
            size: Size parameter (for nested lists)

        Returns:
            The initialized element (builder for structs, list builder for lists)

        """

class _DynamicListReader:
    """List reader type for reading Cap'n Proto list fields.

    This class thinly wraps the C++ Cap'n Proto DynamicList::Reader class.
    __getitem__ and __len__ have been defined properly, so you can treat this
    class mostly like any other iterable class::

        person = addressbook.Person.read(file)

        phones = person.phones  # This returns a _DynamicListReader

        phone = phones[0]
        print(phone.number)

        for phone in phones:
            print(phone.number)

    Provides read-only list-like interface.
    """

    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> Any: ...
    def __iter__(self) -> Iterator[Any]: ...

class _DynamicOrphan:
    """Orphaned Cap'n Proto message.

    An orphan is a message that has been disowned from its parent.
    Don't use this class unless you know what you're doing.
    """

class _DynamicResizableListBuilder:
    """Resizable list builder for Cap'n Proto lists.

    Returned by init_resizable_list(). Allows adding elements one at a time
    without knowing the final size upfront.
    """

    def add(self) -> Any:
        """Add a new element to the list and return a builder for it."""
    def finish(self) -> None:
        """Finish building the list. Must be called before serialization."""

class _EventLoop:
    """Cap'n Proto event loop integration.

    Internal class for managing the KJ event loop.
    """

class _EnumModule:
    """Module/class for a generated enum type.

    Instances of this class are what you get when you access an enum from
    a loaded schema.
    """

    def __init__(self, schema: _EnumSchema, name: str) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    @property
    def schema(self) -> _EnumSchema: ...

class _InterfaceModule:
    """Module/class for a generated interface.

    This is what you get when you access an interface class from a loaded schema.
    Instances of this class are what you get when you access an interface from
    a loaded schema (e.g. `calculator.Calculator`). The module exposes factory and
    RPC helpers for that interface type.

    Nested types (structs, enums) are accessed as attributes.
    The Server base class is accessed via the `Server` attribute.
    """

    def __init__(self, schema: _InterfaceSchema, name: str) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    @property
    def schema(self) -> _InterfaceSchema: ...
    def _new_client(self, server: _DynamicCapabilityServer) -> _DynamicCapabilityClient:
        """Create a new client from a server implementation.

        Note: Requires an active event loop (use within capnp.kj_loop() or async context).

        Args:
            server: Server implementation instance (subclass of this interface's Server class)

        Returns:
            Client capability for this interface

        Raises:
            RuntimeError: If there is no running event loop

        Example:
            class MyCalculator(Calculator.Server):
                def evaluate(self, expression, **kwargs):
                    return 42.0

            with capnp.kj_loop():
                server = MyCalculator()
                client = Calculator._new_client(server)

        """

def _init_capnp_api() -> None:
    """Initialize the Cap'n Proto API.

    Internal function called during module initialization.
    """

# RPC Classes

class TwoPartyClient:
    """Two-party RPC client for Cap'n Proto.

    Args:
        socket: AsyncIoStream connection
        traversal_limit_in_words: Optional limit on pointer dereferences
        nesting_limit: Optional limit on nesting depth

    """

    def __init__(
        self,
        socket: AsyncIoStream | None = None,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> None: ...
    def bootstrap(self) -> _CapabilityClient:
        """Get the bootstrap interface for this client."""
    def close(self) -> None:
        """Close the client connection."""
    async def on_disconnect(self) -> None:
        """Wait until the connection is disconnected."""

class TwoPartyServer:
    """Two-party RPC server for Cap'n Proto.

    Args:
        socket: AsyncIoStream connection
        bootstrap: Bootstrap interface implementation
        traversal_limit_in_words: Optional limit on pointer dereferences
        nesting_limit: Optional limit on nesting depth

    """

    def __init__(
        self,
        socket: AsyncIoStream | None = None,
        bootstrap: Any = None,
        traversal_limit_in_words: int | None = None,
        nesting_limit: int | None = None,
    ) -> None: ...
    def close(self) -> None:
        """Close the server connection."""
    async def on_disconnect(self) -> None:
        """Wait until the connection is disconnected."""

class AsyncIoStream:
    """Async I/O stream wrapper for Cap'n Proto RPC.

    Provides async I/O operations for Cap'n Proto RPC over TCP and Unix domain sockets.
    """

    @staticmethod
    async def create_connection(
        host: str | None = None,
        port: int | None = None,
        ssl: SSLContext | None = None,
        ssl_handshake_timeout: int | None = None,
        **kwargs: Any,
    ) -> AsyncIoStream:
        """Create an async TCP connection.

        Args:
            host: Hostname to connect to
            port: Port number to connect to
            **kwargs: Additional connection options

        Returns:
            AsyncIoStream connected to the server

        """

    @staticmethod
    async def create_unix_connection(
        path: str | None = None,
        **kwargs: Any,
    ) -> AsyncIoStream:
        """Create an async Unix domain socket connection.

        Args:
            path: Path to Unix domain socket
            **kwargs: Additional connection options

        Returns:
            AsyncIoStream connected to the server

        """

    @staticmethod
    async def create_server(
        callback: Callable[[AsyncIoStream], Awaitable[None]],
        host: str | None = None,
        port: int | None = None,
        **kwargs: Any,
    ) -> _Server:
        """Create an async TCP server.

        Args:
            callback: Async callback function for each new connection
            host: Hostname to bind to
            port: Port number to bind to
            **kwargs: Additional server options

        Returns:
            Server instance

        """

    @staticmethod
    async def create_unix_server(
        callback: Callable[[AsyncIoStream], Awaitable[None]],
        path: str | None = None,
        **kwargs: Any,
    ) -> _Server:
        """Create an async Unix domain socket server.

        Args:
            callback: Async callback function for each new connection
            path: Path for Unix domain socket
            **kwargs: Additional server options

        Returns:
            Server instance

        """

    def close(self) -> None:
        """Close the stream."""

    async def wait_closed(self) -> None:
        """Wait until the stream is closed."""

# Async utilities
async def run[T](coro: Awaitable[T]) -> T:
    """Run an async coroutine with Cap'n Proto event loop.

    Ensures that the coroutine runs while the KJ event loop is running.

    Args:
        coro: Coroutine to run

    Returns:
        The result of the coroutine

    """

@asynccontextmanager
def kj_loop() -> AsyncIterator[None]:
    """Context manager for running the KJ event loop.

    Usage:
        with capnp.kj_loop():
            # Run async code
            pass
    """

__all__ = [
    # Public classes
    "AsyncIoStream",
    # Exception class
    "KjException",
    "SchemaLoader",
    "SchemaParser",
    "TwoPartyClient",
    "TwoPartyServer",
    # Internal classes that are exposed but prefixed with underscore
    "_CapabilityClient",
    "_DynamicCapabilityClient",
    "_DynamicListBuilder",
    "_DynamicListReader",
    "_DynamicOrphan",
    "_DynamicResizableListBuilder",
    "_DynamicStructBuilder",
    "_DynamicStructReader",
    "_EnumModule",
    "_EnumSchema",
    "_EventLoop",
    "_InterfaceMethod",
    "_InterfaceModule",
    "_InterfaceSchema",
    "_ListSchema",
    "_List_NestedNode_Reader",
    "_MallocMessageBuilder",
    "_NestedNodeReader",
    "_NodeReader",
    "_PackedFdMessageReader",
    "_ParsedSchema",
    "_PyCustomMessageBuilder",
    "_Schema",
    "_StreamFdMessageReader",
    "_StructModule",
    "_StructSchema",
    "_StructSchemaField",
    "_init_capnp_api",
    "_write_message_to_fd",
    "_write_packed_message_to_fd",
    # Public functions
    "add_import_hook",
    "cleanup_global_schema_parser",
    "deregister_all_types",
    "fill_context",
    "kj_loop",
    "load",
    "read_multiple_bytes_packed",
    "register_type",
    "remove_import_hook",
    "run",
    # Modules
    "types",
    "void_task_done_callback",
]
