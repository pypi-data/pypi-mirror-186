from ..cs import CIELAB as CIELAB, ColorSpace as ColorSpace
from .helpers import create_cs_class_instance as create_cs_class_instance, stress_absolute as stress_absolute, stress_relative as stress_relative
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike
from typing import Callable

class ColorDistanceDataset:
    name: Incomplete
    target_dist: Incomplete
    xyz_pairs: Incomplete
    weights: Incomplete
    def __init__(self, name: str, target_dist: ArrayLike, xyz_pairs: ArrayLike, weights: Union[float, ArrayLike] = ...) -> None: ...
    def plot(self, cs_class: type[ColorSpace]): ...
    def stress(self, cs_class: type[ColorSpace], variant: str = ...) -> float: ...
    def stress_lab_diff(self, fun: Callable, variant: str = ...) -> float: ...
