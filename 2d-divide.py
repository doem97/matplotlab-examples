# Plot two clusters of 2d points with transparency, and draw a division line between them.
import numpy as np
import matplotlib.pyplot as plt

N = 30
dataa = {'a': np.random.uniform(low=0, high=0.5, size=N),
        'b': np.random.uniform(low=0, high=0.5, size=N),
        'd': np.random.rand(N) * 300}

datab = {'a': np.random.uniform(low=0.5, high=1, size=N),
        'b': np.random.uniform(low=0.5, high=1, size=N),
        'd': np.random.rand(N) * 300}

plt.scatter('a', 'b', s='d', data=dataa, label = "Group a", alpha = 0.6)
plt.scatter('a', 'b', s='d', data=datab, label = "Group b", alpha = 0.6)
# plt.scatter('a', 'b', c='blue', s='d', data=datab, alpha = 1, label = "Group b")
plt.plot([0.3, 0.8], [0.8, 0.1],c = 'black', label = "Divide Line")
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
# plt.tight_layout() # cut edge at right and upper, but not beautiful (not centered)
plt.savefig('2dcluster.pdf', 
            format='pdf', 
#             bbox_inches = 'tight' # Works dramatically, 
           )
plt.show()