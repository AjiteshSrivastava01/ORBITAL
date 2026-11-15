import numpy as np

from physics.gravity import compute_accelerations


def velocity_verlet(positions, velocities, masses, dt):
    """
    Advance all bodies by dt seconds.

    positions: array with shape (N, 3), measured in meters
    velocities: array with shape (N, 3), measured in meters/second
    masses: array with shape (N,), measured in kilograms
    dt: positive time step in seconds

    Return new positions and velocities without changing the input arrays.
    """
    dt = float(dt)

    if not np.isfinite(dt) or dt <= 0:
        raise ValueError("dt must be a finite, positive number.")

    old_accelerations = compute_accelerations(positions, masses)

    new_positions = (
        positions
        + velocities * dt
        + 0.5 * old_accelerations * dt**2
    )

    new_accelerations = compute_accelerations(new_positions, masses)

    new_velocities = (
        velocities
        + 0.5 * (old_accelerations + new_accelerations) * dt
    )

    return new_positions, new_velocities