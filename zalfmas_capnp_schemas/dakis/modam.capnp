@0xe7b5fe53a32655c8;

using Cxx = import "/capnp/c++.capnp";
$Cxx.namespace("mas::schema::dakis");

using Python = import "/capnp/python.capnp";
$Python.module("mas.schema.dakis.modam");

using Go = import "/capnp/go.capnp";
$Go.package("modam");
$Go.import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/dakis/modam");

interface ModamWrapperService {
  # Interface for running the MODAM model

  run @0 (input :Text) -> (output :Text);
  # Run the MODAM model with text input and return text output
}
