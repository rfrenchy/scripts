import math
import numpy as np

import matplotlib.pyplot as plt

from triangle_functions import sierpinski_gasket_v2, unit_square

# constants
CUBE_1=3**1   # 3
CUBE_2=3**2   # 9
CUBE_N1=3**-1 # 0.333

def plot_sierpinkski_gasket(n = 0):
    sierpinski_gasket_v2(n)
    plt.show()

# 'the secret to fractals 
# is its relationships to 
# power laws'
# DONE - Shrink
# TODO - MAGNIFY
def sierpinski_carpet(n = 1):
    # generation
    x1, y1 = unit_square()          # init
    x2, y2 = x1*CUBE_N1, y1*CUBE_N1 # shrink
    TX = np.max(x2) - np.min(x2)    # find translate
    x2, y2 = x2+TX, y2+TX           # apply translate

    # plot
    plt.plot(x1, y1, 'b')
    plt.plot(x2, y2, 'b') 
    
    # define recursion
    def carpet_recurse(n, x2, y2, TX):
        # return from recursion
        if n <= 0: return

        # shrink
        x2, y2 = x2/CUBE_1, y2/CUBE_1

        # plot and recurse
        def do(x, y):
            plt.plot(x, y, 'b')
            carpet_recurse(n -1, x, y, TX)
        
        # recurse for each carpet segment
        for i in range(CUBE_2):
            if i == 0: do(x2, y2)
            if i == 1: do(x2, y2+TX) 
            if i == 2: do(x2, y2+TX+TX)
            if i == 3: do(x2+TX, y2)
            # if i == 4: do nothing
            if i == 5: do(x2+TX, y2+TX+TX)
            if i == 6: do(x2+TX+TX, y2)
            if i == 7: do(x2+TX+TX, y2+TX)
            if i == 8: do(x2+TX+TX, y2+TX+TX)

    # recurse
    carpet_recurse(n-1, x2, y2, TX)

sierpinski_carpet(3)

plt.grid()
plt.axis("equal")
plt.show()
