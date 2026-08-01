import streamlit as st
import numpy as np
import plotly.graph_objects as go

from gwpy.timeseries import TimeSeries
from pycbc.waveform import get_td_waveform

st.set_page_config(
    page_title="LIGO Comparison",
    page_icon="📡",
    layout="wide"
)

st.title("📡 GW150914: Observation vs Simulation")

st.markdown("""
This page compares the simulated gravitational-wave signal with the
historic GW150914 event detected by LIGO.

The observed waveform is downloaded directly from the
Gravitational Wave Open Science Center (GWOSC).
""")

# ---------------------------------------------------
# Mission parameters
# ---------------------------------------------------

m1 = st.session_state.get("m1", 36)
m2 = st.session_state.get("m2", 29)

# ---------------------------------------------------
# Download LIGO Data
# ---------------------------------------------------

@st.cache_data(show_spinner=False)
def load_ligo():

    event_time = 1126259462

    h1 = TimeSeries.fetch_open_data(
        "H1",
        event_time-16,
        event_time+16,
        cache=True
    )

    return h1

h1 = load_ligo()

event_time = 1126259462.4

h1 = h1.bandpass(30,400)

zoom = h1.crop(
    event_time-0.2,
    event_time+0.2
)

obs = zoom.value
obs = obs/np.max(np.abs(obs))

obs_time = zoom.times.value-event_time

# ---------------------------------------------------
# Generate Theory
# ---------------------------------------------------

hp,_ = get_td_waveform(

    approximant="IMRPhenomD",

    mass1=m1,

    mass2=m2,

    delta_t=1/4096,

    f_lower=20

)

theory = hp.numpy()

theory /= np.max(np.abs(theory))

time = hp.sample_times.numpy()

peak = np.argmax(np.abs(theory))

time = time-time[peak]

# ---------------------------------------------------
# Plot
# ---------------------------------------------------

fig = go.Figure()

fig.add_trace(

    go.Scatter(

        x=obs_time,

        y=obs,

        name="Observed GW150914",

        line=dict(width=2)

    )

)

fig.add_trace(

    go.Scatter(

        x=time,

        y=theory,

        name="Simulated Waveform",

        line=dict(width=3)

    )

)

fig.update_layout(

    title="Observed vs Simulated Gravitational Wave",

    xaxis_title="Time Relative to Merger (s)",

    yaxis_title="Normalized Strain",

    height=600

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

c1,c2,c3 = st.columns(3)

c1.metric(
    "Primary Mass",
    f"{m1} M☉"
)

c2.metric(
    "Secondary Mass",
    f"{m2} M☉"
)

c3.metric(
    "Observed Event",
    "GW150914"
)

st.success(
"""
The blue curve represents the observed GW150914 signal,
while the orange curve shows the waveform generated from the
current binary black hole parameters.
"""
)
