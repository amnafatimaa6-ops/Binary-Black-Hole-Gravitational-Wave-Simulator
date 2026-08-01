from gwpy.timeseries import TimeSeries

from .constants import GW150914_GPS


def load_gw150914():

    h1 = TimeSeries.fetch_open_data(

        "H1",

        GW150914_GPS-16,

        GW150914_GPS+16,

        cache=True

    )

    return h1


def preprocess_signal(h1):

    signal = h1.bandpass(30,400)

    signal = signal.crop(

        GW150914_GPS-0.2,

        GW150914_GPS+0.2

    )

    return signal


def normalize(signal):

    data = signal.value

    data /= abs(data).max()

    time = signal.times.value
