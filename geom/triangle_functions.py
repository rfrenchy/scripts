import json
import math
import random
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

def unit_trianglev2():
    a = ([0, 1], [0, 0])
    b = ([0, 0], [0, 0.5])
    c = ([[0, 1], [0.5, 0]])

    x1 = np.concatenate((a[0], b[0], c[0]))
    y1 = np.concatenate((a[1], b[1], c[1]))

    return (x1, y1)

""" 
    square constructred from two triangles,
    very jank implementation
"""
def unit_square(scale = 1):
    x1, y1 = unit_trianglev2()
    x2, y2 = unit_trianglev2() 

    x = np.concatenate((x1, (x2 * -1) + 1))
    y = np.concatenate((y1, (y2 * -1) + 0.5)) * 2

    return (x * scale, y * scale)

def equilateral_triangle():
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

"""
    # two copies of previous
    # translate y 1 whole of other
    # translate x half on positive, the other half on negative

    breaks at values >= 3

    magnified version?
    todo reduction/subdivision version?
    single function works for both?
"""
def sierpinski_gasket(n = 1):
    sgx, sgy = equilateral_triangle()

    # todo, print ranges of each triangle at each level of n
    # check for anomalies for expected and not expected range?
    for i in range(n):
        if (i == 0):
            continue
        
        xrange = np.max(sgx) - np.min(sgx)
        yrange = np.max(sgy) - np.min(sgy)

        c1x = sgx + (xrange / 2)
        c2x = sgx - (xrange / 2) 
        c1y = sgy - yrange

        sgx = np.concatenate((sgx, c1x, c2x))
        sgy = np.concatenate((sgy, c1y, c1y))

    return (sgx, sgy)

"""
    recursive function approach  
"""
def sierpinski_gasket_v2(n = 1):
    sgx, sgy = equilateral_triangle()

    def withplot(my_function):
        def wrapper(*args):
            _, sgx, sgy = args
            plt.plot(sgx, sgy)

            return my_function(*args)

        return wrapper

    @withplot    
    def sgn(n, sgx, sgy):
        if n == 0:
            return (sgx, sgy)

        xrange = np.max(sgx) - np.min(sgx)
        yrange = np.max(sgy) - np.min(sgy)

        c1x = sgx + (xrange / 2)
        c2x = sgx - (xrange / 2) 
        c1y = sgy - yrange

        sgx = np.concatenate((sgx, c1x, c2x))
        sgy = np.concatenate((sgy, c1y, c1y))
            
        return sgn(n - 1, sgx, sgy)
    
    return sgn(n, sgx, sgy)

    # any properties of this 'algorithm' which means it can be recursive and
    # other functions not?

def rot(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])
