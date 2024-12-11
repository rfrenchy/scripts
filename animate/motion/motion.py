
# usage: python3 parabola.py


import argparse

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


argp = argparse.ArgumentParser("overlap")
argp.add_argument("-o", "--output", default="motion.gif")
args = argp.parse_args()


def fig_one():
    fig, ax = plt.subplots()

    # set fig dimensions (landscape aspect ratio)
    fig.set
    fig.set_figwidth(1.91 * 4)
    fig.set_figheight(1 * 4)

    x = np.array(range(0, 15)) * 2
    y = np.array([1, 2, 3, 4, 5, 6, 6.25, 6.5, 6.25, 6, 5, 4, 3, 2, 1])

    def animate(i):
        # clear grid data
        ax.cla()

        # print(i)
        # m = np.interp(i, x, y)
        # print("interp value: " + m)

        # reset visuals
        ax.grid()
        ax.set_xlim(np.min(x), np.max(x) + 1)
        ax.set_ylim(0, 6.5)
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        # plot new point
        ax.scatter(x[i], y[i])

    anim = animation.FuncAnimation(fig, animate, repeat=True,
                                   frames=len(x) - 1, interval=100)

    writer = animation.PillowWriter(fps=24, metadata=dict(artist="ry"),
                                    bitrate=2000)

    anim.save(args.output, writer=writer)


def fig_two():
    # ball bouncing
    fig, ax = plt.subplots()

    # set fig dimensions (landscape aspect ratio)
    fig.set
    fig.set_figwidth(1.91 * 4)
    fig.set_figheight(1 * 4)

    x = np.array(range(0, 45))

    y1 = np.array(
        [1, 2, 3, 4, 5, 6, 6.25, 6.5, 6.25, 6, 5, 4, 3, 2, 1])
    scale_factor = 0.8
    y2 = y1 * scale_factor
    y3 = y2 * scale_factor

    y = np.concatenate((y1, y2, y3))

    def animate(i):
        # clear grid data
        ax.cla()

        # print(i)
        # m = np.interp(i, x, y)
        # print("interp value: " + m)

        # reset visuals
        ax.grid()
        ax.set_xlim(np.min(x), np.max(x) + 1)
        ax.set_ylim(0.5, np.max(y) + 1)
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        # plot new point
        ax.scatter(x[i], y[i])

    anim = animation.FuncAnimation(fig, animate, repeat=True,
                                   frames=len(x) - 1, interval=100)

    writer = animation.PillowWriter(fps=24, metadata=dict(artist="ry"),
                                    bitrate=2000)

    anim.save(args.output, writer=writer)


fig_two()
