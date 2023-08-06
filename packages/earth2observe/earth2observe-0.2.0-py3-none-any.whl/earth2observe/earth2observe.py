"""Front end module that runs each data source backend."""
from earth2observe.chirps import CHIRPS
from earth2observe.ecmwf import ECMWF


class Earth2Observe:
    """End user class to call all the data source classes abailable in earth2observe."""

    DataSources = {"ecmwf": ECMWF, "chirps": CHIRPS}

    def __init__(
        self,
        data_source: str = "chirps",
        temporal_resolution: str = "daily",
        start: str = None,
        end: str = None,
        path: str = "",
        variables: list = None,
        lat_lim: list = None,
        lon_lim: list = None,
        fmt: str = "%Y-%m-%d",
    ):
        if data_source not in self.DataSources:
            raise ValueError(f"{data_source} not supported")

        self.datasource = self.DataSources[data_source](
            start=start,
            end=end,
            variables=variables,
            lat_lim=lat_lim,
            lon_lim=lon_lim,
            temporal_resolution=temporal_resolution,
            path=path,
            fmt=fmt,
        )

    def download(self, progress_bar: bool = True, *args, **kwargs):
        self.datasource.download(progress_bar=progress_bar, *args, **kwargs)
