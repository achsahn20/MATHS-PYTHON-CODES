#Application of Linear algebra: Coding and decoding of messages using nonsingular matrices.
import numpy as np

# Define the message to be encoded
message = "HELLO WORLD"

# Convert the message to a matrix
n = len(message)
m = 3  # Choose the size of the key matrix
message_matrix = np.zeros((m, n))
for i in range(n):
    message_matrix[i % m, i] = ord(message[i])

# Generate a random nonsingular matrix
key_matrix = np.random.rand(m, m)
while np.linalg.det(key_matrix) == 0:
    key_matrix = np.random.rand(m, m)

# Encode the message
encoded_matrix = key_matrix @ message_matrix

# Print the encoded message
print("Encoded message:")
print(encoded_matrix)

# Decode the message
decoded_matrix = np.linalg.inv(key_matrix) @ encoded_matrix
decoded_message = ""
for i in range(n):
    decoded_message += chr(int(decoded_matrix[i % m, i]))

# Print the decoded message
print("Decoded message:")
print(decoded_message)
