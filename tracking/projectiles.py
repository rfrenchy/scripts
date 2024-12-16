# README ME

import argparse

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# cli argument handling
argp = argparse.ArgumentParser("projectiles", 
            description="module of differing projectiles")
argp.add_argument("-i", "--input", default="")
argp.add_argument("-t", "--type", default="simple-tracking")
argp.add_argument("-o", "--output", default="strategy.gif")

# simple-tracking needs to be multiple? comma seperated?

args = argp.parse_args()

# helpers, seperate into top level module?
def rotation(theta):
    return np.array([[ np.cos(theta), -np.sin(theta)   ],
                     [ np.sin(theta),  np.cos(theta)   ]])

# projectile movement definitions 
# TODO
def simpleplayerhorizontalmovement(frames, ax):
    # player simulated coordatinates
    # go smoothly across left to right on y = 0
    plyr_x = np.linspace(0, 1, frames)
    plyr_y = np.zeros(frames)

    def animate(i):
        ax.scatter(plyr_x[i], plyr_y[i])
    
    return animate

# def simpletracking(frames, ax, player_cords):
def simpletracking(frames, ax):
    # need to pass player coords as an arg?
    # on twos, (too complicated for me to think with other calc for now)
    # on_twos = int(frames / 2)
    # plyr_x = np.sort(np.concatenate((np.linspace(0, 1, on_twos), np.linspace(0, 1, on_twos))))

    plyr_x = np.linspace(0, 1, frames)
    plyr_y = np.zeros(frames)
    
    # generate projectile initial coords
    # project start coords (could use np.random.uniform(.5,1) but o well)
    prj_start_x = np.random.rand()                     # 1 > x > 0
    prj_start_y = np.random.rand() * (1 - 0.5) + 0.5   # 1 > y > 0.5
    
    # the frame the projectile will start tracking the player from
    track_frame = int(frames / 8)
    
    # do nothing up to tracking frame
    p1x = np.repeat(prj_start_x, track_frame)
    p1y = np.repeat(prj_start_y, track_frame)
    
    # generate coords based on player position on tracking frame
    p2x = np.linspace(prj_start_x, plyr_x[track_frame], frames - track_frame)
    p2y = np.linspace(prj_start_y, plyr_y[track_frame], frames - track_frame)
    
    # add full frame coords together
    trck_x = np.concatenate((p1x, p2x))
    trck_y = np.concatenate((p1y, p2y))
    
    def animate(i):
        # plot player and projectile positions
        ax.scatter(plyr_x[i], plyr_y[i])
        ax.scatter(trck_x[i], trck_y[i])

    return animate

def threepronged(frames, ax):
    a = np.array([0.5, 0.5])# x cords?
    p = np.array([[0.5, 0.5], [0.5, 0]]) # point brancing off circle center

    # x ??
    # a = np.array([0.5, 0.8])# cicle center
    # p = np.array([0.5, 0.5], [0.8, 0.3]) # point brancing off circle center
    # y = rotation(np.pi / 4 ) @ np.linspace(0, 1, 24)

    # on 2's?

    # print(rotation(np.pi / 4))
    # print(np.linspace(0, 1, 24))
    # print(y)

    rot1 = p
    rot2 = rotation(np.pi / 4) @ (p - a) + a
    rot3 = rotation((-np.pi / 4)) @ (p - a) + a

    print(rot2)

    # plot a straight line with rotation applied
    # pre calculate path coords
    def animate(_):
        ax.plot(rot1[0], rot1[1])
        ax.plot(rot2[0], rot2[1])
        ax.plot(rot3[0], rot3[1])
    
    return animate
         

fig, ax = plt.subplots()
frames = 24 # total frames to animate

# pick what to depict based on type passed by cli
animate = None
match args.type: 
    case "simple-tracking":
            a1 = simpletracking(frames, ax)
            a2 = threepronged(frames, ax)

            def m(i):
                ax.cla()
                ax.set_xlim([-0.25, 1.25])
                ax.set_ylim([-0.25, 1.25])

                a1(i)
                a2(i)

            animate = m
    case "three-pronged-projectile":
            a2 = threepronged(frames, ax)

# write the file image 
anim = animation.FuncAnimation(fig, animate, repeat=True,
                                   frames=(frames - 1), interval=100)

writer = animation.PillowWriter(fps=24, metadata=dict(artist="ry"),
                                bitrate=1800)

anim.save(args.output, writer=writer)

# plt.show()
