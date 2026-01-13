# model/weberest/web_berest_data_import.capnp
@0xc4b468a2826bb79b;
$import "/capnp/c++.capnp".namespace("mas::schema::model::weberest");
$import "/capnp/python.capnp".module("mas.schema.model.weberest");
$import "/capnp/java.capnp".package("de.zalf.mas");
$import "/capnp/java.capnp".outerClassname("WebBerestDWDImport");
$import "/capnp/go.capnp".package("weberest");
$import "/capnp/go.capnp".import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/model/weberest");
interface DWLABImport @0xa1a4ad9d143eaa6f {
  importData @0 (id :Text, dwla :Data, dwlb :Data) -> (id :Text, successA :Bool, successB :Bool);
}
