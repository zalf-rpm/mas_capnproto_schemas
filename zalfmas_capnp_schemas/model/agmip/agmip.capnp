@0xe357024d7caac4d7;

using Cxx = import "/capnp/c++.capnp";
$Cxx.namespace("mas::schema::model::agmip");

using Python = import "/capnp/python.capnp";
$Python.module("mas.schema.model.agmip");

using Go = import "/capnp/go.capnp";
$Go.package("agmip");
$Go.import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/model/agmip");

using Soil = import "/soil/soil.capnp";
using Climate = import "/climate/climate.capnp";
using Common = import "/common/common.capnp";

struct FieldExperimentDataTemplate {
  soilProfile @0 :Soil.Profile;
  soil        @1 :Common.StructuredText;
  plot        @2 :Common.StructuredText;
  timeseries  @3 :Climate.TimeSeries;
  treatment   @4 :Common.StructuredText;
  experiment  @5 :Common.StructuredText;
}
