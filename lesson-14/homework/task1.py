import numpy as np


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


vectorized_conversion = np.vectorize(fahrenheit_to_celsius)

fahrenheit_temps = np.array([32, 68, 100, 212, 77])

celsius_temps = vectorized_conversion(fahrenheit_temps)

print("Fahrenheit:", fahrenheit_temps)
print("Celsius:", celsius_temps)
