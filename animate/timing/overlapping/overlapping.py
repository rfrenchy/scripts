import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import math


def move_coordinates_v1(frames):
    return np.append(np.linspace(0, 1, math.ceil(frames / 2)),
                     np.linspace(1, 0, math.ceil(frames / 2)))


def key_coordintes_v1(i, frames):
    return ((i + 4) % frames,  # c-ball's current position
            (i + 5) % frames,  # e-ball's current position
            (i + 6) % frames)  # the rest of the balls current position


def move_coordinates_v2():
    # halves timing
    return np.array([1, 0.95, 0.925, 0.9, 0.875, 0.75, 0.5, 0.25, 0.125, 0.1, 0.05, 0])


def overlap(frames=14):
    # build plot
    fig = plt.figure()
    fig.set_tight_layout(True)

    ax = fig.add_subplot(projection="3d")

    # movement data points
    # TODO slow-in-slow-out

    # may need to remove 1 back down to 0, which means
    # have to change for loop go back down when over 7
    mv = move_coordinates_v1(frames)
    # mv = move_coordinates_v2()

    # numpy.interp
    # arg 1: coordinate/key whose value needs to be interpolated
    # arg 2: keys (x axis)
    # arg 3: values (y/z axis?)

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

        c, e, r = key_coordintes_v1(i, frames)

        # calculate new y positions for each ball based on current frame
        z = np.array([mv[r], mv[r], mv[c], mv[r], mv[e]])

        # new plotted data
        return ax.scatter(x, y, z, zdir="z", depthshade=False)

    # animation function for matplotlib
    anim = animation.FuncAnimation(fig, animate, repeat=False,
                                   frames=(frames - 1), interval=100)

    return (fig, anim)
