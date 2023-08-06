"""
Dummy class with same functionality as gravilab.Seismometer - for backwards-compatibility in old scripts

Artem Basalaev <artem[dot]basalaev[at]physik.uni-hamburg.de>,
Christian Darsow-Fromm <cdarsowf[at]physnet.uni-hamburg.de>
"""
from gravilab.base.seismometer import Seismometer


class SystemElement(Seismometer):
    """Dummy class with same functionality as gravilab.Seismometer - for backwards-compatibility in old scripts."""

    def __init__(self, *args, **kwargs):
        """
        Pass arguments to init method of Seismometer class
        Parameters
        ----------
        args: list
            any positional arguments
        kwargs: dict
            any keyword arguments
        """
        super().__init__(*args, **kwargs)
