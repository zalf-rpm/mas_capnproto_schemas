"""Runtime placeholder module for server helpers of `soil.capnp`."""

from .. import Profile, Service

ProfileServer = Profile.Server
ServiceServer = Service.Server
StreamServer = Service.Stream.Server
