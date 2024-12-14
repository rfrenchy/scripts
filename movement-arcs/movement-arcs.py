# README ME
# usage: python3 movement-arcs.py

import argparse

import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.animation as animation

argp = argparse.ArgumentParser("movement-arcs", 
                               description="3 projectile path rotated from central point")
argp.add_argument("-i", "--input", default="")
argp.add_argument("-o", "--output", default="")

def rotation(theta):
    return np.array([[ np.cos(theta), -np.sin(theta)   ],
                     [ np.sin(theta),  np.cos(theta)   ]])

fig, ax = plt.subplots()

# (x, y)
a = np.array([0, 0])# circle center
# (x, y)(x, y)
p = np.array([a, [-1, 0]])



# TODO fix a and p side-effect variables (or leave it?)

def multiplepaths(total):

    # TODO learn how radians work

    for i in range(total):
        # get start+end points of line after rotation
        r1 = rotation(np.pi / (i+1)) @ (p - a) + a
        r2 = rotation(-np.pi / (i+1)) @ (p - a) + a
        ax.plot(r1[0], r1[1])
        ax.plot(r2[0], r2[1])

def v1():
    rot1 = rotation(np.pi / 4) @ (p - a) + a
    rot2 = rotation((-np.pi / 4)) @ (p - a) + a
    
    # projectile object (just one)
    ax.scatter(a[0], a[1])

    # projectile paths
    ax.plot(p[0], p[1]) 
    ax.plot(rot1[0], rot1[1])
    ax.plot(rot2[0], rot2[1])


def add_circle_viz():
    circle  = plt.Circle(a, 1, 
                         color='gray', 
                         fill=False, 
                         linestyle='dashed')

    # circle visualisation
    ax.add_patch(circle)
    
add_circle_viz()
# v1()
multiplepaths(6)

plt.axis('equal')
plt.show()

# fig.savefig("c2.jpg")