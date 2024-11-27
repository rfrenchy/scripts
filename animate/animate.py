
# usage: python3 animate.py config-path.json directory-name
# description: gif together images from a directory
import argparse
import glob
import json

import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from animators import FromConfig

# command line argument set up
argp = argparse.ArgumentParser("animate")
argp.add_argument("directory")
argp.add_argument("json-path")

args = argp.parse_args()

images = []
# get all .jpg's in given directory
for f in glob.glob(args.directory + "/*.jpg"):
    # for f in glob.glob(args.directory + "/*.png"):
    images.append((f, Image.open(f)))

# sort the images by file name
sorted_images = sorted(images)

# extract just the images now they are ordered
images = []
for i in sorted_images:
    images.append(i[1])


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


with open("in-halves.json") as shot_json:
    shot = json.load(shot_json)

    fc = FromConfig()
    fc.ToGIF(shot, images)
    shot_to_plot(shot)
