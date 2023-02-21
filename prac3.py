#Find cofactors, determinant, adjoint and inverse of a matrix. 

import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
det = np.linalg.det(A)

C = np.zeros_like(A)
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        submatrix = np.delete(np.delete(A, i, axis=0), j, axis=1)
        C[i, j] = (-1)**(i+j) * np.linalg.det(submatrix)

adj = C.T

if det != 0:
    inv = adj / det
else:
    inv = None

print("Matrix:\n", A)
print("Determinant of the Matrix:", det)
print("Cofactor Matrix:\n", C)
print("Adjoint of the Matrix:\n", adj)
print("Inverse of the Matrix:\n", inv)
