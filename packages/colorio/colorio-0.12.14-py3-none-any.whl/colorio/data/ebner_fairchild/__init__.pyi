from ..hue_linearity import HueLinearityDataset as HueLinearityDataset

class EbnerFairchild(HueLinearityDataset):
    L_A: int
    c: float
    Y_b: int
    def __init__(self) -> None: ...
