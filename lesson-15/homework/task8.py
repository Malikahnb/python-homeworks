import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']
values = np.array([[5, 10, 15, 20],   # Category A
                   [3, 6, 9, 12],    # Category B
                   [2, 4, 6, 8]])    # Category C

# Create a stacked bar chart
plt.figure(figsize=(10, 6))
plt.bar(time_periods, values[0], label='Category A', color='blue')
plt.bar(time_periods, values[1], bottom=values[0], label='Category B', color='orange')
plt.bar(time_periods, values[2], bottom=values[0] + values[1], label='Category C', color='green')

# Add title and labels
plt.title('Stacked Bar Chart of Categories Over Time', fontsize=16)
plt.xlabel('Time Periods', fontsize=14)
plt.ylabel('Values', fontsize=14)

plt.legend(title='Categories')

plt.grid(axis='y', alpha=0.7)
plt.tight_layout()
plt.show()