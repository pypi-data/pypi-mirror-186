from .._exception import QuadpyError as QuadpyError
from ..helpers import QuadratureScheme as QuadratureScheme, backend_to_function as backend_to_function, expand_symmetries as expand_symmetries
from _typeshed import Incomplete
from typing import Callable

schemes: Incomplete

def register(in_schemes) -> None: ...

class S3Scheme(QuadratureScheme):
    symmetry_data: Incomplete
    domain: str
    def __init__(self, name, symmetry_data, degree, source: Incomplete | None = ..., tol: float = ...) -> None: ...
    def show(self, backend: str = ..., **kwargs): ...
    def integrate(self, f: Callable, center, radius, dot=...): ...

def get_good_scheme(degree: int) -> Union[S3Scheme, None]: ...
