import numpy                as np
import pandas               as pd
import matplotlib.pyplot    as plt
import triangle_functions   as triangle

def gasket_side_effects(n, x, y): 
    plt.plot(x, y, 'b')
    plt.savefig("sierpinski_gasket.png")
    print(pd.DataFrame({'n': n, 'x': x, 'y': y}))

# BUG: fix triangle closing across other triangles 
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

sierpinski_gasket_v2(3)