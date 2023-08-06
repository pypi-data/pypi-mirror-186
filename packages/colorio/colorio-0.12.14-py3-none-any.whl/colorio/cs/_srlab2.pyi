import numpy as np
from ..cat.cat02 import M_cat02 as M_cat02
from ..illuminants import whitepoints_cie1931 as whitepoints_cie1931
from ._ciecam02 import M_hpe as M_hpe
from ._cielab import A as A, f as f, finv as finv
from ._color_space import ColorSpace as ColorSpace
from ._helpers import register as register
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

class SRLAB2(ColorSpace):
    name: str
    labels: Incomplete
    k0: int
    whitepoint_xyz100: Incomplete
    B: Incomplete
    C: Incomplete
    Binv: Incomplete
    Cinv: Incomplete
    def __init__(self, whitepoint: ArrayLike = ...) -> None: ...
    def from_xyz100(self, xyz: ArrayLike) -> np.ndarray: ...
    def to_xyz100(self, lab: ArrayLike) -> np.ndarray: ...
