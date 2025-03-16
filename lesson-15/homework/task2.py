import numpy as np
import matplotlib.pyplot as plt

# Define the x values
x = np.linspace(0, 2*np.pi, 400)

# Compute sine and cosine values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y_sin, label=r'$\sin(x)$', color='blue', linestyle='-', marker='o', markersize=3)
plt.plot(x, y_cos, label=r'$\cos(x)$', color='red', linestyle='--', marker='s', markersize=3)

# Customize the plot
plt.xlabel('x')
plt.ylabel('Function value')
plt.title('Plot of $\sin(x)$ and $\cos(x)$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

plt.show()
