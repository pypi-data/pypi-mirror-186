"""
Class to read data (base class).

Artem Basalaev <artem[dot]basalaev[at]physik.uni-hamburg.de>,
Christian Darsow-Fromm <cdarsowf[at]physnet.uni-hamburg.de>
"""
import os
from obspy import read

from gravilab.formats.seismic_time_series import SeismicTimeSeries


class DataReader:
    """Class to read seismic data."""

    def __init__(self, data_path, channels=None, ignore_extension=False):
        """
        Create DataReader object.

        Parameters
        ----------
        data_path: str
            A valid path pointing to a data file or a folder with files (contained data files are found recursively).
        channels: dict
            Channels for data, optional (e.g. an axis along which measurement is performed).
            Contains channel name that should be present in miniseed file.
            If not provided, lumping all data files together assuming one channel "all".
            Example: {"vertical":"HHZ"}
        ignore_extension: bool
            Try to open any files present; by default relies on known seismic data file extensions.
        """
        self._channels = channels
        if channels is None:
            self._channels = {"all": "*"}
        self._data_path = data_path
        self._ignore_extension = ignore_extension
        self._one_file = False
        self._check_path()
        self.data_file_list = []

    def read_data(self):
        """
        Read seismic data from the path specified on init.

        Returns
        -------
        SeismicTimeSeries
            time series data in SeismicTimeSeries class.
        """
        self._find_files()
        data = {}
        print("Reading data...")
        for file in self.data_file_list:
            stream = read(file)
            for channel in self._channels:
                channel_mask = self._channels[channel]
                for trace in stream:
                    if channel_mask == trace.stats.channel or channel_mask == "*":
                        if channel not in data:
                            data[channel] = trace
                        else:
                            data[channel] += trace
        if not data:
            raise ValueError("Could not find any data for channels specified")
        for channel in self._channels:
            if channel not in data:
                raise ValueError("Could not find any data for channel" + channel)
        print("Done.")
        return SeismicTimeSeries(data)

    def _is_seismic_data(self, file):
        """
        Check if file extension is known to be seismic data.
        With self._ignore_extension set to True always returns True

        Returns
        -------
        bool
            Whether tested file is seismic data.
        """
        if self._ignore_extension:
            return True
        if ".msd" in file or ".miniseed" in file or ".mseed" in file:
            return True
        return False

    def _find_files(self):
        """Find seismic data in path specified in init. Recursively checks all files."""
        self.data_file_list = []
        if self._one_file and self._is_seismic_data(self._data_path):
            self.data_file_list = [self._data_path]
        else:
            for root, _, files in os.walk(self._data_path):
                for file in files:
                    current_file = os.path.join(root, file)
                    if self._is_seismic_data(current_file):
                        self.data_file_list.append(current_file)

        if len(self.data_file_list) == 0:
            raise ValueError("ERROR: found no seismic data files. Exiting!")

    def _check_path(self):
        """Check input path and determine whether it's just one file or a folder."""
        # first deal with exception
        if not os.path.isdir(self._data_path) and not os.path.isfile(self._data_path):
            # invalid path (not a file and not a folder)
            raise ValueError(
                'ERROR: Could open path "'
                + str(self._data_path)
                + '" Check if this is a valid path. Exiting!'
            )
        if os.path.isdir(self._data_path):
            self._one_file = False
        elif os.path.isfile(self._data_path):
            self._one_file = True
        else:
            # invalid path (not a file and not a folder)
            raise ValueError(
                'ERROR: Could open path "'
                + str(self._data_path)
                + '" Check if this is a valid path. Exiting!'
            )
