project('mas_capnproto_schemas', 'cpp',
  version : '1.0',
  default_options : [
    'cpp_std=c++17',
    'default_library=static',
  ],
)

# Cap'n Proto libraries — installed by the system or vcpkg.
# Meson finds them via pkg-config or CMake config files.
capnp_dep      = dependency('capnp',      required : true)
capnp_rpc_dep  = dependency('capnp-rpc',  required : true)
kj_dep         = dependency('kj',         required : true)
kj_async_dep   = dependency('kj-async',   required : true)
kj_http_dep    = dependency('kj-http',    required : false)
kj_gzip_dep    = dependency('kj-gzip',    required : false)
capnp_json_dep = dependency('capnp-json', required : false)
zlib_dep       = dependency('zlib',       required : false)

capnp_all_deps = [
  capnp_dep,
  capnp_rpc_dep,
  kj_dep,
  kj_async_dep,
  kj_http_dep,
  kj_gzip_dep,
  capnp_json_dep,
  zlib_dep,
]

capnp_schemas_lib = static_library('capnp_schemas',
  sources : files(
    'common/common.capnp.c++',
    'common/date.capnp.c++',
    'climate/climate.capnp.c++',
    'cluster/cluster_admin_service.capnp.c++',
    'crop/crop.capnp.c++',
    'fbp/fbp.capnp.c++',
    'geo/geo.capnp.c++',
    'management/management.capnp.c++',
    'model/model.capnp.c++',
    'model/monica/monica_management.capnp.c++',
    'model/monica/monica_params.capnp.c++',
    'model/monica/soil_params.capnp.c++',
    'model/monica/monica_state.capnp.c++',
    'persistence/persistence.capnp.c++',
    'registry/registry.capnp.c++',
    'service/service.capnp.c++',
    'soil/soil.capnp.c++',
    'storage/storage.capnp.c++',
    'model/yieldstat/yieldstat.capnp.c++',
    'test/x.capnp.c++',
    'test/a.capnp.c++',
  ),
  include_directories : include_directories(
    '.',
    'common',
    'climate',
    'cluster',
    'crop',
    'fbp',
    'geo',
    'management',
    'model',
    'model/monica',
    'persistence',
    'registry',
    'service',
    'soil',
    'storage',
    'model/yieldstat',
    'test',
  ),
  dependencies : capnp_all_deps,
)

capnp_schemas_dep = declare_dependency(
  link_with : capnp_schemas_lib,
  include_directories : include_directories(
    '.',
    'common',
    'climate',
    'cluster',
    'crop',
    'fbp',
    'geo',
    'management',
    'model',
    'model/monica',
    'persistence',
    'registry',
    'service',
    'soil',
    'storage',
    'model/yieldstat',
    'test',
  ),
  dependencies : capnp_all_deps,
)
