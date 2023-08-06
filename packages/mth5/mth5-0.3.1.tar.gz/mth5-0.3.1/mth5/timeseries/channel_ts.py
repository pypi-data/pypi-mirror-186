# -*- coding: utf-8 -*-
"""
.. module:: timeseries
   :synopsis: Deal with MT time series

.. todo:: Check the conversion to netcdf.  There are some weird serializations of
lists and arrays that goes on, seems easiest to convert all lists to strings and then
convert them back if read in.


:copyright:
    Jared Peacock (jpeacock@usgs.gov)

:license:
    MIT
"""

# ==============================================================================
# Imports
# ==============================================================================
import inspect

import numpy as np
import pandas as pd
import xarray as xr

import mt_metadata.timeseries as metadata
from mt_metadata.timeseries.filters import ChannelResponseFilter
from mt_metadata.utils.mttime import MTime
from mt_metadata.utils.list_dict import ListDict

from mth5.utils.mth5_logger import setup_logger
from mth5.utils import fdsn_tools
from mth5.timeseries.ts_filters import RemoveInstrumentResponse

from obspy.core import Trace

# =============================================================================
# make a dictionary of available metadata classes
# =============================================================================
meta_classes = dict(inspect.getmembers(metadata, inspect.isclass))


def make_dt_coordinates(start_time, sample_rate, n_samples, logger):
    """
    get the date time index from the data

    :param string start_time: start time in time format
    :param float sample_rate: sample rate in samples per seconds
    :param int n_samples: number of samples in time series
    :param logger: logger class object
    :type logger: ":class:`logging.logger`
    :return: date-time index

    """

    if sample_rate in [0, None]:
        msg = (
            f"Need to input a valid sample rate. Not {sample_rate}, "
            + "returning a time index assuming a sample rate of 1"
        )
        logger.warning(msg)
        sample_rate = 1
    if start_time is None:
        msg = (
            f"Need to input a start time. Not {start_time}, "
            + "returning a time index with start time of "
            + "1980-01-01T00:00:00"
        )
        logger.warning(msg)
        start_time = "1980-01-01T00:00:00"
    if n_samples < 1:
        msg = f"Need to input a valid n_samples. Not {n_samples}"
        logger.error(msg)
        raise ValueError(msg)
    if not isinstance(start_time, MTime):
        start_time = MTime(start_time)

    # there is something screwy that happens when your sample rate is not a
    # nice value that can easily fit into the 60 base.  For instance if you
    # have a sample rate of 24000 the dt_freq will be '41667N', but that is
    # not quite right since the rounding clips some samples and your
    # end time will be incorrect (short).
    # FIX: therefore estimate the end time based on the decimal sample rate.
    # need to account for the fact that the start time is the first sample
    # need n_samples - 1
    end_time = start_time + (n_samples - 1) / sample_rate

    # dt_freq = "{0:.0f}N".format(1.0e9 / (sample_rate))

    dt_index = pd.date_range(
        start=start_time.iso_no_tz,
        end=end_time.iso_no_tz,
        periods=n_samples,
    )

    return dt_index


