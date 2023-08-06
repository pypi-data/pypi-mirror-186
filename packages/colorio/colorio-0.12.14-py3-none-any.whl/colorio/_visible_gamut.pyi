from . import observers as observers
from ._tools import get_mono_outline_xy as get_mono_outline_xy
from .cs import ColorCoordinates as ColorCoordinates, ColorSpace as ColorSpace, convert as convert, string_to_cs as string_to_cs

def plot_visible_slice(colorspace: Union[ColorSpace, str], lightness: float, outline_prec: float = ..., fill_color: str = ...): ...
