import numpy as np

# Coefficient matrix (A)
A = np.array([[4, 5, 6],
              [3, -1, 1],
              [2, 1, -2]])

# Constants (B)
B = np.array([7, 4, 5])

# Solve for [x, y, z]
solution = np.linalg.solve(A, B)

print("Solution for x, y, z:", solution)
