import numpy as np

# Create a 5x3 random matrix
A = np.random.rand(5, 3)

# Create a 3x2 random matrix
B = np.random.rand(3, 2)

# Matrix multiplication
result = np.dot(A, B) 

print("Matrix A (5x3):\n", A)
print("\nMatrix B (3x2):\n", B)
print("\nResultant Matrix (5x2):\n", result)
