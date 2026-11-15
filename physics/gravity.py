import numpy as np
from physics.constants import G

def compute_accelerations(positions, masses):
    # Return gravitational accelerations with shape (number_of_bodies, 3).
    accelerations = np.zeros_like(positions, dtype=np.float64) # Creates a 0-array with the shape of position
    body_count = len(masses)

    for i in range(body_count):
        for j in range(i + 1, body_count):
            displacement = positions[j] - positions[i]
            distance = np.linalg.norm(displacement)

            if distance == 0:
                raise ValueError(
                    "Gravity is undefined for bodies at the same position."
                )

            direction_over_distance_squared = displacement / distance**3
            # a = GM / (R_E + R_distance) ^ 2 <-- Generic Formula for Gravitational Acceleration
            # a = GM * (displacement / distance^3) <-- Vector Formula for Gravitational Acceleration implemented below
            accelerations[i] += (
                G * masses[j] * direction_over_distance_squared
            )
            accelerations[j] -= (
                G * masses[i] * direction_over_distance_squared
            )

    return accelerations