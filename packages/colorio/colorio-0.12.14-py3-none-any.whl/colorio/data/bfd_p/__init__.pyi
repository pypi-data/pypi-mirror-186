from ...cs import ColorSpace
from ..helpers import create_cs_class_instance as create_cs_class_instance, stress_absolute as stress_absolute, stress_relative as stress_relative
from _typeshed import Incomplete
from typing import Callable, Type

class BfdP:
    c: float
    L_A: int
    Y_b: int
    target_dist: Incomplete
    xyz_pairs: Incomplete
    whitepoints: Incomplete
    def __init__(self) -> None: ...
    def stress(self, cs_class: Type[ColorSpace], variant: str = ...): ...
    def stress_lab_diff(self, fun: Callable, variant: str = ...) -> float: ...
