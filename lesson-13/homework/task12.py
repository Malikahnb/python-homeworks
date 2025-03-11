import numpy as np

# Create a 3x4 random matrix A
A = np.random.rand(3, 4)

# Create a 4x3 random matrix B
B = np.random.rand(4, 3)

# Compute the matrix product A · B
product = np.dot(A, B)

print("Matrix A (3x4):\n", A)
print("\nMatrix B (4x3):\n", B)
print("\nMatrix Product (A · B) (3x3):\n", product)
