
# usage: python3 parabola.py


import argparse

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


argp = argparse.ArgumentParser("bouncing-ball-plan")
argp.add_argument("-o", "--output", default="bouncing-ball-plan.gif")
args = argp.parse_args()

# ball bouncing
fig, ax = plt.subplots()

# set fig dimensions (landscape aspect ratio)
fig.set_figwidth(1.91 * 4)
fig.set_figheight(1 * 4)

# COORD PLANNING PHASE

# TODO


# y = (a * pow(x,2)) + (b * x) + c
# the 'vertex' of a parabola represents the turning point,
# it is often the max or min value of the quadratic equaiton
# reprsenting the parabola
# CRUCIAL for understanding the shape and position of a parabola

# All quadratic functions are shaped like parabolas
# the key features of a parabola depend on the coefficients a, b and c

# the 'a' coefficient controls the steepness of the curve
# larger a, narrower curver, smaller a, wider curve

# the 'b' coeffienct controls the position along the x-axis
# the 'c' coefficient controls the 'y-intercept',
# it moves the parabola up or down, without affecting its curvature

# vertex x = -(b/2a)


# https://www.csun.edu/~ayk38384/notes/mod11/Parabolas.html

a = -1  # parabola steepeness- negative a makes upwards parabolas
b = 0   # controls position along x
c = 0   # controls the y-intercept

vertex_x = -(b / 2*a)
# print(vertex_x) # so you know where the parabola is going to flip back down

steps = 100
x = np.linspace(-2, 2, steps)
y = np.array([])

for i in range(steps):
    y = np.append(y, ((a * (x[i]**2)) + (b * x[i]) + c))  # parabola forumla


print(y)


def animate(i):
    # clear grid data
    ax.cla()

    # print(i)
    # m = np.interp(i, x, y)
    # print("interp value: " + m)

    # reset visuals
    ax.grid()
    # ax.set_xlim(np.min(x), np.max(x) + 1)
    # ax.set_ylim(0, np.max(y) + 1)

    ax.set_xlim(-20, 20)
    ax.set_ylim(min(y) - 1, max(y) + 1)

    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # plot new point
    ax.plot(x, y)
    ax.scatter(x[i], y[i], s=500)


anim = animation.FuncAnimation(fig, animate, repeat=True,
                               frames=len(x) - 1, interval=100)
writer = animation.PillowWriter(fps=24, metadata=dict(artist="ry"),
                                bitrate=2000)
anim.save(args.output, writer=writer)
