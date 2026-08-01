import numpy as np


def circular_orbit(radius, n_points=600):

    theta = np.linspace(
        0,
        2*np.pi,
        n_points
    )

    x = radius*np.cos(theta)
    y = radius*np.sin(theta)

    return x, y


def binary_positions(radius):

    x1, y1 = circular_orbit(radius)

    x2 = -x1
    y2 = -y1

    return x1, y1, x2, y2


def inspiral_radius(initial_radius, progress):

    """
    Shrinks the orbital radius smoothly.
    """

    return initial_radius * (1-progress)
