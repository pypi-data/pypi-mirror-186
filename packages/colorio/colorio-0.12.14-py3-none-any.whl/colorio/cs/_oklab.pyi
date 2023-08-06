import numpy as np
from ._color_space import ColorSpace as ColorSpace
from ._helpers import register as register
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

class OKLAB(ColorSpace):
    name: str
    labels: Incomplete
    k0: int
    M1: Incomplete
    M1inv: Incomplete
    M2: Incomplete
    M2inv: Incomplete
    lightness_type: Incomplete
    k1: float
    k2: float
    k3: Incomplete
    def __init__(self, lightness_type: str = ...) -> None: ...
    def from_xyz100(self, xyz100: ArrayLike) -> np.ndarray: ...
    def to_xyz100(self, lab: ArrayLike) -> np.ndarray: ...
