from openride.viewer.models import MODEL_ROTATIONS
from openride import Rotation

from abc import ABC, abstractclassmethod

import os
import numpy as np
import vtk


class BaseModelLoader(ABC):
    @abstractclassmethod
    def __call__(self, file: str, n_polygons: int = 100000) -> vtk.vtkPolyData:
        """Loads files into vtk.vtkPolyData instances"""


def decimate(polydata:vtk.vtkPolyData, n_polygons:int) -> vtk.vtkPolyData:
    decimate = vtk.vtkQuadricDecimation()
    decimate.SetInputData(polydata)
    decimate.SetTargetReduction(1.0 - n_polygons / polydata.GetNumberOfPolys())
    decimate.Update()
    return decimate.GetOutput()


def rotate(polydata:vtk.vtkPolyData, roll:float, pitch:float, yaw:float) -> vtk.vtkPolyData:
    transform = vtk.vtkTransform()
    transform.RotateX(roll)
    transform.RotateY(pitch)
    transform.RotateZ(yaw)
    fil = vtk.vtkTransformPolyDataFilter()
    fil.SetTransform(transform)
    fil.SetInputDataObject(polydata)
    fil.Update()
    return fil.GetOutput()


class STLLoader(BaseModelLoader):
    def __init__(self):
        self._loaded_files = {}

    def __call__(self, file: str, n_polygons: int = 100000) -> vtk.vtkPolyData:
        """Loads .stl files into vtk.vtkPolyData instances"""
        if file not in self._loaded_files:
            reader = vtk.vtkSTLReader()
            reader.SetFileName(file)
            reader.Update()

            polydata = reader.GetOutput()
            polydata = decimate(polydata, n_polygons)
            rotation = MODEL_ROTATIONS.get(os.path.split(file)[-1], Rotation())
            polydata = rotate(polydata, np.rad2deg(rotation.roll), np.rad2deg(rotation.pitch), np.rad2deg(rotation.yaw))

            self._loaded_files[file] = polydata

        return self._loaded_files[file]


class OBJLoader(BaseModelLoader):
    def __init__(self):
        self._loaded_files = {}

    def __call__(self, file: str, n_polygons: int = 100000) -> vtk.vtkPolyData:
        """Loads .stl files into vtk.vtkPolyData instances"""
        if file not in self._loaded_files:
            reader = vtk.vtkOBJReader()
            reader.SetFileName(file)
            reader.Update()
            polydata = reader.GetOutput()

            polydata = reader.GetOutput()
            polydata = decimate(polydata, n_polygons)
            rotation = MODEL_ROTATIONS.get(os.path.split(file)[-1], Rotation())
            polydata = rotate(polydata, np.rad2deg(rotation.roll), np.rad2deg(rotation.pitch), np.rad2deg(rotation.yaw))

        return self._loaded_files[file]


class ModelLoader(BaseModelLoader):
    def __init__(self):
        self.loaders = {
            "stl": STLLoader(),
            "obj": OBJLoader(),
        }

    def __call__(self, file: str, n_polygons: int = 100000) -> vtk.vtkPolyData:
        loader = self.loaders.get(file.split(".")[-1])
        if loader is None:
            raise NotImplementedError
        else:
            return loader(file, n_polygons)
