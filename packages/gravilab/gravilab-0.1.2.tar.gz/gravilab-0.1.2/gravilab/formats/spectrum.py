"""
Class to hold spectrum data and associated parameters and methods.

Artem Basalaev <artem[dot]basalaev[at]physik.uni-hamburg.de>,
Christian Darsow-Fromm <cdarsowf[at]physnet.uni-hamburg.de>
"""

from scipy import signal
import numpy as np


class Spectrum:
    """
    Class to hold spectrum data and associated parameters and methods.

    Parameters
    ----------
    data: dict
        Spectrum data: dict of spicypy.FrequencySeries
    spectrum_type: str
        Either "psd" or "asd"
    response:
        pole-zero response dictionary associated with this Seismometer
    """

    def __init__(
        self,
        data,
        spectrum_type="asd",
        response=None,
    ):
        self._data = {}
        self._original_data = data
        for channel in data:
            self._data[channel] = data[channel]
        self._spectrum_type = spectrum_type
        self.response = response

    def _convert_to_response(self, response):
        """
        Convert data into different units (typically digital counts to physical units) using user-provided
        pole-zero response model.

        Returns
        -------
        response_data: dict of spicypy.FrequencySeries
           Spectrum data with response applied
        """
        zeros = response["zeros"]
        poles = response["poles"]
        scale_factor = response["scale_factor"]
        omega_exponent = 0
        if "omega_exponent" in response:
            omega_exponent = int(response["omega_exponent"])
        asd = True if self._spectrum_type == "asd" else False

        num_poly_coef, denom_poly_coef = signal.ltisys.zpk2tf(
            zeros, poles, scale_factor
        )

        response_data = {}
        for channel, channel_data in self._data.items():
            f = channel_data.frequencies.value
            omega = f * 2 * np.pi
            _, resp = signal.freqs(num_poly_coef, denom_poly_coef, omega)
            respamp = np.absolute(resp * np.conjugate(resp))
            dc_bin = False
            if omega[0] == 0.0:  # avoid potential divide by zero
                omega = omega[1:]
                dc_bin = True
            omega_factor = np.power(omega, omega_exponent)
            if dc_bin:
                omega_factor = np.insert(omega_factor, 0, 0.0)
            if asd:
                respamp = np.sqrt(respamp)
            response_data[channel] = omega_factor * channel_data / respamp
        return response_data

    def data(self, response=None):
        """
        Return associated data in spicypy.FrequencySeries.

        Returns
        -------
        data: dict of spicypy.FrequencySeries
           Spectrum data: spicypy.FrequencySeries.
        """
        if response is None:
            response = self.response
        if response is not None:
            return self._convert_to_response(response)
        return self._data

    def __getitem__(self, channel):
        """
        Return associated data for specified channel by [] operator.

        Returns
        -------
        data: spicypy.FrequencySeries
           Spectrum data in specified channel
        """
        return self.data()[channel]

    def type(self):
        """
        Return spectrum type (e.g. "lpsd").

        Returns
        -------
        str
           Spectrum type
        """
        return self._spectrum_type
