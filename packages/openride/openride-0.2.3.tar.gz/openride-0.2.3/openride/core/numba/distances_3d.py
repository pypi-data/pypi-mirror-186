from openride.core.numba.box_utils import vertices_inside_box

import numpy as np
import numba

EPSILON = np.finfo(float).eps


@numba.njit(cache=True)
def distance_between_points_3d(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    """Minimum distance between two points in 3D"""
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5


BOX_TRIANGLE_INDICES = np.array(
    [
        [0, 1, 2],
        [1, 2, 3],
        [0, 2, 4],
        [0, 4, 6],
        [2, 3, 4],
        [3, 4, 5],
        [0, 1, 6],
        [1, 6, 7],
        [4, 5, 6],
        [5, 6, 7],
        [1, 3, 5],
        [1, 5, 7],
    ]
)


@numba.njit(cache=True)
def distance_between_box_and_point_3d(
    box_vertices: np.ndarray, box_x: float, box_y: float, box_z: float, px: float, py: float, pz: float
) -> float:
    """Minimum distance between a 3D bounding box and a point"""

    point = np.array((px, py, pz))
    if len(vertices_inside_box(np.reshape(point, (1, 3)), box_vertices)) > 0:
        return 0.0

    box_center = np.array([box_x, box_y, box_z])

    for triangle in BOX_TRIANGLE_INDICES:
        _triangle = np.vstack(
            (
                box_vertices[triangle[0]],
                box_vertices[triangle[1]],
                box_vertices[triangle[2]],
            )
        )
        if ray_triangle_intersect(box_center, point, _triangle):
            return distance_triangle_point_3d(_triangle, point)

    return distance_triangle_point_3d(_triangle, point)


@numba.njit(cache=True)
def distance_between_line_and_point_3d(vertices: np.ndarray, x: float, y: float, z: float) -> float:
    """Minimum distance between a polyline and a point in 3D"""
    distances = np.zeros(vertices.shape[0] - 1)
    p = np.array((x, y, z))
    for i in range(vertices.shape[0] - 1):
        distances[i] = point_segment_distance_3d(p, vertices[i], vertices[i + 1])
    return np.min(distances)


@numba.njit(cache=True)
def distance_between_lines_3d(vertices1: np.ndarray, vertices2: np.ndarray) -> float:
    """Minimum distance between two polylines in 3D"""
    distances = np.zeros((vertices1.shape[0] - 1, vertices2.shape[0] - 1))
    for i in range(vertices1.shape[0] - 1):
        for j in range(vertices2.shape[0] - 1):
            distances[i, j] = segments_distance_3d(vertices1[i], vertices1[i + 1], vertices2[j], vertices2[j + 1])
    return np.min(distances)


@numba.njit(cache=True)
def distance_between_line_and_box_3d(line_vertices: np.ndarray, box_vertices: np.ndarray) -> float:
    """Minimum distance between a polyline and a bounding box in 3D"""
    if len(vertices_inside_box(line_vertices, box_vertices)) > 0:
        return 0.0
    distances = np.zeros((12, line_vertices.shape[0] - 1))
    for i, face in enumerate(BOX_TRIANGLE_INDICES):
        triangle = np.vstack((box_vertices[face[0]], box_vertices[face[1]], box_vertices[face[2]]))
        for j in range(line_vertices.shape[0] - 1):
            distances[i, j] = segment_triangle_distance(line_vertices[j], line_vertices[j + 1], triangle)
            if distances[i, j] == 0.0:
                return 0.0
    return np.min(distances)


BOX_SEGMENT_INDICES = (6, 7, 7, 1, 1, 0, 0, 6, 4, 5, 5, 3, 3, 2, 2, 4, 6, 4, 7, 5, 0, 2, 1, 3)


@numba.njit(cache=True)
def distance_between_boxes_3d(vertices1: np.ndarray, vertices2: np.ndarray) -> float:
    """Minimum distance between two 3D bounding boxes"""
    if len(vertices_inside_box(vertices1, vertices2)) > 0:
        return 0.0
    if len(vertices_inside_box(vertices2, vertices1)) > 0:
        return 0.0
    distances = []
    for face in BOX_TRIANGLE_INDICES:
        triangle = np.vstack((vertices1[face[0]], vertices1[face[1]], vertices1[face[2]]))
        for p in vertices2:
            distances.append(distance_triangle_point_3d(triangle, p))
    for face in BOX_TRIANGLE_INDICES:
        triangle = np.vstack((vertices2[face[0]], vertices2[face[1]], vertices2[face[2]]))
        for p in vertices1:
            distances.append(distance_triangle_point_3d(triangle, p))

    for i in range(0, len(BOX_SEGMENT_INDICES) - 1, 2):
        v1 = vertices1[BOX_SEGMENT_INDICES[i]]
        v2 = vertices1[BOX_SEGMENT_INDICES[i + 1]]
        for j in range(0, len(BOX_SEGMENT_INDICES) - 1, 2):
            v3 = vertices2[BOX_SEGMENT_INDICES[j]]
            v4 = vertices2[BOX_SEGMENT_INDICES[j + 1]]
            distances.append(segments_distance_3d(v1, v2, v3, v4))

    return min(distances)


@numba.njit(cache=True)
def point_segment_distance_3d(p: np.ndarray, a: np.ndarray, b: np.ndarray) -> float:
    """Minimum distance between a line segment (finite length) and a point in 3D"""

    # normalized tangent vector
    diff = b - a
    norm = (diff[0] ** 2 + diff[1] ** 2 + diff[2] ** 2) ** 0.5
    d = np.divide(diff, norm)

    # signed parallel distance components
    s = np.dot(a - p, d)
    t = np.dot(p - b, d)

    # clamped parallel distance
    h = max([s, t, 0.0])

    # perpendicular distance component
    c = np.cross(p - a, d)

    return np.hypot(h, np.linalg.norm(c))


@numba.njit(cache=True)
def clip(a: float, min: float, max: float) -> float:
    if a < min:
        return min
    elif a > max:
        return max
    return a


@numba.njit(cache=True)
def segments_distance_3d(p11: np.ndarray, p12: np.ndarray, p21: np.ndarray, p22: np.ndarray) -> float:
    """Minimum distance between two line segments (finite lengths)"""
    r = p21 - p11
    u = p12 - p11
    v = p22 - p21

    ru = np.dot(r, u)
    rv = np.dot(r, v)
    uu = np.dot(u, u)
    uv = np.dot(u, v)
    vv = np.dot(v, v)

    det = uu * vv - uv * uv

    if det < EPSILON * uu * vv:
        s = ru / uu
        t = 0
    else:
        s = clip((ru * vv - rv * uv) / det, 0, 1)
        t = clip((ru * uv - rv * uu) / det, 0, 1)

    S = clip((t * uv + ru) / uu, 0, 1)
    T = clip((s * uv - rv) / vv, 0, 1)

    A = p11 + S * u
    B = p21 + T * v
    C = B - A
    return (C[0] ** 2 + C[1] ** 2 + C[2] ** 2) ** 0.5


### WIP ###
# def min_distance_triangles_point_3d(triangles: np.ndarray, points: np.ndarray) -> float:
#     """https://stackoverflow.com/questions/32342620/closest-point-projection-of-a-3d-point-to-3d-triangles-with-numpy-scipy"""

#     # Unpack triangle points
#     p0,p1,p2 = np.asarray(triangles).swapaxes(0,1)

#     # Calculate triangle edges
#     e0 = p1-p0
#     e1 = p2-p0
#     a = np.einsum('...i,...i', e0 , e0)
#     b = np.einsum('...i,...i', e0 , e1)
#     c = np.einsum('...i,...i', e1 , e1)

#     # Calculate determinant and denominator
#     det = a*c - b*b
#     invDet = 1. / (det + EPSILON)
#     denom = a-2*b+c

#     # Project to the edges
#     p  = p0-points[:,np.newaxis]
#     d = np.einsum('...i,...i', e0 , p)
#     e = np.einsum('...i,...i', e1 , p)
#     u = b*e - c*d
#     v = b*d - a*e

#     # Calculate numerators
#     bd = b+d
#     ce = c+e
#     numer0 = (ce - bd) / denom
#     numer1 = (c+e-b-d) / denom
#     da = -d/a
#     ec = -e/c


#     # Vectorize test conditions
#     m0 = u + v < det
#     m1 = u < 0
#     m2 = v < 0
#     m3 = d < 0
#     m4 = (a+d > b+e)
#     m5 = ce > bd

#     t0 =  m0 &  m1 &  m2 &  m3
#     t1 =  m0 &  m1 &  m2 & ~m3
#     t2 =  m0 &  m1 & ~m2
#     t3 =  m0 & ~m1 &  m2
#     t4 =  m0 & ~m1 & ~m2
#     t5 = ~m0 &  m1 &  m5
#     t6 = ~m0 &  m1 & ~m5
#     t7 = ~m0 &  m2 &  m4
#     t8 = ~m0 &  m2 & ~m4
#     t9 = ~m0 & ~m1 & ~m2

#     u = np.where(t0, np.clip(da, 0, 1), u)
#     v = np.where(t0, 0, v)
#     u = np.where(t1, 0, u)
#     v = np.where(t1, 0, v)
#     u = np.where(t2, 0, u)
#     v = np.where(t2, np.clip(ec, 0, 1), v)
#     u = np.where(t3, np.clip(da, 0, 1), u)
#     v = np.where(t3, 0, v)
#     u *= np.where(t4, invDet, 1)
#     v *= np.where(t4, invDet, 1)
#     u = np.where(t5, np.clip(numer0, 0, 1), u)
#     v = np.where(t5, 1 - u, v)
#     u = np.where(t6, 0, u)
#     v = np.where(t6, 1, v)
#     u = np.where(t7, np.clip(numer1, 0, 1), u)
#     v = np.where(t7, 1-u, v)
#     u = np.where(t8, 1, u)
#     v = np.where(t8, 0, v)
#     u = np.where(t9, np.clip(numer1, 0, 1), u)
#     v = np.where(t9, 1-u, v)

#     closest_points = (p0.T +  u[:, np.newaxis] * e0.T + v[:, np.newaxis] * e1.T).swapaxes(2,1)
#     distances_sq = (closest_points[:,:,0] - points[:,None,0])**2 + (closest_points[:,:,1] - points[:,None,1])**2 + (closest_points[:,:,2] - points[:,None,2])**2
#     return np.sqrt(np.ravel(distances_sq)[np.argmin(distances_sq)])


@numba.njit(cache=True)
def distance_triangle_point_3d(triangle: np.ndarray, p: np.ndarray) -> float:
    """https://gist.github.com/joshuashaffer/99d58e4ccbd37ca5d96e"""

    B = triangle[0, :]
    E0 = triangle[1, :] - B
    E1 = triangle[2, :] - B
    D = B - p
    a = np.dot(E0, E0)
    b = np.dot(E0, E1)
    c = np.dot(E1, E1)
    d = np.dot(E0, D)
    e = np.dot(E1, D)
    f = np.dot(D, D)

    det = a * c - b * b
    s = b * e - c * d
    t = b * d - a * e

    # Terible tree of conditionals to determine in which region of the diagram
    # shown above the projection of the point into the triangle-plane lies.
    if (s + t) <= det:
        if s < 0.0:
            if t < 0.0:
                # region4
                if d < 0:
                    t = 0.0
                    if -d >= a:
                        s = 1.0
                        sqrdistance = a + 2.0 * d + f
                    else:
                        s = -d / a
                        sqrdistance = d * s + f
                else:
                    s = 0.0
                    if e >= 0.0:
                        t = 0.0
                        sqrdistance = f
                    else:
                        if -e >= c:
                            t = 1.0
                            sqrdistance = c + 2.0 * e + f
                        else:
                            t = -e / c
                            sqrdistance = e * t + f

                            # of region 4
            else:
                # region 3
                s = 0
                if e >= 0:
                    t = 0
                    sqrdistance = f
                else:
                    if -e >= c:
                        t = 1
                        sqrdistance = c + 2.0 * e + f
                    else:
                        t = -e / c
                        sqrdistance = e * t + f
                        # of region 3
        else:
            if t < 0:
                # region 5
                t = 0
                if d >= 0:
                    s = 0
                    sqrdistance = f
                else:
                    if -d >= a:
                        s = 1
                        sqrdistance = a + 2.0 * d + f
                        # GF 20101013 fixed typo d*s ->2*d
                    else:
                        s = -d / a
                        sqrdistance = d * s + f
            else:
                # region 0
                invDet = 1.0 / det
                s = s * invDet
                t = t * invDet
                sqrdistance = s * (a * s + b * t + 2.0 * d) + t * (b * s + c * t + 2.0 * e) + f
    else:
        if s < 0.0:
            # region 2
            tmp0 = b + d
            tmp1 = c + e
            if tmp1 > tmp0:  # minimum on edge s+t=1
                numer = tmp1 - tmp0
                denom = a - 2.0 * b + c
                if numer >= denom:
                    s = 1.0
                    t = 0.0
                    sqrdistance = a + 2.0 * d + f
                    # GF 20101014 fixed typo 2*b -> 2*d
                else:
                    s = numer / denom
                    t = 1 - s
                    sqrdistance = s * (a * s + b * t + 2 * d) + t * (b * s + c * t + 2 * e) + f

            else:  # minimum on edge s=0
                s = 0.0
                if tmp1 <= 0.0:
                    t = 1
                    sqrdistance = c + 2.0 * e + f
                else:
                    if e >= 0.0:
                        t = 0.0
                        sqrdistance = f
                    else:
                        t = -e / c
                        sqrdistance = e * t + f
                        # of region 2
        else:
            if t < 0.0:
                # region6
                tmp0 = b + e
                tmp1 = a + d
                if tmp1 > tmp0:
                    numer = tmp1 - tmp0
                    denom = a - 2.0 * b + c
                    if numer >= denom:
                        t = 1.0
                        s = 0
                        sqrdistance = c + 2.0 * e + f
                    else:
                        t = numer / denom
                        s = 1 - t
                        sqrdistance = s * (a * s + b * t + 2.0 * d) + t * (b * s + c * t + 2.0 * e) + f

                else:
                    t = 0.0
                    if tmp1 <= 0.0:
                        s = 1
                        sqrdistance = a + 2.0 * d + f
                    else:
                        if d >= 0.0:
                            s = 0.0
                            sqrdistance = f
                        else:
                            s = -d / a
                            sqrdistance = d * s + f
            else:
                # region 1
                numer = c + e - b - d
                if numer <= 0:
                    s = 0.0
                    t = 1.0
                    sqrdistance = c + 2.0 * e + f
                else:
                    denom = a - 2.0 * b + c
                    if numer >= denom:
                        s = 1.0
                        t = 0.0
                        sqrdistance = a + 2.0 * d + f
                    else:
                        s = numer / denom
                        t = 1 - s
                        sqrdistance = s * (a * s + b * t + 2.0 * d) + t * (b * s + c * t + 2.0 * e) + f

    # account for numerical round-off error
    if sqrdistance < 0:
        sqrdistance = 0

    dist = sqrdistance**0.5

    return dist


@numba.njit(cache=True)
def ray_triangle_intersect(ray_origin: np.ndarray, ray_direction: np.ndarray, triangle: np.ndarray) -> bool:
    """https://github.com/johnnovak/raytriangle-test/blob/master/python/perftest.py"""
    v0, v1, v2 = triangle[0], triangle[1], triangle[2]
    v0v1 = v1 - v0
    v0v2 = v2 - v0
    pvec = np.cross(ray_direction, v0v2)
    det = np.dot(v0v1, pvec)
    if det < 0.000001:
        return False
    invDet = 1.0 / det
    tvec = ray_origin - v0
    u = np.dot(tvec, pvec) * invDet
    if u < 0 or u > 1:
        return False
    qvec = np.cross(tvec, v0v1)
    v = np.dot(ray_direction, qvec) * invDet
    if v < 0 or u + v > 1:
        return False
    if np.dot(v0v2, qvec) * invDet < 0.000001:
        return False
    return True


@numba.njit(cache=True)
def segment_triangle_intersects(ray_origin: np.ndarray, ray_direction: np.ndarray, triangle: np.ndarray) -> bool:
    """Checks if a line segment (finite length) intersects with a triangle in 3D"""
    intersects1 = ray_triangle_intersect(ray_origin, ray_direction, triangle)
    intersects2 = ray_triangle_intersect((ray_origin + ray_direction), ray_direction * -1, triangle[::-1])
    return intersects1 and intersects2


@numba.njit(cache=True)
def segment_triangle_distance(p1: np.ndarray, p2: np.ndarray, triangle: np.ndarray) -> float:
    """Minimum distance between a line segment (finite length) and a triangle in 3D"""
    if segment_triangle_intersects(p1, p2, triangle):
        return 0.0
    distances = []
    for i, j in ((0, 1), (1, 2), (2, 0)):
        distances.append(segments_distance_3d(p1, p2, triangle[i], triangle[j]))
    return min(distances)
