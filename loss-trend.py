# Plot the loss decreasing data and draw regression curve on it

import numpy as np
import matplotlib.pyplot as plt

with open('./trainingdata/testloss100000') as f:
    lines = f.read().splitlines()
y1 = [float(i) for i in lines]

z1 = np.poly1d(np.polyfit(x1, y1, 25))
plt.figure(figsize=(12,4))
plt.yscale('log')
plt.grid(axis = 'y', alpha = 0.3)
plt.plot(x1, y1, 
#          linewidth=0.8,
#          alpha = 0.6,
         label = r"Raw Data",
         color='b'
        )
plt.plot(x1, z1(x1), 
         linewidth=1.5,
         alpha = 1,
         label = r"Regression Curve",
         color='r'
        )
# plt.plot(x2, y2, 
#          linewidth=0.8,
#          label = r"$20,000$ Epochs",
# #          color='b'
#         )
plt.xlabel('Iterations')
plt.ylabel(r'Test Loss')
# plt.title("Simple Plot")
plt.legend()
plt.savefig('testloss100000.pdf', bbox_inches='tight')
plt.show()