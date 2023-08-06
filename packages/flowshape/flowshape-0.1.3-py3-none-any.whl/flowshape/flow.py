"""Conformalized mean curvature flow, moebius centering and related functions
"""
import igl
import numpy as np
import scipy as sp
from .fit import normalize_area
from .fit import get_area

from scipy.sparse.linalg import spsolve
from scipy.special import sph_harm
from numpy.linalg import norm


def normalize(verts):
    centroid = np.mean(verts, axis=0)
    verts -= centroid
    radii = norm(verts, axis=1)

    m = np.amax(radii)

    verts /= m
    return verts


def get_error(verts, faces):
    W = igl.massmatrix(verts, faces, igl.MASSMATRIX_TYPE_BARYCENTRIC).diagonal()

    centroid = np.average(verts, axis=0, weights=W)
    verts -= centroid
    radii = norm(verts, axis=1)

    m = np.amax(radii)
    err = (m - np.amin(radii)) / m

    return err


def project_sphere_center(verts, faces):
    W = igl.massmatrix(verts, faces, igl.MASSMATRIX_TYPE_BARYCENTRIC).diagonal()

    centroid = np.average(verts, axis=0, weights=W)
    verts -= centroid

    return np.divide(verts, norm(verts, axis=1).reshape((-1, 1)))


def project_sphere(verts):
    return np.divide(verts, norm(verts, axis=1).reshape((-1, 1)))


def get_flipped_normals(verts, faces):
    normals = igl.per_vertex_normals(verts, faces)
    dot = np.sum(normals * verts, axis=1)
    return sum(dot < 0) / verts.shape[0]


def conformal_flow(verts, faces):
    """Run the conformalized mean curvature flow.

    Args:
        verts (ndarray): #v by 3 array of mesh vertex positions
        faces (ndarray): #f by 3 array of mesh face indices into verts

    Returns:
        ndarray: #v by 3 array of resulting spherical vertex positions
    """
    verts = normalize(np.copy(verts))

    L = igl.cotmatrix(verts, faces)

    # timestep might need to be smaller if  the mesh is very complex/dense
    # this is optimized for meshes with 1000 - 2000 verts
    itrs = 40
    time_step = 0.2

    # values used in thesis
    # itrs = 20
    # time_step = 0.1

    for i in range(itrs):
        verts = normalize(verts)

        M = igl.massmatrix(verts, faces, igl.MASSMATRIX_TYPE_BARYCENTRIC)
        S = M - time_step * L
        b = M.dot(verts)
        verts = spsolve(S, b)

    verts = normalize(verts)

    # err = get_error(verts, faces)
    # print("flow error: " + str(err))

    verts = project_sphere_center(verts, faces)

    flip = get_flipped_normals(verts, faces)
    if flip > 0:
        print("WARNING: percentage of flipped faces: " + str(100 * flip))
    return verts


def compute_jacobian(M, verts):
    """Jacobian used in the moebius balancing."""
    areas = M.diagonal()

    # outer product of verts with themselves
    outer = np.einsum("li, lj -> lij", verts, verts)

    # sum of (I_3 - outer) with areas as weights
    J = np.sum(areas) * np.eye(3) - np.einsum("l, lij -> ij", areas, outer)

    J *= 2
    return J


def _compute_jacobian_unvectorized(M, verts):
    # for reference only
    areas = M.diagonal()
    J = np.zeros((3, 3))
    for i in range(verts.shape[0]):
        J += areas[i] * (np.eye(3) - np.outer(verts[i], verts[i]))

    J *= 2
    return J


# Moebius centering for spherical meshes
def mobius_center(orig_v, verts, faces):
    """Summary

    Args:
        orig_v (TYPE): Description
        verts (TYPE): Description
        faces (TYPE): Description

    Returns:
        TYPE: Description
    """
    M = igl.massmatrix(orig_v, faces, igl.MASSMATRIX_TYPE_BARYCENTRIC)

    for i in range(10):
        # center of mass
        mu = np.sum(M.dot(verts), axis=0)

        err = norm(mu)
        # print("mobius error: " + str(norm(mu)))
        if err < 1e-10:
            break

        # c = -J^-1 * mu
        J = compute_jacobian(M, verts)
        c = -np.linalg.inv(J).dot(mu)

        # compute inversion
        verts = np.divide((verts + c), norm(verts + c, axis=1).reshape((-1, 1)) ** 2)
        verts = (1 - norm(c) ** 2) * verts + c

    return verts


