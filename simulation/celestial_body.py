import numpy as np


class CelestialBody:

    def __init__(self, name: str, mass: float, radius: float,
                 position: np.ndarray, velocity: np.ndarray):
        self.name = name
        self.mass = self._positive_float(mass, "mass")
        self.radius = self._positive_float(radius, "radius")
        self.position = self._vector3(position, "position")
        self.velocity = self._vector3(velocity, "velocity")

    @staticmethod
    def _positive_float(value, field_name):
        value = float(value)

        if not np.isfinite(value) or value <= 0:
            raise ValueError(
                f"{field_name} must be a finite, positive number."
            )

        return value

    @staticmethod
    def _vector3(value, field_name):
        vector = np.array(value, dtype=np.float64, copy=True)

        if vector.shape != (3,):
            raise ValueError(
                f"{field_name} must contain exactly three components."
            )

        if not np.all(np.isfinite(vector)):
            raise ValueError(
                f"{field_name} must contain only finite numbers."
            )

        return vector