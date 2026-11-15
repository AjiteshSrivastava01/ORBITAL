import numpy as np

from physics.integrators import velocity_verlet
from simulation.celestial_body import CelestialBody


def main():
    sun = CelestialBody(
        name="Sun",
        mass=1.989e30,
        radius=6.957e8,
        position=np.array([0.0, 0.0, 0.0]),
        velocity=np.array([0.0, 0.0, 0.0]),
    )

    earth = CelestialBody(
        name="Earth",
        mass=5.972e24,
        radius=6.371e6,
        position=np.array([1.496e11, 0.0, 0.0]),
        velocity=np.array([0.0, 29_780.0, 0.0]),
    )

    bodies = [sun, earth]

    positions = np.array(
        [body.position for body in bodies], dtype=np.float64
    )
    velocities = np.array(
        [body.velocity for body in bodies], dtype=np.float64
    )
    masses = np.array(
        [body.mass for body in bodies], dtype=np.float64
    )

    dt = 60.0  # Advance the simulation by one minute

    new_positions, new_velocities = velocity_verlet(
        positions, velocities, masses, dt
    )

    for i, body in enumerate(bodies):
        body.position = new_positions[i].copy()
        body.velocity = new_velocities[i].copy()

    print(earth.position)
    print(earth.velocity)


if __name__ == "__main__":
    main()