# ==============================================================================
# Channel Time Series Object
# ==============================================================================
class ChannelTS:
    """

    .. note:: Assumes equally spaced samples from the start time.

    The time series is stored in an :class:`xarray.Dataset` that has
    coordinates of time and is a 1-D array labeled 'data'.
    The :class:`xarray.Dataset` can be accessed and set from the `ts`.
    The data is stored in 'ts.data' and the time index is a coordinate of `ts`.

    The time coordinate is made from the start time, sample rate and
    number of samples.  Currently, End time is a derived property and
    cannot be set.

    Channel time series object is based on xarray and :class:`mth5.metadata` therefore
    any type of interpolation, resampling, groupby, etc can be done using xarray
    methods.

    There are 3 metadata classes that hold important metadata

        * :class:`mth5.metadata.Station` holds information about the station
        * :class:`mth5.metadata.Run` holds information about the run the channel
        belongs to.
        * :class`mth5.metadata.Channel` holds information specific to the channel.

    This way a single channel will hold all information needed to represent the
    channel.

    :rubric:

        >>> from mth5.timeseries import ChannelTS
        >>> ts_obj = ChannelTS('auxiliary')
        >>> ts_obj.sample_rate = 8
        >>> ts_obj.start = '2020-01-01T12:00:00+00:00'
        >>> ts_obj.ts = range(4096)
        >>> ts_obj.station_metadata.id = 'MT001'
        >>> ts_obj.run_metadata.id = 'MT001a'
        >>> ts_obj.component = 'temperature'
        >>> print(ts_obj)
                Station      = MT001
                Run          = MT001a
                Channel Type = auxiliary
            Component    = temperature
                Sample Rate  = 8.0
                Start        = 2020-01-01T12:00:00+00:00
                End          = 2020-01-01T12:08:31.875000+00:00
                N Samples    = 4096
        >>> p = ts_obj.ts.plot()



    """

    def __init__(
        self,
        channel_type="auxiliary",
        data=None,
        channel_metadata=None,
        station_metadata=None,
        run_metadata=None,
        survey_metadata=None,
        **kwargs,
    ):

        self.logger = setup_logger(f"{__name__}.{self.__class__.__name__}")

        self._channel_type = self._validate_channel_type(channel_type)
        self._survey_metadata = self._initialize_metadata()

        self._ts = xr.DataArray([1], coords=[("time", [1])], name="ts")
        self._channel_response = ChannelResponseFilter()

        self.survey_metadata = survey_metadata
        self.station_metadata = station_metadata
        self.run_metadata = run_metadata
        self.channel_metadata = channel_metadata

        # input data
        if data is not None:
            self.ts = data
        self._update_xarray_metadata()

        for key in list(kwargs.keys()):
            setattr(self, key, kwargs[key])

    def __str__(self):
        lines = [
            f"Survey:       {self.survey_metadata.id}",
            f"Station:      {self.station_metadata.id}",
            f"Run:          {self.run_metadata.id}",
            f"Channel Type: {self.channel_type}",
            f"Component:    {self.component}",
            f"Sample Rate:  {self.sample_rate}",
            f"Start:        {self.start}",
            f"End:          {self.end}",
            f"N Samples:    {self.n_samples}",
        ]

        return "\n\t".join(["Channel Summary:"] + lines)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):

        if not isinstance(other, ChannelTS):
            raise ValueError(f"Cannot compare ChannelTS with {type(other)}")
        if not other.channel_metadata == self.channel_metadata:
            return False
        if self._ts.equals(other._ts) is False:
            msg = "timeseries are not equal"
            self.logger.info(msg)
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, ChannelTS):
            raise ValueError(f"Cannot compare ChannelTS with {type(other)}")
        self.logger.info("Only testing start time")
        if other.start < self.start and other.sample_rate == self.sample_rate:
            return True
        return False

    def __gt__(self, other):
        return not self.__lt__(other)

    def _initialize_metadata(self):
        """
        Create a single `Survey` object to store all metadata

        :param channel_type: DESCRIPTION
        :type channel_type: TYPE
        :return: DESCRIPTION
        :rtype: TYPE

        """

        survey_metadata = metadata.Survey(id="0")
        survey_metadata.stations.append(metadata.Station(id="0"))
        survey_metadata.stations[0].runs.append(metadata.Run(id="0"))

        ch_metadata = meta_classes[self.channel_type]()
        ch_metadata.type = self.channel_type.lower()
        survey_metadata.stations[0].runs[0].channels.append(ch_metadata)

        return survey_metadata

    def _validate_channel_type(self, channel_type):
        """
        Validate channel type should be [ electric | magnetic | auxiliary ]

        """

        if channel_type is None:
            channel_type = "auxiliary"

        if not channel_type.capitalize() in meta_classes.keys():
            msg = (
                "Channel type is undefined, must be [ electric | "
                "magnetic | auxiliary ]"
            )
            self.logger.error(msg)
            raise ValueError(msg)

        return channel_type.capitalize()

    def _validate_channel_metadata(self, channel_metadata):
        """
        validate input channel metadata
        """

        if not isinstance(
            channel_metadata,
            (metadata.Electric, metadata.Magnetic, metadata.Auxiliary),
        ):
            if isinstance(channel_metadata, dict):
                if self.channel_type.lower() not in [
                    cc.lower() for cc in channel_metadata.keys()
                ]:
                    try:
                        self.channel_type = channel_metadata["type"]
                    except KeyError:
                        pass
                    channel_metadata = {self.channel_type: channel_metadata}

                self.channel_type = list(channel_metadata.keys())[0]
                ch_metadata = meta_classes[self.channel_type]()
                ch_metadata.from_dict(channel_metadata)
                channel_metadata = ch_metadata.copy()
                self.logger.debug("Loading from metadata dict")
                return channel_metadata
            else:
                msg = "input metadata must be type %s or dict, not %s"
                self.logger.error(
                    msg, type(self.channel_metadata), type(channel_metadata)
                )
                raise TypeError(
                    msg % (type(self.channel_metadata), type(channel_metadata))
                )

        return channel_metadata.copy()

    def _validate_run_metadata(self, run_metadata):
        """
        validate run metadata

        """

        if not isinstance(run_metadata, metadata.Run):
            if isinstance(run_metadata, dict):
                if "run" not in [cc.lower() for cc in run_metadata.keys()]:
                    run_metadata = {"Run": run_metadata}
                r_metadata = metadata.Run()
                r_metadata.from_dict(run_metadata)
                self.logger.debug("Loading from metadata dict")
                return r_metadata
            else:
                msg = "input metadata must be type %s or dict, not %s"
                self.logger.error(
                    msg, type(self.run_metadata), type(run_metadata)
                )
                raise TypeError(
                    msg % (type(self.run_metadata), type(run_metadata))
                )
        return run_metadata.copy()

    def _validate_station_metadata(self, station_metadata):
        """
        validate station metadata
        """

        if not isinstance(station_metadata, metadata.Station):
            if isinstance(station_metadata, dict):
                if "station" not in [
                    cc.lower() for cc in station_metadata.keys()
                ]:
                    station_metadata = {"Station": station_metadata}

                st_metadata = metadata.Station()
                st_metadata.from_dict(station_metadata)
                self.logger.debug("Loading from metadata dict")
                return st_metadata
            else:
                msg = "input metadata must be type {0} or dict, not {1}".format(
                    type(self.station_metadata), type(station_metadata)
                )
                self.logger.error(msg)
                raise TypeError(msg)

        return station_metadata.copy()

    def _validate_survey_metadata(self, survey_metadata):
        """
        validate station metadata
        """

        if not isinstance(survey_metadata, metadata.Survey):
            if isinstance(survey_metadata, dict):
                if "station" not in [
                    cc.lower() for cc in survey_metadata.keys()
                ]:
                    survey_metadata = {"Survey": survey_metadata}

                sv_metadata = metadata.Station()
                sv_metadata.from_dict(survey_metadata)
                self.logger.debug("Loading from metadata dict")
                return sv_metadata
            else:
                msg = "input metadata must be type {0} or dict, not {1}".format(
                    type(self.survey_metadata), type(survey_metadata)
                )
                self.logger.error(msg)
                raise TypeError(msg)

        return survey_metadata.copy()

    ### Properties ------------------------------------------------------------
    @property
    def survey_metadata(self):
        """
        survey metadata
        """
        return self._survey_metadata

    @survey_metadata.setter
    def survey_metadata(self, survey_metadata):
        """

        :param survey_metadata: survey metadata object or dictionary
        :type survey_metadata: :class:`mt_metadata.timeseries.Survey` or dict

        """

        if survey_metadata is not None:
            survey_metadata = self._validate_survey_metadata(survey_metadata)
            self._survey_metadata.update(survey_metadata)

    @property
    def station_metadata(self):
        """
        station metadata
        """

        return self.survey_metadata.stations[0]

    @station_metadata.setter
    def station_metadata(self, station_metadata):
        """
        set station metadata from a valid input
        """

        if station_metadata is not None:
            station_metadata = self._validate_station_metadata(station_metadata)

            runs = ListDict()
            if self.run_metadata.id not in ["0", 0, None]:
                runs.append(self.run_metadata.copy())
            runs.extend(station_metadata.runs)
            if len(runs) == 0:
                runs[0] = metadata.Run(id="0")

            # be sure there is a level below
            if len(runs[0].channels) == 0:
                ch_metadata = meta_classes[self.channel_type]()
                ch_metadata.type = self.channel_type.lower()
                runs[0].channels.append(ch_metadata)

            stations = ListDict()
            stations.append(station_metadata)
            stations[0].runs = runs

            self.survey_metadata.stations = stations

    @property
    def run_metadata(self):
        """
        station metadata
        """

        return self.survey_metadata.stations[0].runs[0]

    @run_metadata.setter
    def run_metadata(self, run_metadata):
        """
        set run metadata from a valid input
        """

        # need to make sure the first index is the desired channel
        if run_metadata is not None:
            run_metadata = self._validate_run_metadata(run_metadata)

            runs = ListDict()
            runs.append(run_metadata)
            channels = ListDict()
            if self.component is not None:
                key = str(self.component)

                channels.append(self.station_metadata.runs[0].channels[key])
                # add existing channels
                channels.extend(
                    self.run_metadata.channels, skip_keys=[key, "0"]
                )

            # add channels from input metadata
            channels.extend(run_metadata.channels)

            runs[0].channels = channels
            runs.extend(
                self.station_metadata.runs, skip_keys=[run_metadata.id, "0"]
            )

            self._survey_metadata.stations[0].runs = runs

    @property
    def channel_metadata(self):
        """
        station metadata
        """

        return self._survey_metadata.stations[0].runs[0].channels[0]

    @channel_metadata.setter
    def channel_metadata(self, channel_metadata):
        """
        set run metadata from a valid input
        """

        if channel_metadata is not None:
            channel_metadata = self._validate_channel_metadata(channel_metadata)
            if channel_metadata.component is not None:
                channels = ListDict()
                if (
                    channel_metadata.component
                    in self.run_metadata.channels.keys()
                ):
                    channels.append(
                        self.run_metadata.channels[channel_metadata.component]
                    )
                    channels[0].update(channel_metadata)
                else:
                    channels.append(channel_metadata)
                channels.extend(
                    self.run_metadata.channels,
                    skip_keys=[channel_metadata.component, None],
                )

                self.run_metadata.channels = channels
                self.channel_type = self.run_metadata.channels[0].type
            else:
                raise ValueError("Channel ID cannot be None")

    @property
    def ts(self):
        return self._ts.data

    @ts.setter
    def ts(self, ts_arr):
        """
        if setting ts with a pandas data frame, make sure the data is in a
        column name 'data'

        """

        if isinstance(ts_arr, (np.ndarray, list, tuple)):
            if not isinstance(ts_arr, np.ndarray):
                ts_arr = np.array(ts_arr)
            # Validate an input array to make sure its 1D
            if len(ts_arr.shape) == 2:
                if 1 in ts_arr.shape:
                    ts_arr = ts_arr.reshape(ts_arr.size)
                else:
                    msg = f"Input array must be 1-D array not {ts_arr.shape}"
                    self.logger.error(msg)
                    raise ValueError(msg)
            dt = make_dt_coordinates(
                self.start, self.sample_rate, ts_arr.size, self.logger
            )
            self._ts = xr.DataArray(
                ts_arr, coords=[("time", dt)], name=self.component
            )
            self._update_xarray_metadata()
        elif isinstance(ts_arr, pd.core.frame.DataFrame):
            if isinstance(
                ts_arr.index[0], pd._libs.tslibs.timestamps.Timestamp
            ):
                dt = ts_arr.index
            else:
                dt = make_dt_coordinates(
                    self.start,
                    self.sample_rate,
                    ts_arr["data"].size,
                    self.logger,
                )
            try:
                self._ts = xr.DataArray(
                    ts_arr["data"], coords=[("time", dt)], name=self.component
                )
                self._update_xarray_metadata()
            except AttributeError:
                msg = (
                    "Data frame needs to have a column named `data` "
                    + "where the time series data is stored"
                )
                self.logger.error(msg)
                raise ValueError(msg)
        elif isinstance(ts_arr, pd.core.series.Series):
            if isinstance(
                ts_arr.index[0], pd._libs.tslibs.timestamps.Timestamp
            ):
                dt = ts_arr.index
            else:
                dt = make_dt_coordinates(
                    self.start,
                    self.sample_rate,
                    ts_arr["data"].size,
                    self.logger,
                )
            self._ts = xr.DataArray(
                ts_arr.values, coords=[("time", dt)], name=self.component
            )
            self._update_xarray_metadata()
        elif isinstance(ts_arr, xr.DataArray):
            # TODO: need to validate the input xarray
            self._ts = ts_arr
            # need to pull out the metadata as a separate dictionary
            meta_dict = dict([(k, v) for k, v in ts_arr.attrs.items()])

            # need to get station and run metadata out
            survey_dict = {}
            station_dict = {}
            run_dict = {}

            for key in [k for k in meta_dict.keys() if "survey." in k]:
                survey_dict[key.split("station.")[-1]] = meta_dict.pop(key)
            for key in [k for k in meta_dict.keys() if "station." in k]:
                station_dict[key.split("station.")[-1]] = meta_dict.pop(key)
            for key in [k for k in meta_dict.keys() if "run." in k]:
                run_dict[key.split("run.")[-1]] = meta_dict.pop(key)

            self.channel_type = meta_dict["type"]
            ch_metadata = meta_classes[self.channel_type]()
            ch_metadata.from_dict({self.channel_type: meta_dict})

            self.survey_metadata.from_dict({"survey": survey_dict})
            self.station_metadata.from_dict({"station": station_dict})
            self.run_metadata.from_dict({"run": run_dict})
            self.channel_metadata = ch_metadata
            # need to run this incase things are different.
            self._update_xarray_metadata()
        else:
            msg = (
                "Data type {0} not supported".format(type(ts_arr))
                + ", ts needs to be a numpy.ndarray, pandas DataFrame, "
                + "or xarray.DataArray."
            )
            raise TypeError(msg)

    @property
    def time_index(self):
        """
        time index as a numpy array dtype np.datetime[ns]

        :return: array of the time index
        :rtype: np.ndarray(dtype=np.datetime[ns])

        """

        try:
            return self._ts.time.to_numpy()
        except AttributeError:
            return self._ts.time.values

    @property
    def channel_type(self):
        """Channel Type"""
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        """change channel type means changing the metadata type"""

        value = self._validate_channel_type(value)
        if value != self._channel_type:
            m_dict = self.channel_metadata.to_dict(single=True)

            msg = (
                f"Changing metadata from {self.channel_type} to {value}, "
                "will translate any similar attributes."
            )
            channel_metadata = meta_classes[value]()
            self.logger.debug(msg)
            for key in channel_metadata.to_dict(single=True).keys():
                # need to skip type otherwise it keeps the same type
                if key in ["type"]:
                    continue
                try:
                    channel_metadata.set_attr_from_name(key, m_dict[key])
                except KeyError:
                    pass
            self._channel_type = value
            self.run_metadata.channels[0] = channel_metadata

    def _update_xarray_metadata(self):
        """
        Update xarray attrs dictionary with metadata.  Here we are assuming that
        self.channel_metadata is the parent and attrs in xarray are children because all
        metadata will be validated by :class:`mth5.metadata` class objects.

        Eventually there should be a way that this is automatic, but I'm not that
        clever yet.

        This should be mainly used internally but gives the user a way to update
        metadata.

        """
        self.logger.debug("Updating xarray attributes")

        self.channel_metadata.time_period.start = self.start.iso_no_tz
        self.channel_metadata.time_period.end = self.end.iso_no_tz
        self.channel_metadata.sample_rate = self.sample_rate

        self._ts.attrs.update(
            self.channel_metadata.to_dict()[self.channel_metadata._class_name]
        )
        # add station and run id's here, for now this is all we need but may need
        # more metadata down the road.
        self._ts.attrs["station.id"] = self.station_metadata.id
        self._ts.attrs["run.id"] = self.run_metadata.id

    @property
    def component(self):
        """component"""
        return self.channel_metadata.component

    @component.setter
    def component(self, comp):
        """set component in metadata and carry through"""
        if self.channel_metadata.type == "electric":
            if comp[0].lower() != "e":
                msg = (
                    "The current timeseries is an electric channel. "
                    "Cannot change channel type, create a new ChannelTS object."
                )
                self.logger.error(msg)
                raise ValueError(msg)
        elif self.channel_metadata.type == "magnetic":
            if comp[0].lower() not in ["h", "b"]:
                msg = (
                    "The current timeseries is a magnetic channel. "
                    "Cannot change channel type, create a new ChannelTS object."
                )
                self.logger.error(msg)
                raise ValueError(msg)
        if self.channel_metadata.type == "auxiliary":
            if comp[0].lower() in ["e", "h", "b"]:
                msg = (
                    "The current timeseries is an auxiliary channel. "
                    "Cannot change channel type, create a new ChannelTS object."
                )
                self.logger.error(msg)
                raise ValueError(msg)
        self.channel_metadata.component = comp

        # need to update the keys in the list dict
        channels = ListDict()
        channels.append(self.channel_metadata)
        if len(self.run_metadata.channels) > 1:
            for ch in self.run_metadata.channels[1:]:
                channels.append(ch)
        self.run_metadata.channels = channels

        self._update_xarray_metadata()

    # --> number of samples just to make sure there is consistency
    @property
    def n_samples(self):
        """number of samples"""
        return int(self.ts.size)

    @n_samples.setter
    def n_samples(self, n_samples):
        """number of samples (int)"""
        self.logger.warning(
            "Cannot set the number of samples. Use `ChannelTS.resample` or `get_slice`"
        )

    @property
    def has_data(self):
        """
        check to see if there is an index in the time series
        """
        if len(self._ts) > 1:
            if isinstance(
                self._ts.indexes["time"][0],
                pd._libs.tslibs.timestamps.Timestamp,
            ):
                return True
            return False
        else:
            return False

    # --> sample rate
    @property
    def sample_rate(self):
        """sample rate in samples/second"""
        if self.has_data:
            # this is more accurate for high sample rates, the way
            # pandas.date_range rounds nanoseconds is not consistent between
            # samples, therefore taking the median provides better results
            # if the time series is long this can be inefficient so test first
            if (
                self._ts.coords.indexes["time"][1]
                - self._ts.coords.indexes["time"][0]
            ).total_seconds() < 1e-4:

                sr = 1 / (
                    float(np.median(np.diff(self._ts.coords.indexes["time"])))
                    / 1e9
                )

            else:
                t_diff = (
                    self._ts.coords.indexes["time"][-1]
                    - self._ts.coords.indexes["time"][0]
                )
                sr = self._ts.size / t_diff.total_seconds()

        else:
            self.logger.debug(
                "Data has not been set yet, sample rate is from metadata"
            )
            sr = self.channel_metadata.sample_rate
            if sr is None:
                sr = 0.0
        return np.round(sr, 0)

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """
        sample rate in samples/second

        type float
        """
        if self.has_data:
            self.logger.warning(
                "Resetting sample_rate assumes same start time and "
                + "same number of samples, resulting in new end time. "
                + "If you want to downsample existing time series "
                + "use the method channelTS.resample()"
            )
            self.logger.debug(
                f"Resetting sample rate from {self.sample_rate} to {sample_rate}"
            )
            new_dt = make_dt_coordinates(
                self.start, sample_rate, self.n_samples, self.logger
            )
            self._ts.coords["time"] = new_dt
        else:
            if self.channel_metadata.sample_rate not in [0.0, None]:
                self.logger.warning(
                    f"Resetting ChannelTS.channel_metadata.sample_rate to {sample_rate}. "
                )
            self.channel_metadata.sample_rate = sample_rate
        self._update_xarray_metadata()

    @property
    def sample_interval(self):
        """
        Sample interval = 1 / sample_rate

        :return: DESCRIPTION
        :rtype: TYPE

        """

        if self.sample_rate != 0:
            return 1.0 / self.sample_rate
        return 0.0

    ## set time and set index
    @property
    def start(self):
        """MTime object"""
        if self.has_data:
            return MTime(self._ts.coords.indexes["time"][0].isoformat())
        else:
            self.logger.debug(
                "Data not set yet, pulling start time from "
                + "metadata.time_period.start"
            )
            return MTime(self.channel_metadata.time_period.start)

    @start.setter
    def start(self, start_time):
        """
        start time of time series in UTC given in some format or a datetime
        object.

        Resets epoch seconds if the new value is not equivalent to previous
        value.

        Resets how the ts data frame is indexed, setting the starting time to
        the new start time.

        :param start_time: start time of time series, can be string or epoch seconds

        """

        if not isinstance(start_time, MTime):
            start_time = MTime(start_time)
        self.channel_metadata.time_period.start = start_time.iso_str
        if self.has_data:
            if start_time == MTime(
                self._ts.coords.indexes["time"][0].isoformat()
            ):
                return
            else:
                new_dt = make_dt_coordinates(
                    start_time, self.sample_rate, self.n_samples, self.logger
                )
                self._ts.coords["time"] = new_dt
        # make a time series that the data can be indexed by
        else:
            self.logger.debug("No data, just updating metadata start")

        self._survey_metadata.stations[0].runs[0].update_time_period()
        self._survey_metadata.stations[0].update_time_period()
        self._survey_metadata.update_time_period()

        self._update_xarray_metadata()

    @property
    def end(self):
        """MTime object"""
        if self.has_data:
            return MTime(self._ts.coords.indexes["time"][-1].isoformat())
        else:
            self.logger.debug(
                "Data not set yet, pulling end time from "
                + "metadata.time_period.end"
            )
            return MTime(self.channel_metadata.time_period.end)

    @end.setter
    def end(self, end_time):
        """
        end time of time series in UTC given in some format or a datetime
        object.

        Resets epoch seconds if the new value is not equivalent to previous
        value.

        Resets how the ts data frame is indexed, setting the starting time to
        the new start time.
        """
        self.logger.warning(
            "Cannot set `end`. If you want a slice, then "
            + "use get_slice method"
        )

    @property
    def channel_response_filter(self):
        """
        Full channel response filter

        :return: DESCRIPTION
        :rtype: TYPE

        """

        return self._channel_response

    @channel_response_filter.setter
    def channel_response_filter(self, value):
        """

        :param value: DESCRIPTION
        :type value: TYPE
        :return: DESCRIPTION
        :rtype: TYPE

        """
        if value is None:
            return
        if not isinstance(value, ChannelResponseFilter):
            msg = (
                "channel response must be a "
                "mt_metadata.timeseries.filters.ChannelResponseFilter object "
                f"not {type(value)}."
            )
            self.logger.error(msg)
            raise TypeError(msg)
        self._channel_response = value

        # update channel metadata
        if self.channel_metadata.filter.name != value.names:
            self.channel_metadata.filter.name = []
            self.channel_metadata.filter.applied = []

            for f_name in self._channel_response.names:
                self.channel_metadata.filter.name.append(f_name)
            self.channel_metadata.filter.applied = [False] * len(
                self.channel_metadata.filter.name
            )

    def remove_instrument_response(self, **kwargs):
        """
        Remove instrument response from the given channel response filter

        The order of operations is important (if applied):

            1) detrend
            2) zero mean
            3) zero pad
            4) time window
            5) frequency window
            6) remove response
            7) undo time window
            8) bandpass

        **kwargs**

        :param plot: to plot the calibration process [ False | True ]
        :type plot: boolean, default True
        :param detrend: Remove linar trend of the time series
        :type detrend: boolean, default True
        :param zero_mean: Remove the mean of the time series
        :type zero_mean: boolean, default True
        :param zero_pad: pad the time series to the next power of 2 for efficiency
        :type zero_pad: boolean, default True
        :param t_window: Time domain windown name see `scipy.signal.windows` for options
        :type t_window: string, default None
        :param t_window_params: Time domain window parameters, parameters can be
        found in `scipy.signal.windows`
        :type t_window_params: dictionary
        :param f_window: Frequency domain windown name see `scipy.signal.windows` for options
        :type f_window: string, defualt None
        :param f_window_params: Frequency window parameters, parameters can be
        found in `scipy.signal.windows`
        :type f_window_params: dictionary
        :param bandpass: bandpass freequency and order {"low":, "high":, "order":,}
        :type bandpass: dictionary

        """

        calibrated_ts = ChannelTS()
        calibrated_ts.__dict__.update(self.__dict__)

        if self.channel_metadata.filter.name is []:
            self.logger.warning(
                "No filters to apply to calibrate time series data"
            )
            return calibrated_ts

        remover = RemoveInstrumentResponse(
            self.ts,
            self.time_index,
            self.sample_interval,
            self.channel_response_filter,
            **kwargs,
        )

        calibrated_ts.ts = remover.remove_instrument_response()
        # change applied booleans
        calibrated_ts.channel_metadata.filter.applied = [True] * len(
            self.channel_metadata.filter.applied
        )

        # update units
        # This is a hack for now until we come up with a standard for
        # setting up the filter list.  Currently it follows the FDSN standard
        # which has the filter stages starting with physical units to digital
        # counts.
        if (
            self.channel_response_filter.units_out
            == self.channel_metadata.units
        ):
            calibrated_ts._ts.attrs[
                "units"
            ] = self.channel_response_filter.units_in
            calibrated_ts.channel_metadata.units = (
                self.channel_response_filter.units_in
            )
        elif (
            self.channel_response_filter.units_out == None
            and self.channel_response_filter.units_out == None
        ):
            calibrated_ts.channel_metadata.units = self.channel_metadata.units
        else:
            calibrated_ts._ts.attrs[
                "units"
            ] = self.channel_response_filter.units_in
            calibrated_ts.channel_metadata.units = (
                self.channel_response_filter.units_in
            )

        calibrated_ts._update_xarray_metadata()

        return calibrated_ts

    def get_slice(self, start, end=None, n_samples=None):
        """
        Get a slice from the time series given a start and end time.

        Looks for >= start & <= end

        Uses loc to be exact with milliseconds

        :param start: DESCRIPTION
        :type start: TYPE
        :param end: DESCRIPTION
        :type end: TYPE
        :return: DESCRIPTION
        :rtype: TYPE

        """

        if n_samples is None and end is None:
            msg = "Must input either end_time or n_samples."
            self.logger.error(msg)
            raise ValueError(msg)
        if n_samples is not None and end is not None:
            msg = "Must input either end_time or n_samples, not both."
            self.logger.error(msg)
            raise ValueError(msg)
        if not isinstance(start, MTime):
            start = MTime(start)
        if n_samples is not None:
            n_samples = int(n_samples)
            end = start + ((n_samples - 1) / self.sample_rate)
        if end is not None:
            if not isinstance(end, MTime):
                end = MTime(end)

        chunk = self._ts.indexes["time"].slice_indexer(
            start=np.datetime64(start.iso_no_tz),
            end=np.datetime64(end.iso_no_tz),
        )
        new_ts = self._ts.isel(indexers={"time": chunk})

        new_ch_ts = ChannelTS(
            channel_type=self.channel_type,
            data=new_ts,
            survey_metadata=self.survey_metadata,
            channel_response_filter=self.channel_response_filter,
        )

        return new_ch_ts

    # decimate data
    def resample(self, dec_factor=1, inplace=False):
        """
        decimate the data by using scipy.signal.decimate

        :param dec_factor: decimation factor
        :type dec_factor: int

        * refills ts.data with decimated data and replaces sample_rate

        """

        new_dt_freq = "{0:.0f}N".format(1e9 / (self.sample_rate / dec_factor))

        new_ts = self._ts.resample(time=new_dt_freq).nearest(
            tolerance=new_dt_freq
        )
        new_ts.attrs["sample_rate"] = self.sample_rate / dec_factor
        self.channel_metadata.sample_rate = new_ts.attrs["sample_rate"]

        if inplace:
            self.ts = new_ts
        else:
            new_ts.attrs.update(
                self.channel_metadata.to_dict()[
                    self.channel_metadata._class_name
                ]
            )
            # return new_ts
            return ChannelTS(
                self.channel_metadata.type,
                data=new_ts,
                metadata=self.channel_metadata,
            )

    def to_xarray(self):
        """
        Returns a :class:`xarray.DataArray` object of the channel timeseries
        this way metadata from the metadata class is updated upon return.

        :return: Returns a :class:`xarray.DataArray` object of the channel timeseries
        this way metadata from the metadata class is updated upon return.
        :rtype: :class:`xarray.DataArray`


        >>> import numpy as np
        >>> from mth5.timeseries import ChannelTS
        >>> ex = ChannelTS("electric")
        >>> ex.start = "2020-01-01T12:00:00"
        >>> ex.sample_rate = 16
        >>> ex.ts = np.random.rand(4096)


        """
        self._update_xarray_metadata()
        return self._ts

    def to_obspy_trace(self):
        """
        Convert the time series to an :class:`obspy.core.trace.Trace` object.  This
        will be helpful for converting between data pulled from IRIS and data going
        into IRIS.

        :return: DESCRIPTION
        :rtype: TYPE

        """

        obspy_trace = Trace(self.ts)
        obspy_trace.stats.channel = fdsn_tools.make_channel_code(
            self.channel_metadata
        )
        obspy_trace.stats.starttime = self.start.iso_str
        obspy_trace.stats.sampling_rate = self.sample_rate
        obspy_trace.stats.station = self.station_metadata.fdsn.id

        return obspy_trace

    def from_obspy_trace(self, obspy_trace):
        """
        Fill data from an :class:`obspy.core.Trace`

        :param obspy.core.trace obspy_trace: Obspy trace object

        """

        if not isinstance(obspy_trace, Trace):
            msg = f"Input must be obspy.core.Trace, not {type(obspy_trace)}"
            self.logger.error(msg)
            raise TypeError(msg)
        if obspy_trace.stats.channel[1].lower() in ["e", "q"]:
            self.channel_type = "electric"
        elif obspy_trace.stats.channel[1].lower() in ["h", "b", "f"]:
            self.channel_type = "magnetic"
        else:
            self.channel_type = "auxiliary"
        mt_code = fdsn_tools.make_mt_channel(
            fdsn_tools.read_channel_code(obspy_trace.stats.channel)
        )
        self.channel_metadata.component = mt_code
        self.start = obspy_trace.stats.starttime.isoformat()
        self.sample_rate = obspy_trace.stats.sampling_rate
        self.station_metadata.fdsn.id = obspy_trace.stats.station
        self.station_metadata.fdsn.network = obspy_trace.stats.network
        self.station_metadata.id = obspy_trace.stats.station
        self.channel_metadata.units = "counts"
        self.ts = obspy_trace.data

    def plot(self):
        """
        Simple plot of the data

        :return: figure object
        :rtype: matplotlib.figure

        """

        return self._ts.plot()
