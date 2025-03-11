import numpy as np

# Create a 5x5 random matrix
random_matrix = np.random.rand(5, 5)

# Normalize the matrix
min_val = np.min(random_matrix)
max_val = np.max(random_matrix)
normalized_matrix = (random_matrix - min_val) / (max_val - min_val)

print("Original Matrix:\n", random_matrix)
print("\nNormalized Matrix:\n", normalized_matrix)
