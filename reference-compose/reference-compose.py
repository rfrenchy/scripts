
# usage: python3 reference-compose.py config-path.json directory-name
import argparse
import glob

from PIL import Image

# command line argument set up
argp = argparse.ArgumentParser("reference-compose")

argp.add_argument("directory")  # todo change to glob
# argp.add_argument("-g", "--glob", default="./*.jpg")
argp.add_argument("-r", "--rows", default=5)
argp.add_argument("-c", "--columns", default=6)
argp.add_argument("-o", "--output", default="pinboard.png")

args = argp.parse_args()

# assumes 1:1 dimensions for each image
image_globs = glob.glob(args.directory + "/*.jpg")
pixels = 800  # size of each image

# main image all the other images will be stitched into
pinboard = Image.new("RGB", (args.columns * pixels, args.rows * pixels))

for i, m in enumerate(image_globs):
    # open and resize image
    img = Image.open(m)
    img.thumbnail((pixels, pixels))

    # calculate where to stitch into pinboard
    x = (i % args.columns) * pixels
    y = (i // args.columns) * pixels

    # paste into pinboard image
    pinboard.paste(img, (x, y))

pinboard.save(args.output)
