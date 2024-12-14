
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

theta    = np.pi / 4
rotation = np.array([[ np.cos(theta), -np.sin(theta)   ],
                     [ np.sin(theta),  np.cos(theta)   ]])
a = np.array([1, 1])# circle center
p = np.array([[1,1 ],[1, 0]])

# p = {"x": [a.x, a.y], "y": [a.x, a.y - 1] } # line from circle center
# r = (p.x - a.x)**2 + (p.y - a.y) # radius of circle

p_prime   = p - a
p_rotated = rotation @ p_prime

final_rotated = p_rotated + a 

circle  = plt.Circle(a, 1, 
                     color='gray', 
                     fill=False, 
                     linestyle='dashed')

fig, ax = plt.subplots()

# ax.add_artist(circle)

# plt.quiver(a[0], a[1], p[0] - a[0], p[1] - a[1], 
#             angles='xy',
#             scale_units='xy',
#             scale='1',
#             color='r'
#            )

ax.add_patch(circle)

print(p)
print(p_rotated)

ax.scatter(a[0], a[1])
ax.plot(p[0], p[1])
ax.plot(final_rotated[0], final_rotated[1])

plt.axis('equal')
plt.show()
# fig.savefig("test.jpg")

# rotation transform?
# 
#  