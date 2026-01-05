@0xe7e7e2edc72e660c;

using Cxx = import "/capnp/c++.capnp";
$Cxx.namespace("mas::schema::jobs");

using Python = import "/capnp/python.capnp";
$Python.module("mas.schema.jobs");

using Go = import "/capnp/go.capnp";
$Go.package("jobs");
$Go.import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/jobs");

using Persistent = import "/persistence/persistence.capnp".Persistent;
using Identifiable = import "/common/common.capnp".Identifiable;

struct Job(Payload) {
    data            @0 :Payload;
    noFurtherJobs   @1 :Bool = false;
}

interface Service extends(Identifiable, Persistent) {
    nextJob @0 () -> (job :Job);
}
