import math
import numpy as np

import matplotlib.pyplot as plt


def line():
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

def print_power_laws(n):
    x = np.linspace(1, 10, 1)

    th = "val\tpow"
    
    print("-" * len(th.expandtabs()))
    print(th)
    print("-" * len(th.expandtabs()))

    for i in range(len(x)):
        print(i)
        # plt.plot(x[i], n ** (i*-1))


# plot a triangle on a line to find an angle?

print_power_laws(3)

plt.show()