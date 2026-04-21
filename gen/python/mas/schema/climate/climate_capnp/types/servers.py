"""Runtime placeholder module for server helpers of `climate.capnp`."""

# pyright: reportUnusedClass=none

from .. import (
    AlterTimeSeriesWrapper,
    AlterTimeSeriesWrapperFactory,
    CSVTimeSeriesFactory,
    Dataset,
    Metadata,
    Service,
    TimeSeries,
)

AlterTimeSeriesWrapperFactoryServer = AlterTimeSeriesWrapperFactory.Server
AlterTimeSeriesWrapperServer = AlterTimeSeriesWrapper.Server
CSVTimeSeriesFactoryServer = CSVTimeSeriesFactory.Server
DatasetServer = Dataset.Server
GetLocationsCallbackServer = Dataset.GetLocationsCallback.Server
InformationServer = Metadata.Information.Server
ServiceServer = Service.Server
SupportedServer = Metadata.Supported.Server
TimeSeriesServer = TimeSeries.Server
