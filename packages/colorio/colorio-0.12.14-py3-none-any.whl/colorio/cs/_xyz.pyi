import numpy as np
from .._exceptions import ColorioError as ColorioError
from ._color_space import ColorSpace as ColorSpace
from ._helpers import register as register
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

class XYZ(ColorSpace):
    name: str
    labels: Incomplete
    k0: Incomplete
    scaling: Incomplete
    def __init__(self, scaling: float) -> None: ...
    def from_xyz100(self, xyz: ArrayLike) -> np.ndarray: ...
    def to_xyz100(self, xyz: ArrayLike) -> np.ndarray: ...

class XYZ1(XYZ):
    name: str
    def __init__(self) -> None: ...

class XYZ100(ColorSpace):
    name: str
    labels: Incomplete
    def __init__(self) -> None: ...
    def from_xyz100(self, xyz: ArrayLike) -> np.ndarray: ...
    def to_xyz100(self, xyz: ArrayLike) -> np.ndarray: ...
