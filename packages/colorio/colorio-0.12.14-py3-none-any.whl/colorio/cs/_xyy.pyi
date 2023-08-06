import numpy as np
from .._exceptions import ColorioError as ColorioError
from ._color_space import ColorSpace as ColorSpace
from ._helpers import register as register
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

class XYY(ColorSpace):
    name: str
    labels: Incomplete
    k0: int
    is_origin_well_defined: bool
    Y_scaling: Incomplete
    def __init__(self, Y_scaling: int) -> None: ...
    def from_xyz100(self, xyz100: ArrayLike) -> np.ndarray: ...
    def to_xyz100(self, xyy: ArrayLike) -> np.ndarray: ...

class XYY1(XYY):
    name: str
    labels: Incomplete
    def __init__(self) -> None: ...

class XYY100(XYY):
    name: str
    labels: Incomplete
    def __init__(self) -> None: ...
