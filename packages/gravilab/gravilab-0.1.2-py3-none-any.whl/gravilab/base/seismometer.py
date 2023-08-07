"""
Class containing data in various formats associated with a seismometer (time series, spectra, response).

Artem Basalaev <artem[dot]basalaev[at]physik.uni-hamburg.de>,
Christian Darsow-Fromm <cdarsowf[at]physnet.uni-hamburg.de>
"""
from copy import copy

from gravilab.formats.spectrum import Spectrum


class Seismometer:
    """Class containing data in various formats associated with a seismometer (time series, spectra, response)."""

    def __init__(
        self, time_series=None, spectrum=None, name="generic seismometer", response=None
    ):
        """
        Create object of Seismometer class. Either SeismicTimeSeries or Spectrum should be supplied on input.

        Parameters
        ----------
        name: str
            name for this seismometer, optional
        time_series: SeismicTimeSeries
            time series associated with this seismometer (for each channel)
        spectrum: dict of Spectrum
            spectrum associated with this seismometer (for each channel)
        response:
            pole-zero response dictionary associated with this Seismometer
        """
        if time_series is None and spectrum is None:
            raise ValueError(
                "Must specify either time series (`time_series`) or a spectrum (`spectrum`) on input"
            )
        self._name = name
        self._time_series = time_series
        if spectrum is None:
            self._spectrum = {}
        else:
            self._spectrum = spectrum
        self.response = response

    def __copy__(self):
        """
        Copy this Seismometer object.

        Returns
        -------
        s: Seismometer
            Copy of this Seismometer
        """
        s = Seismometer(
            name=self.name, time_series=self.time_series, spectrum=self._spectrum
        )
        s.response = self.response
        return s

    @property
    def name(self):
        """
        Get seismometer name.

        Returns
        -------
        str
            Name
        """
        return self._name

    def slice_time_series(self, starttime, endtime):
        """
        Slice time series data associated with this element.

        Parameters
        ----------
        starttime: UTCDateTime
            new starting time
        endtime: UTCDateTime
            new end time
        """
        s = copy(self)
        s._time_series = self._time_series.slice(starttime, endtime)
        return s

    @property
    def time_series(self):
        """
        Get time series data associated with this element.

        Returns
        -------
        time_series: TimeSeries
            Time series
        """
        if self._time_series is None:
            raise ValueError("don't have time series data!")
        return self._time_series

    def psd(self, **kwargs):
        """
        Shorthand to calculate default PSD spectrum.

        Parameters
        ----------
        kwargs: dict
            Arguments accepted by spicypy.TimeSeries.psd

        Returns
        -------
        Spectrum
            Spectrum containing pandas DataFrame and some parameters
        """
        return self.spectrum(spectrum_type="psd", **kwargs)

    def asd(self, **kwargs):
        """
        Shorthand to calculate ASD spectrum.

        Parameters
        ----------
        kwargs: dict
            Arguments accepted by spicypy.TimeSeries.psd

        Returns
        -------
        Spectrum
            Spectrum containing pandas DataFrame and some parameters
        """
        return self.spectrum(spectrum_type="asd", **kwargs)

    def spectrum(self, spectrum_type="asd", **kwargs):
        """
        Get time spectrum associated with this element, of specified spectrum type.

        Parameters
        ----------
        spectrum_type: str
            Specify which spectrum type to compute, e.g. "lpsd"

        Returns
        -------
        Spectrum
            Spectrum containing pandas DataFrame and some parameters
        """

        if self._time_series is None:
            raise ValueError(
                'Do not have associated spectrum of type "'
                + spectrum_type
                + '"'
                + " and no time series data to calculate it. Exiting!"
            )

        time_series = self._time_series.to_spicypy()
        spectra_dict = {}
        for channel in time_series:
            if spectrum_type == "psd":  # use default (Welch) averaging in Spicypy
                spectra_dict[channel] = time_series[channel].psd(**kwargs)
            elif spectrum_type == "asd":
                spectra_dict[channel] = time_series[channel].asd(**kwargs)
            else:
                raise ValueError(
                    "Only `asd` and `psd` are supported as spectrum types. "
                    "Perhaps you wanted to specify different averaging method? `method` keyword."
                )

        self._spectrum[spectrum_type] = Spectrum(
            data=spectra_dict, spectrum_type=spectrum_type, response=self.response
        )
        return self._spectrum[spectrum_type]
