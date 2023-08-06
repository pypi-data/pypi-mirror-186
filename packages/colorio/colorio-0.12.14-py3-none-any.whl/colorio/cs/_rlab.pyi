import numpy as np
from ..illuminants import whitepoints_cie1931 as whitepoints_cie1931
from ._color_space import ColorSpace as ColorSpace
from ._helpers import register as register
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

class RLAB(ColorSpace):
    name: str
    labels: Incomplete
    k0: int
    whitepoint: Incomplete
    sigma: Incomplete
    A: Incomplete
    Ainv: Incomplete
    def __init__(self, Y_n: float = ..., D: float = ..., whitepoint: ArrayLike = ..., sigma: float = ...) -> None: ...
    def from_xyz100(self, xyz: ArrayLike) -> np.ndarray: ...
    def to_xyz100(self, lab: ArrayLike) -> np.ndarray: ...
