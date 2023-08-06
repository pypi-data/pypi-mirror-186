import numpy as np
from ._color_space import ColorSpace as ColorSpace
from ._helpers import register as register
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

class OsaUcs(ColorSpace):
    name: str
    labels: Incomplete
    k0: int
    M: Incomplete
    Minv: Incomplete
    def __init__(self) -> None: ...
    def from_xyz100(self, xyz100: ArrayLike) -> np.ndarray: ...
    def to_xyz100(self, ljg: ArrayLike, tol: float = ..., max_num_newton_steps: int = ...): ...
