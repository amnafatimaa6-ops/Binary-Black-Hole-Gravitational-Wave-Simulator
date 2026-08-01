import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Gravitational Wave Generator",
    page_icon="🌊",
    layout="wide"
)

st.title("🌊 Gravitational Wave Generator")

st.markdown("""
This module generates a simplified gravitational-wave signal from the
binary black hole system configured in Mission Control.

The waveform reproduces the characteristic **chirp**, where both the
frequency and amplitude increase as the two black holes spiral inward.
""")

# ====================================================
# Mission Parameters
# ====================================================

m1 = st.session
