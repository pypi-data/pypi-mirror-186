from ..illuminants import whitepoints_cie1931 as whitepoints_cie1931
from ._cieluv import CIELUV as CIELUV
from ._color_space import ColorSpace as ColorSpace
from ._helpers import register as register
from _typeshed import Incomplete

class CIEHCL(ColorSpace):
    name: str
    labels: Incomplete
    k0: int
    is_origin_well_defined: bool
    cieluv: Incomplete
    def __init__(self, whitepoint=...) -> None: ...
    def from_xyz100(self, xyz): ...
    def to_xyz100(self, lch): ...
