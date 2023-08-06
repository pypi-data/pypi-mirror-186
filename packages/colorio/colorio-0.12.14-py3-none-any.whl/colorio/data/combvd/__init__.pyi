from ...cs import ColorSpace
from ..bfd_p import BfdP as BfdP
from ..helpers import create_cs_class_instance as create_cs_class_instance, stress_absolute as stress_absolute, stress_relative as stress_relative
from ..leeds import Leeds as Leeds
from ..rit_dupont import RitDupont as RitDupont
from ..witt import Witt as Witt
from _typeshed import Incomplete
from typing import Callable, Type

class COMBVD:
    bfd_p: Incomplete
    leeds: Incomplete
    rit_dupont: Incomplete
    witt: Incomplete
    def __init__(self) -> None: ...
    def stress(self, cs_class: Type[ColorSpace], variant: str = ...): ...
    def stress_lab_diff(self, fun: Callable, variant: str = ...) -> float: ...
