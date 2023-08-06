from openride.core.numba.transforms import transform_vertices, rotation_matrix

import numba
import numpy as np


@numba.njit(cache=True)
def bird_eye_view_box_vertices(
    position_x: float, position_y: float, size_x: float, size_y: float, yaw: float
) -> np.ndarray:
    """Get the 4 (x,y) coordinates of the corners of a bounding_box in bird eye view"""
    vertices = np.zeros((4, 3))
    vertices[:, 0] = size_x
    vertices[:, 1] = size_y
    vertices[2:, 0] *= -1
    vertices[1:3, 1] *= -1
    matrix4x4 = np.eye(4)
    matrix4x4[:3, :3] = rotation_matrix(0, 0, -yaw)
    vertices = transform_vertices(vertices, matrix4x4)
    vertices[:, 0] += position_x
    vertices[:, 1] += position_y
    return vertices[:, :2]


@numba.njit(cache=True)
def box_vertices(
    position_x: float,
    position_y: float,
    position_z: float,
    size_x: float,
    size_y: float,
    size_z: float,
    roll: float,
    pitch: float,
    yaw: float,
) -> np.ndarray:
    """Get the 8 (x,y,z) coordinates of the corners of a bounding box in 3D"""
    vertices = np.zeros((8, 3))
    vertices[:, 0] = size_x
    vertices[:, 1] = size_y
    vertices[:, 2] = size_z
    vertices[:2, 0] *= -1
    vertices[6:, 0] *= -1
    vertices[4:, 1] *= -1
    vertices[::2, 2] *= -1
    matrix4x4 = np.eye(4)
    matrix4x4[:3, :3] = rotation_matrix(roll, pitch, yaw)
    vertices = transform_vertices(vertices, matrix4x4)
    vertices[:, 0] += position_x
    vertices[:, 1] += position_y
    vertices[:, 2] += position_z
    return vertices


@numba.njit(cache=True)
def vertices_inside_box(vertices: np.ndarray, box_vertices: np.ndarray) -> np.ndarray:
    """Returns indices of the vertices that are inside the box"""
    P = box_vertices
    u, v, w = P[1] - P[0], P[2] - P[0], P[6] - P[0]
    pu, pv, pw = np.dot(vertices, u), np.dot(vertices, v), np.dot(vertices, w)
    inside_box = np.where(
        (pu <= np.dot(P[1], u))
        & (pu >= np.dot(P[0], u))
        & (pv <= np.dot(P[2], v))
        & (pv >= np.dot(P[0], v))
        & (pw <= np.dot(P[6], w))
        & (pw >= np.dot(P[0], w))
    )[0]
    return inside_box
