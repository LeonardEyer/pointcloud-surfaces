import numpy as np


def read_off(file):
    """
    Read OFF Files
    :param file: off file to load
    :return: vertices and faces
    """
    if 'OFF' != file.readline().strip():
        raise Exception('Not a valid OFF header')
    n_verts, n_faces, n_dontknow = tuple([int(s) for s in file.readline().strip().split(' ')])
    verts = np.array([[float(s) for s in file.readline().strip().split(' ')] for i_vert in range(n_verts)])
    faces = np.array([[int(s) for s in file.readline().strip().split(' ')][1:] for i_face in range(n_faces)])
    return verts, faces


def b(x):
    """
    Polynomial basis (quadratic, bivariate)
    :param x: 2d Point
    :return: polynomial at this point
    """
    return np.array([1, x[0], x[1], x[0] ** 2, x[0] * x[1], x[1] ** 2])


def phi(h, d):
    """
    Wendland weighting function
    :param h: this function is defined on interval [0,h]
    :param d: distance
    :return: weight
    """
    d = np.clip(d, 0, h)
    return (1 - d / h) ** 4 * (4 * d / h + 1)


def dist2d(a, b):
    return np.linalg.norm(a[:2] - b[:2])
