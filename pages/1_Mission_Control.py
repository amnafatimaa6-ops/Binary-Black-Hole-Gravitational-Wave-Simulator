import streamlit as st

st.set_page_config(
    page_title="Mission Control",
    page_icon="🌌",
    layout="wide"
)

# ===========================================
# Header
# ===========================================

st.title("🌌 Binary Black Hole Mission Control")

st.markdown("""
Welcome to the **Binary Black Hole & Gravitational Wave Simulator**.

This application allows you to investigate how two orbiting black holes
produce gravitational waves and how the simulated waveform compares with
the historic **GW150914** LIGO observation.
""")

st.divider()

# ===========================================
# Session State
# ===========================================

if "m1" not in st.session_state:
    st.session_state.m1 = 36

if "m2" not in st.session_state:
    st.session_state.m2 = 29

if "distance" not in st.session_state:
    st.session_state.distance = 250

if "spin1" not in st.session_state:
    st.session_state.spin1 = 0.2

if "spin2" not in st.session_state:
    st.session_state.spin2 = 0.3

if "speed" not in st.session_state:
    st.session_state.speed = 1.0

# ===========================================
# Layout
# ===========================================

left, right = st.columns([1,1])

# ===========================================
# LEFT PANEL
# ===========================================

with left:

    st.subheader("Mission Configuration")

    st.session_state.m1 = st.slider(
        "Black Hole 1 Mass (Solar Masses)",
        5,
        100,
        st.session_state.m1
    )

    st.session_state.m2 = st.slider(
        "Black Hole 2 Mass (Solar Masses)",
        5,
        100,
        st.session_state.m2
    )

    st.session_state.distance = st.slider(
        "Initial Separation",
        50,
        1000,
        st.session_state.distance
    )

    st.session_state.spin1 = st.slider(
        "Spin of Black Hole 1",
        0.0,
        0.99,
        st.session_state.spin1
    )

    st.session_state.spin2 = st.slider(
        "Spin of Black Hole 2",
        0.0,
        0.99,
        st.session_state.spin2
    )

    st.session_state.speed = st.slider(
        "Simulation Speed",
        0.2,
        5.0,
        st.session_state.speed
    )

# ===========================================
# RIGHT PANEL
# ===========================================

with right:

    st.subheader("Mission Status")

    st.success("🟢 Simulator Ready")

    st.metric(
        "Primary Black Hole",
        f"{st.session_state.m1} M☉"
    )

    st.metric(
        "Secondary Black Hole",
        f"{st.session_state.m2} M☉"
    )

    st.metric(
        "Initial Separation",
        f"{st.session_state.distance}"
    )

    st.metric(
        "Simulation Speed",
        f"{st.session_state.speed:.1f}×"
    )

st.divider()

# ===========================================
# Mission Summary
# ===========================================

st.subheader("Mission Summary")

total_mass = st.session_state.m1 + st.session_state.m2

mass_ratio = round(
    st.session_state.m1 /
    st.session_state.m2,
    2
)

c1, c2, c3 = st.columns(3)

c1.metric("Total Mass", f"{total_mass} M☉")

c2.metric("Mass Ratio", mass_ratio)

c3.metric(
    "Target Event",
    "GW150914"
)

st.divider()

st.info("""
Proceed to **Page 2 – Binary Black Hole Simulator**
to begin the orbital evolution simulation.
""")
