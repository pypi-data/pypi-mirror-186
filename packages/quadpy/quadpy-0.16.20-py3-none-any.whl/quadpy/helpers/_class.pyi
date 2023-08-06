from _typeshed import Incomplete

class QuadratureScheme:
    test_tolerance: Incomplete
    name: Incomplete
    degree: Incomplete
    source: Incomplete
    comments: Incomplete
    weights: Incomplete
    weights_symbolic: Incomplete
    points: Incomplete
    points_symbolic: Incomplete
    def __init__(self, name: str, weights, points, degree: int, source, tol: float = ..., comments: Union[list[str], None] = ...) -> None: ...
    def savefig(self, filename, *args, **kwargs) -> None: ...
    def show(self, *args, **kwargs) -> None: ...
