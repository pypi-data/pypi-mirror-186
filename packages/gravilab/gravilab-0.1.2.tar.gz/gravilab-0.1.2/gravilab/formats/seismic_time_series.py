"""
Base class to hold time series data and associated parameters and methods.

Artem Basalaev <artem[dot]basalaev[at]physik.uni-hamburg.de>,
Christian Darsow-Fromm <cdarsowf[at]physnet.uni-hamburg.de>
"""
import numpy as np
import pandas as pd

from spicypy.signal.time_series import TimeSeries


class SeismicTimeSeries:
    """Class to hold seismic time series and associated parameters and methods."""

    def __init__(self, data):
        """
        Create SeismicTimeSeries from input seismic data.

        Parameters
        ----------
        data: dict of obspy.Trace
        """
        self._data = data

    def data(self):
        """
        Return associated data.

        Returns
        -------
        data: dict
           Time series data as dict of obspy.Trace objects
        """
        return self._data

    def __getitem__(self, channel):
        """
        Return associated data for specified channel

        Returns
        -------
        data: obspy.Trace
           Time series data as obspy.Trace object
        """
        return self.data()[channel]

    @property
    def sampling_rate(self):
        """
        Get sampling rate for these TimeSeries.

        Returns
        -------
        sample_rate: float
           sampling rate
        """
        sampling_rates = []
        for channel in self._data:
            sampling_rates.append(self._data[channel].stats.sampling_rate)
        sample_rate = np.median(sampling_rates)
        std = np.std(sampling_rates)

        if std / sample_rate > 1e-1:
            raise ValueError(
                "Length of some sampling rates deviates a lot from the median. Some data may be corrupt!\n"
                f"Median sample rate: {sample_rate}, standard deviation: {std}"
            )
        return sample_rate

    def to_spicypy(self):
        """
        Return associated data as a dict of Spicypy TimeSeries.

        Returns
        -------
        ts_dict: dict
           Dictionary of spicypy.TimeSeries.
        """
        ts_dict = {}
        df = self.to_data_frame() * 1.0  # multiplying by 1.0 to convert to float,
        for channel in df:  # spectrum calculation algorithms "don't like" integers
            ts = TimeSeries(
                df[channel], sample_rate=self.sampling_rate, channel=channel
            )
            ts_dict[channel] = ts
        return ts_dict

    def to_data_frame(self):
        """
        Return associated data in a common (DataFrame) format.

        Returns
        -------
        df: pandas::DataFrame
           Time series data: DataFrame with times as index and columns for different channels
        """
        data = self._data
        df = pd.DataFrame()
        index = {}
        for channel in data:
            index[channel] = data[channel].times()
            df.index = data[channel].times()
            df[channel] = data[channel].data

        # sanity check - we expect ALL channels to have the same indices
        if len(index) > 1:
            for _, channel_index in index.items():
                if not np.array_equal(channel_index, df.index):
                    raise ValueError(
                        "ALL channels should have the same time stamps to convert to a DataFrame"
                    )
        return df

    def slice(self, *args, **kwargs):
        """
        Get time series for specified time slices.

        Parameters
        ----------
        args: list
            Positional arguments passed to obspy.Stream()
        kwargs: dict
            Keyword arguments passed to obspy.Stream()

        Returns
        -------
        SeismicTimeSeries
           Sliced time series
        """
        sliced_series = {}
        for channel in self._data:
            st = self._data[channel]
            sliced_series[channel] = st.slice(*args, **kwargs)
        return SeismicTimeSeries(data=sliced_series)

    def __sub__(self, other):
        """
        Subtraction overload.

        Parameters
        ----------
        other: TimeSeries
            Another time series

        Returns
        -------
        TimeSeries
            Subtracted time series
        """
        return self.subtract(other)

    def subtract(self, other_time_series):
        """
        Subtract another time series.

        Parameters
        ----------
        other_time_series: TimeSeries
            Another time series

        Returns
        -------
        TimeSeries
            Subtracted time series
        """
        if not self._match(other_time_series):
            raise ValueError(
                "Time series for subtraction don't match! (Check lengths, channel names etc)"
            )
        subtracted_data = {}
        other_data = other_time_series.data()
        for channel in self._data:
            st1 = self._data[channel].copy()
            st2 = other_data[channel]
            st1.data = st1.data - st2.data
            subtracted_data[channel] = st1
        return SeismicTimeSeries(data=subtracted_data)

    def _match(self, other_time_series):
        """
        Match with another time series, to find out if operations such as subtraction are possible.

        Parameters
        ----------
        other_time_series: TimeSeries
            Another time series

        Returns
        -------
        bool
            Matching or not
        """
        our_data = self._data
        other_data = other_time_series.data()
        for channel in our_data:
            if channel not in other_data:
                print("No channel " + channel + " in other time series")
                return False
        for channel in other_data:
            if channel not in our_data:
                print("No channel " + channel + " in this time series")
                return False
        for channel in our_data:
            if len(our_data[channel]) != len(other_data[channel]):
                print(
                    "Number of traces in our data ("
                    + str(len(our_data[channel]))
                    + ") does not match number of traces in other data"
                    + str(len(other_data[channel]))
                )
                return False
        return True
