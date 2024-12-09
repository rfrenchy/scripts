import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import math


def overlap(frames=14):
    # build plot
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    # movement data points
    # TODO slow-in-slow-out
    mv = np.append(np.linspace(0, 1, math.ceil(frames / 2)),
                   np.linspace(1, 0, math.ceil(frames / 2)))

    # initial data points
    x = np.array([0, 1, 2, 3, 4])
    y = np.zeros(5)

    # plot movement of balls for each frame
    def animate(i):
        # clear previous animated data on plot
        ax.cla()

        # reset axis data
        ax.set_xlim([-1, 5])
        ax.set_ylim([-1, 1])
        ax.set_zlim([0, 1])

        ax.set_xticklabels(["", "A", "B", "C", "D", "E", ""])
        # ax.set_yticks([])
        ax.set_yticklabels([])
        # ax.set_zticks([])

        c = (i + 4) % frames  # c-ball's current position
        e = (i + 5) % frames  # e-ball's current position
        r = (i + 6) % frames  # the rest of the balls current position

        # calculate new y positions for each ball based on current frame
        z = np.array([mv[r], mv[r], mv[c], mv[r], mv[e]])

        # new plotted data
        return ax.scatter(x, y, z, zdir="z")

    # animation function for matplotlib
    anim = animation.FuncAnimation(fig, animate, repeat=True,
                                   frames=(frames - 1), interval=100)

    return (fig, anim)
