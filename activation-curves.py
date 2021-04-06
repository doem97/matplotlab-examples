# Plot activation function curves in same plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 100)
sig = 1/(1+np.exp(-x))
relu = np.maximum(x, 0)
tanh = np.tanh(x)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
# ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x, label='$Linear(x)$')  # Plot more data on the axes...
ax.plot(x, sig, label='$Sigmoid(x)$')  # Plot more data on the axes...
ax.plot(x, relu, label='$ReLU(x)$')  # Plot more data on the axes...
ax.plot(x, tanh, label='$Tanh(x)$')  # Plot more data on the axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x')  # Add an x-label to the axes.
ax.set_ylabel('$\Phi(x)$')  # Add a y-label to the axes.
# ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.grid()
# plt.tight_layout()
# plt.savefig('sigmoid.pdf', format='pdf', 
#             bbox_inches='tight'
#            )
plt.show()