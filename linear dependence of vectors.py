'''Check the linear dependence of vectors. Generate a linear combination of
given vectors of Rn/ matrices of the same size and find the transition matrix of given matrix space.'''
import numpy as np

# Check linear dependence of vectors
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])

vectors = np.array([v1, v2, v3])

# Compute the rank of the matrix containing the vectors
rank = np.linalg.matrix_rank(vectors)

if rank == len(vectors):
    print("The vectors are linearly independent.")
else:
    print("The vectors are linearly dependent.")

# Generate a linear combination of vectors/matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[9, 10], [11, 12]])

# Generate a random set of coefficients
coefficients = np.random.rand(3)

# Compute the linear combination
linear_combination = coefficients[0] * A + coefficients[1] * B + coefficients[2] * C

print("Linear combination of matrices:")
print(linear_combination)

# Find the transition matrix of a matrix space
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Compute the transition matrix from A to B
transition_matrix = np.linalg.inv(A) @ B

print("Transition matrix from A to B:")
print(transition_matrix)
