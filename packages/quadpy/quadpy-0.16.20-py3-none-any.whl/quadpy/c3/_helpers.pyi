from .. import helpers as helpers
from ..cn import CnScheme as CnScheme, transform as transform
from _typeshed import Incomplete

schemes: Incomplete

def register(in_schemes) -> None: ...

class C3Scheme(CnScheme):
    symmetry_data: Incomplete
    domain: str
    def __init__(self, name, symmetry_data, degree, source: Incomplete | None = ..., tol: float = ...) -> None: ...
    def show(self, hexa=..., backend: str = ...): ...

def get_good_scheme(degree): ...
