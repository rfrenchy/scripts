import math
import numpy as np

import matplotlib.pyplot as plt

from triangle_functions import sierpinski_gasket_v2, unit_square


def plot_sierpinkski_gasket(n = 0):
    sierpinski_gasket_v2(n)
    plt.show()

# D
cube1=3**1
cube2=3**2
n_cube1=3**-1

# 'the secret to fractals is its relationships to power laws'
def carpet_d(n = 1):
    # generation
    x1, y1 = unit_square()          # init
    x2, y2 = x1*n_cube1, y1*n_cube1 # shrink
    TX = np.max(x2) - np.min(x2)    # find translate
    x2, y2 = x2+TX, y2+TX           # apply translate

    # plot
    plt.plot(x1, y1, 'b')
    plt.plot(x2, y2, 'b') 
    
    # recurse
    carpet_recurse(n-1, x2, y2, TX)

def carpet_recurse(n, x2, y2, TX):
    # return from recursion
    if n <= 0: return

    # shrink
    x2, y2 = x2/cube1, y2/cube1

    def do(x, y):
        plt.plot(x, y, 'b')
        carpet_recurse(n -1, x, y, TX)
    
    # plot in each segment of carpet
    for i in range(cube2):
        if i == 0: do(x2, y2)
        if i == 1: do(x2, y2+TX) 
        if i == 2: do(x2, y2+TX+TX)
        if i == 3: do(x2+TX, y2)
        # if i == 4: do nothing
        if i == 5: do(x2+TX, y2+TX+TX)
        if i == 6: do(x2+TX+TX, y2)
        if i == 7: do(x2+TX+TX, y2+TX)
        if i == 8: do(x2+TX+TX, y2+TX+TX)


carpet_d(3)

plt.grid()
plt.axis("equal")
plt.show()
