import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values for each function
x_cubed = np.linspace(-2, 2, 400)
x_sin = np.linspace(-2 * np.pi, 2 * np.pi, 400)
x_exp = np.linspace(0, 2, 400)
x_log = np.linspace(0, 5, 400)

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Top-left: f(x) = x^3
axs[0, 0].plot(x_cubed, x_cubed**3, color='blue')
axs[0, 0].set_title(r'$f(x) = x^3$', fontsize=14)
axs[0, 0].set_xlabel('x', fontsize=12)
axs[0, 0].set_ylabel('f(x)', fontsize=12)

# Top-right: f(x) = sin(x)
axs[0, 1].plot(x_sin, np.sin(x_sin), color='orange')
axs[0, 1].set_title(r'$f(x) = \sin(x)$', fontsize=14)
axs[0, 1].set_xlabel('x', fontsize=12)
axs[0, 1].set_ylabel('f(x)', fontsize=12)

# Bottom-left: f(x) = e^x
axs[1, 0].plot(x_exp, np.exp(x_exp), color='green')
axs[1, 0].set_title(r'$f(x) = e^x$', fontsize=14)
axs[1, 0].set_xlabel('x', fontsize=12)
axs[1, 0].set_ylabel('f(x)', fontsize=12)

# Bottom-right: f(x) = log(x+1)
axs[1, 1].plot(x_log, np.log(x_log + 1), color='red')
axs[1, 1].set_title(r'$f(x) = \log(x+1)$', fontsize=14)
axs[1, 1].set_xlabel('x', fontsize=12)
axs[1, 1].set_ylabel('f(x)', fontsize=12)

# Adjust layout
plt.tight_layout()
plt.show()