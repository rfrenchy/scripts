
# usage: python3 animate.py config-path.json directory-name
# description: gif together images from a directory
import argparse
import glob
import json

import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

# command line argument set up
argp = argparse.ArgumentParser("animate")
argp.add_argument("directory")

args = argp.parse_args()

images = []
# get all .jpg's in given directory
for f in glob.glob(args.directory + "/*.jpg"):
    images.append((f, Image.open(f)))

# sort the images by file name
sorted_images = sorted(images)

# extract just the images now they are ordered
images = []
for i in sorted_images:
    images.append(i[1])


def shot_to_gif(shot, images):
    M = []  # preallocate 24 spaces in array?

    for i, frame in enumerate(shot):
        for _ in range(shot[frame]):
            M.append(images[i])

    # TODO 25 frames? issue? how to test?
    M[0].save("arms-config-test.gif",
              save_all=True,
              append_images=M[1:],
              duration=1,
              loop=0)


def shot_to_plot(shot):
    """ Plots timings
        @param json - the config for the frame
    """
    # x coords (frame/time?)
    x = np.array([])
    xi = 1

    # todo, fix, should be same size as x, all 1s
    y = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])

    for sketch_number, frame in enumerate(shot):
        shot[frame]
        x = np.append(x, xi)
        xi += shot[frame]

    plt.scatter(x, y)
    plt.savefig("timing.jpg", bbox_inches="tight")


def write_in_ones(images):
    """ Write gif in ones

        @param images, a sorted array of singular drawings
    """

    images[0].save("arm-in-ones.gif",
                   save_all=True,
                   append_images=images[1:],
                   duration=1,
                   loop=0)


def write_in_twos(images):
    """ Write gif of images with each drawing repeated twice over 1 second

        @param images, a sorted array of images
    """

    in_twos = []
    for i in images:
        in_twos.append(i)
        in_twos.append(i)

    in_twos[0].save("arm-in-twos.gif",
                    save_all=True,
                    append_images=in_twos[1:],
                    duration=1,
                    loop=0)


def write_in_halfs(images):
    """ Write gif with halves timing (specific to arms animation for now)

        @param images, a sorted array of images
    """
    in_halves = []

    for i in range(4):
        in_halves.append(images[0])  # frame 1
    for i in range(3):
        in_halves.append(images[1])  # frame 2
    for i in range(3):
        in_halves.append(images[2])  # frame 3
    for i in range(2):
        in_halves.append(images[3])  # frame 4
    for i in range(1):
        in_halves.append(images[4])  # frame 5
    for i in range(2):
        in_halves.append(images[5])  # frame 6
    for i in range(3):
        in_halves.append(images[6])  # frame 7
    for i in range(3):
        in_halves.append(images[7])  # frame 8
    for i in range(4):
        in_halves.append(images[8])  # frame 9

    in_halves[0].save("arm-in-halves.gif",
                      save_all=True,
                      append_images=in_halves[1:],
                      duration=1,
                      loop=0)


with open("in-halves.json") as shot_json:
    shot = json.load(shot_json)

    shot_to_gif(shot, images)
    shot_to_plot(shot)

# write_in_halves(images)

# write_in_thrids

# write_in_quarters
