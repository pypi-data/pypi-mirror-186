import numpy as np
from numpy.typing import ArrayLike as ArrayLike

def ciede2000(lab1: ArrayLike, lab2: ArrayLike, k_L: float = ..., k_C: float = ..., k_H: float = ...) -> np.ndarray: ...
