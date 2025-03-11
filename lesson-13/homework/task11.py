import numpy as np

# Create a random 3x3 matrix
matrix = np.random.rand(3, 3)

# Compute the determinant
determinant = np.linalg.det(matrix)

print("Matrix:\n", matrix)
print("\nDeterminant:", determinant)
