import math
import numpy as np
import matplotlib.pyplot as plt

def rot(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])

# print rads numeric values around a circle
def print_rads_table(total_rotations = 16):
    full_circle = math.pi * 2
    x = full_circle / total_rotations

    th = "div\tval\tunit"

    print("-" * len(th.expandtabs()))
    print(th)
    print("-" * len(th.expandtabs()))

    for i in range(total_rotations):
        print(f"{i+1}/{total_rotations}\t{x * (i + 1):.4f}\trads")

    print("-" * len(th.expandtabs()))

def plot_circle_rads(ax: plt.Axes, total_rotations = 16):
    # unit vector line
    v = np.array([[0, 1], [0, 0]])

    # how much to rotate each line
    r = (math.pi * 2) / total_rotations
    for i in range(total_rotations):
        # note, the order you multiple matrics important
        vv = rot(r * (i+1)) @ v 
        ax.plot(vv[0], vv[1])


# plot a point along each degree of edge of circle
def unit_circle(xtranslate = 0):
    total = 360 # 

    # unit vector line
    v = np.array([[0, 1], [0, 0]])
    r = (math.pi * 2) / total

    cx = np.zeros(total)
    cy = np.zeros(total)

    for i in range(total):
        p = rot(r * (i+1)) @ v
        cx[i] = p[0][1] + xtranslate # grab x value
        cy[i] = p[1][1] # grab y value
    
    return (cx, cy)
