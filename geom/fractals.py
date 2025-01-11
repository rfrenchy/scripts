import math
import numpy as np
import matplotlib.pyplot as plt

from triangle_functions import sierpinski_gasket_v2
from circle_functions import unit_circlev2

def plot_sierpinkski_gasket(n = 0):
    sierpinski_gasket_v2(n)
    plt.show()


def simple_fractal():
    # plot aesthetics
    plt.axis("equal")

    # unit circle 'dimension'? D
    cx, cy = unit_circlev2()
    plt.plot(cx, cy)

    # area of a circle so i can know if growth point is
    # outside of it?
     
    ox = [0]
    oy = [0]

    # what is the size of the point?
    plt.scatter(ox, oy, color="red")    

    plt.show()

plot_sierpinkski_gasket(3)

# it looks the same after 2/3?