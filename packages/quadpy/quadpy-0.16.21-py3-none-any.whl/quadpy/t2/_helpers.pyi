from ..helpers import expand_symmetries as expand_symmetries, plot_disks as plot_disks
from ..tn import TnScheme as TnScheme, get_vol as get_vol, transform as transform
from _typeshed import Incomplete

schemes: Incomplete

def register(in_schemes) -> None: ...

class T2Scheme(TnScheme):
    symmetry_data: Incomplete
    domain: str
    def __init__(self, name: str, symmetry_data, degree: int, source: Incomplete | None = ..., tol: float = ..., comments: Union[list[str], None] = ..., weight_factor: Union[float, None] = ...) -> None: ...
    def plot(self, triangle=..., show_axes: bool = ...): ...

def get_good_scheme(degree: int) -> Union[T2Scheme, None]: ...
