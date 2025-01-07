import math
import numpy as np
import matplotlib.pyplot as plt

from circle_functions import rot, unit_circle, unit_circlev2
from triangle_functions import unit_triangle, unit_trianglev2


"""
    t_rotations = total rotations
    x_translate = how much to translate each triangle segment along
                    its x axis
"""
def spyrograph(t_rotations = 16, x_translate = 0):
    # create plot
    _, ax = plt.subplots()
    ax.axis("equal")
#    ax.grid()

    xc, yc = unit_circle()
    ax.plot(xc, yc)

    seg = (math.pi * 2 / t_rotations)
    for i in range(t_rotations): 
        x1, y1 = unit_triangle()
        x1 = x1 + x_translate

        vv = rot(seg * i) @ [x1, y1]    
        ax.plot(vv[0], vv[1], 'red')

    # show plot 
    plt.show()



# fig, ax = plt.subplots()
# ax.grid()
# ax.axis("equal")

# ucx, ucy = unit_circle()
# plt.plot(ucx, ucy)

# utx, uty = unit_triangle()
# plt.plot(utx, uty)

# plt.show()

fig, ax = plt.subplots()
ax.grid()
ax.axis("equal")

ucx, ucy = unit_circlev2()
plt.plot(ucx, ucy)

# utx, uty = unit_trianglev2()
# plt.plot(utx, uty)
plt.show()
#spyrograph(2)
