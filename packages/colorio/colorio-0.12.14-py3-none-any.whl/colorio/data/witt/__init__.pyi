from ..color_distance import ColorDistanceDataset as ColorDistanceDataset
from _typeshed import Incomplete

class Witt(ColorDistanceDataset):
    whitepoint_xyz100: Incomplete
    c: float
    L_A: float
    Y_b: float
    def __init__(self) -> None: ...
