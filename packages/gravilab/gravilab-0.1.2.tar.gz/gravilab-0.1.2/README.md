# GraviLab

Package to analyze seismic data based on [obspy](obspy.org) and [spicypy](https://gitlab.com/pyda-group/spicypy) packages.

## Installation

```bash
pip install gravilab
```

## Usage

The main element of the package is [`Seismometer`](https://gitlab.com/pyda-group/gravilab/-/blob/main/gravilab/base/seismometer.py) class, which represents a seismic instrument.
It can be created by loading seismic data with `open` function and specifying channels,
both their names in the file and "human-readable" names. The folder is then scanned for any suitable data
and only those channels are loaded. All functionality related to seismic time series data is
provided by the underlying [obspy](obspy.org) package (specifically [`obspy.Trace`](https://docs.obspy.org/packages/autogen/obspy.core.trace.Trace.html)).

[`Seismometer`](https://gitlab.com/pyda-group/gravilab/-/blob/main/gravilab/base/seismometer.py) class also supports calculating spectrum
(`Seismometer.asd()`, `Seismometer.psd()`) using [spicypy](https://gitlab.com/pyda-group/spicypy) package.
Spectrum can be adjusted by the response of specific instrument specified by pole-zero model,
and units can be converted between displacement, velocity
and acceleration by specifying the `omega` factor. Resulting spectrum is [`spicypy.FrequencySeries`](https://pyda-group.gitlab.io/spicypy/autoapi/spicypy/signal/frequency_series/index.html). Additionally,
time series can also be converted to [`spicypy.TimeSeries`](https://pyda-group.gitlab.io/spicypy/autoapi/spicypy/signal/time_series/index.html) to profit from its rich signal processing functionality.

Minimal example:
```python
import gravilab as gl
Seismometer1 = gl.open("seismic", channels = {"vertical":"HNZ","north":"HNY","east":"HNX"}, name="seismometer1")
Seismometer1.time_series["north"].plot()
response = {"poles" : [-0.036614 +0.037059j, -0.036614 -0.037059j, -32.55, -142, -364 +404j, -364 -404j, -1260, -4900 +5200j, -4900 -5200j, -7100 +1700j, -7100 -1700j],
            "zeros" : [0, 0, -31.63, -160, -350, -3177],
            "scale_factor" : 1202.5 * 8.31871e17 * 400000, #V/(m/s) times gain times counts/V
            "omega_exponent": -1, #convert from m/s to m
           }
Seismometer1.response = response
Seismometer1.asd()["north"].plot()
```

More detailed usage examples are provided in [gravilab/examples](https://gitlab.com/pyda-group/gravilab/-/tree/main/examples) folder.
