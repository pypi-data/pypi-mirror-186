from ..cn import CnScheme as CnScheme, transform as transform
from ..helpers import expand_symmetries as expand_symmetries, plot_disks as plot_disks
from ..tn import get_vol as get_vol
from _typeshed import Incomplete

schemes: Incomplete

def register(in_schemes) -> None: ...

class C2Scheme(CnScheme):
    symmetry_data: Incomplete
    domain: str
    def __init__(self, name: str, symmetry_data, degree: int, source: Incomplete | None = ..., tol: float = ..., comments: Union[list[str], None] = ...) -> None: ...
    def plot(self, quad=..., show_axes: bool = ...) -> None: ...

def get_good_scheme(degree: int) -> Union[C2Scheme, None]: ...
