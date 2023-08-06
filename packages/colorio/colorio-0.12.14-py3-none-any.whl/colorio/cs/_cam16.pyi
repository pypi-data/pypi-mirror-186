import numpy as np
from ..cat import cat16 as cat16
from ..illuminants import whitepoints_cie1931 as whitepoints_cie1931
from ._ciecam02 import compute_from as compute_from, compute_to as compute_to
from ._color_space import ColorSpace as ColorSpace
from ._helpers import register as register
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

class CAM16:
    name: str
    c: Incomplete
    N_c: Incomplete
    F_L: Incomplete
    n: Incomplete
    z: Incomplete
    N_bb: Incomplete
    N_cb: Incomplete
    A_w: Incomplete
    h: Incomplete
    e: Incomplete
    H: Incomplete
    def __init__(self, c: float, Y_b: float, L_A: float, whitepoint: ArrayLike = ...) -> None: ...
    def from_xyz100(self, xyz): ...
    def to_xyz100(self, data, description): ...

class CAM16UCS(ColorSpace):
    name: str
    labels: Incomplete
    k0: int
    K_L: float
    c1: float
    c2: float
    cam16: Incomplete
    def __init__(self, c: float, Y_b: float, L_A: float, whitepoint: ArrayLike = ...) -> None: ...
    def from_xyz100(self, xyz: ArrayLike) -> np.ndarray: ...
    def to_xyz100(self, jab: ArrayLike) -> np.ndarray: ...
