import numpy as np

from .constants import G
from .constants import C
from .constants import M_SUN


def schwarzschild_radius(mass):

    """
    Schwarzschild Radius (meters)
    """

    mass *= M_SUN

    return 2 * G * mass / C**2


def chirp_mass(m1, m2):

    """
    Chirp Mass (solar masses)
    """

    return ((m1 * m2)**(3/5)) / ((m1 + m2)**(1/5))


def orbital_velocity(mass, radius):

    """
    Circular orbital velocity.
    """

    mass *= M_SUN

    return np.sqrt(G * mass / radius)


def escape_velocity(mass, radius):

    mass *= M_SUN

    return np.sqrt(2 * G * mass / radius)


def gravitational_wave_frequency(orbital_frequency):

    """
    GW frequency is twice the orbital frequency.
    """

    return 2 * orbital_frequency


def orbital_period(radius, total_mass):

    total_mass *= M_SUN

    return 2 * np.pi * np.sqrt(radius**3 / (G * total_mass))
