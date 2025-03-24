import numpy as np

# Coefficient matrix (A)
A_circuit = np.array([[10, -2, 3],
                      [-2, 8, -1],
                      [3, -1, 6]])

# Constants (B)
B_circuit = np.array([12, -5, 15])

# Solve for [I1, I2, I3]
currents = np.linalg.solve(A_circuit, B_circuit)

print("Solution for I1, I2, I3:", currents)
