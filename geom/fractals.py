import random

import numpy                as np
import pandas               as pd
import matplotlib.pyplot    as plt
import triangle_functions   as triangle
import circle_functions     as circle
import square_functions     as square


### "The secret to fractals is its relationships to power laws"

## constants
CUBE_1  = 3**1      # 3
CUBE_2  = 3**2      # 9
CUBE_N1 = 3**-1     # 0.333

def gasket_side_effects(n, x, y): 
    plt.plot(x, y, 'b')
    print(pd.DataFrame({'n': n, 'x': x, 'y': y}))

def sierpinski_gasket_v2(n = 1, side_effects = gasket_side_effects):
    sgx, sgy = triangle.equilateral()

    def sgn(n, sgx, sgy):
        if n == 0:
            return (sgx, sgy)

        xrange = np.max(sgx) - np.min(sgx)
        yrange = np.max(sgy) - np.min(sgy)

        c1x = sgx + (xrange / 2)
        c2x = sgx - (xrange / 2) 
        c1y = sgy - yrange

        sgx = np.concatenate((sgx, c1x, c2x))
        sgy = np.concatenate((sgy, c1y, c1y))
        
        side_effects(n, sgx, sgy)

        return sgn(n - 1, sgx, sgy)
    
    return sgn(n, sgx, sgy)

def carpet_side_effects(n, x, y): 
    plt.plot(x, y, 'b')
    print(pd.DataFrame({'n': n, 'x': x, 'y': y}))

### DONE - Shrink
### TODO - Magnify
def sierpinski_carpet(n = 1, side_effects = carpet_side_effects):
    # generation
    x1, y1  = square.unit_square()      # init
    x2, y2  = x1*CUBE_N1, y1*CUBE_N1    # shrink
    TX      = np.max(x2) - np.min(x2)   # find translate
    x2, y2  = x2+TX, y2+TX              # apply translate

    # side effects e.g. print
    side_effects(n, x1, y1)
    side_effects(n, x2, y2)
    
    # define recursion
    def carpet_recurse(n, x2, y2, TX):
        # return from recursion
        if n <= 0: return

        # shrink
        x2, y2 = x2/CUBE_1, y2/CUBE_1

        # plot and recurse
        def do(x, y):
            side_effects(n, x, y)
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

def fractal_side_effects(x, y): 
    plt.plot(x, y, 'b')
    print(pd.DataFrame({'x': x, 'y': y}))

def fractal_tree(n = 1, side_effects = fractal_side_effects):

    T = 10 # Amount of parts in a tree line
    random_rotation = lambda : circle.rot(random.uniform(0, np.pi*2)) 

    branch = np.linspace(0, 1, T)

    # scramble branch
    for i in range(len(branch)):
        rand = random.uniform(0,1)
        if rand > 0.666: branch[i] = branch[i]+1
        if rand < 0.333: branch[i] = branch[i]-1
        
    x = np.linspace(0, 1, T)

    fractal_side_effects(x, branch)

    def recurse(n, origin):
        if n == 0: return

        xlin    = np.linspace(0, 1, T)
        branch  = np.linspace(0, 1, T)
        ox, oy  = origin

        xlin    = xlin + ox
        branch  = branch + oy
        
        # scramble branch
        for i in range(len(branch)):
            rand = random.uniform(0,1)
            if rand > 0.666: branch[i] = branch[i]+1
            if rand < 0.333: branch[i] = branch[i]-1

        side_effects(xlin, branch)

        rp = random.randint(0,T-1)
        ox = xlin[rp]
        oy = branch[rp] 

        recurse(n-1, (ox, oy))
            
    rp = random.randint(0, T-1)
    ox = x[rp]
    oy = branch[rp] 

    # recurse for n
    recurse(n-1, (ox, oy))

def scatter(data):
    plt.grid()
    plt.axis("equal")
    plt.show()


def show():
    plt.grid()
    plt.axis("equal")
    plt.show()

# scatter(fractal_tree(3))
# scatter(sierpinski_gasket_v2(3))
scatter(sierpinski_carpet(3))
# show()
