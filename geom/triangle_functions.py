import math
import numpy as np
import matplotlib.pyplot as plt

a = ([0, 1], [0, 0])
b = ([1, 1], [0, 1])
c = ([[0, 1], [0, 1]])


x1 = np.concatenate((a[0], b[0], c[0]))
y1 = np.concatenate((a[1], b[1], c[1]))

fig, ax = plt.subplots()

ax.axis("equal")
ax.grid()

# plt.plot(a[0], a[1])
# plt.plot(b[0], b[1])
# plt.plot(c[0], c[1])

plt.plot(x1, y1)

plt.show()

