import math
import numpy as np

import matplotlib.pyplot as plt

from functools import lru_cache
from triangle_functions import sierpinski_gasket_v2, unit_square

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
def carpet_d(n = 1):
    N = np.linspace(-1, n*-1, n)
    cube2=3**2
    
    # generation
    x1, y1 = carpet_initiator()
    plt.plot(x1, y1) 

    x1, y1 = e((x1, y1)) 
    tx = dim(tuple(x1))
    plt.plot(x1+tx, y1+tx)

    # do 9 times
    theta = np.linspace(0, np.pi*2, cube2)

    # recurse from (n+1)
    for i in range(len(N)):
        x1, y1 = e((x1, y1))
#        plt.plot(x1, y1)
        # x1, y1 = gen(N[i], (x1, y1))

        # for j in range(cube2):
        #     print("translate 9 times")
        #     print("shrink")
        #     # recurse?

# TODO make carpet_d no side effects
def withplot(my_function):
    carpet = my_function

carpet_d(3)

plt.grid()
plt.axis("equal")
plt.show()