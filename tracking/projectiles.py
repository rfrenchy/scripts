# README ME

import argparse

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import math

# cli argument handling
argp = argparse.ArgumentParser("projectiles", 
            description="module of differing projectiles",)
            # usage="python3 --type simple-tracking")
argp.add_argument("-i", "--input", default="")
argp.add_argument("-t", "--type", default="wave")
argp.add_argument("-o", "--output", default="strategy.gif")

# simple-tracking needs to be multiple? comma seperated?

args = argp.parse_args()

# projectile movement definitions 
# TODO
def horizontalmovement(frames, ax):
    # player simulated coordatinates
    # go smoothly across left to right on y = 0
    plyr_x = np.linspace(0, 1, frames)
    plyr_y = np.zeros(frames)

    def animate(i):
        ax.scatter(plyr_x[i], plyr_y[i])
    
    return animate

# def simpletracking(frames, ax, player_cords):
def tracking(frames, ax):
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

def wave(frames, ax):
    plyr_x = np.linspace(0, 1, frames)
    
    theta = np.pi / 2
    up = np.array([0, 1])

    # rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
    #                             [np.sin(theta), np.cos(theta)]])

    
    # print(np.cos(degreestoradians(0)))
    # print(np.cos(degreestoradians(90)))
    # print(np.cos(degreestoradians(180)))
    # print(np.cos(degreestoradians(270)))
    # print(np.cos(degreestoradians(360)))



    # print(up @ rotation(theta))
    

     # unit circle
     # radius = 1 

def degreestoradians(degrees):
     return degrees * (np.pi / 180)

def rotation(theta):
    return np.array([[ np.cos(theta), -np.sin(theta)   ],
                     [ np.sin(theta),  np.cos(theta)   ]])

def triad(frames, ax, translate = [0, 0]):
    # translate = 
    # np.array([0.5, 0.5]) # arbitrary translation
    a = np.array([0, 0]) + translate# x cords?
    p = np.array([[0, 0], [0, -1]]) + translate # point brancing off circle center

    # i only have to pre calc once, then add translatiosn 
    # when needed?

    # [0.5, 0.5] - [[0.5, 0.5], [0.5, 0]]
    # have to try and remember matrix maths...

    # i have my center points and end points,
    # linear space algorithm between?
    # TODO how to to do a linear space algorithm?

    # TODO RADIANS

    # first projectile 
    rot1 = p
    ani_rot1_x = np.linspace(rot1[0][0], rot1[0][1], frames) # x path points
    ani_rot1_y = np.linspace(rot1[1][0], rot1[1][1], frames) # y path points

    # second projectile
    rot2 = rotation(np.pi / 6) @ (p - a) + a
    ani_rot2_x = np.linspace(rot2[0][0], rot2[0][1], frames) # x path points
    ani_rot2_y = np.linspace(rot2[1][0], rot2[1][1], frames) # y path points

    # third projectile
    rot3 = rotation((-np.pi / 6)) @ (p - a) + a
    ani_rot3_x = np.linspace(rot3[0][0], rot3[0][1], frames) # x path points
    ani_rot3_y = np.linspace(rot3[1][0], rot3[1][1], frames) # y path points

    def withpath():
        # plots the path of the projectiles
        ax.plot(rot1[0], rot1[1])
        ax.plot(rot2[0], rot2[1])
        ax.plot(rot3[0], rot3[1])

    def animate(i):
        # plots the movement of projectile along path
        ax.scatter(ani_rot1_x[i], ani_rot1_y[i])
        ax.scatter(ani_rot2_x[i], ani_rot2_y[i])
        ax.scatter(ani_rot3_x[i], ani_rot3_y[i])

    return animate
         
fig, ax = plt.subplots()
frames = 24 # total frames to animate

# pick what to depict based on type passed by cli
animate = None
match args.type: 
    case "simple-tracking":
            a1 = tracking(frames, ax)
            a2 = triad(frames, ax, np.array([0.5, 0.5]))

            def m(i):
                ax.cla()
                ax.grid()
                ax.set_xlim([-0.25, 1.25])
                ax.set_ylim([-0.25, 1.25])

                a1(i), a2(i)

            animate = m
    case "three-pronged":
            a2 = triad(frames, ax)
            def m(i):
                ax.cla()
                ax.grid()
                ax.set_xlim([-0.25, 1.25])
                ax.set_ylim([-0.25, 1.25])

                a2(i)

            animate = m
    case "wave":
          # print("wave")
            wave(frames, ax)
            exit()

# write the file image 
anim = animation.FuncAnimation(fig, animate, repeat=True,
                                   frames=(frames - 1), interval=100)

writer = animation.PillowWriter(fps=12, metadata=dict(artist="ry"),
                                bitrate=1800)

anim.save(args.output, writer=writer)

# plt.show()
