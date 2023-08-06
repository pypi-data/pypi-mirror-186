from ...cs import ColorSpace
from ..helpers import create_cs_class_instance as create_cs_class_instance, stress_absolute as stress_absolute
from _typeshed import Incomplete
from typing import Type

this_dir: Incomplete

class FairchildChen:
    c: float
    Y_b: int
    L_A: int
    Lw: int
    whitepoint_xyz100: Incomplete
    data: Incomplete
    key: Incomplete
    def __init__(self, key: str) -> None: ...
    def plot(self, cs_class: Type[ColorSpace]): ...
    def stress(self, cs_class: Type[ColorSpace]) -> float: ...
