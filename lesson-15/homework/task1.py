import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**2 - 4*x + 4

# Generate x values
x = np.linspace(-10, 10, 400)
y = f(x)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$f(x) = x^2 - 4x + 4$', color='blue')

# Customize the plot
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of $f(x) = x^2 - 4x + 4$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

plt.show()
