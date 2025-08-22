import numpy as np

import triangle_functions as triangle

"""
    Finds and returns the center point of a given square.

    Parameters:
    a (float): The side length of the square.

    Returns:
    tuple: A tuple containing the coordinates of the center point of the square.
"""
# built for pyplot 
def center(a, x1, y1): # incorrect, used?
    return (x1+a/2, y1+a/2); 

# built for pyplot
def centroid(x1, y1): # inefficient
    return np.average(x1), np.average(y1)

# built for pyplot
def unit_square(scale = 1):
    x1, y1 = triangle.unit_trianglev2()
    x2, y2 = triangle.unit_trianglev2() 

    x = np.concatenate((x1, (x2 * -1) + 1))
    y = np.concatenate((y1, (y2 * -1) + 0.5)) * 2

    return (x * scale, y * scale)

# built for vedo
def unit_square_3d(scale = 1):
    return triangle.unit_trianglev3()
