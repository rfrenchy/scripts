# README ME

import argparse

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

argp = argparse.ArgumentParser("tracking", 
                               description="3 projectile path rotated from central point")
argp.add_argument("-i", "--input", default="")
argp.add_argument("-o", "--output", default="")

args = argp.parse_args()

fig, ax = plt.subplots()

# plot/scatter a moving figure moving along x axis, y 0
# generate random point within area (1 > y > 0.5), x whereever

frames = 24

# all coords
player = {
    "x": np.linspace(0.1, 0.9, frames),
    "y": np.zeros(frames)
}

# random y coord in top half of unit square 


# generate initial coords
# np.random.uniform(0.5, 1)
projectile = {
    "x": [np.random.rand()],                    # 1 > x > 0
    "y": [np.random.rand() * (1 - 0.5) + 0.5]   # 1 > y > 0.5
}

tracking_frame = int(frames / 8)

# do nothing up to tracking frame
p1x = np.repeat(projectile.get("x")[0], tracking_frame)
p1y = np.repeat(projectile.get("y")[0], tracking_frame)


# gen last two thrid of frames points based
# on player position at tracking frame
p2x = np.linspace(projectile.get("x")[0], player.get("x")[tracking_frame], frames - tracking_frame)
p2y = np.linspace(projectile.get("y")[0], player.get("y")[tracking_frame], frames - tracking_frame)

track_x = np.concatenate((p1x, p2x))
track_y = np.concatenate((p1y, p2y))

# use magnitude to 

def animate(i):
    ax.cla()
    ax.set_xlim([0, 1])
    ax.set_ylim([-0.25, 1])

    ax.scatter(player.get("x")[i], player.get("y")[i])
    ax.scatter(track_x[i], track_y[i])

anim = animation.FuncAnimation(fig, animate, repeat=True,
                                   frames=(frames - 1), interval=100)

writer = animation.PillowWriter(fps=24, metadata=dict(artist="ry"),
                                bitrate=1800)

anim.save("tracking.gif", writer=writer)

plt.show()
