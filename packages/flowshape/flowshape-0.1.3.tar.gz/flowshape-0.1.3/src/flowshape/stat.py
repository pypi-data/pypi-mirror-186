"""
Statistics (wip)

For an introduction on random fields, see: 
https://matthew-brett.github.io/teaching/random_fields.html

The formula here are from: Adler. J - Random Fields and Geometry
specifically see:
- lemma 15.7.2
for gaussian: eq. 15.10.5
for chi2: Theorem 15.10.1
the Lipschitz–Killing curvatures for a 2-sphere are: see eq. 6.3.8
L0 = 2
L1 = 0
L2 = 4*pi
"""

# @todo: add t-statistic

from math import floor, comb, factorial
from scipy.special import gamma
from scipy.special import eval_hermite
from scipy.stats import chi2
from scipy.stats import norm
import numpy as np

## gaussian case
def z_EC(c, j):
    if j == 0:
        # P[ normal > c ]
        return norm.sf(c)
    if j > 0:
        ## the (2**(1-j)) factor is because of the difference between physicist and probablist hermite polynomials
        val = (
            (2 * np.pi) ** (-(j + 1) / 2)
            * eval_hermite(j - 1, c)
            * (2 ** (1 - j))
            * np.exp((c**2) * (-0.5))
        )
        return val


def expected_ec_z(z):
    """Expected Euler characteristic of a thresholded spherical random field with Gaussian distribution.

    Args:
        z (float): threshold value (Z-score)

    Returns:
        float: expected Euler characteristic
    """
    s = 0
    # L0 = 2
    s += 2 * z_EC(z, 0)
    # L1 = 0

    # L2 = 4*pi
    s += 4 * np.pi * z_EC(z, 2)

    return s


## Chi2 case:
# c = u
# k = dof
def chi2_EC(c, k, j):
    if j == 0:
        # P[ chi > c ]
        return chi2.sf(c, k)
    if j > 0:
        psum = 0
        for l in range(0, floor(0.5 * (j - 1)) + 1):
            for m in range(0, j - 1 - 2 * l + 1):

                if k >= (j - m - 2 * l):
                    psum += (
                        comb(k - 1, j - 1 - m - 2 * l)
                        * ((-1) ** (j - 1 + m + l) * factorial(j - 1))
                        * c ** (m + l)
                        / (factorial(m) * factorial(l) * 2**l)
                    )

        val = (
            c ** (0.5 * (k - j))
            * np.exp(-c / 2)
            * psum
            / ((2 * np.pi) ** (j / 2) * gamma(k / 2) * 2 ** (0.5 * (k - 2)))
        )
        return val


def expected_ec_chi2(u, dof):
    """Expected Euler characteristic of a thresholded spherical random field with chi-squared distribution.

    Args:
        u (float): threshold value
        dof (integer): degrees of freedom

    Returns:
        float: expected Euler characteristic
    """
    s = 0
    # L0 = 2
    s += 2 * chi2_EC(u, dof, 0)
    # L1 = 0

    # L2 = 4*pi
    s += 4 * np.pi * chi2_EC(u, dof, 2)

    return s


# u_crit = chi2.isf(0.05, 3)
