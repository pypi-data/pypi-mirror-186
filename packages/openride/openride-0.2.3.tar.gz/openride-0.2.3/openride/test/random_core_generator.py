from openride import BoundingBox, Point, Polygon, Polyline, Rotation, Size, Transform

import numpy as np


def get_random(cls):

    if cls == Point:
        return Point(*np.random.random(3) * 10)

    elif cls == BoundingBox:
        return BoundingBox(
            Point(*np.random.random(3) * 10),
            Rotation(0, 0, np.random.random() * 2 * np.pi),
            Size(*np.random.random(3) * 10),
        )

    elif cls == Polyline:
        return Polyline(np.random.random((10, 3)))

    elif cls == Polygon:
        right_side = [Point(x + np.random.random() * 0.3, np.random.random() - 5) for x in range(10)]
        left_side = [Point(10 - x - np.random.random() * 0.3, np.random.random() + 5) for x in range(10)]
        return Polygon(right_side + left_side)

    elif cls == Transform:
        return Transform(
            Point(*np.random.random(3) * 10),
            Rotation(0, 0, np.random.random() * 2 * np.pi),
        )
