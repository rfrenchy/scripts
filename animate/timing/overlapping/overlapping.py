import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import math


def overlap(frames=14):
    # build plot
    fig, ax = plt.subplots()

    # https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html#sphx-glr-gallery-mplot3d-2dcollections3d-py
    # fig.add_subplot(projection="3d")

    math.ceil(frames / 2)

    # movement data points (along y-axis)
    mv = np.append(np.linspace(0, 1, math.ceil(frames / 2)),
                   np.linspace(1, 0, math.ceil(frames / 2)))

    # TODO slow-in-slow-out

    # initial data points
    x = np.array([0, 1, 2, 3, 4])

    # graph visual adjustments
    ax.spines.get("top").set_visible(False)
    ax.spines.get("right").set_visible(False)

    # plot movement of each ball for each frame
    def animate(i):
        # clear previous animated data on plot
        ax.cla()
        ax.set_xlim([-1, 5])
        ax.set_ylim([0, 1.5])

        c = (i + 4) % frames  # c-ball's current position
        e = (i + 5) % frames  # e-ball's current position
        r = (i + 6) % frames  # the rest of the balls current position

        # calculate new y positions for each ball based on current frame
        y = np.array([mv[r], mv[r], mv[c], mv[r], mv[e]])

        z = np.zeros(5)

        # new plotted data
        return ax.scatter(x, y)
        # return ax.scatter(x, y, z)

    # animation function for matplotlib
    anim = animation.FuncAnimation(fig, animate, repeat=True,
                                   frames=(frames - 1), interval=100)

    return (fig, anim)
