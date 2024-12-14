
# A
# usage: python3 track-arc.py -i dancer-1000.jpg

import argparse

import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.animation as animation

argp = argparse.ArgumentParser("movement-arcs")
argp.add_argument("-i", "--input", default="")
argp.add_argument("-o", "--output", default="")

# 3 projectiles rotated from central point 
# problem, how to not make them overlap, anticiptaion animation?

# Quarternions are for 3d? I'm working in 2d
# therefore use 2d rotation matrix
# theta = 45


def rotation(theta):
    return np.array([[ np.cos(theta), -np.sin(theta)   ],
                     [ np.sin(theta),  np.cos(theta)   ]])



# c1
# a = np.array([0, 0])# circle center
# p = np.array([[1,1 ],[1, 0]])

a = np.array([1, 1])# circle center
p = np.array([ a,[1, 0]])

rot1 = rotation(np.pi / 4) @ (p - a) + a
rot2 = rotation((-np.pi / 4)) @ (p - a) + a

circle  = plt.Circle(a, 1, 
                     color='gray', 
                     fill=False, 
                     linestyle='dashed')

fig, ax = plt.subplots()


# plt.quiver(a[0], a[1], p[0] - a[0], p[1] - a[1], 
#             angles='xy',
#             scale_units='xy',
#             scale='1',
#             color='r'
#            )

# circle visualisationg
ax.add_patch(circle)

# projectile object (just one)
ax.scatter(a[0], a[1])

# projectile paths
ax.plot(p[0], p[1])
ax.plot(rot1[0], rot1[1])
ax.plot(rot2[0], rot2[1])

plt.axis('equal')
# plt.show()

fig.savefig("c2.jpg")

# rotation transform?
# 
#  