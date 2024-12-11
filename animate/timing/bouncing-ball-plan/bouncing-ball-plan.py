
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

y1 = np.array(
    [1, 2, 3, 4, 5, 6, 6.25, 6.5, 6.25, 6, 5, 4, 3, 2, 1])
y_scale_factor = 0.66
y2 = y1 * y_scale_factor
y3 = y2 * y_scale_factor
y4 = y3 * y_scale_factor
y5 = y4 * y_scale_factor
y6 = y5 * y_scale_factor

# work with one arc
# x range 0 - 5, horizontal of one arc, therefore 2.5x is y's peak

# y needs to peak half way between x coords in the arc

y = np.concatenate((y1, y2, y3, y4, y5, y6))
# x = np.array(range(0, len(y)))

# x1 = np.array([0, 1, 2, 3, 4, 5])

x = np.array([])
# x1 = np.linspace(0, 5, 15)
x_shrink_factor = 0.66

mi = 0     # min
ma = 5     # max
st = 15    # steps
sc = 0.66  # scale

x1 = np.linspace(mi, ma, st)
print(x1)
for i in range(6):
    print("mi", mi, "ma", ma)
    m = np.array([x1])
    ma = ((ma * i + 1) * sc) + (ma - mi)
    mi = ma
    print(x1)
    # print("ma", ma)
    x1 = np.linspace(mi, ma, st)

    # print(x1)
    x = np.concatenate((x, x1))


# need to plot line of arc straight away / repeatedly?


def animate(i):
    # clear grid data
    ax.cla()

    # print(i)
    # m = np.interp(i, x, y)
    # print("interp value: " + m)

    # reset visuals
    ax.grid()
    ax.set_xlim(np.min(x), np.max(x) + 1)
    ax.set_ylim(0, np.max(y) + 1)
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
