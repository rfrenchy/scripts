import json
import math
import random
import string
import numpy as np

import matplotlib.pyplot as plt

def tojson(my_function):
    def wrapper(*args):
        # Call the original function and get the result
        result = my_function(*args)
        
        # Generate a random filename
        filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '.json'
        
        # Save the result to a JSON file
        with open(filename, 'w') as f:
            json.dump(result, f)
        
        print(f"Data saved to {filename}")
        return result
    return wrapper

def withdebugplot(my_function):
    def wrapper(*args):
        x, y = my_function(*args)

        plt.plot(x, y)
        plt.axis("equal")
        plt.grid()
        # plt.show()

        return (x, y)
    return wrapper

def unit_triangle():
    a = ([0, 1], [0, 0])
    b = ([1, 1], [0, 1])
    c = ([[0, 1], [0, 1]])

    x1 = np.concatenate((a[0], b[0], c[0]))
    y1 = np.concatenate((a[1], b[1], c[1]))

    return (x1, y1)

# built fot pyplot
def unit_trianglev2():
    a = ([0, 1], [0, 0])
    b = ([0, 0], [0, 0.5])
    c = ([[0, 1], [0.5, 0]])

    x1 = np.concatenate((a[0], b[0], c[0]))
    y1 = np.concatenate((a[1], b[1], c[1]))

    return (x1, y1)

def equilateral():
    a = ([0, 0.5], [0, 1])
    b = ([0.5, 1], [1, 0])
    c = ([[1, 0], [0, 0]])

    x1 = np.concatenate((a[0], b[0], c[0]))
    y1 = np.concatenate((a[1], b[1], c[1]))

    return (x1, y1)

def print_trig_data(my_function):
    def wrapper():
        v, sv, cv = my_function()

        if not v.any() or not sv.any() or not cv.any():
            return

        th = "i\trad\tsin\tcos"

        print("-" * len(th.expandtabs()))
        print(th)
        print("-" * len(th.expandtabs()))


        for i in range(len(v)):
            print(f"{i}\t{v[i]:.4f}\t{sv[i]:.4f}\t{cv[i]:.4f}")

        print("-" * len(th.expandtabs()))

    return wrapper

@print_trig_data
def trig_data():
    # generate plot data
    total = 360
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

# built fot vedo
def unit_trianglev3():
    x = (1, 0, 0)
    y = (0, 1, 0)
    z = (0, 0, 0)

    return [(x[0],y[0],z[0]), (x[1],y[1],z[1]), (x[2],y[2],z[2])]

    x1 = np.concatenate((x[0], y[0], z[0]))
    y1 = np.concatenate((x[1], y[1], z[1]))

    return (x1, y1)
