from functools import lru_cache

import numpy as np

from .wigner_d import wigner_d_matrix

from scipy.fftpack import fft2, ifft2, fftshift


def SO3_FFT_synthesize(f_hat):
    """
    Perform the inverse (spectral to spatial) SO(3) Fourier transform.

    :param f_hat: a list of matrices of with shapes [1x1, 3x3, 5x5, ..., 2 L_max + 1 x 2 L_max + 1]
    """
    F = wigner_d_transform_synthesis(f_hat)

    # The rest of the SO(3) FFT is just a standard torus FFT
    F = fftshift(F, axes=(0, 2))
    f = ifft2(F, axes=(0, 2))

    b = len(f_hat)
    return f * (2 * b)**2


def wigner_d_transform_synthesis(f_hat):

    b = len(f_hat)
    d = setup_d_transform(b, L2_normalized=False)

    # Perform the brute-force Wigner-d transform
    # Note: the frequencies where m=-B or n=-B are set to zero,
    # because they are not used in the forward transform either
    # (the forward transform is up to m=-l, l<B
    df_hat = [d[l] * f_hat[l][:, None, :] for l in range(b)]
    F = np.zeros((2 * b, 2 * b, 2 * b), dtype=complex)
    for l in range(b):
        F[b - l:b + l + 1, :, b - l:b + l + 1] += df_hat[l]

    return F


@lru_cache(maxsize=32)
def setup_d_transform(b,
                      L2_normalized=False,
                      field='complex',
                      normalization='quantum',
                      order='centered',
                      condon_shortley='cs'):
    """
    Precompute arrays of samples from the Wigner-d function, for use in the Wigner-d transform.

    Specifically, the samples that are required are:
    d^l_mn(beta_k)
    for:
     l = 0, ..., b - 1
     -l <= m, n <= l
     k = 0, ..., 2b - 1
     (where beta_k = pi (2 b + 1) / 4b)

    This data is returned as a list d indexed by l (of length b),
    where each element of the list is an array d[l] of shape (2l+1, 2b, 2l+1) indexed by (m, k, n)

    In the Wigner-d transform, for each l, we reduce an array d[l] of shape (2l+1, 2b, 2l+1)
     against a data array of the same shape, along the beta axis (axis 1 of length 2b).

    :param b: bandwidth of the transform
    :param L2_normalized: whether to use L2_normalized versions of the Wigner-d functions.
    :param field, normalization, order, condon_shortley: the basis and normalization convention (see irrep_bases.py)
    :return a list d of length b, where d[l] is an array of shape (2l+1, 2b, 2l+1)
    """
    # Compute array of beta values as described in SOFT 2.0 documentation
    beta = np.pi * (2 * np.arange(0, 2 * b) + 1) / (4. * b)

    # For each l=0, ..., b-1, we compute a 3D tensor of shape (2l+1, 2b, 2l+1) for axes (m, beta, n)
    # Together, these indices (l, m, beta, n) identify d^l_mn(beta)
    convention = {
        'field': field,
        'normalization': normalization,
        'order': order,
        'condon_shortley': condon_shortley
    }
    d = [
        np.array([wigner_d_matrix(l, bt, **convention)
                  for bt in beta]).transpose(1, 0, 2) for l in range(b)
    ]

    if L2_normalized:  # TODO: this should be integrated in the normalization spec above, no?
        # The Unitary matrix elements have norm:
        # | U^\lambda_mn |^2 = 1/(2l+1)
        # where the 2-norm is defined in terms of normalized Haar measure.
        # So T = sqrt(2l + 1) U are L2-normalized functions
        d = [d[l] * np.sqrt(2 * l + 1) for l in range(len(d))]

        # We want the L2 normalized functions:
        # d = [d[l] * np.sqrt(l + 0.5) for l in range(len(d))]

    return d
