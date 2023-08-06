"""Utilities for fitting SH 
"""
import igl
import numpy as np
import scipy as sp

from scipy.sparse.linalg import spsolve
from scipy.special import sph_harm
from numpy.linalg import norm


def get_area(verts, faces):
    """Get the total surface area of a mesh.

    Args:
        verts (ndarray): #v by 3 array of mesh vertex positions
        faces (ndarray): #f by 3 array of mesh face indices into verts

    Returns:
        float: Total area
    """
    return 0.5 * np.sum(igl.doublearea(verts, faces))


def normalize_area(verts, faces, M=None, return_transformation=False):
    """Normalize the mesh. Translate so that the origin is at the center of mass.
    Scale so that total area equals 4*pi, the area of a unit sphere.

    Args:
        verts (ndarray): #v by 3 array of mesh vertex positions
        faces (ndarray): #f by 3 array of mesh face indices into verts
        M (optional): mass matrix. When not given it will be calculated from the mesh.
        return_transformation (bool, optional): Return scale and translation applied. default: False

    Returns:
        ndarray: #v by 3 array of new vertex positions
        float (optional): scale
        ndarray (optional): Coordinates of the translation vector (3,)
    """
    if M is None:
        M = igl.massmatrix(verts, faces, igl.MASSMATRIX_TYPE_BARYCENTRIC)
    A = get_area(verts, faces)

    v_w = M.dot(verts)

    centroid = np.sum(v_w, axis=0) / A
    verts -= centroid

    scaling = np.sqrt(A / (np.pi * 4))

    verts /= scaling

    if return_transformation:
        return verts, scaling, centroid
    else:
        return verts


def project_sphere(verts):
    """Make all vectors unit norm without any recentering.
    Equivalent to projecting to a unit sphere centered at the origin.

    Args:
        verts (ndarray): #v by 3 array of vertex positions

    Returns:
        ndarray: #v by 3 array of normalized vertex positions
    """
    return np.divide(verts, norm(verts, axis=1).reshape((-1, 1)))


def sph_real(l, m, phi, theta):
    """Evaluate real spherical harmonics on an array of spherical coordinates.

    Args:
        l (int): Degree of the harmonic. Must have l >= 0.
        m (int): Order of the harmonic. Must have |m| <= l.
        phi (ndarray): Array of azimuthal (longitudinal) coordinates. Must be in [0, 2*pi].
        theta (ndarray): Array of polar (colatitudinal) coordinates. Must be in [0, pi].

    Returns:
        ndarray: real spherical harmonics sampled at theta and phi.
    """
    scale = 1
    if m != 0:
        scale = np.sqrt(2)
    if m >= 0:
        return scale * sph_harm(m, l, phi, theta).real
    else:
        return scale * sph_harm(abs(m), l, phi, theta).imag


def get_Y_mat(verts, max_degree=16):
    """Build the matrix of spherical harmonics evaluated on a spherical mesh.

    Args:
        verts (ndarray): #v by 3 array of mesh vertex positions
        max_degree (int, optional): max degree of SH

    Returns:
        ndarray: matrix containing spherical harmonics evaluated on each vertex
    """
    theta = np.arccos(verts[:, 2])
    phi = np.arctan2(verts[:, 1], verts[:, 0])

    Y_mat = []

    for l in range(0, max_degree):
        for m in range(-l, l + 1):
            y = sph_real(l, m, phi, theta)
            Y_mat.append(y)

    Y_mat = np.vstack(Y_mat).T

    return Y_mat


def IRF_vector(orig_v, verts, faces, max_degree=16):
    """Iterated residual fitting for vertex positions as coordinate functions.

    Args:
        orig_v (ndarray): n by 3 array of original mesh vertex positions to be fitted
        verts (ndarray): #v by 3 array of spherical mesh vertex positions
        faces (ndarray): #f by 3 array of spherical mesh face indices into verts
        max_degree (int, optional): max degree of SH to fit

    Returns:
        ndarray: matrix of the three SH weight vectors
        ndarray: matrix containing spherical harmonics evaluated on each vertex
    """
    num_harm = max_degree**2
    # orig_v = normalize_area(orig_v, faces)

    # weighted least squares with mass matrix to account for unequal mesh resolution.
    W = igl.massmatrix(verts, faces, igl.MASSMATRIX_TYPE_BARYCENTRIC)

    Y_full = get_Y_mat(verts, max_degree=max_degree)

    weights = np.zeros((num_harm, 3))

    residual = np.copy(orig_v)

    for it in range(10):
        # print(it, np.average(residual ** 2))
        for l in range(0, max_degree):
            i1 = l**2
            i2 = (l + 1) ** 2

            Y = Y_full[:, i1:i2]

            # w = np.linalg.solve(Y.T.dot(Y), Y.T.dot(residual))
            w = np.linalg.solve(Y.T.dot(W.dot(Y)), Y.T.dot(W.dot(residual)))

            residual = residual - Y.dot(w)

            weights[i1:i2] += w

    return weights, Y_full


def IRF_scalar(f, verts, W, max_degree=16):
    """Iterated residual fitting for a scalar function

    Args:
        f (ndarray): #v by 1 array of function values to fit
        verts (ndarray): #v by 3 array of spherical mesh vertex positions
        W (ndarray): mass matrix, used as weights for the least squares
        max_degree (int, optional): maximum degree of spherical harmonics

    Returns:
        ndarray: flat SH weight vector
        ndarray: matrix containing spherical harmonics evaluated on each vertex
    """
    num_harm = max_degree**2

    Y_full = get_Y_mat(verts, max_degree=max_degree)

    weights = np.zeros(num_harm)
    residual = np.copy(f)

    err = 0
    for it in range(10):
        newerr = np.average(residual**2, weights=W.diagonal())
        diff = np.abs(err - newerr)
        err = newerr
        # print(it, diff, err)

        if diff < 1e-10:
            break

        for l in range(0, max_degree):
            i1 = l**2
            i2 = (l + 1) ** 2

            Y = Y_full[:, i1:i2]

            # w = np.linalg.solve(Y.T.dot(Y),Y.T.dot(residual))
            w = np.linalg.solve(Y.T.dot(W.dot(Y)), Y.T.dot(W.dot(residual)))

            residual = residual - Y.dot(w)

            weights[i1:i2] += w

    return weights, Y_full


