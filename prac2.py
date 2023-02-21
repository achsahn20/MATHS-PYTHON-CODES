#Generate the matrix into echelon form and find its rank.
import numpy as np
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

rref, pivots = np.linalg.eigh(np.dot(A.T, A))
rank = len(np.where(abs(rref) > 1e-8)[0])

print("Echelon Form of the Matrix:\n", rref)
print("Rank of the Matrix:", rank)
