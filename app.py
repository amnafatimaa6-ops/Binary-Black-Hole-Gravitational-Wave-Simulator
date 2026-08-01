import streamlit as st

st.set_page_config(
    page_title="Binary Black Hole & Gravitational Wave Simulator",
    page_icon="🌌",
    layout="wide"
)

st.title("🌌 Binary Black Hole & Gravitational Wave Simulator")

st.markdown("""
Welcome to the **Binary Black Hole & Gravitational Wave Simulator**.

This interactive application demonstrates how binary black hole systems
produce gravitational waves and compares simulated signals with the
historic **GW150914** detection by LIGO.

---

### Features

- 🌑 Binary Black Hole Simulation
- 🌌 Interactive 3D Spacetime Curvature
- 🌊 Gravitational Wave Generation
- 📡 Real LIGO GW150914 Comparison
- 📊 Scientific Visualizations

---

### Workflow

Mission Control

⬇

Binary Black Hole Simulation

⬇

3D Spacetime Curvature

⬇

Gravitational Wave Generation

⬇

Comparison with Real LIGO Observations

---

Select a page from the **sidebar** to begin exploring the simulation.
""")

st.success("Ready for Mission 🚀")
