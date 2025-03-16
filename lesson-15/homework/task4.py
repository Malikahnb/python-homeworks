import numpy as np
import matplotlib.pyplot as plt

# Generate 100 random points from a uniform distribution between 0 and 10
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color=np.random.rand(100, 3), marker='o', s=100, alpha=0.7)

# Add title and labels
plt.title('Scatter Plot of 100 Random Points', fontsize=16)
plt.xlabel('X-axis', fontsize=14)
plt.ylabel('Y-axis', fontsize=14)

plt.grid(True)

plt.show()