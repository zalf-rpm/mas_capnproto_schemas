# dakis/modam.capnp
@0xe7b5fe53a32655c8;
$import "/capnp/c++.capnp".namespace("mas::schema::dakis");
$import "/capnp/python.capnp".module("mas.schema.dakis.modam");
$import "/capnp/go.capnp".package("modam");
$import "/capnp/go.capnp".import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/dakis/modam");
interface ModamWrapperService @0xdb3fb36057abc378 {
  runAemModel @0 (input :Text) -> (output :Text);
  runFieldModel @1 (input :Text) -> (output :Text);
}
