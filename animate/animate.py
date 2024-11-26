
# usage: python3 animate.py directory-name
# description: stitch together images in a directory into a gif at 24 FPS
import numpy as np
import argparse
import glob

from PIL import Image, ImageOps

# command line argument set up
argp = argparse.ArgumentParser("animate")
argp.add_argument("directory")

args = argp.parse_args()

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

# make a jif
images[0].save("arm-animation.gif",
               save_all=True,
               append_images=images[1:],
               duration=1,
               loop=0)
