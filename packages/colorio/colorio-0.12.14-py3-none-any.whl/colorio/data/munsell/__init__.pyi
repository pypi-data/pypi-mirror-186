from ...cs import ColorSpace
from ..helpers import create_cs_class_instance as create_cs_class_instance, stress_absolute as stress_absolute
from _typeshed import Incomplete
from typing import Type

this_dir: Incomplete

class Munsell:
    h: Incomplete
    V: Incomplete
    C: Incomplete
    xyz100: Incomplete
    whitepoint_xyz100: Incomplete
    L_A: int
    c: float
    Y_b: int
    lightness: Incomplete
    def __init__(self) -> None: ...
    def plot(self, cs_class: Type[ColorSpace], V: int): ...
    def plot_lightness(self, cs_class: Type[ColorSpace]): ...
    def stress_lightness(self, cs_class: Type[ColorSpace]) -> float: ...
    stress: Incomplete
