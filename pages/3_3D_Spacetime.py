import streamlit as st
import numpy as np
import pyvista as pv
from stpyvista import stpyvista

st.set_page_config(
    page_title="3D Spacetime Curvature",
    page_icon="🌌",
    layout="wide"
)

st.title("🌌 3D Spacetime Curvature")

st.markdown("""
This visualization illustrates how two black holes deform spacetime during
their inspiral. The surface is a qualitative representation intended to show
the evolution of gravitational curvature as the black holes move toward merger.
""")

# ---------------------------------------------------
# Read mission parameters
# ---------------------------------------------------

m1 = st.session_state.get("m1", 36)
m2 = st.session_state.get("m2", 29)
distance = st.session_state.get("distance", 250)

# Scale distance for visualization
d = distance / 100

# ---------------------------------------------------
# Grid
# ---------------------------------------------------

x = np.linspace(-6, 6, 250)
y = np.linspace(-6, 6, 250)

X, Y = np.meshgrid(x, y)

# ---------------------------------------------------
# Black hole positions
# ---------------------------------------------------

x1 = -d / 2
x2 = d / 2

# ---------------------------------------------------
# Simple spacetime curvature
# ---------------------------------------------------

eps = 0.2

Z = (
    -m1 / np.sqrt((X - x1) ** 2 + Y ** 2 + eps)
    -m2 / np.sqrt((X - x2) ** 2 + Y ** 2 + eps)
)

# Normalize for nicer rendering
Z /= np.max(np.abs(Z))

# ---------------------------------------------------
# Create structured grid
# ---------------------------------------------------

grid = pv.StructuredGrid(
    X,
    Y,
    Z * 3
)

plotter = pv.Plotter(window_size=(900, 700))

plotter.add_mesh(
    grid,
    smooth_shading=True,
    cmap="viridis"
)

# Black holes
plotter.add_mesh(
    pv.Sphere(
        radius=0.18,
        center=(x1, 0, Z.min() * 3)
    ),
    color="black"
)

plotter.add_mesh(
    pv.Sphere(
        radius=0.16,
        center=(x2, 0, Z.min() * 3)
    ),
    color="dimgray"
)

plotter.camera_position = "iso"

stpyvista(plotter)

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Primary Mass",
    f"{m1} M☉"
)

col2.metric(
    "Secondary Mass",
    f"{m2} M☉"
)

col3.metric(
    "Separation",
    distance
)

st.info("""
The depth of each well increases with black hole mass, while the separation
between the wells reflects the initial orbital distance chosen in Mission Control.
Later pages will use these same parameters to generate gravitational waves and
compare the simulated signal with the real GW150914 event.
""")
