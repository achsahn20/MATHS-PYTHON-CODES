#Find the orthonormal basis of a given vector space using the Gram-Schmidt orthogonalization process.
import numpy as np

# Define the original set of vectors
v1 = np.array([1, 1, 1])
v2 = np.array([1, 0, 1])
v3 = np.array([0, 1, 1])
V = np.array([v1, v2, v3])

# Define a function to perform Gram-Schmidt orthogonalization
def gram_schmidt(V):
    # Initialize an empty list to store the orthonormal basis
    Q = []
    for i in range(len(V)):
        # Compute the orthogonal projection of V[i] onto the span of Q
        u = V[i]
        for j in range(len(Q)):
            u = u - np.dot(V[i], Q[j]) * Q[j]
        # Normalize u to obtain a unit vector
        q = u / np.linalg.norm(u)
        # Add q to the orthonormal basis Q
        Q.append(q)
    return np.array(Q)

# Find the orthonormal basis of V using Gram-Schmidt orthogonalization
Q = gram_schmidt(V)

# Print the orthonormal basis
print("Orthonormal basis of V:")
for q in Q:
    print(q)
