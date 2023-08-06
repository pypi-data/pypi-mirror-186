import numpy as np
from ..cs import ColorCoordinates as ColorCoordinates, ColorSpace as ColorSpace, convert as convert
from .helpers import create_cs_class_instance as create_cs_class_instance
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

class HueLinearityDataset:
    name: Incomplete
    whitepoint_xyz100: Incomplete
    arms: Incomplete
    neutral_gray: Incomplete
    def __init__(self, name: str, whitepoint_xyz100: ArrayLike, arms, neutral_gray: Union[ArrayLike, None] = ...) -> None: ...
    def plot(self, cs_class: type[ColorSpace]): ...
    def stress(self, cs_class: type[ColorSpace]) -> np.ndarray: ...
