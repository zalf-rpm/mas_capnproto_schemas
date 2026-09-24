@0xbf602c4868dbb22f;

using Cxx = import "/capnp/c++.capnp";
$Cxx.namespace("mas::schema::fbp");

using Python = import "/capnp/python.capnp";
$Python.module("mas.schema.fbp");

using Go = import "/capnp/go.capnp";
$Go.package("fbp");
$Go.import("github.com/zalf-rpm/mas_capnproto_schemas/gen/go/fbp");

using Persistent = import "/persistence/persistence.capnp".Persistent;
using SturdyRef = import "/persistence/persistence.capnp".SturdyRef;
using GatewayRegistrable = import "/persistence/persistence.capnp".GatewayRegistrable;
using Common = import "/common/common.capnp";
using Stoppable = import "/service/service.capnp".Stoppable;

struct IP {
  # an FBP information packet

  struct KV {
    key         @0 :Text;
    desc        @1 :Text; # optional human readable info on what value is
    value       @2 :AnyPointer;  # would often be a Common.Value
    valueType   @3 :Text; # Cap'n Proto type id (@0xbf602c...) = path/file.capnp:Type
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

  struct ChunkedData{
    chunkCount @0 :UInt64;
  }
  struct SysAttributes{
    bracketType : union {
      standard @0:Void;
      chunkedContent @1:ChunkedData;
      chunkedIp @2:ChunkedData;
    }
    contentType @3:Text;
  }
  sysAttributes @3:SysAttributes;
  # fixed systemlevel attributes
}

struct IIP {
  content @0 :AnyPointer;
  # might often be a Common.Value or common.StructuredText
}

interface Channel(V) extends(Common.Identifiable, Persistent) {
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

    bufferSize      @0 :UInt64;
    # size of the buffer

    closeSemantics  @1 :CloseSemantics;
    # semantics of closing the channel

    channelSR       @2 :SturdyRef;
    # sturdy reference to the channel

    channel         @5 :Channel(V);
    # capability to started channel

    readerSRs       @3 :List(SturdyRef);
    # sturdy references to the readers

    readers         @6 :List(Reader);
    # list of caps to the created Readers

    writerSRs       @4 :List(SturdyRef);
    # sturdy references to the writers

    writers         @7 :List(Writer);
    # list of caps to the created Writers
  }

  interface Reader extends(Common.Identifiable, Persistent) $Cxx.name("ChanReader") {
    read          @0 () -> Msg $Cxx.allowCancellation;
    # read blocking until message is available
    #
    # This hands the message over for good: the channel lets go of it as soon as the response is
    # on its way, so the message exists only inside this call. A caller which cancels the call or
    # discards its response destroys the message - silently, because the writer upstream has long
    # been told that its write succeeded and no one is in a position to notice the loss.
    # Use readLeased if the reader cannot rule that out.

    readLeased    @3 () -> (msg :Msg, lease :Lease) $Cxx.allowCancellation;
    # read blocking until a message is available, but keep the message owed to the channel until
    # the lease is acknowledged
    #
    # If the lease is released without acknowledging it - the call was canceled, the client died,
    # the connection broke - the message goes back to the front of the channel and is delivered
    # again, to this or to another reader. A reader may hold only one unacknowledged lease at a
    # time, so that a returning message keeps its place in the queue.

    interface Lease {
      ack @0 ();
      # confirm that the message arrived
      #
      # Acknowledge as early as possible, ideally before processing the message: everything
      # between receiving and acknowledging is a window in which a dying reader causes the
      # message to be delivered a second time.
    }

    readIfMsg     @2 () -> Msg;
    # read non blocking if there is a message available

    close         @1 ();
    # close this reading end of the channel
  }

  interface Writer extends(Common.Identifiable, Persistent) $Cxx.name("ChanWriter") {
    write           @0 Msg $Cxx.allowCancellation;
    # write blocking until message is written

    writeIfSpace    @2 Msg -> (success :Bool);
    # write non blocking if there is space in the buffer

    close           @1 ();
    # close this writing end of the channel
  }

  interface StatsCallback {
    # delivers some status information about this channel
    struct Stats {
      noOfWaitingWriters    @0 :UInt16;
      noOfWaitingReaders    @1 :UInt16;
      noOfIpsInQueue        @2 :UInt64;
      totalNoOfIpsReceived  @3 :UInt64;
      timestamp             @4 :Text;
      updateIntervalInMs    @5 :UInt32;
    }

    interface Unregister {
      unreg @0 () -> (success :Bool);
    }

    status @0 (stats :Stats);
  }

  interface Observer {
    # sees what travels through the channel, without being part of the flow

