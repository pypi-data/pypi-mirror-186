# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gravilab', 'gravilab.base', 'gravilab.formats', 'gravilab.input']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19,<2.0',
 'obspy>=1.2.2,<2.0.0',
 'pandas>=1.1,<2.0',
 'spicypy>=0.4.1,<0.5.0']

extras_require = \
{':python_full_version <= "3.7.0"': ['importlib-metadata>=1.1.3']}

setup_kwargs = {
    'name': 'gravilab',
    'version': '0.1.2',
    'description': 'Package to analyze seismic data based on obspy and spicypy packages.',
    'long_description': '# GraviLab\n\nPackage to analyze seismic data based on [obspy](obspy.org) and [spicypy](https://gitlab.com/pyda-group/spicypy) packages.\n\n## Installation\n\n```bash\npip install gravilab\n```\n\n## Usage\n\nThe main element of the package is [`Seismometer`](https://gitlab.com/pyda-group/gravilab/-/blob/main/gravilab/base/seismometer.py) class, which represents a seismic instrument.\nIt can be created by loading seismic data with `open` function and specifying channels,\nboth their names in the file and "human-readable" names. The folder is then scanned for any suitable data\nand only those channels are loaded. All functionality related to seismic time series data is\nprovided by the underlying [obspy](obspy.org) package (specifically [`obspy.Trace`](https://docs.obspy.org/packages/autogen/obspy.core.trace.Trace.html)).\n\n[`Seismometer`](https://gitlab.com/pyda-group/gravilab/-/blob/main/gravilab/base/seismometer.py) class also supports calculating spectrum\n(`Seismometer.asd()`, `Seismometer.psd()`) using [spicypy](https://gitlab.com/pyda-group/spicypy) package.\nSpectrum can be adjusted by the response of specific instrument specified by pole-zero model,\nand units can be converted between displacement, velocity\nand acceleration by specifying the `omega` factor. Resulting spectrum is [`spicypy.FrequencySeries`](https://pyda-group.gitlab.io/spicypy/autoapi/spicypy/signal/frequency_series/index.html). Additionally,\ntime series can also be converted to [`spicypy.TimeSeries`](https://pyda-group.gitlab.io/spicypy/autoapi/spicypy/signal/time_series/index.html) to profit from its rich signal processing functionality.\n\nMinimal example:\n```python\nimport gravilab as gl\nSeismometer1 = gl.open("seismic", channels = {"vertical":"HNZ","north":"HNY","east":"HNX"}, name="seismometer1")\nSeismometer1.time_series["north"].plot()\nresponse = {"poles" : [-0.036614 +0.037059j, -0.036614 -0.037059j, -32.55, -142, -364 +404j, -364 -404j, -1260, -4900 +5200j, -4900 -5200j, -7100 +1700j, -7100 -1700j],\n            "zeros" : [0, 0, -31.63, -160, -350, -3177],\n            "scale_factor" : 1202.5 * 8.31871e17 * 400000, #V/(m/s) times gain times counts/V\n            "omega_exponent": -1, #convert from m/s to m\n           }\nSeismometer1.response = response\nSeismometer1.asd()["north"].plot()\n```\n\nMore detailed usage examples are provided in [gravilab/examples](https://gitlab.com/pyda-group/gravilab/-/tree/main/examples) folder.\n',
    'author': 'Artem Basalaev',
    'author_email': 'artemDOTbasalaev@physikDOTuni-hamburg.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/pyda-group/gravilab',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
