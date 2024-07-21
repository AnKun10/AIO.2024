from Module2.Week2.model.eigenvalues_eigenvectors import compute_eigenvalues_eigenvectors
import numpy as np

A = np.array([[0.9, 0.2], [0.1, 0.8]])
evalue, evect = compute_eigenvalues_eigenvectors(A)
print(evalue)
print(evect)