    struct Event {
      seqNo       @0 :UInt64;
      # number of this message since the channel was created, counted from 1; gaps mean that
      # messages were skipped because of everyNth or because a best effort observer was too slow

      timestamp   @1 :Text;

      sizeInWords @2 :UInt64;
      # size of the message as it arrived at the channel

      content     @3 :V;
      # the message content, only set if the observer asked for it
    }

    saw @0 (event :Event);
    # called for a message the channel accepted from a writer
    #
    # For a gating observer the channel waits for this call to return before the message may be
    # delivered to a reader, which is what stepping through a flow needs: hold the call and the
    # message is held with it. For a best effort observer the channel does not wait and skips
    # messages while a previous call is still on its way.

    interface Unregister {
      unreg @0 () -> (success :Bool);
    }

    struct Params {
      everyNth    @0 :UInt32 = 1;
      # observe only every nth message, 1 meaning every message

      withContent @1 :Bool = false;
      # include the message content in the event, which means copying every observed message

      gate        @2 :Bool = false;
      # make the channel wait for saw() to return before the message is delivered
      #
      # A gating observer sits in the data path and can hold up the flow indefinitely, which is
      # the point for a debugger, but means a hung observer stalls the channel. Best effort
      # observers (the default) can never slow the channel down.
    }
  }

  observe @7 (callback :Observer, params :Observer.Params) -> (unregister :Observer.Unregister);
  # watch the messages travelling through this channel

  pause  @8 ();
  # stop delivering messages to readers
  #
  # Writers keep filling the buffer and block once it is full, so a paused channel back-pressures
  # its upstream by itself. Reads issued while paused wait, they do not return empty.

  resume @9 ();
  # deliver freely again, dropping any step credits left over

  step   @10 (count :UInt64 = 1) -> (delivered :UInt64);
  # allow count more messages to be delivered and stay paused
  #
  # Returns how many of them could be delivered right away; the rest stay as credit and are used
  # up by the next reads. Stepping a channel which is not paused pauses it first.

  registerStatsCallback @6 (callback :StatsCallback, updateIntervalInMs :UInt32) -> (unregisterCallback :StatsCallback.Unregister);
  # register a callback to receive status information every "updateIntervalInMs" milliseconds
  # 0 ms means update on every received message (which will be very slow)
  # returns an unregister callback

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

interface StartChannelsService extends(Common.Identifiable) {
    # starting channels

    struct Params {
        name            @0 :Text;       # name of channel
        noOfChannels    @1 :UInt16 = 1; # how many channels to create
        noOfReaders     @2 :UInt16 = 1; # no of readers to create per channel
        noOfWriters     @3 :UInt16 = 1; # no of writers to create per channel
        readerSrts      @4 :List(Text); # fixed sturdy ref tokens per reader
        writerSrts      @5 :List(Text); # fixed sturdy ref tokens per writer
        bufferSize      @6 :UInt16 = 1; # how large is the buffer supposed to be
        registerAtGateway @7 :Bool = false; # Whether to register the channel at the gateway
    }
    start @0 Params -> (startupInfos :List(Channel.StartupInfo), stop :Stoppable);
    # create one (or multiple with same properties) channel and return reader and writer sturdy refs to the channel(s)
}

struct PortInfos {
  # information for component to connect to in/out ports

  struct NameAndSR {
    name        @0 :Text;
    union {
        sr      @1 :SturdyRef;           # for single ports
        srs     @2 :List(SturdyRef);     # for array ports
    }
  }

  inPorts  @0 :List(NameAndSR);
  # reader sturdy refs for the IN ports

  outPorts @1 :List(NameAndSR);
  # writer sturdy refs for the OUT ports
}

struct Component {
    enum ComponentType {
        standard    @0; # standard FBP component
        iip         @1; # initial information packet
        subflow     @2; # represents a subflow
        view        @3; # is a view component
        process     @4; # is a standard FBP component, but based on Process interface
    }

    struct Port {
        enum PortType {
            standard  @0; # standard port
            array     @1; # array port (only an out port can be an array port)
        }

        name        @0 :Text;
        # port name

        contentType @1 :Text;
        # type of content, e.g. common.capnp:StructuredText or geo.capnp:LatLngCoord or Text

        desc @3 :Text;
        # description of the ports meaning

        type        @2 :PortType = standard;
        # port type
    }

    info          @0 :Common.IdInformation; # id, name and description of this FBP component
    type          @1 :ComponentType; # the type of FBP component
    inPorts       @2 :List(Port); # the components allowed input ports
    outPorts      @3 :List(Port); # the components allowed input ports

    defaultConfig @4 :Common.StructuredText; # default configuration for component

