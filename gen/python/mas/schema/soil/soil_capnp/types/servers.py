"""Runtime placeholder module for server helpers of `soil.capnp`."""

# pyright: reportUnusedClass=none

from .. import Profile, Service

ProfileServer = Profile.Server
ServiceServer = Service.Server
StreamServer = Service.Stream.Server
