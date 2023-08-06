from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

requirements = [
    "shapely",
    "numba",
    "numpy",
    "dataclasses",
    "vtk>=9.1.0",
    "matplotlib",
    "multipledispatch",
    "opencv-python",
    "sk-video",
]

setup(
    name="openride",
    version="0.2.3",
    author="Jean-Luc Déziel",
    author_email="jluc1011@hotmail.com",
    url="https://gitlab.com/jldez/openride",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={"": ["*.stl"]},
    include_package_data=True,
    install_requires=requirements,
)
