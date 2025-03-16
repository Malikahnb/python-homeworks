import numpy as np
import matplotlib.pyplot as plt

# Generate a random dataset of 1000 values from a normal distribution (mean=0, std=1)
data = np.random.normal(0, 1, 1000)

# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='blue', alpha=0.7)

# Add title and labels
plt.title('Histogram of Random Values from Normal Distribution', fontsize=16)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Frequency', fontsize=14)


plt.grid(axis='y', alpha=0.75)
plt.show()