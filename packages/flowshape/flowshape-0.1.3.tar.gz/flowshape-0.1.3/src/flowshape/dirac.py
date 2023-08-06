"""Everything that deals with quaternions and the Dirac reconstruction.
"""
import numpy as np
import scipy
import igl
from scipy.spatial.transform import Rotation as R
import time

from scipy.sparse.linalg import spsolve
from numpy.linalg import norm

# basic quaternion operations
def norm2(q):
    """Calculates the L2 norm of the quaternion q.

    Args:
        q (ndarray): Quaternion as a 4x4 array

    Returns:
        float: L2 norm
    """
    return np.matmul(q.T, q)[0, 0]


def quatAsMatrix(q):
    """Convert array quaternion to its matrix representation.

    Args:
        q (ndarray): Array of length 4 representing a quaternion as q[0] + q[1]i + q[2]j + q[3]k.

    Returns:
        ndarray: 4x4 matrix.
    """
    a = q[0]
    b = q[1]
    c = q[2]
    d = q[3]
    return np.array(
        [
            [a, -b, -c, -d],
            [b, a, -d, c],
            [c, d, a, -b],
            [d, -c, b, a],
        ]
    )


def quatFromVector(v):
    """Imaginary quaternion from vector in R^3.

    Args:
        v (ndarray): Array of length 3 representing a 3D vector.

    Returns:
        ndarray: Array of length 4 representing a quaternion as q[0] + q[1]i + q[2]j + q[3]k.
    """
    return np.array([0, v[0], v[1], v[2]])


def quatFromScalar(a):
    """Make quaternion from a single scalar.

    Args:
        a (float): Scalar value

    Returns:
        ndarray: Array representing quaterion with scalar part equal to a.
    """
    return np.array([a, 0, 0, 0])


def quatFromRot(r):
    """Convert Rotation instance to quaternion.

    Args:
        r (Rotation): Scipy Rotation instance.

    Returns:
        ndarray: Quaternion representation of the input rotation.
    """
    v = r.as_quat()
    a = v[3]
    b = v[0]
    c = v[1]
    d = v[2]

    return np.array([a, b, c, d])


def hyper_edges(verts, faces):
    """Construct list of hyper-edges. Each edge is a quaternion.
    The vector part is the oriented edge vector.
    The scalar part is 2 times the integrated mean curvature along the edge.

    calculation:
    H = 1/2 * |e| * tan(theta / 2)
    where theta is the angle between normals
    using tan half angle:
    tan(theta / 2) = sin(theta) / (1 + cos(theta))

    Args:
        verts (ndarray): #v by 3 array of mesh vertex positions
        faces (ndarray): #f by 3 array of mesh face indices into verts

    Returns:
        ndarray: Array of quaternions, ordered as edges. Each quaternion is in its matrix representation.
    """
    h = np.zeros(faces.shape[0])

    normals = igl.per_face_normals(verts, faces, np.array([1.0, 0.0, 0.0]))

    ev, fe, ef = igl.edge_topology(verts, faces)

    edge = verts[ev[:, 1]] - verts[ev[:, 0]]

    i = ef[:, 0]
    j = ef[:, 1]

    ni = normals[i]
    nj = normals[j]

    # half angle tangent formula
    # per edge, calculate:
    # (ni x nj) * e / (1.0 + ni * nj)
    tan = np.sum((np.cross(ni, nj)) * edge, axis=1) / (1.0 + np.sum(ni * nj, axis=1))

    # build quaternion array
    he = np.concatenate((tan[:, np.newaxis], edge), axis=1)

    return np.array([quatAsMatrix(v) for v in he])


# unvectorized code for reference
def _hyper_edges_unvectorized(verts, faces):
    h = np.zeros(faces.shape[0])

    normals = igl.per_face_normals(verts, faces, np.array([1.0, 0.0, 0.0]))

    ev, fe, ef = igl.edge_topology(verts, faces)

    he = np.zeros((ef.shape[0], 4))

    for k, e in enumerate(ef):
        edge = verts[ev[k, 1]] - verts[ev[k, 0]]
        i = e[0]
        j = e[1]

        ni = normals[i]
        nj = normals[j]

        # half angle tangent formula
        tan = (np.cross(ni, nj).dot(edge)) / (1 + ni.dot(nj))

        he[k] = np.array([tan, edge[0], edge[1], edge[2]])

    return np.array([quatAsMatrix(v) for v in he])


