import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 11)
y = x ** 2

# Functional method
# plt.plot(x, y, 'r--')
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Title')

# Multiple plots on the same canvas
# plt.subplot(1, 2, 1)
# plt.plot(x, y, 'r')
# plt.subplot(1, 2, 2)
# plt.plot(y, x, 'b')


# Object-oriented method
# fig = plt.figure()
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # left, bottom, width, height
# axes.plot(x, y, 'g')
# axes.set_xlabel("X Label")
# axes.set_ylabel("Y Label")
# axes.set_title("Title")

# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
# axes1.plot(x, y, 'b')
# axes1.set_title('Main Plot')
# axes2.plot(y, x, 'r')
# axes2.set_title('Insert Plot')

# fig, axes = plt.subplots(nrows = 1, ncols = 2)
# # for current_ax in axes:      # Iterate through each axis
# #     current_ax.plot(x, y)
# axes[0].plot(y, x)             # Access by index
# axes[1].set_title('Second Plot')


# Figure Size & DPI
# fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (8,2))
# axes[0].plot(x, y, 'r')
# axes[1].plot(y, x, 'b')

# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.plot(x, x ** 2, '#FFEE8C', linewidth = 2, marker = 'o', markersize = 15, label = 'X Squared')
# ax.plot(x, x ** 3, 'purple', lw = 8, alpha = .8, ls = '--', label = 'X Cubed')
# ax.legend(loc = 0) # Can also pass in specific location using a tuple

# ax.set_xlim([0, 1])
# ax.set_ylim([0, 2])

# plt.tight_layout()
plt.show()