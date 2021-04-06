# 2d-gaussian plot in 2d and 3d
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from sklearn.datasets.samples_generator import make_blobs

n_components = 1
X, truth = make_blobs(n_samples=200, centers=n_components, 
                      cluster_std = [1.5], 
                      random_state=24)
x = X[:, 0]
y = X[:, 1]
# Define the borders
deltaX = (max(x) - min(x))/10
deltaY = (max(y) - min(y))/10
xmin = min(x) - deltaX
xmax = max(x) + deltaX
ymin = min(y) - deltaY
ymax = max(y) + deltaY
# print(xmin, xmax, ymin, ymax)
# Create meshgrid
xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([xx.ravel(), yy.ravel()])
values = np.vstack([x, y])
kernel = st.gaussian_kde(values)
f = np.reshape(kernel(positions).T, xx.shape)
fig = plt.figure(
    figsize=(8,8)
)
ax = fig.gca()
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
cfset = ax.contourf(xx, 
                    yy, 
                    f, 
                    cmap='rainbow'
                   )
ax.imshow(np.rot90(f),
#           cmap='gnuplot2',
#           alpha = 0.2,
          extent=[xmin, xmax, ymin, ymax])
cset = ax.contour(xx, yy, f, colors='k')
ax.clabel(cset, inline=1, fontsize=8)
plt.savefig('gaussian2d.pdf',
#             bbox_inches='tight'
           )
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# plt.title('2D Gaussian Kernel density estimation')
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = plt.axes(projection='3d')
surf = ax.plot_surface(xx, yy, f, rstride=1, cstride=1, cmap='rainbow', edgecolor='none')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('PDF')
# ax.set_title('Surface plot of Gaussian 2D KDE')
fig.colorbar(surf, shrink=0.6, aspect=15) # add color bar indicating the PDF
plt.savefig('gaussian3d.pdf',bbox_inches='tight')
plt.show()