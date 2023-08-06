from openride import Point, BoundingBox, Rotation, PointCloud, BoundingBoxCollection, Polyline

import cv2
import numpy as np

from typing import List, Tuple, Union

TO_CAMERA_COORDINATES = Rotation(-np.pi / 2, 0, -np.pi / 2).get_matrix()


class ImageViewer:
    def __init__(
        self, title: str = "Openride Image Viewer", camera_matrix: np.ndarray = np.eye(3), distortion: List[float] = []
    ):
        self.title = title
        self.camera_matrix = camera_matrix
        self.distortion = distortion

        cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)
        cv2.setMouseCallback(title, self.mouse_callback)

        self.display = None

    def update(self):
        if self.display is None:
            return
        cv2.imshow(self.title, self.display[..., ::-1])
        cv2.waitKey(1)

    def draw_image(self, image: np.ndarray):
        self.display = image / 256

    def draw_point(self, point: Point, color: tuple = (1, 1, 1), size: int = 3):
        if point.x < 0:
            return
        point2d = self.__project_points(np.array((point.x, point.y, point.z))).astype(int)
        for p in point2d:
            cv2.circle(self.display, p, size, color, -1)

    def draw_point_cloud(
        self,
        pcloud: PointCloud,
        color: tuple = (1, 1, 1),
        size: int = 3,
    ):
        mask = np.where(pcloud.get_point_cloud()[:, 0] > 0.0)[0]
        points2d = self.__project_points(pcloud.get_point_cloud()[mask]).astype(int)
        for p in points2d:
            if p[0] < 0 or p[1] < 0 or p[0] >= self.display.shape[1] or p[1] >= self.display.shape[0]:
                continue
            cv2.circle(self.display, p, size, color, -1)

    def draw_bounding_box(
        self,
        bounding_box: Union[BoundingBox, BoundingBoxCollection],
        color: tuple = (1, 1, 1),
        linewidth: int = 2,
    ):
        if isinstance(bounding_box, BoundingBoxCollection):
            [self.draw_bounding_box(box, color) for box in bounding_box]
            return

        for line in self.__get_box_projection(bounding_box):
            cv2.line(self.display, line[0], line[1], color, linewidth)

    def draw_polyline(
        self,
        line: Polyline,
        color: tuple = (1, 1, 1),
        linewidth: int = 2,
    ):
        mask = np.where(line.vertices[:, 0] > 0.0)[0]
        if mask.shape[0] < 2:
            return
        points2d = self.__project_points(line.vertices).astype(int)
        for i in range(mask.shape[0] - 1):
            cv2.line(self.display, points2d[mask][i], points2d[mask][i + 1], color, linewidth)

    def mouse_callback(self, event, x, y, *_):
        pass

    def close(self):
        cv2.destroyWindow(self.title)

    def __project_points(self, points: np.ndarray) -> np.ndarray:
        if points.shape[0] == 0:
            return np.empty((0, 2))
        R = T = np.zeros((3, 1))
        pts2d, _ = cv2.projectPoints(
            points @ TO_CAMERA_COORDINATES, R, T, self.camera_matrix, np.array(self.distortion)
        )
        return pts2d[:, 0, :]

    def __get_box_projection(self, box: BoundingBox) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:

        lines: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
        vertices = box.get_vertices()
        mask = vertices[:, 0] >= 0
        pts2d = self.__project_points(vertices)

        indices = [6, 7, 7, 1, 1, 0, 0, 6, 4, 5, 5, 3, 3, 2, 2, 4, 6, 4, 7, 5, 0, 2, 1, 3]
        for i in range(0, len(indices) - 1, 2):
            if not mask[indices[i]] or not mask[indices[i + 1]]:
                continue
            p1 = tuple(pts2d[indices[i]].astype(int))
            p2 = tuple(pts2d[indices[i + 1]].astype(int))
            lines.append((p1, p2))
        return lines
