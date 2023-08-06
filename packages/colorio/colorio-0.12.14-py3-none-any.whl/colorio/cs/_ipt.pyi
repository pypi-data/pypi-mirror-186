import numpy as np
from ._color_space import ColorSpace as ColorSpace
from ._helpers import register as register
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

class IPT(ColorSpace):
    name: str
    labels: Incomplete
    k0: int
    M1: Incomplete
    M2: Incomplete
    def __init__(self) -> None: ...
    def from_xyz100(self, xyz: ArrayLike) -> np.ndarray: ...
    def to_xyz100(self, ipt: ArrayLike) -> np.ndarray: ...
