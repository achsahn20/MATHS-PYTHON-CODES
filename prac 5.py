#Solve a system of Homogeneous equations using the Gauss Jordan method. 
import numpy as np

# Define the system of equations
A = np.array([[2, 3, -1], [4, 7, -3], [-2, -2, 1]])

# Augment the matrix A with the identity matrix
A_aug = np.column_stack((A, np.identity(3)))

# Perform Gauss Jordan elimination
nrows, ncols = A_aug.shape
for i in range(nrows):
    pivot_row = i
    for j in range(i+1, nrows):
        if abs(A_aug[j,i]) > abs(A_aug[pivot_row,i]):
            pivot_row = j
    A_aug[[i, pivot_row]] = A_aug[[pivot_row, i]]
    pivot = A_aug[i,i]
    if pivot != 0:
        A_aug[i] = A_aug[i]/pivot
        for j in range(nrows):
            if j != i:
                factor = A_aug[j,i]
                A_aug[j] -= factor*A_aug[i]

# Extract the solutions
x = A_aug[:,3:]

print(x)
