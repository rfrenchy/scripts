# usage: add_border.py my_image.png
import numpy as np
import argparse

from PIL import Image, ImageOps

# command line argument set up
argp = argparse.ArgumentParser("add_border")
argp.add_argument("image_url")

# gradient args,Todo make gradient args a tuple?
argp.add_argument("gradient_start", "-gs")
argp.add_argument("gradient_end", "-ge")
argp.add_argument("steps", "-st")

args = argp.parse_args()

# open the image for processing
img = Image.open(args.image_url)

# start and end colours for border gradient
lambent = np.array([165, 229, 255])
storm   = np.array([0, 71, 100])

## number of interpolations
N = 50

for i in range(N):
    # get interpolated color
    cx = lambent + (i / (N - 1)) * (storm - lambent)

    #pix = img.load()

    x  = np.rint(cx).astype(int)
    fill = (x[0],x[1],x[2])

    # might need to change to pad

    border_img = ImageOps.expand(img,
        border=1,
        fill=fill)

    img = border_img

    
    # img = border_img    

border_img.save("bordered_" + args.image_url)

    # use numpy to add border

# save and close image
