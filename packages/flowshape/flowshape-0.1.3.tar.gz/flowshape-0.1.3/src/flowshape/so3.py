"""
Routines for dealing with the rotation group SO(3) and alignment, 
as well as providing an interface to lie_learn.
"""
import igl
import numpy as np
import scipy
from scipy.spatial.transform import Rotation as R

from .lie_learn.SO3.SO3FFT import SO3_FFT_synthesize
from .lie_learn.SO3.irrep_bases import change_of_basis_matrix
from .lie_learn.SO3.pinchon_hoggan_dense import SO3_irrep


def compute_max_correlation(w1, w2, l_max=32, return_corr=False):
    """Compute the rotation that maximizes the correlation between two real spherical harmonic weight vectors,
    using inverse FFT method on the rotation group.
    The iFFT is sampled on a grid of zyz euler angles with resolution
    (2*l_max, 2*l_max, 2*l_max)
    If l_max is larger than the degree of the weights, the array gets zero-padded, which results in a higher grid resolution.

    Args:
        w1 (ndarray): Flat array of weights.
        w2 (ndarray): Flat array of weights.
        l_max (int, optional): maximum SH degree. Zero-padding is used when it is larger than the weight arrays.
        return_corr (bool, optional): also return the matrix of correlations.
    Returns:
        scipy.spatial.transform.Rotation: Scipy Rotation object corresponding to the optimal rotation for the two SH weights.
    """
    assert w1.shape == w2.shape

    # Calculate original correlation.
    # The rotation sampling grid does _not_ include the identity rotation!
    corr_orig = w1.dot(w2)

    l_max_weights = int(np.sqrt(w1.shape[0]))

    assert l_max >= l_max_weights

    # Compute change of basis from real to complex SH.
    r2c = [
        change_of_basis_matrix(
            l,
            frm=("real", "quantum", "centered", "cs"),
            to=("complex", "quantum", "centered", "cs"),
        )
        for l in range(l_max_weights)
    ]

    # Zero fill initial (cf. FFT zero padding to get better resolution)
    f_hat = np.array(
        [np.zeros((2 * ll + 1, 2 * ll + 1)) for ll in range(l_max)], dtype=object
    )

    # Calculate the outer conjugate product of each subspace,
    # and compute the real to complex change of basis:
    #   f_hat = B * (w1 (x) w2) * B^H
    # where B is the change of basis matrix, (x) is outer product.
    for l in range(l_max_weights):
        f_hat[l] = r2c[l].dot(
            np.outer(w1[l**2 : (l + 1) ** 2], w2[l**2 : (l + 1) ** 2]).dot(
                r2c[l].T.conj()
            )
        )

    # Take inverse fourier transform on SO(3).
    res = SO3_FFT_synthesize(f_hat)

    # The correlation function of two real functions is also real.
    assert np.allclose(res.imag, 0)

    res = res.real

    rot, corr_new = get_max(res, l_max=l_max)

    # If we cannot improve then just return identity.
    if corr_orig > corr_new:
        rot = R.identity()

    if return_corr:
        return rot, res

    return rot

# Find maximum correlation in SO(3) grid, using quadratic interpolation, and convert to scipy convention.
def get_max(res, l_max=32):
    corr_new = res.max()

    # Get maximum indices.
    ind = np.unravel_index(res.argmax(), res.shape)

    ind = np.array(ind)

    B = l_max * 2

    # To get the non-integer coordinates, fit a quadratic to neighbors in each dimension and take the location of the maximum.
    m0 = quadmin(
        res[tuple((ind + [-1, 0, 0]) % B)],
        res[tuple(ind)],
        res[tuple((ind + [1, 0, 0]) % B)],
    )

    # Beta doesn't wrap since it ranges from 0 to pi.
    if ind[1] > 0 and ind[1] < B - 1:
        m1 = quadmin(
            res[tuple((ind + [0, -1, 0]))],
            res[tuple(ind)],
            res[tuple((ind + [0, 1, 0]))],
        )
    else:
        m1 = 0

    m2 = quadmin(
        res[tuple((ind + [0, 0, -1]) % B)],
        res[tuple(ind)],
        res[tuple((ind + [0, 0, 1]) % B)],
    )

    ind = ind + [m0, m1, m2]

    # convert grid indices to euler angles
    alpha = 2 * np.pi * ind[0] / res.shape[0]
    beta = np.pi * (2 * ind[1] + 1) / (2 * res.shape[1])
    gamma = 2 * np.pi * ind[2] / res.shape[2]

    # convert array of zyz euler angles to scipy rotation object.
    rot = R.from_euler("zyz", [alpha, beta, gamma])

    return rot, corr_new


def rotate_weights(r, weights):
    """Rotate SH weight vector using Pinchon Hoggan method.
    For efficiency, the full matrix is never stored, only the diagonal block for each degree.

    Args:
        r (scipy.spatial.transform.Rotation): Scipy rotation object to rotate the weights by.
        weights (ndarray): Flat array of real spherical harmonic weights.

    Returns:
        ndarray: Rotated array of real SH weights.
    """

    # Convert to intrinsic euler angles (alpha, beta, gamma)
    # This can result in a gimbal lock warning being printed, but it is safe to ignore since the returned angles are correct.
    g = r.as_euler("ZYZ")
    # There is a sign flip here for unknown reasons (?)
    g[1] = -g[1]

    l_max = int(np.sqrt(weights.shape[0]))

    # Get diagonal blocks from SO3 irreps.
    r_mat = np.array(
        [np.squeeze(SO3_irrep(np.atleast_2d(g).T, l)) for l in range(l_max)],
        dtype=object,
    )

    weights_rot = np.empty(weights.shape)
    # Rotate each degree by the respective block.
    for l in range(l_max):
        weights_rot[l**2 : (l + 1) ** 2] = r_mat[l].dot(
            weights[l**2 : (l + 1) ** 2]
        )

    return weights_rot


# Return max of second degree polynomial fit to data points.
# Used to get FFT maximum in non-integer locations.
def quadmin(a, b, c):
    p = np.polyfit([-1, 0, 1], [a, b, c], 2)
    assert p[0] < 0  # we should have a maximum
    return -p[1] / (2 * p[0])


# @todo: haar measure.
# from the ZYZ representation it should be sin(beta) (or squared?) see:
# https://math.stackexchange.com/questions/3125811/haar-measure-from-axis-angle-representation-of-so3
# https://pure.uva.nl/ws/files/60770359/Thesis.pdf  p. 71
