import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Binary Black Hole Simulator",
    page_icon="🕳️",
    layout="wide"
)

st.title("🕳️ Binary Black Hole Simulator")

st.markdown("""
This simulation shows the inspiral of two black holes before they merge.
The orbital motion is generated from the mission parameters selected on the
Mission Control page.
""")

# --------------------------------------------------
# Read Mission Control values
# --------------------------------------------------

m1 = st.session_state.get("m1", 36)
m2 = st.session_state.get("m2", 29)
distance = st.session_state.get("distance", 250)
speed = st.session_state.get("speed", 1.0)

# --------------------------------------------------
# Simulation Settings
# --------------------------------------------------

frames = st.slider(
    "Simulation Frames",
    200,
    1000,
    500
)

# Spiral decay
theta = np.linspace(0, 12*np.pi, frames)

radius = np.linspace(distance, 10, frames)

# Centre of mass scaling
r1 = radius * m2/(m1+m2)
r2 = radius * m1/(m1+m2)

x1 = r1*np.cos(theta)
y1 = r1*np.sin(theta)

x2 = -r2*np.cos(theta)
y2 = -r2*np.sin(theta)

# --------------------------------------------------
# Animation
# --------------------------------------------------

fig = go.Figure()

# Orbit paths
fig.add_trace(
    go.Scatter(
        x=x1,
        y=y1,
        mode="lines",
        line=dict(width=2),
        name="Black Hole 1 Orbit"
    )
)

fig.add_trace(
    go.Scatter(
        x=x2,
        y=y2,
        mode="lines",
        line=dict(width=2),
        name="Black Hole 2 Orbit"
    )
)

# Current BH positions
fig.add_trace(
    go.Scatter(
        x=[x1[0]],
        y=[y1[0]],
        mode="markers",
        marker=dict(
            size=18,
            color="black"
        ),
        name="BH 1"
    )
)

fig.add_trace(
    go.Scatter(
        x=[x2[0]],
        y=[y2[0]],
        mode="markers",
        marker=dict(
            size=16,
            color="gray"
        ),
        name="BH 2"
    )
)

# Build animation frames
animation = []

for i in range(frames):

    animation.append(

        go.Frame(

            data=[

                go.Scatter(x=x1, y=y1),

                go.Scatter(x=x2, y=y2),

                go.Scatter(
                    x=[x1[i]],
                    y=[y1[i]]
                ),

                go.Scatter(
                    x=[x2[i]],
                    y=[y2[i]]
                )

            ]

        )

    )

fig.frames = animation

fig.update_layout(

    title="Binary Black Hole Inspiral",

    xaxis_title="x",

    yaxis_title="y",

    width=900,

    height=700,

    xaxis=dict(scaleanchor="y"),

    updatemenus=[

        dict(

            type="buttons",

            buttons=[

                dict(

                    label="▶ Play",

                    method="animate",

                    args=[

                        None,

                        dict(

                            frame=dict(
                                duration=25/speed,
                                redraw=True
                            ),

                            fromcurrent=True

                        )

                    ]

                )

            ]

        )

    ]

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

left,right = st.columns(2)

with left:

    st.metric(
        "Primary Mass",
        f"{m1} M☉"
    )

    st.metric(
        "Initial Separation",
        distance
    )

with right:

    st.metric(
        "Secondary Mass",
        f"{m2} M☉"
    )

    st.metric(
        "Simulation Frames",
        frames
    )
