# Plot the loss decreasing data for multi-branches in deep learning
# Here the three branches are called 'grid', 'masking', 'pixel'
# Over 100,000 iterations

import numpy as np
import matplotlib.pyplot as plt

with open('./trainingdata/grid_ori_loss') as f:
    lines = f.read().splitlines()
grid = [float(i) for i in lines]
with open('./trainingdata/masking_ori_loss') as f:
    lines = f.read().splitlines()
masking = [float(i) for i in lines]
with open('./trainingdata/pixel_ori_loss') as f:
    lines = f.read().splitlines()
pixel = [float(i) for i in lines]

x = np.linspace(1,100000,10000)

z1 = np.poly1d(np.polyfit(x, grid, 25))
z2 = np.poly1d(np.polyfit(x, masking, 25))
z3 = np.poly1d(np.polyfit(x, pixel, 25))
plt.figure(figsize=(12,6))
plt.yscale('log')
plt.grid(axis = 'y', alpha = 0.3)
plt.plot(x, grid, 
         linewidth=1,
         label = r"Grid Box",
#          color='b'
        )
plt.plot(x, pixel, 
         linewidth=1,
         label = r"Multi-label Classification",
#          color='b'
        )
plt.plot(x, masking, 
         linewidth=1,
         alpha = 0.5,
         label = r"Masking",
#          color='b'
        )
plt.plot(x, z1(x), 
         linewidth=1.5,
#          alpha = 0.7,
         label = r"Grid Regression Curve",
#          color='r'
        )
plt.plot(x, z2(x), 
         linewidth=1.5,
#          alpha = 0.7,
         label = r"Masking Regression Curve",
#          color='r'
        )
plt.plot(x, z3(x), 
         linewidth=1.5,
#          alpha = 0.7,
         label = r"Multi-label Regression Curve",
#          color='r'
        )
plt.xlabel('Iterations')
plt.ylabel(r'Test Loss')
# plt.title("Simple Plot")
plt.legend(fontsize='medium')
plt.savefig('testlossbranch.pdf',bbox_inches='tight')
plt.show()