def dirac(verts, faces, rho):
    """Sparse matrix constructor for intrinsic dirac operator.
    It is a quaternionic operator, so the construction uses 4x4 blocks.

    D = (dirac - rho)

    Args:
        verts (ndarray): #v by 3 array of mesh vertex positions
        faces (ndarray): #f by 3 array of mesh face indices into verts
        rho (ndarray): #f by 1 array of scalar rho (= mean curvature density)

    Returns:
        sparse.csc_matrix: Sparse matrix representation of intrinsic dirac operator.
    """
    h_edges = hyper_edges(verts, faces)
    h_edges *= 0.5

    ev, fe, ef = igl.edge_topology(verts, faces)

    nV = verts.shape[0]
    nF = faces.shape[0]
    nE = ev.shape[0]

    # total number of entries is
    # 2*#edges (dirac)
    # + #faces (rho)
    s = 2 * nE + nF
    data = np.zeros((s, 16))
    roff = np.zeros((s), dtype=int)
    coff = np.zeros((s), dtype=int)

    # dirac construction
    for k, e in enumerate(ef):
        h = h_edges[k]

        # E[e[0],e[1]] += h
        # E[e[1],e[0]] += h.T
        ind = k * 2

        data[ind] = h.flatten()
        data[ind + 1] = h.T.flatten()

        roff[ind] = e[0]
        roff[ind + 1] = e[1]

        coff[ind] = e[1]
        coff[ind + 1] = e[0]

    M = 0.5 * igl.doublearea(verts, faces)

    # subtract rho on the diagonal
    # since rho is a scalar, the blocks are 4x4 identity matrices scaled by rho
    for k, r in enumerate(rho):
        # E[k,k] -= M[k]*r*np.eye(4,4)
        entry = -M[k] * r * np.eye(4, 4)
        ind = nE * 2 + k

        data[ind] = entry.flatten()
        roff[ind] = k
        coff[ind] = k

    # E = E.swapaxes(1,2).reshape((nF*4,nF*4))
    # return scipy.sparse.csc_matrix(E)

    # construct indices for coo_matrix
    rows, cols = np.indices((4, 4))

    rows = rows.flatten()
    cols = cols.flatten()

    row = np.repeat(4 * roff, 16) + np.tile(rows, s)
    col = np.repeat(4 * coff, 16) + np.tile(cols, s)

    data = data.flatten()

    return scipy.sparse.coo_matrix((data, (row, col))).tocsc()


def normalize_quat(vec):
    """Normalize list of quaternions so theyhave unit length on average.

    Args:
        vec (ndarray): Flat list of quaternions.

    Returns:
        ndarray: Flat list of normalized quaternions.
    """
    nr = vec.shape[0] / 4

    norm = np.sum(vec**2) / nr
    norm = np.sqrt(norm)

    # print(1 / norm)
    return vec / norm


def vertToFaceQuat(verts, faces):
    """Vertex to face incidence matrix.
    Same as vertToFace except it is constructed with 4x4 identity submatrices so it works with quaternion matrices.

    Args:
        verts (ndarray): #v by 3 array of mesh vertex positions
        faces (ndarray): #f by 3 array of mesh face indices into verts

    Returns:
        sparse.csc_matrix: 4*#f by 4*#v sparse adjacency matrix.
    """
    A = scipy.sparse.lil_matrix((faces.shape[0] * 4, verts.shape[0] * 4))

    for k, f in enumerate(faces):
        for i in range(3):
            A[k * 4, f[i] * 4] = 1.0
            A[k * 4 + 1, f[i] * 4 + 1] = 1.0
            A[k * 4 + 2, f[i] * 4 + 2] = 1.0
            A[k * 4 + 3, f[i] * 4 + 3] = 1.0

    return A.tocsc()


