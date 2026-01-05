cmake_minimum_required(VERSION 3.22)
project(MAS-infrastructure-capnp-schemas)

message(STATUS "-> MAS-infrastructure-capnp-schemas")

find_package(CapnProto CONFIG REQUIRED)
find_package(ZLIB)

set(CAPNPC_SRC_PREFIX ${CAPNP_SCHEMAS_DIR}/zalfmas_capnp_schemas)

capnp_generate_cpp(CAPNP_SRCS CAPNP_HDRS
	zalfmas_capnp_schemas/common/common.capnp
	zalfmas_capnp_schemas/climate/climate.capnp
	zalfmas_capnp_schemas/cluster/cluster_admin_service.capnp
	zalfmas_capnp_schemas/crop/crop.capnp
	zalfmas_capnp_schemas/date/date.capnp
	zalfmas_capnp_schemas/fbp/fbp.capnp
	zalfmas_capnp_schemas/geo/geo.capnp
	zalfmas_capnp_schemas/management/management.capnp
	zalfmas_capnp_schemas/model/model.capnp
	zalfmas_capnp_schemas/model/monica/monica_management.capnp
	zalfmas_capnp_schemas/model/monica/monica_params.capnp
	zalfmas_capnp_schemas/model/monica/soil_params.capnp
	zalfmas_capnp_schemas/model/monica/monica_state.capnp
	zalfmas_capnp_schemas/persistence/persistence.capnp
	zalfmas_capnp_schemas/registry/registry.capnp
	zalfmas_capnp_schemas/service/service.capnp
	zalfmas_capnp_schemas/soil/soil.capnp
	zalfmas_capnp_schemas/storage/storage.capnp
	zalfmas_capnp_schemas/model/yieldstat/yieldstat.capnp
	zalfmas_capnp_schemas/test/x.capnp
)
message(STATUS "CAPNP_HDRS: " ${CAPNP_HDRS})
message(STATUS "CAPNP_SRCS: " ${CAPNP_SRCS})

add_library(capnp_schemas_lib
	STATIC
	${CAPNP_HDRS}
	${CAPNP_SRCS}
)

target_link_libraries(capnp_schemas_lib
	PUBLIC
	CapnProto::capnp
	CapnProto::capnpc
	CapnProto::capnp-rpc
	CapnProto::kj
	CapnProto::kj-async
	CapnProto::kj-http
	CapnProto::kj-gzip
	CapnProto::capnp-json
)
target_include_directories(capnp_schemas_lib PUBLIC ${CMAKE_CURRENT_BINARY_DIR})

if(MSVC AND MT_RUNTIME_LIB)
	target_compile_options(capnp_schemas_lib PRIVATE "/MT$<$<CONFIG:Debug>:d>")
endif()

#message(STATUS "capnp csd: " ${CMAKE_CURRENT_SOURCE_DIR} " cbd: " ${CMAKE_CURRENT_BINARY_DIR})

message(STATUS "<- MAS-infrastructure-capnp-schemas")
