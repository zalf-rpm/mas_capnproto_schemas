@0xbf602c4868dbb22f;

using Cxx = import "/capnp/c++.capnp";
$Cxx.namespace("mas::schema::fbp");

using Go = import "/capnp/go.capnp";
$Go.package("fbp");
$Go.import("github.com/zalf-rpm/mas-infrastructure/capnproto_schemas/gen/go/fbp");

using Persistent = import "persistence.capnp".Persistent;
using SturdyRef = import "persistence.capnp".SturdyRef;
using Identifiable = import "common.capnp".Identifiable;
using Value = import "common.capnp".Value;

struct IP {
  # an FBP information packet

  struct KV {
    key 	@0 :Text;
    desc 	@1 :Text; # optional human readable info on what value is
    value @2 :AnyPointer;  # would often be a common.Value
  }
  attributes @0 :List(KV);
  # key value pair attributes attached to IP additional to main content

  enum Type {
    standard     @0;
    openBracket  @1;
    closeBracket @2;
  }
  type @2 :Type = standard;

  content @1 :AnyPointer;
  # main content of IP
}

struct IIP {
  content @0 :AnyPointer;
  # might often be a common.Value or common.StructuredText
}

interface Channel(V) extends(Identifiable, Persistent) {
  # a potentially buffered channel to transport values of type V
  
  enum CloseSemantics {
    fbp   @0; # close channel automatically if there are no writers anymore and buffer is empty = no upstream data
    no    @1; # keep channel open until close message received
  }

  struct Msg {
    union {
      value @0 :V;
      done  @1 :Void;   # done message, no more data will be sent (indicate upstream is done - but semantics up to user)
      noMsg @2 :Void;   # no message available, if readIfMsg is used
    }
  }

  struct StartupInfo {
    # information about the startup of a channel

    bufferSize @0 :UInt64;
    # size of the buffer

    closeSemantics @1 :CloseSemantics;
    # semantics of closing the channel

    channelSR @2 :Text;
    # sturdy reference to the channel

    readerSRs @3 :List(Text);
    # sturdy references to the readers

    writerSRs @4 :List(Text);
    # sturdy references to the writers
  }

  interface Reader $Cxx.name("ChanReader") {
    read          @0 () -> Msg;
    # read blocking until message is available

    readIfMsg     @2 () -> Msg;
    # read non blocking if there is a message available

    close         @1 ();
    # close this reading end of the channel
  }

  interface Writer $Cxx.name("ChanWriter") {
    write           @0 Msg;
    # write blocking until message is written

    writeIfSpace    @2 Msg -> (success :Bool);
    # write non blocking if there is space in the buffer

    close           @1 ();
    # close this writing end of the channel
  }

  setBufferSize @0 (size :UInt64 = 1);
  # set buffer size of channel, lowest allowed value = 1, meaning basically no buffer

  reader        @1 () -> (r :Reader);
  # get just a reader

  writer        @2 () -> (w :Writer);
  # get just a writer

  endpoints     @3 () -> (r :Reader, w :Writer);
  # get both endpoints of channel

  setAutoCloseSemantics @4 (cs :CloseSemantics);
  # set semantics when to automatically close this channel

  close         @5 (waitForEmptyBuffer :Bool = true);
  # close this channel
  # wait for empty buffer or kill channel right away
}

struct NewPortInfo {
  # data for a component which port has been connected
  name          @0 :Text;
  union {
    inPortReaderCap     @1 :Channel(IP).Reader;
    inPortReaderSR      @2 :Text;
    outPortWriterCap    @3 :Channel(IP).Writer;
    outPortWriterSR     @4 :Text;
  }
}

struct PortInfos {
  # information for component to connect to in/out ports

  struct NameAndSR {
    name        @0 :Text;
    union {
        sr      @1 :Text;           # for single ports
        srs     @2 :List(Text);     # for array ports
    }
  }

  inPorts  @0 :List(NameAndSR);
  # reader sturdy refs for the IN ports

  outPorts @1 :List(NameAndSR);
  # writer sturdy refs for the OUT ports
}

interface Component extends(Identifiable) {
  # interface to manage remote FBP components

  start @0 (portInfosReaderSr :Text) -> (success :Bool);
  # start component with a sturdy ref to a reader of PortInfos
  # the component will use the port infos to connect to the channels

  stop  @1 () -> (success :Bool);
  # stop the component
}