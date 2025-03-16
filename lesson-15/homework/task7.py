import matplotlib.pyplot as plt

# Product names and sales data
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

# Create a vertical bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(products, sales, color=['blue', 'orange', 'green', 'red', 'purple'])

# Add title and labels
plt.title('Sales Data for Different Products', fontsize=16)
plt.xlabel('Products', fontsize=14)
plt.ylabel('Sales (Units)', fontsize=14)

# Different bar colors
for bar in bars:
    bar.set_alpha(0.8)

plt.grid(axis='y', alpha=0.7)
plt.show()