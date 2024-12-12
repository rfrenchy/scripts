import numpy as np
import argparse

from PIL import Image, ImageOps

# command line argument set up
argp = argparse.ArgumentParser("add_border", description="adds a border to an image", usage="add_border.py -i van-dyck.jpg --size 89 -o bordered-van-dyck.jpg")
argp.add_argument(
    "-i", "--input", help="the url of the image you want to add a border to", type=str)
argp.add_argument("-o", "--output", help="name of output", type=str)

WHITE = np.array([255, 255, 255])

argp.add_argument("--size", help="border size to apply", default=25, type=int)
argp.add_argument("-gs", "--gradientstart", default=WHITE, help="" )
argp.add_argument("-ge", "--gradientend", default=WHITE)
argp.add_argument("-st", "--steps", default=1)

args = argp.parse_args()

# open the image for processing
img = Image.open(args.input)

# start and end colours for border gradient
# lambent = np.array([165, 229, 255])
# storm = np.array([0, 71, 100])

# number of interpolations
N = args.steps

# check if need to interpolate color
same_color = (args.gradientstart == args.gradientend).all()

cx = WHITE

for i in range(N):
    # get interpolated color
    if not same_color:
        cx = args.gradientend + (i / (N - 1)) * \
            (args.gradientend - args.gradientstart)

    x = np.rint(cx).astype(int)

    # RGB of border color fill
    fill = (x[0], x[1], x[2])

    # might need to change to pad

    border_img = ImageOps.expand(img,
                                 border=args.size,
                                 fill=fill)

    img = border_img


border_img.save(args.output)


# use numpy to add border

# save and close image
