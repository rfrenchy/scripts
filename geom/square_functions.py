import numpy as np
"""
    Finds and returns the center point of a given square.

    Parameters:
    a (float): The side length of the square.

    Returns:
    tuple: A tuple containing the coordinates of the center point of the square.
"""
def center(a, x1, y1): # incorrect
    return (x1+a/2, y1+a/2); 

def centroid(x1, y1): # inefficient
    return np.average(x1), np.average(y1)