def vertToFace(verts, faces):
    """Regular vertex to face incidence matrix.

    Args:
        verts (ndarray): #v by 3 array of mesh vertex positions
        faces (ndarray): #f by 3 array of mesh face indices into verts

    Returns:
        sparse.csc_matrix: #f by #v sparse adjacency matrix.
    """
    A = scipy.sparse.lil_matrix((faces.shape[0], verts.shape[0]))

    for k, f in enumerate(faces):
        for i in range(3):
            A[k, f[i]] = 1.0

    return A.tocsc()


def eigSolve(verts, faces, D, A=None, solver="LU"):
    """Inverse power iteration to solve for smallest eigenvalue of the Dirac operator.

    Args:
        verts (ndarray): #v by 3 array of mesh vertex positions
        faces (ndarray): #f by 3 array of mesh face indices into verts
        D (ndarray): Dirac operator matrix
        A (ndarray, optional): vertToFaceQuat matrix, for efficiency since it can be reused between iterations.
            When not provided it will be calculated.
        solver (str, optional):
            "LU": 3 iterations with LU decomposition (slow but accurate, default)
            "CG": 3 iterations with the conjugate gradient method
                            (fast but can be inaccurate, only recommended for large meshes after testing results against LU)
            "eigsh": Solve eigenvalue with Scipy sparse eigsh. Accurate, but slow for large problems.

    Returns:
        ndarray: Flat array of quaternions that approximate the smallest eigenvalue of D.
    """
    # this is here so we can reuse the vertToFaceQuat matrix,
    # which only depends on the topology
    if A is None:
        A = vertToFaceQuat(verts, faces)

    # mass matrix, repeated in 4x4 blocks
    M = igl.massmatrix(verts, faces, igl.MASSMATRIX_TYPE_BARYCENTRIC)
    M = M.diagonal()
    M = np.repeat(M, 4)
    M = scipy.sparse.diags(M)

    # initial guess is identity
    b = np.array([[1, 0, 0, 0] for v in verts])
    b = b.flatten()

    A_T = A.transpose().tocsc()
    D_s = A_T.dot(D.dot(D.dot(A)))

    # solve by LU decomposition
    if solver == "LU":
        # fixed number of iterations
        itr = 10

        # prefactor solver
        D_solver = scipy.sparse.linalg.factorized(D_s)

        # power iteration loop
        for i in range(itr):
            x = D_solver(M.dot(b))

            b = normalize_quat(x)

    # fast approximate conjugate gradient solver
    elif solver == "CG":
        # fixed number of iterations
        itr = 3

        for i in range(itr):
            x = scipy.sparse.linalg.cg(D_s, M.dot(b))[0]
            b = normalize_quat(x)

    elif solver == "eigsh":
        sol = scipy.sparse.linalg.eigsh(D_s, k=1, v0=b, which="SM", M=M)
        b = sol[1]
        b = normalize_quat(b)

    return A.dot(b)


