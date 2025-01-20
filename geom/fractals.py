import numpy                as np
import matplotlib.pyplot    as plt
import triangle_functions   as triangle
import square_functions     as square


### "The secret to fractals 
###   is its relationships to 
###  power laws"

## constants
CUBE_1  = 3**1      # 3
CUBE_2  = 3**2      # 9
CUBE_N1 = 3**-1     # 0.333

"""
    # two copies of previous
    # translate y 1 whole of other
    # translate x half on positive, the other half on negative

    breaks at values >= 3

    magnified version?
    todo reduction/subdivision version?
    single function works for both?
"""
def sierpinski_gasket(n = 1):
    sgx, sgy = triangle.equilateral()

    # todo, print ranges of each triangle at each level of n
    # check for anomalies for expected and not expected range?
    for i in range(n):
        if (i == 0):
            continue
        
        xrange = np.max(sgx) - np.min(sgx)
        yrange = np.max(sgy) - np.min(sgy)

        c1x = sgx + (xrange / 2)
        c2x = sgx - (xrange / 2) 
        c1y = sgy - yrange

        sgx = np.concatenate((sgx, c1x, c2x))
        sgy = np.concatenate((sgy, c1y, c1y))

    return (sgx, sgy)

"""
    recursive function approach  
"""
def sierpinski_gasket_v2(n = 1):
    sgx, sgy = triangle.equilateral()

    def withplot(my_function):
        def wrapper(*args):
            _, sgx, sgy = args
            plt.plot(sgx, sgy)

            return my_function(*args)

        return wrapper

    @withplot    
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
            
        return sgn(n - 1, sgx, sgy)
    
    return sgn(n, sgx, sgy)

### DONE - Shrink
### TODO - Magnify
def sierpinski_carpet(n = 1):
    # generation
    x1, y1 = square.unit_square()   # init
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
