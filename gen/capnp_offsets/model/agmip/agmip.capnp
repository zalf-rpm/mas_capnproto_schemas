# model/agmip/agmip.capnp
@0xe357024d7caac4d7;
$import "/capnp/c++.capnp".namespace("mas::schema::model::agmip");
$import "/capnp/python.capnp".module("mas.schema.model.agmip");
$import "/capnp/go.capnp".package("agmip");
$import "/capnp/go.capnp".import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/model/agmip");
struct FieldExperimentDataTemplate @0xdee9ee5191b1e4a2 {  # 0 bytes, 6 ptrs
  soilProfile @0 :import "/soil/soil.capnp".Profile;  # ptr[0]
  soil @1 :import "/common/common.capnp".StructuredText;  # ptr[1]
  plot @2 :import "/common/common.capnp".StructuredText;  # ptr[2]
  timeseries @3 :import "/climate/climate.capnp".TimeSeries;  # ptr[3]
  treatment @4 :import "/common/common.capnp".StructuredText;  # ptr[4]
  experiment @5 :import "/common/common.capnp".StructuredText;  # ptr[5]
}
