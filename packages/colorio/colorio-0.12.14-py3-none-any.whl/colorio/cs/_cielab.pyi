import numpy as np
from ..illuminants import whitepoints_cie1931 as whitepoints_cie1931
from ._color_space import ColorSpace as ColorSpace
from ._helpers import register as register
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

def f(t): ...
def finv(t): ...

A: Incomplete
Ainv: Incomplete

class CIELAB(ColorSpace):
    name: str
    labels: Incomplete
    k0: int
    whitepoint_xyz100: Incomplete
    def __init__(self, whitepoint: ArrayLike = ...) -> None: ...
    def from_xyz100(self, xyz: ArrayLike) -> np.ndarray: ...
    def to_xyz100(self, lab: ArrayLike) -> np.ndarray: ...
