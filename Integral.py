import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define boundaries for x, y, z
x = np.linspace(0, 1, 100)  # Boundaries for x: 0 to 1
y = np.linspace(0, 1, 100)  # Boundaries for y: 0 to x^2
z = np.linspace(0, 1, 100)  # Boundaries for z: 0 to y^2

# Create meshgrid
X, Y, Z = np.meshgrid(x, y, z)

# Filter the points to represent the region defined by the inequalities
condition = (Y <= X**2) & (Z <= Y**2)
X = X[condition]
Y = Y[condition]
Z = Z[condition]

# Define a colormap for the points
cmap = 'viridis'

# Plot the points representing the region with color
ax.scatter(X, Y, Z, c=Z, cmap=cmap, alpha=0.8)

# Customize the plot (labels, title, etc.)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('Integral Region Visualization')

# Show the plot
plt.show()