def fit_regularized(f, verts, W, k, max_degree=16):
    """Alternative way to fit a scalar function using L2 smoothness regularization.
    The penalty is k |nabla f|^2, or k (l*(l+1))^2 for each SH degree.

    Args:
        f (ndarray): #v by 1 array of function values to fit
        verts (ndarray): #v by 3 array of spherical mesh vertex positions
        W (ndarray): mass matrix, used as weights for the least squares
        k (ndarray): regularization constant
        max_degree (int, optional): maximum degree of spherical harmonics to fit

    Returns:
        ndarray: flat SH weight vector
        ndarray: matrix containing spherical harmonics evaluated on each vertex
    """
    num_harm = max_degree**2

    Y_full = get_Y_mat(verts, max_degree=max_degree)

    weights = np.zeros(num_harm)

    k_factor = np.zeros(num_harm)
    for l in range(0, max_degree):
        i1 = l**2
        i2 = (l + 1) ** 2

        k_factor[i1:i2] = (l * (l + 1)) ** 2

    weights = np.linalg.solve(
        Y_full.T @ W @ Y_full + k * np.diag(k_factor), Y_full.T @ (W @ f)
    )

    return weights, Y_full


def power_spectrum(w):
    """Calculate the power spectrum, which is the sum of squares for each degree of SH.

    Args:
        w (ndarray): flat vector of SH coefficients

    Returns:
        ndarray: Flat vector of spectral power
    """

    squared = w**2

    max_degree = int(np.sqrt(w.shape[0]))
    spectrum = np.zeros(max_degree)
    for l in range(0, max_degree):
        i1 = l**2
        i2 = (l + 1) ** 2
        spectrum[l] = np.sum(squared[i1:i2])

    return spectrum


def get_quadrature_weights(verts, max_degree=12):
    """Get vertex weights such that the spherical harmonics up to degree max_degree integrate exactly.
    This can becomes unstable if the number of coefficients is close to the number of vertices.
    In practice it is recommended to just use vertex areas as weights.

    Args:
        verts (ndarray): #v by 3 array of mesh vertex positions
        max_degree (int, optional): maximum degree to fit

    Returns:
        ndarray: array of vertex weights
    """
    Y_mat = get_Y_mat(verts, max_degree=max_degree)

    Y_inv = sp.linalg.pinv(Y_mat)
    q_weights = Y_inv[0] * (2 * np.sqrt(np.pi))

    cond = np.linalg.cond(Y_mat)
    if cond > 100:
        print("Warning: Large condition number of Y matrix.")
        print("Condition number = " + str(cond))

    if np.any(q_weights < 0):
        print("Warning: get_quadrature_weights produced negative weights.")

    return q_weights


def canonical_rotation(orig_v, verts, faces):
    """Canonical rotation based on first order ellipsoid representation. Unstable to 180 degree rotations.
    This method is generally not a good way to align surfaces.

    Args:
        orig_v (ndarray): #v by 3 array of original vertex positions
        verts (ndarray): #v by 3 array of spherical vertex positions
        faces (ndarray): #f by 3 array of mesh face indices into verts. orig_v and verts must share the same topology defined by faces.

    Returns:
        ndarray: Rotated original vertex positions
        ndarray: Rotated spherical vertex positions
    """
    weights, A = IRF_vector(orig_v, verts, faces, 3)

    Q = np.vstack([-weights[3], -weights[1], weights[2]]).T

    u, s, vh = np.linalg.svd(Q)

    # product here is reversed because the verts are row vectors (ie: A * v -> v^T * A^T)
    orig_v = orig_v.dot(u)
    verts = verts.dot(vh.T)

    # project to sphere again because of numerical issues w rotation
    verts = project_sphere(verts)

    # pi rotations: yz, xz, xy
    rx = np.diag([1, -1, -1])
    ry = np.diag([-1, 1, -1])
    rz = np.diag([-1, -1, 1])

    M = igl.massmatrix(orig_v, faces, igl.MASSMATRIX_TYPE_BARYCENTRIC)

    # this is kind of a hack to get rid of the symmetry
    weights, A = IRF_vector(orig_v, verts, faces, 8)
    weights_x, A_x = IRF_vector(orig_v.dot(rx), verts.dot(rx), faces, 8)
    weights_y, A_y = IRF_vector(orig_v.dot(ry), verts.dot(ry), faces, 8)
    weights_z, A_z = IRF_vector(orig_v.dot(rz), verts.dot(rz), faces, 8)

    ## calculate center of mass for each
    l = [
        np.sum(np.sum(M.dot(A.dot(weights)), axis=0)),
        np.sum(np.sum(M.dot(A_x.dot(weights_x)), axis=0)),
        np.sum(np.sum(M.dot(A_y.dot(weights_y)), axis=0)),
        np.sum(np.sum(M.dot(A_z.dot(weights_z)), axis=0)),
    ]

    ind = l.index(max(l))

    if ind == 0:
        return orig_v, verts
    elif ind == 1:
        return orig_v.dot(rx), verts.dot(rx)
    elif ind == 2:
        return orig_v.dot(ry), verts.dot(ry)
    elif ind == 3:
        return orig_v.dot(rz), verts.dot(rz)
