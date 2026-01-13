# test/x.capnp
@0xffd06af2f026177b;
$import "/capnp/c++.capnp".namespace("mas::schema::test");
$import "/capnp/python.capnp".module("mas.schema.test");
$import "/capnp/go.capnp".package("test");
$import "/capnp/go.capnp".import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/test");
struct S @0xd227ef68de0bc647 {  # 0 bytes, 1 ptrs
  c @0 :X;  # ptr[0]
}
interface X @0xdcf28e81fa4de615 {
  m @0 (i :Int64) -> (t :Text);
}
interface Y @0xac121e5aa82ca6bd {
  m @0 (hello :Text) -> ();
}
interface Z @0xc64526206425c2ab {
  m @0 (n :Int64) -> (r :Float64);
}
