import math
import numpy as np

def unit_triangle():
    a = ([0, 1], [0, 0])
    b = ([1, 1], [0, 1])
    c = ([[0, 1], [0, 1]])

    x1 = np.concatenate((a[0], b[0], c[0]))
    y1 = np.concatenate((a[1], b[1], c[1]))

    return (x1, y1)



def trig_data():
    # generate plot data
    total = 100
    total_unit_circles = 3
    unit_circle_translate = 2 # how much to translate circle by along x
    ranges = (-2, total_unit_circles * unit_circle_translate)

    v = np.linspace(ranges[0], ranges[1], total) # linear walk
    sv = np.zeros(total) # sin values
    cv = np.zeros(total) # cos values

    # generate values from linear walk
    for i in range(len(v)):
        sv[i] = math.sin(v[i])
        cv[i] = math.cos(v[i])

    return v, sv, cv

def rot(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])