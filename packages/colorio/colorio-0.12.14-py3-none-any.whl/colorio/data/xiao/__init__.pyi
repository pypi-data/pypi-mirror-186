from ..hue_linearity import HueLinearityDataset as HueLinearityDataset

class Xiao(HueLinearityDataset):
    Lw: float
    Y_b: int
    c: float
    L_A: int
    def __init__(self) -> None: ...
