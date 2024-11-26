
# usage: python3 animate.py directory-name
# description: stitch together images in a directory into a gif
import numpy as np
import argparse
import glob

from PIL import Image, ImageOps

# command line argument set up
argp = argparse.ArgumentParser("animate")
argp.add_argument("directory")

args = argp.parse_args()

# images: tuple[Any, ImageFile] = []
images = []
# get all images in given directory
for f in glob.glob(args.directory + "/*.jpg"):
    images.append((f, Image.open(f)))

# sort the images by file name
sorted_images = sorted(images)

# extract just the images now they are ordered
images = []
for i in sorted_images:
    images.append(i[1])


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


write_in_halfs(images)


# arm specific settings
# inbetween in halfs?
