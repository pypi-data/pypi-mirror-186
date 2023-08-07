from .c1 import integrate_adaptive as integrate_adaptive
from typing import Callable

def quad(f: Callable, a, b, args=..., epsabs: float = ..., epsrel: float = ..., limit: int = ...): ...
