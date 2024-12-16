# README ME

import argparse

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

argp = argparse.ArgumentParser("tracking", 
                               description="simulate tracking a player with a projectile")
argp.add_argument("-i", "--input", default="")
argp.add_argument("-o", "--output", default="simple-tracking.gif")

args = argp.parse_args()

fig, ax = plt.subplots()

# total frames to animate
frms = 24

# player simulated coordatinates
# go smoothly across left to right on y = 0
plyr_x = np.linspace(0, 1, frms)
plyr_y = np.zeros(frms)

# generate projectile initial coords
# project start coords (could use np.random.uniform(.5,1) but o well)
prj_start_x = np.random.rand()                     # 1 > x > 0
prj_start_y = np.random.rand() * (1 - 0.5) + 0.5   # 1 > y > 0.5

# the frame the projectile will start tracking the player from
track_frame = int(frms / 8)

# do nothing up to tracking frame
p1x = np.repeat(prj_start_x, track_frame)
p1y = np.repeat(prj_start_y, track_frame)

# generate coords based on player position on tracking frame
p2x = np.linspace(prj_start_x, plyr_x[track_frame], frms - track_frame)
p2y = np.linspace(prj_start_y, plyr_y[track_frame], frms - track_frame)

# add full frame coords together
trck_x = np.concatenate((p1x, p2x))
trck_y = np.concatenate((p1y, p2y))

def animate(i):
    ax.cla()
    ax.set_xlim([-0.25, 1.25])
    ax.set_ylim([-0.25, 1.25])

    # plot player and projectile positions
    ax.scatter(plyr_x[i], plyr_y[i])
    ax.scatter(trck_x[i], trck_y[i])

anim = animation.FuncAnimation(fig, animate, repeat=True,
                                   frames=(frms - 1), interval=100)

writer = animation.PillowWriter(fps=24, metadata=dict(artist="ry"),
                                bitrate=1800)

anim.save(args.output, writer=writer)

plt.show()

# TODO combine with movement-arc projectile?
# means exporting coordinates?
# single file exporting 'enemies'/'projectiles'?
# def tracking-projectile():
# def three-pronged-projectile():
# main file to animate 'scene'?