import numpy as np

from .pinchon_hoggan_dense import Jd, rot_mat
from .irrep_bases import change_of_basis_matrix

def wigner_d_matrix(
    l,
    beta,
    field="real",
    normalization="quantum",
    order="centered",
    condon_shortley="cs",
):
    """
    Compute the Wigner-d matrix of degree l at beta, in the basis defined by
    (field, normalization, order, condon_shortley)

    The Wigner-d matrix of degree l has shape (2l + 1) x (2l + 1).

    :param l: the degree of the Wigner-d function. l >= 0
    :param beta: the argument. 0 <= beta <= pi
    :param field: 'real' or 'complex'
    :param normalization: 'quantum', 'seismology', 'geodesy' or 'nfft'
    :param order: 'centered' or 'block'
    :param condon_shortley: 'cs' or 'nocs'
    :return: d^l_mn(beta) in the chosen basis
    """
    # This returns the d matrix in the (real, quantum-normalized, centered, cs) convention
    d = rot_mat(alpha=0.0, beta=beta, gamma=0.0, l=l, J=Jd[l])

    if (field, normalization, order, condon_shortley) != (
        "real",
        "quantum",
        "centered",
        "cs",
    ):
        # TODO use change of basis function instead of matrix?
        B = change_of_basis_matrix(
            l,
            frm=("real", "quantum", "centered", "cs"),
            to=(field, normalization, order, condon_shortley),
        )
        BB = change_of_basis_matrix(
            l,
            frm=(field, normalization, order, condon_shortley),
            to=("real", "quantum", "centered", "cs"),
        )
        d = B.dot(d).dot(BB)

        # The Wigner-d matrices are always real, even in the complex basis
        # (I tested this numerically, and have seen it in several texts)
        # assert np.isclose(np.sum(np.abs(d.imag)), 0.0)
        d = d.real

    return d
