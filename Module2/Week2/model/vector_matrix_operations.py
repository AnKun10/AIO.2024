import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector


def compute_dot_product(vector1, vector2):
    return vector1 @ vector2


def matrix_multi_vector(matrix, vector):
    result = matrix.dot(vector)
    return result


def matrix_multi_matrix(matrix1, matrix2):
    result = matrix1.dot(matrix2)
    return result


def __get_minor_element(matrix, row, col):
    minor_matrix = []
    for r in range(len(matrix)):
        if r == row:
            continue
        row_elements = np.array([matrix[r][c] for c in range(len(matrix[r])) if (c != col)])
        minor_matrix.append(row_elements)
    return np.linalg.det(np.array(minor_matrix))


def __get_cofactor_matrix(matrix):
    cofactor_matrix = np.zeros(shape=matrix.shape)
    for r in range(len(cofactor_matrix)):
        for c in range(len(cofactor_matrix[r])):
            cofactor_matrix[r][c] = ((-1) ** (r + c)) * __get_minor_element(matrix, r, c)
    return cofactor_matrix


def inverse_matrix(matrix):
    # Step 1: Determinant of A (matrix)
    det_matrix = np.linalg.det(matrix)

    # Step 2: Evaluate the inverse of A
    if det_matrix == 0 or matrix.shape[0] != matrix.shape[1]:
        return None

    # Step 3: Adjoint of the matrix A
    adj_matrix = __get_cofactor_matrix(matrix).transpose()

    # Step 4: Inverse of A
    result = adj_matrix / det_matrix
    return result
