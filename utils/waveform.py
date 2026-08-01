import numpy as np

from pycbc.waveform import get_td_waveform


def generate_waveform(
    m1,
    m2,
    sample_rate=4096
):

    hp, hc = get_td_waveform(

        approximant="IMRPhenomD",

        mass1=m1,

        mass2=m2,

        delta_t=1/sample_rate,

        f_lower=20

    )

    time = hp.sample_times.numpy()

    strain = hp.numpy()

    strain /= np.max(np.abs(strain))

    return time, strain


def align_merger(time, strain):

    peak = np.argmax(np.abs(strain))

    return time-time[peak], strain
