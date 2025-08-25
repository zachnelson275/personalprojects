import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x * 2
z = x ** 2

# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.plot(x, y)
# ax.set_title('title')
# ax.set_xlabel('x')
# ax.set_ylabel('y')

# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])
# axes1.plot(x, y, 'r')
# axes2.plot(x, y, 'b')

# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.4])
# axes1.plot(x, y)
# axes1.plot(x, z)
# axes1.set_xlabel('x')
# axes1.set_ylabel('z')
# axes2.plot(x, y)
# axes2.set_ylim(30, 50)
# axes2.set_xlim(20, 22)
# axes2.set_title('zoom')
# axes2.set_xlabel('x')
# axes2.set_ylabel('y')

# fig, axes = plt.subplots(nrows = 1, ncols = 2)
# axes[0].plot(x, y, 'b--', lw = 3)
# axes[1].plot(x, z, 'r-', lw = 3)

plt.show()