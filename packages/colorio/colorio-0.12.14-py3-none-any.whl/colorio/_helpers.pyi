from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

class SpectralData:
    name: Incomplete
    lmbda_nm: Incomplete
    data: Incomplete
    def __init__(self, lmbda_nm: ArrayLike, data: ArrayLike, name: Union[str, None] = ...) -> None: ...
