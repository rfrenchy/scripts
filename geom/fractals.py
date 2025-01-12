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
# Fails at n > 2
def carpet_segment(n, sg = unit_square()):
    # exit recursion
    if n == 0:
        return

    sgx, sgy = sg 
    plt.plot(sgx, sgy, "b")

    x2, y2 = (1/c)*sgx, (1/c)*sgy         
    ux, uy = unit_square()

    # inefficient - replace
    if np.array_equal(sgx, ux) or np.array_equal(sgy, uy):
        tx = (np.max(x2) - np.min(x2)) 

        plt.plot(x2+tx, y2+tx)
        carpet_segment(n, (x2+tx,y2+tx))

    else:
        tx = (np.max(sgx) - np.min(sgx))

        # need to have an origin? to translate from

        # (0,0),(1,0),(2,0)
        carpet_segment(n-1, (x2, y2))     
        carpet_segment(n-1, (x2+tx, y2))
        carpet_segment(n-1, (x2+(tx*2), y2))

        # (0,1),(1,1),(2,1)
        carpet_segment(n-1, (x2, y2+tx))
        # carpet_segment(n-1, (x2+trs, y2+trs))
        carpet_segment(n-1, (x2+(tx*2), y2+tx))

        # (0,2),(1,2),(2,2)
        carpet_segment(n-1, (x2, y2+(tx*2)))      
        carpet_segment(n-1, (x2+tx, y2+(tx*2)))
        carpet_segment(n-1, (x2+(tx*2), y2+(tx*2)))

carpet_segment(2)

# plot setup
plt.summer()
plt.grid()
plt.axis("equal")

# show plot
plt.show()