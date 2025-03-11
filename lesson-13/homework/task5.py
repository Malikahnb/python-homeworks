import numpy as np

random_array = np.random.rand(10, 10)

min_value = np.min(random_array)
max_value = np.max(random_array)

print("Random 10x10 array:\n", random_array)
print("\nMinimum value:", min_value)
print("Maximum value:", max_value)