def reconstruct_lsqr(verts, faces, lamb):
    """Reconstruct vertex positions from quaternion edge vectors by least squares.

    Args:
        verts (ndarray): #v by 3 array of mesh vertex positions
        faces (ndarray): #f by 3 array of mesh face indices into verts
        lamb (ndarray): Flat array of quaternions

    Returns:
        ndarray: #v by 3 array of new mesh vertex positions.
    """

    # convert lambda to matrix representation
    assert lamb.shape[0] == faces.shape[0] * 4

    lamb = lamb.reshape(-1, 4)
    lamb = np.array([quatAsMatrix(q) for q in lamb])

    h_edges = hyper_edges(verts, faces)

    ev, fe, ef = igl.edge_topology(verts, faces)
    edgeMat = scipy.sparse.lil_matrix((ef.shape[0], verts.shape[0]))
    new_edges = np.zeros((ef.shape[0], 3))

    # iterate over all edges to build sparse edge incidence matrix
    for k, e in enumerate(ef):
        # vertex indices corresponding to the edge
        a = ev[k, 0]
        b = ev[k, 1]

        # build directed edge incidence matrix
        edgeMat[k, a] = -1
        edgeMat[k, b] = 1

    edgeMat = edgeMat.tocsc()

    # for each edge, get the two quaternions from the adjacent faces
    lambi = lamb[ef[:, 0]]
    lambj = lamb[ef[:, 1]]

    # E' = lambda_i^conj * E * lambda_j
    # vectorized over arrays of 4*4 matrices
    # standard matrix product einsum is "ij,jk->ik" so on a list of matrices just add an extra index l:
    # "lij,ljk->lik"
    # the conjugate quaternion is made by transposing the matrix representation, so in the einsum the first term becomes lji
    new_edges = np.einsum(
        "lji,ljk->lik", lambi, np.einsum("lij,ljk->lik", h_edges, lambj)
    )

    # extract edge vectors in R^3 from the imaginary part of quaternions
    new_edges = new_edges[:, 1:4, 0]

    # solve for vertex positions in least square sense. the systems are independent in each coordinate
    final0, istop0, itn0, norm0 = scipy.sparse.linalg.lsmr(
        edgeMat, new_edges[:, 0], x0=verts[:, 0]
    )[0:4]
    final1, istop1, itn1, norm1 = scipy.sparse.linalg.lsmr(
        edgeMat, new_edges[:, 1], x0=verts[:, 1]
    )[0:4]
    final2, istop2, itn2, norm2 = scipy.sparse.linalg.lsmr(
        edgeMat, new_edges[:, 2], x0=verts[:, 2]
    )[0:4]

    # print("lsqr rec norm: " + str(np.sqrt(norm0**2 + norm1**2 + norm2**2)))

    return np.vstack((final0, final1, final2)).T


def curvature_density(verts, faces):
    """Mean curvature half-density over each triangle face.

    calculation:
    h = H * |df|
    |df| is discretized as sqrt(A), A the triangle area
    since H is integrated over each triangle we have
    H_int = H * A
    H = H_int / A
    h = H_int / sqrt(A)
    Calculation of H is the same as in hyper_edges.
    The curvature per face is then the sum of the three adjacent edges.

    Args:
        verts (ndarray): #v by 3 array of mesh vertex positions
        faces (ndarray): #f by 3 array of mesh face indices into verts

    Returns:
        ndarray: #f by 1 array of mean curvature half-density scalars.
    """
    h = np.zeros(faces.shape[0])

    normals = igl.per_face_normals(verts, faces, np.array([1.0, 0.0, 0.0]))

    ev, fe, ef = igl.edge_topology(verts, faces)

    edge = verts[ev[:, 1]] - verts[ev[:, 0]]

    i = ef[:, 0]
    j = ef[:, 1]

    ni = normals[i]
    nj = normals[j]

    # half angle tangent formula
    # per edge, calculate:
    # (ni x nj) * e / (1.0 + ni * nj)
    tan = np.sum((np.cross(ni, nj)) * edge, axis=1) / (1.0 + np.sum(ni * nj, axis=1))

    np.add.at(h, i, tan)
    np.add.at(h, j, tan)

    h = h / (2 * np.sqrt(0.5 * igl.doublearea(verts, faces)))

    return h


# unvectorized code for reference
def _curvature_density_unvectorized(verts, faces):
    h = np.zeros(faces.shape[0])

    normals = igl.per_face_normals(verts, faces, np.array([1.0, 0.0, 0.0]))

    ev, fe, ef = igl.edge_topology(verts, faces)

    for k, e in enumerate(ef):
        edge = verts[ev[k][1]] - verts[ev[k][0]]

        i = e[0]
        j = e[1]

        ni = normals[i]
        nj = normals[j]

        # half angle tangent formula
        tan = (np.cross(ni, nj).dot(edge)) / (1 + ni.dot(nj))

        h[i] += tan
        h[j] += tan

    h = h / (2 * np.sqrt(0.5 * igl.doublearea(verts, faces)))

    return h
