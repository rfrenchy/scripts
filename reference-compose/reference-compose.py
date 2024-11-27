
# usage: python3 reference-compose.py config-path.json directory-name
import argparse
import glob
import math


from PIL import Image

# command line argument set up
argp = argparse.ArgumentParser("reference-compose")
argp.add_argument("directory")

args = argp.parse_args()

# assumes 1:1 dimensions for each image

image_globs = glob.glob(args.directory + "/*.jpg")

# stiched image properties
pixels = 800  # size of each image
rows = 5
columns = math.ceil(len(image_globs) / rows)

# main image all the other images will be stitched into
stitched_image = Image.new("RGB", (columns * pixels, rows * pixels))

# print(len(image_globs))
for i, x in enumerate(image_globs):
    # open and resize image
    img = Image.open(x)
    img.thumbnail((pixels, pixels))

    # calculate where to stitch into main image
    x = (i % columns) * pixels
    y = (i // columns) * pixels

    # print(x)
    # print(y)

    # pase into main image
    stitched_image.paste(img, (x, y))

stitched_image.save("stiched_image.png")
