from ...cs import ColorSpace
from ..color_distance import ColorDistanceDataset as ColorDistanceDataset
from ..helpers import create_cs_class_instance as create_cs_class_instance
from _typeshed import Incomplete
from typing import Type

class MacAdam1942(ColorDistanceDataset):
    Y: Incomplete
    whitepoint_xyz100: Incomplete
    L_A: int
    c: float
    Y_b: int
    xy_centers: Incomplete
    xy_offsets: Incomplete
    def __init__(self, Y) -> None: ...
    def plot(self, cs_class: Type[ColorSpace], ellipse_scaling: float = ...): ...