    factory :union {
      none        @5 :Void;               # no factory available
      runnable    @6 :Runnable.Factory;   # factory for simple Runnable processes
      process     @7 :Process.Factory;    # factory for Process based components
    }
}

interface Runnable extends(Common.Identifiable) {
  # interface to run remote FBP component

  interface Factory extends(Common.Identifiable) {
    # minimal interface to produce a Runnable instance

    create @0 () -> (out :Runnable);
  }

  interface StoppedCallback {
    # notify listener that the Runnable stopped
    stopped @0 ();
  }

  start @0 (portInfosReaderSr :SturdyRef, name :Text, stoppedCb :StoppedCallback) -> (success :Bool);
  # start component with a sturdy ref to a reader of PortInfos
  # the component will use the port infos to connect to the channels
  # and given an optional nam

  stop  @1 () -> (success :Bool);
  # stop the component
}

interface Process extends(Common.Identifiable, GatewayRegistrable) {
  # bootstrap interface of a running process = instantiated component

  interface Factory extends(Common.Identifiable) {
    # minimal interface to produce a managed Process instance

    create @0 () -> (out :ProcessHandle);
  }

  interface ProcessHandle {
    # service-owned lifecycle handle for a Process instance

    process @0 () -> (process :Process);
    # return the Process capability used for component execution

    close @1 () -> (closed :Bool);
    # close logical process resources and terminate/reap the backing runtime if owned

    alive @2 () -> (alive :Bool);
    # true if the backing runtime is still alive
  }

  interface Disconnect {
    # disconnect a port connection created by connectInPort or connectOutPort

    disconnect @0 () -> (disconnected :Bool);
  }

  inPorts @0 () -> (ports :List(Component.Port));
  # input ports available on the process

  connectInPort @1 (name :Text, sturdyRef :SturdyRef) -> (connected :Bool, disconnect :Disconnect);
  # connect named input port via given sturdyRef

  outPorts @2 () -> (ports :List(Component.Port));
  # output ports available on the process

  connectOutPort @3 (name :Text, sturdyRef :SturdyRef) -> (connected :Bool, disconnect :Disconnect);
  # connect named output port via given sturdyRef

  struct ConfigEntry {
    name @0 :Text;
    val  @1 :Common.Value;
  }

  configEntries @4 () -> (config :List(ConfigEntry));
  # configuration data for this process

  setConfigEntry @7 ConfigEntry;
  # set configuration value

  start @5 () -> (started :Bool);
  # accept start request and begin execution asynchronously if idle

  stop @6 () -> (stopped :Bool);
  # request cooperative stop of the current run invocation; Process remains usable

  enum State {
    idle     @0; # reachable and startable, but no active run task
    starting @1; # runtime accepted start, setup still in progress
    running  @2; # actively processing or waiting for input
    stopping @3; # stop requested, shutdown not finished yet
    failed   @4; # last run ended unexpectedly
  }

  interface StateTransition {
    stateChanged @0 (old :State, new :State);
  }

  enum ActivityState {
    none          @0; # no active run activity; usually lifecycle state is idle or failed
    waitingInput  @1; # run task is blocked waiting for input
    processing    @2; # run task is executing component logic
    waitingOutput @3; # run task is blocked writing output
    closing       @4; # run task is closing ports or other resources
  }

  struct ActivityInfo {
    state @0 :ActivityState;
    port  @1 :Text; # optional port name related to the activity, empty if not applicable
  }

  interface ActivityTransition {
    activityChanged @0 (old :ActivityInfo, new :ActivityInfo);
  }

  struct RunInfo {
    hasRunInfo    @0 :Bool;
    processId     @1 :Text;
    processName   @2 :Text;
    outcome       @3 :Outcome = none;
    phase         @4 :Phase = unknown;
    port          @5 :Text;
    detailType    @6 :Text;
    message       @7 :Text;
    causeType     @8 :Text;
    causeMessage  @9 :Text;
    traceback     @10 :List(Text);

    enum Outcome {
      none      @0; # nothing recorded yet / current run still in progress
      completed @1; # run() returned normally
      stopped   @2; # stop() was requested and the run exited cooperatively
      failed    @3; # run() ended with an error
    }

    enum Phase {
      unknown @0;
      config  @1;
      read    @2;
      run     @3;
      write   @4;
      close   @5;
    }
  }

  state @8 (transitionCallback :StateTransition) -> (currentState :State);
  # return current state of process and
  # optionally ask for notifications if there's a state transition
  # callbacks emit only the states defined in State

  lastRun @9 () -> (info :RunInfo);
  # returns information about how the last run ended

  activity @10 (transitionCallback :ActivityTransition) -> (currentActivity :ActivityInfo);
  # return current process activity and
  # optionally ask for notifications if there's an activity transition
}
