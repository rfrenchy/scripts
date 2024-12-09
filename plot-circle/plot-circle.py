import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# build plot
fig = plt.figure()
# fig.set_tight_layout(True)
ax = fig.add_subplot(projection="3d")
# ax = fig.add_subplot()

frames = 1

# given circles center point
# measure out from center to an edge = D
# then circle formula to find the rest of the points?

# ax.fill_between()

c = plt.Circle((0, 0), radius=5, color="purple")

# area = pi * (r * r)

# TODO
# https://stackoverflow.com/questions/56870675/how-to-do-a-3d-circle-in-matplotlib


def animate(i):
    # clear previous animated data on plot
    ax.cla()

    # reset axis data
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])

    ax.add_patch(c)


# animation function for matplotlib
anim = animation.FuncAnimation(fig, animate, repeat=False,
                               frames=1, interval=100)

writer = animation.PillowWriter(fps=12, metadata=dict(artist="ry"),
                                bitrate=1800)

anim.save("circle.gif", writer=writer)
