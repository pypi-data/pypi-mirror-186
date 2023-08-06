from ..tn import get_vol as get_vol
from ._dunavant import dunavant_05 as dunavant_05, dunavant_10 as dunavant_10
from _typeshed import Incomplete

def integrate_adaptive(f, triangles, eps, minimum_triangle_area: Incomplete | None = ..., scheme1=..., scheme2=..., dot=...): ...
