# test/a.capnp
@0xf22d616110f0b140;
$import "/capnp/c++.capnp".namespace("mas::rpc::test");
$import "/capnp/python.capnp".module("mas.schema.test");
$import "/capnp/java.capnp".package("de.zalf.mas");
$import "/capnp/java.capnp".outerClassname("OuterA");
$import "/capnp/go.capnp".package("test");
$import "/capnp/go.capnp".import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/test");
interface A @0xf2067f36913b4d37 {
  method @0 (param :Text) -> (res :Text);
}
