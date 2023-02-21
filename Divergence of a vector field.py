#Compute Divergence of a vector field.
import numpy as np

# Define the vector field
def vector_field(x, y, z):
    Fx = 2*x*y*z
    Fy = x**2 + z**2
    Fz = y**2 - 2*x*z
    return np.array([Fx, Fy, Fz])

# Define the divergence operator
def divergence(x, y, z):
    Fx = 2*y*z
    Fy = 2*x
    Fz = y - 2*x
    return Fx + Fy + Fz

# Define a point at which to compute the divergence
x = 1
y = 2
z = 3

# Compute the divergence at the given point
div = divergence(x, y, z)

# Print the divergence value
print("Divergence value:", div)
