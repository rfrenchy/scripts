import math
import numpy as np
import matplotlib.pyplot as plt

def print_table(v, sv, cv):
    th = "v\t\tsv\t\tcv\t"

    print("-" * len(th.expandtabs()))
    print(th)
    print("-" * len(th.expandtabs()))

    for i in range(len(v)):
        print(f"{v[i]:.4f}\t\t{sv[i]:.4f}\t\t{cv[i]:.4f}\t")

def rot(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

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
    
    # add finish point (aka the start)
    cx = np.append(cx, cx[0])
    cy = np.append(cy, cy[0])

    return (cx, cy)

"""
    points for a unit circle, uses cos and sin functions to gen
"""
def unit_circlev2():
    t_points = 24
    
    seg = (np.pi * 2) / t_points

    cx = np.zeros(t_points)
    cy = np.zeros(t_points)

    for i in range(t_points):
        cx[i] = np.cos(seg * i)
        cy[i] = np.sin(seg * i)

    # add finish point (aka the start)
    cx = np.append(cx, cx[0])
    cy = np.append(cy, cy[0])

    return (cx, cy)

def spiral(oscilations = 1):
    t_points = 90

    for i in range(oscilations):    
        seg = (np.pi * 2) / t_points

        cx = np.zeros(t_points)
        cy = np.zeros(t_points)

        for i in range(t_points):
            cx[i] = np.cos(seg * i) * 1.1
            cy[i] = np.sin(seg * i) * 0.9


    return (cx, cy)
