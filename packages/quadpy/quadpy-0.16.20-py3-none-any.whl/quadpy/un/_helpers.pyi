from ..helpers import QuadratureScheme as QuadratureScheme
from _typeshed import Incomplete

class UnScheme(QuadratureScheme):
    domain: Incomplete
    dim: Incomplete
    def __init__(self, name, dim, weights, points, degree, source, tol: float = ...) -> None: ...
    def integrate(self, f, center, radius, dot=...): ...
