from ...cs import ColorSpace
from ..color_distance import ColorDistanceDataset as ColorDistanceDataset
from ..helpers import create_cs_class_instance as create_cs_class_instance
from _typeshed import Incomplete
from typing import Type

class MacAdam1974(ColorDistanceDataset):
    whitepoint_xyz100: Incomplete
    c: float
    Y_b: int
    L_A: int
    xyz100_tiles: Incomplete
    is_flat_pair: Incomplete
    def __init__(self) -> None: ...
    def plot(self, cs_class: Type[ColorSpace]): ...
