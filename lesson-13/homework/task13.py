import numpy as np

# Create a 3x3 random matrix
matrix = np.random.rand(3, 3)

# Create a 3-element column vector (3x1)
vector = np.random.rand(3, 1)

# Compute the matrix-vector product
product = np.dot(matrix, vector) 

print("Matrix (3x3):\n", matrix)
print("\nColumn Vector (3x1):\n", vector)
print("\nMatrix-Vector Product (3x1):\n", product)
