# crop/crop.capnp
@0xf98a24e1969df972;
$import "/capnp/c++.capnp".namespace("mas::schema::crop");
$import "/capnp/python.capnp".module("mas.schema.crop");
$import "/capnp/go.capnp".package("crop");
$import "/capnp/go.capnp".import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/crop");
interface Crop @0xe88d97a324bf5c84 superclasses(import "/common/common.capnp".Identifiable, import "/persistence/persistence.capnp".Persistent) {
  species @2 () -> (info :import "/common/common.capnp".IdInformation);
  cultivar @1 () -> (info :import "/common/common.capnp".IdInformation);
  parameters @0 () -> (params :AnyPointer);
}
interface Service @0x8ddcc2b6c0386bc4 superclasses(import "/registry/registry.capnp".Registry) {
}
