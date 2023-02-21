#Generate basis of column space, null space, row space and left null space of a matrix space.
import numpy as np

# Define the matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Basis of column space
col_space_basis = np.linalg.matrix_rank(A)
col_space_basis = np.linalg.svd(A)[0][:, :col_space_basis]

# Basis of null space
null_space_basis = np.linalg.svd(A)[2][col_space_basis.shape[1]:, :]

# Basis of row space
row_space_basis = col_space_basis.transpose()

# Basis of left null space
left_null_space_basis = np.linalg.svd(A.transpose())[2][row_space_basis.shape[1]:, :]

print("Basis of column space:\n", col_space_basis)
print("Basis of null space:\n", null_space_basis)
print("Basis of row space:\n", row_space_basis)
print("Basis of left null space:\n", left_null_space_basis)
