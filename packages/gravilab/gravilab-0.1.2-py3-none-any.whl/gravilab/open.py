"""
User interface function to open seismic data files.

Artem Basalaev <artem[dot]basalaev[at]physik.uni-hamburg.de>,
Christian Darsow-Fromm <cdarsowf[at]physnet.uni-hamburg.de>
"""


from gravilab.input.data_reader import DataReader
from gravilab.base.seismometer import Seismometer


def open(
    data_path,
    channels=None,
    name="generic seismometer",
    response=None,
    ignore_extension=False,
):
    """
    User interface function to open data files.

    Parameters
    ----------
    data_path: str
        A valid path pointing to a data file or a folder with files (contained data files are found recursively)
    channels: dict
        Channels for data, optional (e.g. an axis along which measurement is performed).
        Contains channel name that should be present in miniseed file.
        If not provided, lumping all data files together assuming one channel "all".
    name: str
            name for this seismometer, optional
    response: dict
        Frequency response of the instrument in pole-zero model. Used to convert digital counts to physical units.
        Example: {"poles" =  [-0.036614 +0.037059j, -0.036614 -0.037059j],
                  "zeros" = [0, 0, -31.63, -160, -350, -3177],
                  "scale_factor" = 1202.5 * 8.31871e17 * 400000 #V/(m/s) times gain times counts/V}
    ignore_extension: bool
        Whether to try to open all files independently of extension
        (be careful as any non-seismic files in the folder, such as text files, will lead to a crash).

    Returns
    -------
    Seismometer
       Seismometer object containing time series data
    """
    time_series = DataReader(data_path, channels, ignore_extension).read_data()
    return Seismometer(time_series, name=name, response=response)
