from _typeshed import Incomplete
from typing import NamedTuple

class article(NamedTuple):
    authors: Incomplete
    title: Incomplete
    journal: Incomplete
    volume: Incomplete
    number: Incomplete
    year: Incomplete
    month: Incomplete
    pages: Incomplete
    url: Incomplete
    issn: Incomplete
    issne: Incomplete
    note: Incomplete

class book(NamedTuple):
    authors: Incomplete
    title: Incomplete
    publisher: Incomplete
    isbn: Incomplete
    year: Incomplete
    url: Incomplete
    note: Incomplete

class techreport(NamedTuple):
    authors: Incomplete
    title: Incomplete
    year: Incomplete
    month: Incomplete
    institution: Incomplete
    number: Incomplete
    url: Incomplete
    note: Incomplete

class phdthesis(NamedTuple):
    authors: Incomplete
    title: Incomplete
    year: Incomplete
    school: Incomplete
    url: Incomplete
    note: Incomplete

class online(NamedTuple):
    authors: Incomplete
    title: Incomplete
    year: Incomplete
    url: Incomplete
    note: Incomplete

def untangle(data): ...
def n_outer(a): ...
def compute_dobrodeev(n, I0, I2, I22, I4, pm_type, i, j, k, symbolic: bool = ...): ...
def get_nsimplex_points(n, sqrt, frac): ...
def prod(lst): ...
def comb(a, b): ...
def gamma_n_2(n, symbolic): ...
