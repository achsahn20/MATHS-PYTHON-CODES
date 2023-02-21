#Compute Gradient of a scalar field.
import numpy as np

# Define the scalar field
def scalar_field(x, y, z):
    return x**2 + 2*y**2 + 3*z**2

# Define the gradient operator
def gradient(x, y, z):
    dx = 2*x
    dy = 4*y
    dz = 6*z
    return np.array([dx, dy, dz])

# Define a point at which to compute the gradient
x = 1
y = 2
z = 3

# Compute the gradient at the given point
grad = gradient(x, y, z)

# Print the gradient vector
print("Gradient vector:", grad)
