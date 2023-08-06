from ..cs import ColorCoordinates as ColorCoordinates, ColorSpace as ColorSpace, convert as convert, string_to_cs as string_to_cs
from _typeshed import Incomplete

class EllipseDataset:
    name: Incomplete
    centers: Incomplete
    points: Incomplete
    def __init__(self, name: str, centers: ColorCoordinates, points: ColorCoordinates) -> None: ...
    def stress(self, cs: ColorSpace): ...
    def plot(self, cs: Union[ColorSpace, str], ellipse_scaling: float = ...): ...
