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

# 'secret to fractals is its relationships to power laws'
# todo, try using logarithms/powers to magnify or reduce the fractal

def carpet_initiator():
    return unit_square()

def carpet_generator(scale = 1):
    ix, iy = carpet_initiator()

    x3, y3 = (1/c)*ix, (1/c)*iy     
    tx = (np.max(x3) - np.min(x3)) 

    x3=x3+tx
    y3=y3+tx

    return [(ix,iy),(x3, y3)]

def carpet_d():
    print("todo")

# plot carpet segment
# Fails at n > 2
def carpet_segment(n, sg = unit_square()):
    # exit recursion
    if n == 0:
        return

    # unit square is the initiator
    sgx, sgy = sg     
    plt.plot(sgx, sgy, "b")

    x3, y3 = (1/c)*sgx, (1/c)*sgy  # cubed subdivision
    ux, uy = unit_square()

    # inefficient - replace
    if np.array_equal(sgx, ux) or np.array_equal(sgy, uy):
        tx = (np.max(x3) - np.min(x3)) 

        x3 = x3+tx
        y3 = y3+tx

        # this plus the unit square is the generator
        plt.plot(x3, y3)


        # pass cubed subdivided square
        carpet_segment(n, (x3+tx,y3+tx))

    else:
        # 02
        tx = (np.max(sgx) - np.min(sgx)) # translation factor
        carpet_segment(n-1, (x3, y3))     

        # need to have an origin? to translate from

        # (0,0),(1,0),(2,0)
        
        carpet_segment(n-1, (x3+tx, y3))
        # carpet_segment(n-1, (x2+(tx*2), y2))

        # # (0,1),(1,1),(2,1)
        # carpet_segment(n-1, (x2, y2+tx))
        # # carpet_segment(n-1, (x2+trs, y2+trs))
        # carpet_segment(n-1, (x2+(tx*2), y2+tx))

        # # (0,2),(1,2),(2,2)
        # carpet_segment(n-1, (x2, y2+(tx*2)))      
        # carpet_segment(n-1, (x2+tx, y2+(tx*2)))
        # carpet_segment(n-1, (x2+(tx*2), y2+(tx*2)))

# n = 3 # fractal dimension
# carpet_segment(n)


carpet = carpet_generator()

plt.plot(carpet[0][0], carpet[0][1])
plt.plot(carpet[1][0], carpet[1][1])

plt.grid()
plt.axis("equal")

# show plot
plt.show()