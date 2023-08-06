from openride.core.point import Point
from openride.core.rotation import Rotation
from openride.core.numba import transform_matrix, transform_inverse_matrix

from dataclasses import dataclass

import numpy as np


@dataclass
class Transform:

    translation: Point = Point(0, 0, 0)
    rotation: Rotation = Rotation(0, 0, 0)

    def get_matrix(self) -> np.ndarray:
        return transform_matrix(
            self.translation.x,
            self.translation.y,
            self.translation.z,
            self.rotation.roll,
            self.rotation.pitch,
            self.rotation.yaw,
        )

    def get_inverse_matrix(self) -> np.ndarray:
        return transform_inverse_matrix(
            self.translation.x,
            self.translation.y,
            self.translation.z,
            self.rotation.roll,
            self.rotation.pitch,
            self.rotation.yaw,
        )

    def inverse(self) -> "Transform":
        return Transform.from_matrix(self.get_inverse_matrix())

    @classmethod
    def from_matrix(cls, matrix: np.ndarray) -> "Transform":
        return cls(Point(*matrix[:3, 3]), Rotation.from_matrix(matrix))
