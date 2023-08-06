from ._helpers import SpectralData as SpectralData
from ._tools import spectrum_to_xyz100 as spectrum_to_xyz100
from .cs import ColorSpace as ColorSpace, string_to_cs as string_to_cs

def plot_surface_gamut(colorspace: Union[ColorSpace, str], observer, illuminant, show_grid: bool = ...): ...
