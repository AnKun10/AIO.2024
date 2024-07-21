import numpy as np


def compute_eigenvalues_eigenvectors(matrix):
    evalue, evect = np.linalg.eig(matrix)
    return evalue, evect
