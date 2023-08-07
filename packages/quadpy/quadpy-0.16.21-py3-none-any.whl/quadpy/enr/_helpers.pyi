from .._exception import QuadpyError as QuadpyError
from ..helpers import QuadratureScheme as QuadratureScheme
from _typeshed import Incomplete
from typing import Callable

class EnrScheme(QuadratureScheme):
    domain: Incomplete
    dim: Incomplete
    def __init__(self, name, dim, weights, points, degree, source, tol: float = ...) -> None: ...
    def integrate(self, f: Callable, dot=...): ...
