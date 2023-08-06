import numpy as np
from ..cs import ColorCoordinates as ColorCoordinates, convert as convert
from numpy.typing import ArrayLike as ArrayLike

def cmc(lab1: ArrayLike, lab2: ArrayLike, l: float = ..., c: float = ...) -> np.ndarray: ...
