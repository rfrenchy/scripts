
# usage: python3 animate.py config-path.json directory-name
# description: gif together images from a directory
import argparse
import glob
import json

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from commands import FromConfig

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

with open("in-halves.json") as shot_json:
    shot = json.load(shot_json)

    fc = FromConfig()
    fc.ToGIF(shot, images)
