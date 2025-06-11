import math
import numpy as np
import matplotlib.pyplot as plt

from circle_functions import rot, unit_circlev2, spiral
from triangle_functions import unit_triangle, trig_data
import square_functions


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

    xc, yc = unit_circlev2()
    ax.plot(xc, yc)

    seg = (math.pi * 2 / t_rotations)
    for i in range(t_rotations):
        x1, y1 = unit_triangle()
        x1 = x1 + x_translate

        vv = rot(seg * i) @ [x1, y1]
        ax.plot(vv[0], vv[1], 'red')

    # show plot
    plt.show()

def temp():
    cx, cy = spiral(5)

    trig_data()

    plt.axis("equal")
    plt.plot(cx, cy)
    plt.show()

def test():
    def square():
        print("geom square")
