from openride.core.geometry import Geometry
from openride.core.point import Point
from openride.core.rotation import Rotation
from openride.core.size import Size
from openride.core.transform import Transform
from openride.core.numba import (
    bird_eye_view_box_vertices,
    box_vertices,
)

from dataclasses import dataclass
from shapely import geometry

import numpy as np


@dataclass
class BoundingBox(Geometry):
    """3D bounding box defined by a center position, rotation (euler angles) and size."""

    position: Point = Point(0, 0, 0)
    rotation: Rotation = Rotation(0, 0, 0)
    size: Size = Size(1, 1, 1)

    def to_shapely(self) -> geometry.Polygon:
        return geometry.Polygon(self.get_bird_eye_view_vertices())

    def transform(self, transform: "Transform") -> "BoundingBox":
        return BoundingBox(
            self.position.transform(transform),
            self.rotation + transform.rotation,
            self.size,
        )

    def get_transform(self) -> Transform:
        return Transform(self.position, self.rotation)

    def get_bird_eye_view_vertices(self) -> np.ndarray:
        return bird_eye_view_box_vertices(
            self.position.x,
            self.position.y,
            self.size.x,
            self.size.y,
            self.rotation.yaw,
        )

    def get_vertices(self) -> np.ndarray:
        return box_vertices(
            self.position.x,
            self.position.y,
            self.position.z,
            self.size.x,
            self.size.y,
            self.size.z,
            self.rotation.roll,
            self.rotation.pitch,
            self.rotation.yaw,
        )