# Moebius centering for general meshes
def mobius_center2(orig_v, verts, faces):
    """Summary

    Args:
        orig_v (TYPE): Description
        verts (TYPE): Description
        faces (TYPE): Description

    Returns:
        TYPE: Description
    """
    M = igl.massmatrix(orig_v, faces, igl.MASSMATRIX_TYPE_BARYCENTRIC)

    # initial step size is 1/2 because we do a double inversion
    step = 0.5

    # center of mass
    mu = np.sum(M.dot(verts), axis=0)
    err = norm(mu)
    # print("mobius error: " + str(norm(mu)))
    if err < 1e-10:
        return verts

    for i in range(20):
        # c = -J^-1 * mu
        J = compute_jacobian(M, verts)
        c = -np.linalg.inv(J).dot(mu)
        c = c * step

        # make sure the norm never exceeds 1
        while norm(c) > 1.0:
            c *= 0.5

        # moebius transforms in general can be expressed as en even number of sphere inversions
        # doing a double inversion avoids flipping the mesh inside out
        new_v = np.copy(verts)
        for k in range(2):
            # compute inversion
            new_v = np.divide(
                (new_v + c), norm(new_v + c, axis=1).reshape((-1, 1)) ** 2
            )
            new_v = (1 - norm(c) ** 2) * new_v + c

        new_v = normalize_area(new_v, faces)

        # center of mass
        mu = np.sum(M.dot(new_v), axis=0)
        new_err = norm(mu)

        if new_err < 1e-10:
            break

        # accept if new error is smaller, otherwise halve the step size
        if new_err < err:
            err = new_err
            verts = new_v
            # print("mobius error: " + str(norm(mu)))
        else:
            step = step * 0.5

    return verts


def area_ratio(orig_v, verts, faces):
    """Ratio of vertex areas between two meshes with the same connectivity.

    Args:
        orig_v (TYPE): Description
        verts (TYPE): Description
        faces (TYPE): Shared face connectivity

    Returns:
        TYPE: Description
    """
    orig_v = normalize_area(orig_v, faces)
    a1 = igl.massmatrix(orig_v, faces, igl.MASSMATRIX_TYPE_BARYCENTRIC).diagonal()
    a2 = igl.massmatrix(verts, faces, igl.MASSMATRIX_TYPE_BARYCENTRIC).diagonal()

    return np.divide(a1, a2)


def dist(w1, w2):
    """Euclidean (L2) distance between two vectors.

    Args:
        w1 (ndarray): First input vector
        w2 (ndarray): Second input vector

    Returns:
        float64: Distance
    """
    return np.sqrt(np.sum((w1 - w2) ** 2))


def corr(w1, w2):
    """Normalized correlation between two vectors.

    Args:
        w1 (ndarray): First input vector
        w2 (ndarray): Second input vector

    Returns:
        float64: Correlation
    """
    return w1.dot(w2) / np.sqrt(w1.dot(w1) * w2.dot(w2))


def conformal_error(vert1, vert2, f):
    """Compute quasi conformal error between two meshes, also known as the Q-value.

    Args:
        vert1 (ndarray): Description
        vert2 (ndarray): Description
        f (ndarray): Description

    Returns:
        ndarray: Description
    """
    Q = np.zeros(shape=f.shape[0])

    for i, tri in enumerate(f):
        A = vert1[tri]
        B = vert2[tri]

        A = A - np.average(A, axis=0)
        B = B - np.average(B, axis=0)

        # edges
        u1 = A[1] - A[0]
        u2 = A[2] - A[0]

        v1 = B[1] - B[0]
        v2 = B[2] - B[0]

        # gram schmidt orthonormal basis
        e1 = u1 / np.sqrt(np.sum(u1**2))
        e2 = u2 - u2.dot(e1) * e1
        e2 = e2 / np.sqrt(np.sum(e2**2))

        f1 = v1 / np.sqrt(np.sum(v1**2))
        f2 = v2 - v2.dot(f1) * f1
        f2 = f2 / np.sqrt(np.sum(f2**2))

        # poject to new basis
        p1 = np.array([u1.dot(e1), u1.dot(e2)])
        p2 = np.array([u2.dot(e1), u2.dot(e2)])

        q1 = np.array([v1.dot(f1), v1.dot(f2)])
        q2 = np.array([v2.dot(f1), v2.dot(f2)])

        # get jacobian matrix
        Ss = q1 * p2[1] - q2 * p1[1]
        St = q2 * p1[0] - q1 * p2[0]

        S = np.vstack([Ss, St])

        # get singular values
        u, s, vt = np.linalg.svd(S)

        Q[i] = s[0] / s[1]

    return Q
