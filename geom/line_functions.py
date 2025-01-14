import math
import numpy as np

import matplotlib.pyplot as plt


x = np.linspace(0, 10, 10)
m = 0.5 # steepness? (slope/gradient)
c = 4 # almost like a starting point for y at x=0

y = np.zeros(len(x))

for i in range(len(x)):
    y[i] = (m*x[i]) + c

plt.grid()
plt.xlim(0, 10)
plt.ylim(-1, 10)

plt.plot(x, y)

# plot a triangle on a line to find an angle?


plt.show()