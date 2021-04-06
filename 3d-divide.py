# 3d division surface between two clusters of points.
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
import numpy as np

def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

# Make data.
X = np.arange(-5, 5, 1)
Y = np.arange(-5, 5, 1)
X, Y = np.meshgrid(X, Y)
Z = np.random.uniform(low = -0.05, high = 0.05, size = (10,10))

# Plot the surface.
# surf = ax.plot_wireframe(X, Y, Z,
surf = ax.plot_surface(X, Y, Z,
                       color = "grey",
                       label = "Divide Surf",
                       antialiased=True
                      )

# Plot the nodes

n = 40

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].

xs = randrange(n, -4, 4)
ys = randrange(n, -4, 4)
zs = randrange(n, -1, 0)
ax.scatter(xs, ys, zs, marker='^', label = "Lower")

xs = randrange(n, -4, 4)
ys = randrange(n, -4, 4)
zs = randrange(n, 0, 1)
ax.scatter(xs, ys, zs, marker='o', label = "Higher")


# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(8))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
surf._facecolors2d=surf._facecolors3d
surf._edgecolors2d=surf._edgecolors3d

# Change the legend sequence
handles,labels = ax.get_legend_handles_labels()
handles = [handles[2], handles[0], handles[1]]
labels = [labels[2], labels[0], labels[1]]
plt.legend(handles, labels)

plt.tight_layout()
# ax.view_init(60, 35)
# ax.plot()
# plt.savefig('3dcluster.svg', format='svg', bbox_inches='tight')
# plt.savefig('3dcluster.pdf', format='pdf', bbox_inches='tight')
plt.show()