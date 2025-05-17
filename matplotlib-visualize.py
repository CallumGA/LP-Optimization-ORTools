'''
Notes:
    Visualize the LP model from pulp-LP.py using matplotlib.
    Plot only x1 and x2, since x3 is 0 in the final solution
'''

import matplotlib.pyplot as plt

# Example data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Create the plot
plt.plot(x, y, marker='o', label='y = x²')

# Add labels and title
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Basic Line Plot')
plt.legend()

# Show the plot
plt.show()