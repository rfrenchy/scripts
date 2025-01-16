"""
Fractals Module
===============

This module provides functions to generate fractal patterns.

Generating a Sierpinski Gasket::

    >>> from fractals import sierpinski_gasket
    >>> v, sv, cv = sierpinski_gasket(3)
    >>> print(v)
    [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    >>> print(sv)
    [0.0, 0.479425538604203, 0.8414709848078965, 0.9974949866040544, 0.9092974268256817, 0.5984721441039564, 0.1411200080598672]
    >>> print(cv)
    [1.0, 0.8775825618903728, 0.5403023058681398, 0.0707372016677029, -0.4161468365471424, -0.8011436155469337, -0.9899924966004454]

"""

import numpy as np
import math
import functools

def save_as_obj_decorator(filename):
    def decorator_save_as_obj(func):
        @functools.wraps(func)
        def wrapper_save_as_obj(*args, **kwargs):
            v, sv, cv = func(*args, **kwargs)
            with open(filename, 'w') as f:
                for i in range(len(v)):
                    f.write(f"v {v[i]} {sv[i]} {cv[i]}\n")
                for i in range(len(v) - 1):
                    f.write(f"l {i + 1} {i + 2}\n")
            print(f"Data saved to {filename}")
            return v, sv, cv
        return wrapper_save_as_obj
    return decorator_save_as_obj

@save_as_obj_decorator('sierpinski_gasket.obj')
def sierpinski_gasket(n=1):
    """
    Generate a Sierpinski Gasket.

    Parameters:
    n (int): The number of iterations to perform.

    Returns:
    tuple: A tuple containing three numpy arrays:
        - v: The linear walk values.
        - sv: The sine values of the linear walk.
        - cv: The cosine values of the linear walk.

    Example:
    >>> v, sv, cv = sierpinski_gasket(3)
    >>> print(v)
    [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    >>> print(sv)
    [0.0, 0.479425538604203, 0.8414709848078965, 0.9974949866040544, 0.9092974268256817, 0.5984721441039564, 0.1411200080598672]
    >>> print(cv)
    [1.0, 0.8775825618903728, 0.5403023058681398, 0.0707372016677029, -0.4161468365471424, -0.8011436155469337, -0.9899924966004454]
    """
    ranges = [0, 3]
    total = 7
    v = np.linspace(ranges[0], ranges[1], total) # linear walk
    sv = np.zeros(total) # sin values
    cv = np.zeros(total) # cos values

    # generate values from linear walk
    for i in range(len(v)):
        sv[i] = math.sin(v[i])
        cv[i] = math.cos(v[i])

    return v, sv, cv

# Example usage
sierpinski_gasket(3)
