from ._color_space import ColorSpace as ColorSpace
from ._hdr import HdrLinear as HdrLinear
from ._helpers import register as register
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

class ICtCp(ColorSpace):
    name: str
    labels: Incomplete
    k0: int
    M1: Incomplete
    m1: Incomplete
    m2: Incomplete
    c1: Incomplete
    c2: Incomplete
    c3: Incomplete
    M2: Incomplete
    def __init__(self) -> None: ...
    def from_rec2100(self, rgb: ArrayLike) -> ArrayLike: ...
    def to_rec2100(self, ictcp: ArrayLike) -> ArrayLike: ...
    def from_xyz100(self, xyz100: ArrayLike) -> ArrayLike: ...
    def to_xyz100(self, ictcp: ArrayLike) -> ArrayLike: ...
