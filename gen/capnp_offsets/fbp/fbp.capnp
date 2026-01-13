# fbp/fbp.capnp
@0xbf602c4868dbb22f;
$import "/capnp/c++.capnp".namespace("mas::schema::fbp");
$import "/capnp/python.capnp".module("mas.schema.fbp");
$import "/capnp/go.capnp".package("fbp");
$import "/capnp/go.capnp".import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/fbp");
struct IP @0xaf0a1dc4709a5ccf {  # 8 bytes, 2 ptrs
  attributes @0 :List(KV);  # ptr[0]
  type @2 :Type;  # bits[0, 16)
  content @1 :AnyPointer;  # ptr[1]
  struct KV @0x9e9e5391e0c499e6 {  # 0 bytes, 3 ptrs
    key @0 :Text;  # ptr[0]
    desc @1 :Text;  # ptr[1]
    value @2 :AnyPointer;  # ptr[2]
  }
  enum Type @0xf684cae29bdc484e {
    standard @0;
    openBracket @1;
    closeBracket @2;
  }
}
struct IIP @0xf3705fb36d44a21f {  # 0 bytes, 1 ptrs
  content @0 :AnyPointer;  # ptr[0]
}
interface Channel @0x9c62c32b2ff2b1e8 (V) superclasses(import "/common/common.capnp".Identifiable, import "/persistence/persistence.capnp".Persistent) {
  setBufferSize @0 (size :UInt64 = 1) -> ();
  reader @1 () -> (r :Reader);
  writer @2 () -> (w :Writer);
  endpoints @3 () -> (r :Reader, w :Writer);
  setAutoCloseSemantics @4 (cs :CloseSemantics) -> ();
  close @5 (waitForEmptyBuffer :Bool = true) -> ();
  enum CloseSemantics @0xa8d787cae7e0b243 {
    fbp @0;
    no @1;
  }
  struct Msg @0xd5b512f4bcd0aa2e {  # 8 bytes, 1 ptrs
    union {  # tag bits [0, 16)
      value @0 :V;  # ptr[0], union tag = 0
      done @1 :Void;  # bits[0, 0), union tag = 1
      noMsg @2 :Void;  # bits[0, 0), union tag = 2
    }
  }
  struct StartupInfo @0xe3d7a3237f175028 {  # 16 bytes, 6 ptrs
    bufferSize @0 :UInt64;  # bits[0, 64)
    closeSemantics @1 :CloseSemantics;  # bits[64, 80)
    channelSR @2 :import "/persistence/persistence.capnp".SturdyRef;  # ptr[0]
    channel @5 :Channel(V);  # ptr[3]
    readerSRs @3 :List(import "/persistence/persistence.capnp".SturdyRef);  # ptr[1]
    readers @6 :List(Reader);  # ptr[4]
    writerSRs @4 :List(import "/persistence/persistence.capnp".SturdyRef);  # ptr[2]
    writers @7 :List(Writer);  # ptr[5]
  }
  interface Reader @0x8bc69192f3bc97cc superclasses(import "/common/common.capnp".Identifiable, import "/persistence/persistence.capnp".Persistent) $import "/capnp/c++.capnp".name("ChanReader") {
    read @0 () -> Msg;
    readIfMsg @2 () -> Msg;
    close @1 () -> ();
  }
  interface Writer @0xf7fec613b4a8c79f superclasses(import "/common/common.capnp".Identifiable, import "/persistence/persistence.capnp".Persistent) $import "/capnp/c++.capnp".name("ChanWriter") {
    write @0 Msg -> ();
    writeIfSpace @2 Msg -> (success :Bool);
    close @1 () -> ();
  }
}
interface StartChannelsService @0xd0cd6d829b810229 superclasses(import "/common/common.capnp".Identifiable) {
  start @0 Params -> (startupInfos :List(Channel.StartupInfo), stop :import "/service/service.capnp".Stoppable);
  struct Params @0x9576b9a98d58fba2 {  # 8 bytes, 3 ptrs
    name @0 :Text;  # ptr[0]
    noOfChannels @1 :UInt16 = 1;  # bits[0, 16)
    noOfReaders @2 :UInt16 = 1;  # bits[16, 32)
    noOfWriters @3 :UInt16 = 1;  # bits[32, 48)
    readerSrts @4 :List(Text);  # ptr[1]
    writerSrts @5 :List(Text);  # ptr[2]
    bufferSize @6 :UInt16 = 1;  # bits[48, 64)
  }
}
struct PortInfos @0xece0efa9a922d4a8 {  # 0 bytes, 2 ptrs
  inPorts @0 :List(NameAndSR);  # ptr[0]
  outPorts @1 :List(NameAndSR);  # ptr[1]
  struct NameAndSR @0x8a4d34c4b5eb1545 {  # 8 bytes, 2 ptrs
    name @0 :Text;  # ptr[0]
    union {  # tag bits [0, 16)
      sr @1 :import "/persistence/persistence.capnp".SturdyRef;  # ptr[1], union tag = 0
      srs @2 :List(import "/persistence/persistence.capnp".SturdyRef);  # ptr[1], union tag = 1
    }
  }
}
struct Component @0xd717ff7d6815a6b0 {  # 8 bytes, 5 ptrs
  info @0 :import "/common/common.capnp".IdInformation;  # ptr[0]
  type @1 :ComponentType;  # bits[0, 16)
  inPorts @2 :List(Port);  # ptr[1]
  outPorts @3 :List(Port);  # ptr[2]
  defaultConfig @4 :Text;  # ptr[3]
  factory :group {
    union {  # tag bits [16, 32)
      none @5 :Void;  # bits[0, 0), union tag = 0
      runnable @6 :Runnable.Factory;  # ptr[4], union tag = 1
      process @7 :Process.Factory;  # ptr[4], union tag = 2
    }
  }
  enum ComponentType @0xc6976ac75246b450 {
    standard @0;
    iip @1;
    subflow @2;
    view @3;
    process @4;
  }
  struct Port @0xc28d2829add1cd72 {  # 8 bytes, 2 ptrs
    name @0 :Text;  # ptr[0]
    contentType @1 :Text;  # ptr[1]
    type @2 :PortType;  # bits[0, 16)
    enum PortType @0xf58d7a7318a06224 {
      standard @0;
    }
    enum ContentType @0xf30610cf0ed94a2f {
      structuredText @0;
    }
  }
}
interface Runnable @0xbde616d300754ff0 superclasses(import "/common/common.capnp".Identifiable) {
  start @0 (portInfosReaderSr :import "/persistence/persistence.capnp".SturdyRef, name :Text) -> (success :Bool);
  stop @1 () -> (success :Bool);
  interface Factory @0xf5694db406aa9975 superclasses(import "/common/common.capnp".Identifiable) {
    create @0 () -> (out :Runnable);
  }
}
interface Process @0xbbad56943a039783 superclasses(import "/common/common.capnp".Identifiable, import "/persistence/persistence.capnp".GatewayRegistrable) {
  inPorts @0 () -> (ports :List(Component.Port));
  connectInPort @1 (name :Text, sturdyRef :import "/persistence/persistence.capnp".SturdyRef) -> (connected :Bool);
  outPorts @2 () -> (ports :List(Component.Port));
  connectOutPort @3 (name :Text, sturdyRef :import "/persistence/persistence.capnp".SturdyRef) -> (connected :Bool);
  configEntries @4 () -> (config :List(ConfigEntry));
  setConfigEntry @7 ConfigEntry -> ();
  start @5 () -> ();
  stop @6 () -> ();
  state @8 (transitionCallback :StateTransition) -> (currentState :State);
  interface Factory @0xb01652ab8f1ac0d3 superclasses(import "/common/common.capnp".Identifiable) {
    create @0 () -> (out :Process);
  }
  struct ConfigEntry @0xa8d0bdfb4ddda7b3 {  # 0 bytes, 2 ptrs
    name @0 :Text;  # ptr[0]
    val @1 :import "/common/common.capnp".Value;  # ptr[1]
  }
  enum State @0xe67044233be769a5 {
    started @0;
    stopped @1;
    canceled @2;
  }
  interface StateTransition @0x9c8fa975665cfafa {
    stateChanged @0 (old :State, new :State) -> ();
  }
}
