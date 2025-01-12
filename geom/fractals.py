import math
import numpy as np
import matplotlib.pyplot as plt

from triangle_functions import sierpinski_gasket_v2, unit_square

def plot_sierpinkski_gasket(n = 0):
    sierpinski_gasket_v2(n)
    plt.show()

c=3 # cubed

def assert_carpet_range():
    print("todo")

# plot carpet segment
def carpet_segment(n, sg = unit_square()):
    sgx, sgy = sg
    # exit recursion
    if n == 0:
        return
    
    x2, y2 = c*sgx, c*sgy
    x1, y1 = sgx, sgy

    rng = np.max(x1) - np.min(x1)  # x1 will have the same range as y1
    x1 = x1 + rng # translate x to middle of carpet segment
    y1 = y1 + rng # translate y to middle of carpet segment

    # paint
    plt.plot(x2, y2) # paint main square
    plt.plot(x1, y1) # paint inner whtie square

    # recurse
    sgx = np.concatenate((x2, x1))
    sgy = np.concatenate((y2, y1))
    carpet_segment(n-1, (sgx, sgy))

carpet_segment(2)

# plot setup
plt.summer()
plt.grid()
plt.axis("equal")

# show plot
plt.show()