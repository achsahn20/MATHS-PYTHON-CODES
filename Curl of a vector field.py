#Compute Curl of a vector field.
import numpy as np

# Define the vector field
def vector_field(x, y, z):
    Fx = 2*x*y*z
    Fy = x**2 + z**2
    Fz = y**2 - 2*x*z
    return np.array([Fx, Fy, Fz])

# Define the curl operator
def curl(x, y, z):
    Fx = 2*y
    Fy = -2*z
    Fz = 2*x - 2*y*z
    return np.array([Fx, Fy, Fz])

# Define a point at which to compute the curl
x = 1
y = 2
z = 3

# Compute the curl at the given point
c = curl(x, y, z)

# Print the curl value
print("Curl value:", c)
