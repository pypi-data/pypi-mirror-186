from ._adaptive import integrate_adaptive as integrate_adaptive
from ._chebyshev_gauss import chebyshev_gauss_1 as chebyshev_gauss_1, chebyshev_gauss_2 as chebyshev_gauss_2
from ._clenshaw_curtis import clenshaw_curtis as clenshaw_curtis
from ._fejer import fejer_1 as fejer_1, fejer_2 as fejer_2
from ._gauss_jacobi import gauss_jacobi as gauss_jacobi
from ._gauss_kronrod import gauss_kronrod as gauss_kronrod
from ._gauss_legendre import gauss_legendre as gauss_legendre
from ._gauss_lobatto import gauss_lobatto as gauss_lobatto
from ._gauss_patterson import gauss_patterson as gauss_patterson
from ._gauss_radau import gauss_radau as gauss_radau
from ._midpoint import midpoint as midpoint
from ._newton_cotes import newton_cotes_closed as newton_cotes_closed, newton_cotes_open as newton_cotes_open
from ._trapezoidal import trapezoidal as trapezoidal
