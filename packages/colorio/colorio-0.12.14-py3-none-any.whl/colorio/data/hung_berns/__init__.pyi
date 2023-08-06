from ..hue_linearity import HueLinearityDataset as HueLinearityDataset

class HungBerns(HueLinearityDataset):
    c: float
    Y_b: int
    L_A: int
    def __init__(self) -> None: ...
