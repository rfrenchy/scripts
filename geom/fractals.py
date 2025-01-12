import math
import numpy as np
import matplotlib.pyplot as plt

from triangle_functions import sierpinski_gasket_v2, unit_square

def plot_sierpinkski_gasket(n = 0):
    sierpinski_gasket_v2(n)
    plt.show()

c=3 # cubed

def assert_carpet_range():
    print("or dont")

# plot carpet segment
# INCORRECT
def carpet_segment(n, sg = unit_square()):
    # exit recursion
    if n == 0:
        return

    sgx, sgy = sg 

    x2, y2 = (1/c)*sgx, (1/c)*sgy         
    tr_rng = (np.max(x2) - np.min(x2)) 

    ux, uy = unit_square()

    if np.array_equal(sgx, ux) or np.array_equal(sgy, uy):
        x1, y1 = sgx - tr_rng, sgy - tr_rng

        # paint
        plt.plot(x2, y2) # paint inner square
        plt.plot(x1, y1) # paint inner whtie square

        carpet_segment(n-1, (x2,y2))

    else:
        plt.plot(sgx, sgy)
        # (0,0),(1,0),(2,0)



        carpet_segment(n-1, (x2, y2))     
        carpet_segment(n-1, (x2-tr_rng, y2))
        carpet_segment(n-1, (x2-(tr_rng*2), y2))

        # (0,1),(1,1),(2,1)
        carpet_segment(n-1, (x2, y2-tr_rng))
        carpet_segment(n-1, (x2-tr_rng, y2-tr_rng))
        carpet_segment(n-1, (x2-(tr_rng*2), y2-tr_rng))

        # (0,2),(1,2),(2,2)
        carpet_segment(n-1, (x2, y2-(tr_rng*2)))      
        carpet_segment(n-1, (x2-tr_rng, y2-(tr_rng*2)))
        carpet_segment(n-1, (x2-(tr_rng*2), y2-(tr_rng*2)))

carpet_segment(3)

# plot setup
plt.summer()
plt.grid()
plt.axis("equal")

# show plot
plt.show()