# Plot the accuracy curve/data for multi-branch
import matplotlib.pyplot as plt
import numpy as np

with open('./trainingdata/masking_acc') as f:
    lines = f.read().splitlines()
masking = [float(i) for i in lines]
with open('./trainingdata/pixel_acc') as f:
    lines = f.read().splitlines()
pixel = [float(i) for i in lines]
x = np.linspace(1,100000,1001)
plt.figure(figsize=(12,4))
plt.grid(axis = 'y', alpha = 0.3)
plt.plot(x, masking, 
#          linewidth=1,
         alpha = 0.7,
         label = r"Masking",
         color='b'
        )
plt.plot(x, pixel, 
#          linewidth=0.5,
         alpha = 0.7,
         label = r"Multi-label Classification",
         color='r'
        )
plt.yscale('logit')
plt.xlabel('Iterations')
plt.ylabel(r'Test Accuracy')
# plt.title("Simple Plot")
plt.legend()
plt.savefig('testacc.pdf',bbox_inches='tight')
plt.show()