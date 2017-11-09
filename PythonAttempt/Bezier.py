#-----THIS IS THE IMPLEMENTATION OF THE BEZIER CURVE SUBROUTINE-------#
import numpy as np
from scipy.special import binom


def Bernstein(n, k):
    # Bernstein polynomial.
    coeff = binom(n, k)

    def _bpoly(x):
        return coeff * x ** k * (1 - x) ** (n - k)
    return _bpoly


def Bezier(points, num=200):
    # Build Bézier curve from points.
    N = len(points)
    t = np.linspace(0, 1, num=num)
    curve = np.zeros((num, 2))
    for ii in range(N):
        curve += np.outer(Bernstein(N - 1, ii)(t), points[ii])
    return curve
#-----END BEZIER SUBROUTINE-------------------------------------------#
