
# usage: python3 animate.py config-path.json directory-name
# description: gif together images from a directory
import argparse
import glob
import json

from PIL import Image
from commands import FromConfig

# command line argument set up
argp = argparse.ArgumentParser("animate")

argp.add_argument("-g", "--glob", default="./*.jpg")
argp.add_argument("-j", "--json", required=False)
argp.add_argument("-o", "--output", default="animate.gif")

args = argp.parse_args()

commands = []

if args.glob:
    print(args.glob)

if args.json:
    print(args.json)

images = []
# get all .jpg's in given directory
for f in glob.glob(args.glob):
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
