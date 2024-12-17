import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import time

# build plot
fig, ax = plt.subplots()

frames = 24

def rotation(theta):
    return np.array([[ np.cos(theta), -np.sin(theta)   ],
                     [ np.sin(theta),  np.cos(theta)   ]])

def growingcircle(scale = 1):
    a = np.array([0, 0]) # circle center
    b = np.array([0, 1])

    # rotation angle (360/8 = 45)
    rots = 60
    theta =(2 * np.pi) / rots

    circle_x = np.array([])
    circle_y = np.array([])

    for i in range(rots):
        m = rotation(theta * i) @ b
        circle_x = np.append(circle_x, m[0])
        circle_y = np.append(circle_y, m[1])

    # last entry to join back up to make full circle
    circle_x = np.append(circle_x, circle_x[0])
    circle_y = np.append(circle_y, circle_y[0])

    circle_x = circle_x * scale
    circle_y = circle_y * scale

    # probably a better way to plot a circle than 
    # this, curve function?

    # ax.cla()
    ax.axis("equal")
    ax.set_title("frame " + str(scale + 1))
    ax.set_xlim(-50, 50)
    ax.set_ylim(-50, 50)
    ax.plot(circle_x, circle_y)


# growingcircle(ax, frames)

# fig.savefig("circle.jpg")


# ax.axis("equal")
# ax.set_xlim(-24, 24)
# ax.set_ylim(-24, 24)

anim = animation.FuncAnimation(fig, growingcircle, repeat=False,
                                frames=24, interval=100)

writer = animation.PillowWriter(fps=12, metadata=dict(artist="ry"),
                                 bitrate=1800)

anim.save("circle.gif", writer=writer)


with open("vid.txt", "w") as text_file:
    text_file.write(anim.to_html5_video())
