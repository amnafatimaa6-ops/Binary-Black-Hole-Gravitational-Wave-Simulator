import streamlit as st

st.set_page_config(page_title="Theory", page_icon="🌌", layout="wide")

st.title("🌌 Theory of Binary Black Holes & Gravitational Waves")

st.markdown("""
This section introduces the fundamental physics behind binary black holes,
gravitational waves, and the historic GW150914 detection.

The concepts presented here provide the scientific foundation for the
interactive simulations available throughout this application.
""")

st.divider()

# =====================================================
# Binary Black Holes
# =====================================================

with st.expander("🕳️ Binary Black Hole Systems", expanded=True):

    st.markdown("""
A **binary black hole system** consists of two black holes orbiting around
their common center of mass.

As they orbit, they continuously emit **gravitational waves**.
The emitted radiation carries away energy and angular momentum, causing
the orbit to shrink over time.

This process is called the **inspiral**.

Eventually the two black holes merge into a single, more massive black hole.
""")

st.divider()

# =====================================================
# Gravitational Waves
# =====================================================

with st.expander("〰️ Gravitational Waves", expanded=True):

    st.markdown(r"""
According to **Einstein's General Theory of Relativity**, accelerating massive
objects distort spacetime and generate gravitational waves.

Unlike electromagnetic waves, gravitational waves are oscillations
of spacetime itself.

The dimensionless gravitational-wave strain is

$$
h=\frac{\Delta L}{L}
$$

where

- **L** = detector arm length

- **ΔL** = tiny change caused by the passing wave

Typical strains detected by LIGO are approximately

$$
10^{-21}
$$

which is smaller than the diameter of a proton relative to the detector arm length.
""")

st.divider()

# =====================================================
# Inspiral
# =====================================================

with st.expander("🌠 Inspiral → Merger → Ringdown", expanded=True):

    st.markdown("""
A binary black hole merger occurs in three stages.

### Inspiral

The black holes orbit each other while slowly losing orbital energy.

---

### Merger

The event horizons combine to form one black hole.

---

### Ringdown

The newly formed black hole vibrates before settling into a stable
Kerr black hole.

These three stages produce the characteristic gravitational-wave waveform
observed by LIGO.
""")

st.divider()

# =====================================================
# GW150914
# =====================================================

with st.expander("📡 The GW150914 Discovery", expanded=True):

    st.markdown("""
On **14 September 2015**, the LIGO detectors made the first direct detection
of gravitational waves.

The signal, known as **GW150914**, originated from the merger of two stellar-mass
black holes approximately **1.3 billion light-years
