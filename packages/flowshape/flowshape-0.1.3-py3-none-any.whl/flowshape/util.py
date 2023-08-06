"""Utilities
"""
import igl
import numpy as np
import scipy as sp

from .flow import conformal_flow
from .flow import mobius_center
from .flow import project_sphere_center
from .flow import project_sphere
from .fit import normalize_area
from .fit import IRF_scalar
from .dirac import vertToFaceQuat
from .dirac import curvature_density
from .dirac import dirac
from .dirac import eigSolve
from .dirac import reconstruct_lsqr


def sphere_map(v, f):
    """Perform spherical mapping on an input mesh, followed by Mobius centering.

    Args:
        v (ndarray): #v by 3 array of mesh vertex positions
        f (ndarray): #f by 3 array of mesh face indices into verts

    Returns:
        ndarray: #v by 3 array of spherical map mesh vertex positions
    """
    v_sphere = conformal_flow(v, f)
    v_sphere = mobius_center(v, v_sphere, f)
    v_sphere = project_sphere_center(v_sphere, f)
    return v_sphere


def curvature_function(v_orig, v_sphere, f):
    """Compute the mean curvature function rho of the mesh (v_orig, f), with area distortion term relative to (v_sphere, f).
    This returns a scalar function on the faces of the mesh.

    Args:
        v_orig (ndarray): #v by 3 array of original mesh vertex positions
        v_sphere (ndarray): #v by 3 array of spherical mesh vertex positions
        f (ndarray): #f by 3 array of mesh face indices into verts

    Returns:
        ndarray: #f by 1 array of curvature function.
    """
    h = curvature_density(v_orig, f)
    A = 0.5 * igl.doublearea(v_sphere, f)
    rho = h / np.sqrt(A)
    return rho


def do_mapping(v, f, l_max=24):
    """Utility function to do the spherical mapping and Spherical Harmonics decomposition in one go.

    Args:
        v (ndarray): #v by 3 array of mesh vertex positions
        f (ndarray): #f by 3 array of mesh face indices into verts
        l_max (int, optional): Max degree of SH to fit. Default = 24.

    Returns:
        weights, Y_mat, v_sphere:
            weights = flat array of SH weights,
            Y_mat = matrix used in fitting procedure (useful for calculating the inverse),
            v_sphere = #v by 3 array of spherical map mesh vertex positions
    """
    v_sphere = sphere_map(v, f)

    rho = curvature_function(v, v_sphere, f)

    v_bary = igl.barycenter(v_sphere, f)
    v_bary = project_sphere(v_bary)
    W = 0.5 * igl.doublearea(v_sphere, f)
    W = sp.sparse.diags(W)
    weights, Y_mat = IRF_scalar(rho, v_bary, W, max_degree=l_max)

    return weights, Y_mat, v_sphere


def reconstruct_shape(v, f, rho, mobius=False):
    """Reconstruct the shape from a spherical mesh (v, f), given curvature function rho.

    Args:
        v (ndarray): #v by 3 array of spherical vertex positions
        f (ndarray): #f by 3 array of mesh face indices into verts
        rho (ndarray): #f by 1, curvature function
        mobius (bool, optional): Optionally do Mobius centering on the output mesh. May give better results for low quality meshes.

    Returns:
        ndarray: #v by 3 array of reconstructed vertex postions.
    """
    nit = 3

    A1 = 0.5 * igl.doublearea(v, f)

    final = v.copy()

    h_target = rho * np.sqrt(A1)

    vert_face = vertToFaceQuat(final, f)

    for k in range(nit):
        A2 = 0.5 * igl.doublearea(final, f)

        rho_new = h_target / np.sqrt(A2)

        rho_current = curvature_density(final, f) / np.sqrt(A2)

        ww = 0.5 + 0.5 * ((k + 1) / nit)

        D = dirac(final, f, ww * rho_new)
        lamb = eigSolve(final, f, D, A=vert_face, solver="LU")
        final = reconstruct_lsqr(final, f, lamb)
        final = normalize_area(final, f)

    if mobius:
        final = mobius_center2(v, final, f)

    return final


def build_filter_gaussian(k, l_max=24):
    """Build a Gaussian filter."""
    ww = np.zeros(l_max**2)
    for l in range(0, l_max):
        i = int(l) ** 2
        i2 = int(l + 1) ** 2

        ww[i:i2] = np.exp(-k * l * (l + 1))
    return ww


def build_filter_log(k, l_max=24):
    """Build a Laplacian of Gaussian filter."""
    ww = np.zeros(l_max**2)
    for l in range(0, l_max):
        i = int(l) ** 2
        i2 = int(l + 1) ** 2

        ww[i:i2] = np.exp(1 - k * l * (l + 1)) * k * l * (l + 1)
    return ww
