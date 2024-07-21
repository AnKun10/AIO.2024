from Module2.Week2.model.vector_matrix_operations import compute_vector_length, compute_dot_product, \
    matrix_multi_vector, matrix_multi_matrix, inverse_matrix
import numpy as np

A = np.array([[1, 9, 3], [2, 5, 4], [3, 7, 8]])
print(inverse_matrix(A))
