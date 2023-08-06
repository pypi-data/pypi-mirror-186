from ..color_distance import ColorDistanceDataset as ColorDistanceDataset
from _typeshed import Incomplete

class Leeds(ColorDistanceDataset):
    whitepoint_xyz100: Incomplete
    c: float
    L_A: int
    Y_b: int
    def __init__(self) -> None: ...
