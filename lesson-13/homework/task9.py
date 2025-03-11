import numpy as np

# Create two random 3x3 matrices
A = np.random.rand(3, 3)
B = np.random.rand(3, 3)

# Compute the dot product
dot_product = np.dot(A, B)  # or A @ B

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nDot Product (A · B):\n", dot_product)
