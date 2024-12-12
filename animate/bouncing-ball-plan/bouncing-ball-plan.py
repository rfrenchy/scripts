
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
# fig.set_figwidth(1.91 * 10)
# fig.set_figheight(1 * 10)

fig.set_figwidth(6)
fig.set_figheight(3)

# COORD PLANNING PHASE

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

# quadratic has to move from negative to the positive to plot as a curve?
# only curves at this inflexion point?


# https://www.csun.edu/~ayk38384/notes/mod11/Parabolas.html

a = -5  # parabola steepeness- negative a makes upwards parabolas
b = 0   # controls position along x
c = 0  # controls the y-intercept, the max y?


def parabola(x = [], a = -1 , b = 0, c = 0):
    y = np.array([])

    for i in range(len(x)):
        yi = ((a * (x[i]**2)) + (b* x[i]) + c)
        if yi < 0:
            yi = 0
        y = np.append(y, yi) 

    return y




x = np.array([])
y = np.array([])

steps = 24
x1 = np.linspace(-3, 3, steps)
c = 40
for i in range(10):
    x = np.append(x, x1 + (5 * (i+1)))     
    y = np.append(y, parabola(x1, -5, 0, c))
    c = c * (2/3)




#x2 = np.linspace(-3, 3, steps)
#y2 = parabola(x2, -5, 0, 40 * (2/3))

# x = np.concatenate((x1 + 3, x1 + 9))
#y = np.concatenate((y1, y2))

# chop off a golden section amount each time?

# increase in a, decrease in c, reduction in range in x
# c coefficent influenced by x coords?

# y = (a * pow(x,2)) + (b * x) + c
# can i find x from this?

def animate(i):
    # clear grid data
    ax.cla()

    # reset visuals
    ax.grid()
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 60)

    ax.plot(x, y)
    # ax.scatter(x[i], y[i], s=100)


anim = animation.FuncAnimation(fig, animate, repeat=True,
                               frames=len(x) - 1, interval=100)
writer = animation.PillowWriter(fps=24, metadata=dict(artist="ry"),
                                bitrate=2000)
anim.save(args.output, writer=writer)
