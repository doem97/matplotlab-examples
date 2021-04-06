# Scatter points onto a 3d Axis
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.array([[-37.530, 3.109, -16.452],
                [40.247, 5.483, -15.209],
                [-31.920, 12.584, -12.916],
                [-32.760, 14.072, -13.749],
                [-37.100, 1.953, -15.720]])

data2 = np.array([[-32.143, 12.990, -13.488],
                [-41.077, 4.651, -15.651], 
                [-34.219, 13.611, -13.090],
                [-33.117, 15.875, -13.738]])


fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:,0], data[:,1], data[:,2], s=300, alpha = 0.6)
ax.scatter(data2[:,0], data2[:,1], data2[:,2], s=300)
ax.view_init(azim=200)
# plt.savefig('test.svg', format = 'svg', bbox_inches = 'tight', transparent = True, pad_inches = 0.01) # Uncomment to save as .svg file

plt.show()