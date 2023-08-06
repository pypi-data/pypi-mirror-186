from openride import BoundingBox, BoundingBoxCollection
from openride import Point, Polyline, Polygon, PointCloud
from openride import Category, SubCategory
from openride import Transform
from openride.core.numba.coordinate_systems import spherical_to_cartesian
from openride.core.numba.transforms import transform_point
from openride.viewer import vtk_utils
from openride.viewer.camera import Camera
from openride.viewer.interactor import Interactor, Event
from openride.viewer.hud import Hud
from openride.viewer.model_loader import ModelLoader
from openride.viewer.models import DEFAULT_MODELS

from typing import Iterable, List, Optional, Tuple, Union
from vtk.util.numpy_support import vtk_to_numpy

import numpy as np
import vtk


class Viewer:
    def __init__(
        self,
        resolution: Tuple[int, int] = (1600, 900),
        background: Tuple[float, float, float] = (0.05, 0.05, 0.1),
        mouse_camera_interactions: bool = True,
        render_offscreen: bool = False,
        exit_callback: callable = exit,
    ):

        self.renderer = vtk.vtkRenderer()
        self.renderWindow = vtk.vtkRenderWindow()
        self.renderWindow.AddRenderer(self.renderer)

        if render_offscreen:
            self.renderWindow.SetOffScreenRendering(1)

        self.set_resolution(resolution)
        self.set_background(background)

        self.callbacks: List[callable] = []

        self.camera = Camera(self)
        self.interactor = Interactor(self, mouse_camera_interactions)
        self.interactor.set_callback(Event.ExitEvent, exit_callback)
        self.hud = Hud(self, position=(50, 50))

        self._model_loader = ModelLoader()

        self._actors_to_clear = []
        self._text_actor_index = 0

    def set_resolution(self, resolution: Tuple[int, int]):
        self._resolution = resolution
        self.renderWindow.SetSize(resolution[0], resolution[1])

    def set_background(self, color=Tuple[float, float, float]):
        self.renderer.SetBackground(*color)

    def set_callback(self, callback: callable):
        self.callbacks.append(callback)

    def update(self, return_image: bool = False) -> Optional[np.ndarray]:
        [callback() for callback in self.callbacks]
        if not hasattr(self, "renderWindow"):
            return
        self.renderWindow.Render()
        self.__clear_actors()
        if return_image:
            return get_last_rendered_image(self)

    def render_actor(self, actor: vtk.vtkActor, persist: bool = False):
        self.renderer.AddActor(actor)
        if not persist:
            self._actors_to_clear.append(actor)

    def draw_point(
        self,
        point: Point,
        color: tuple = (1, 1, 1),
        size: float = 0.15,
        alpha: float = 1,
        resolution: int = 10,
        persist: bool = False,
    ):
        actor = vtk_utils.get_point_actor(point.x, point.y, point.z, color, size, alpha, resolution)
        self.render_actor(actor, persist)

    def draw_point_cloud(
        self,
        pcloud: PointCloud,
        color: tuple = None,
        colors: Iterable[float] = None,
        colormap: str = "jet",
        color_range: float = 2**16,
        size: int = 10,
        alpha: float = 1,
        persist: bool = False,
    ):
        if color is None and colors is None:
            color = (1, 1, 1)
        actor = vtk_utils.get_point_cloud_actor(
            pcloud.get_point_cloud(), colors, color, colormap, size, alpha, color_range
        )
        self.render_actor(actor, persist)

    def draw_bounding_box(
        self,
        bounding_box: Union[BoundingBox, BoundingBoxCollection],
        color: tuple = (1, 1, 1),
        alpha: float = 1,
        edge_color: tuple = None,
        persist: bool = False,
    ):

        if isinstance(bounding_box, BoundingBoxCollection):
            [self.draw_bounding_box(box, color, alpha, edge_color, persist) for box in bounding_box]
            return

        actor = vtk_utils.get_box_actor(
            bounding_box.position.x,
            bounding_box.position.y,
            bounding_box.position.z,
            bounding_box.size.x,
            bounding_box.size.y,
            bounding_box.size.z,
            bounding_box.rotation.roll,
            bounding_box.rotation.pitch,
            bounding_box.rotation.yaw,
            color,
            alpha,
        )

        if edge_color is not None:
            actor.GetProperty().SetEdgeVisibility(1)
            actor.GetProperty().SetLineWidth(10)
            actor.GetProperty().SetEdgeColor(*edge_color)

        self.render_actor(actor, persist)

    def draw_model(
        self,
        model: Union[str, Category, SubCategory],
        bounding_box: BoundingBox,
        number_polygons: int = 100000,
        color: tuple = (1, 1, 1),
        alpha: float = 1,
        persist: bool = False,
    ):
        p = bounding_box.position
        s = bounding_box.size
        r = bounding_box.rotation
        if isinstance(model, (Category, SubCategory)):
            file = DEFAULT_MODELS.get(model)
        else:
            file = model
        if not file:
            return
        actor = vtk_utils.get_model_actor(
            self._model_loader,
            file,
            number_polygons,
            p.x,
            p.y,
            p.z,
            s.x,
            s.y,
            s.z,
            r.roll,
            r.pitch,
            r.yaw,
            color,
            alpha,
        )
        self.render_actor(actor, persist)

    def draw_polyline(
        self,
        line: Polyline,
        color: tuple = (1, 1, 1),
        alpha: float = 1,
        linewidth: int = 2,
        persist: bool = False,
    ):
        actor = vtk_utils.get_line_actor(line.vertices, color, alpha, linewidth)
        self.render_actor(actor, persist)

    def draw_polylines(
        self,
        lines: List[Polyline],
        color: tuple = (1, 1, 1),
        alpha: float = 1,
        linewidth: int = 2,
        persist: bool = False,
    ):
        actor = vtk_utils.get_lines_actor(
            [line.vertices for line in lines],
            color=color,
            alpha=alpha,
            linewidth=linewidth,
        )
        self.render_actor(actor, persist)

    def draw_polygon(
        self,
        polygon: Polygon,
        color: tuple = (1, 1, 1),
        alpha: float = 1,
        persist: bool = False,
    ):
        actor = vtk_utils.get_polygon_actor(polygon.vertices, color=color, alpha=alpha)
        self.render_actor(actor, persist)

    def labelize(self, label: str, pos: Point, fontsize: int = 16, persist: bool = False):
        if not self.camera.is_in_front(pos):
            return
        actor = vtk_utils.get_text_actor(label, pos.x, pos.y, pos.z, fontsize, self._text_actor_index)
        self.render_actor(actor, persist)
        self._text_actor_index += 1

    def draw_arrow(
        self,
        start: Point,
        end: Point,
        color: tuple = (1, 1, 1),
        alpha: float = 1.0,
        linewidth: int = 10,
        headsize: float = 1.0,
        persist: bool = False,
    ):
        self.draw_polyline(Polyline([start, end]), color=color, alpha=alpha, linewidth=linewidth, persist=persist)
        actor = vtk_utils.get_cone_actor(
            start.x,
            start.y,
            start.z,
            end.x,
            end.y,
            end.z,
            color,
            alpha,
            headsize,
        )
        self.render_actor(actor, persist)

    def draw_transform(
        self,
        transform: Transform,
        ax_length: float = 1.0,
        alpha: float = 1.0,
        linewidth: int = 10,
        headsize: float = 0.1,
        persist: bool = False,
    ):
        origin = transform.translation
        matrix = transform.get_matrix()

        for ax, color in zip(
            ((ax_length, 0, 0), (0, ax_length, 0), (0, 0, ax_length)), ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        ):
            end = Point(*transform_point(*ax, matrix))
            self.draw_arrow(
                origin, end, color=color, alpha=alpha, linewidth=linewidth, headsize=headsize, persist=persist
            )

    def draw_grid(
        self,
        origin: Point = Point(),
        delta: float = 5.0,
        extent: float = 200.0,
        alpha: float = 1.0,
        persist: bool = True,
    ):
        lines = []

        for s in [0, 1]:
            for i in range(int(2 * extent / delta) + 1):
                points = []
                if s == 0:
                    points.append(Point(-extent, -extent + i * delta) + origin)
                    points.append(Point(extent, -extent + i * delta) + origin)
                else:
                    points.append(Point(-extent + i * delta, -extent) + origin)
                    points.append(Point(-extent + i * delta, extent) + origin)
                lines.append(Polyline(points))

        self.draw_polylines(lines, color=(0.3, 0.3, 0.3), alpha=alpha, linewidth=1, persist=persist)

    def draw_polar_grid(
        self,
        origin: Point = Point(),
        delta_radius: float = 10.0,
        delta_theta: float = 15.0,
        extent: float = 300.0,
        alpha: float = 1.0,
        persist: bool = True,
    ):
        lines = []

        for radius in np.arange(delta_radius, extent + delta_radius, delta_radius):

            points = []
            for theta in np.linspace(0, 2 * np.pi, 100):
                points.append(Point(*spherical_to_cartesian(radius, theta, np.pi / 2)) + origin)
            lines.append(Polyline(points))

        for theta in np.arange(0.0, 2 * np.pi, np.deg2rad(delta_theta)):
            lines.append(Polyline([origin, origin + Point(*spherical_to_cartesian(extent, theta, np.pi / 2))]))

        self.draw_polylines(lines, color=(0.3, 0.3, 0.3), alpha=alpha, linewidth=1, persist=persist)

    def __clear_actors(self):
        for actor in self._actors_to_clear:
            self.renderer.RemoveActor(actor)
        self._actors_to_clear = []
        self._text_actor_index = 0

    def close(self):
        self.renderWindow.Finalize()
        self.interactor._interactor.TerminateApp()
        del self.interactor._interactor
        del self.renderWindow


def get_last_rendered_image(viewer: Viewer) -> np.ndarray:
    win_to_img = vtk.vtkWindowToImageFilter()
    win_to_img.SetShouldRerender(0)
    win_to_img.SetInput(viewer.renderWindow)
    win_to_img.Update()
    vtk_image = win_to_img.GetOutput()

    flip = vtk.vtkImageFlip()
    flip.SetInputData(vtk_image)
    flip.SetFilteredAxis(1)
    flip.FlipAboutOriginOn()
    flip.Update()
    vtk_image = flip.GetOutput()

    width, height, _ = vtk_image.GetDimensions()
    vtk_array = vtk_image.GetPointData().GetScalars()
    components = vtk_array.GetNumberOfComponents()
    return vtk_to_numpy(vtk_array).reshape(height, width, components)
