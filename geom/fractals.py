import math
import numpy as np

import matplotlib.pyplot as plt

from functools import lru_cache # TODO move to fractals_cache.py)
from triangle_functions import sierpinski_gasket_v2, unit_square, rot

import square_functions as square 

rotate = lambda m, theta: np.array(([np.cos(theta), -np.sin(theta)],
                                    [np.sin(theta),  np.cos(theta)])) @ m

def plot_sierpinkski_gasket(n = 0):
    sierpinski_gasket_v2(n)
    plt.show()

# 'secret to fractals is its relationships to power laws'
def carpet_initiator():
    return unit_square()

def exp(scale = -1):
    return 3 ** scale # need to chan

### TODO make recursable
#### has to use data from previous output in recurse chain
def gen(n = -1, carpet = carpet_initiator()):
    ix, iy = carpet

    # how to know how much to translate N**e?
    # translation
    x3, y3 = ix*exp(n), iy*exp(n) # memoize function here
    tx = (np.max(x3) - np.min(x3)) # memoize function here
    x3=x3+tx
    y3=y3+tx

    return (x3, y3)

def e(carpet, c = 1/3):
    ix, iy = carpet
    return(ix*c, iy*c)

@lru_cache(maxsize=None)
def dim(x1):
    dx = np.array(x1)
    return np.max(dx) - np.min(dx)

# D?
cube1=3**1
cube2=3**2

def carpet_d(n = 1):
    # generation
    x1, y1 = carpet_initiator()     # init
    x2, y2 = e((x1, y1))            # shrink
    TX = np.max(x2) - np.min(x2)    # find translate
    x2, y2 = x2+TX, y2+TX           # apply translate

    # plot
    plt.plot(x1, y1)
    plt.plot(x2, y2) 
    
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


# TODO make carpet_d no side effects
def withplot(my_function):
    carpet = my_function

carpet_d(3)

plt.grid()
plt.axis("equal")
plt.show()
