# usage: add_border.py my_image.png
import numpy as np
import argparse

from PIL import Image, ImageOps

# command line argument set up
argp = argparse.ArgumentParser("add_border")
argp.add_argument(
    "image_url", "-i", help="the url of the image you want to add a border to", type=str)

WHITE = np.array([255, 255, 255])

argp.add_argument("-gs", "--gradientstart", default=WHITE)
argp.add_argument("-ge", "--gradientend", default=WHITE)
argp.add_argument("-st", "--steps", default=1)

args = argp.parse_args()

# open the image for processing
img = Image.open(args.image_url)

# start and end colours for border gradient
# lambent = np.array([165, 229, 255])
# storm = np.array([0, 71, 100])

# number of interpolations
N = 50

# check if need to interpolate color
change_color = (args.gradientstart == args.gradientend).all()

print(change_color)

for i in range(N):
    # get interpolated color
    if change_color:
        cx = args.gradientend + (i / (N - 1)) * \
            (args.gradientend - args.gradientstart)

    x = np.rint(cx).astype(int)
    fill = (x[0], x[1], x[2])

    # might need to change to pad

    border_img = ImageOps.expand(img,
                                 border=1,
                                 fill=fill)

    img = border_img


border_img.save("bordered_" + args.image_url)


# use numpy to add border

# save and close image
