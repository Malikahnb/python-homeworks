import numpy as np

# Create a 5x5 random matrix
matrix = np.random.rand(5, 5)

# Compute row-wise sums
row_sums = np.sum(matrix, axis=1)

# Compute column-wise sums
column_sums = np.sum(matrix, axis=0)

print("Matrix (5x5):\n", matrix)
print("\nRow-wise Sums:\n", row_sums)
print("\nColumn-wise Sums:\n", column_sums)
