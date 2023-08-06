import numpy as np
from ._cielab import CIELAB as CIELAB
from ._color_space import ColorSpace as ColorSpace
from ._helpers import register as register
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

class DIN99(ColorSpace):
    name: str
    labels: Incomplete
    k0: int
    k_E: Incomplete
    k_CH: Incomplete
    cielab: Incomplete
    p: Incomplete
    sin_p2: Incomplete
    cos_p2: Incomplete
    sin_p6: Incomplete
    cos_p6: Incomplete
    def __init__(self, k_E: float = ..., k_CH: float = ..., variant: Union[str, None] = ...) -> None: ...
    def from_xyz100(self, xyz: ArrayLike) -> np.ndarray: ...
    def to_xyz100(self, lab99: ArrayLike) -> np.ndarray: ...
