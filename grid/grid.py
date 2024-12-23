# README ME

import numpy as np
import argparse

from PIL import Image, ImageDraw, ImageOps

# command line argument set up
argp = argparse.ArgumentParser("grid", 
            description="overlays a 2x4 grid on an image", 
            usage="grid.py -i ballerina.jpg -o ballerina-grid.jpg")
argp.add_argument(
    "-i", "--input", help="the url of the input image", type=str)
argp.add_argument("-o", "--output", 
    help="name of output image", type=str)
argp.add_argument("-d", "--debug", help="print debug comments",
					action=argparse.BooleanOptionalAction)

args = argp.parse_args()

# width 157 add

# open the image for processing
img = Image.open(args.input)

# drawer
drw = ImageDraw.Draw(img, "RGBA")

# dimensions
w, h = img.size
if args.debug:
	print(f"Image width: {w}, height: {h}")


# draw vertical line through the iddle
wx = w / 2
drw.line([(wx, 0), (wx, h)], fill=(0, 0, 50, 50), width=16)

for i in range(4):
	hx = h / 4 * i
	drw.line([(0, hx), (w, hx)], fill=(0, 0, 50, 50), width=16)

# draw vertical line through middle


img.save(args.output)

# create a new image with the same size as the original
# add grid lines
# 

# composite grid on top of the image

    # border_img = ImageOps.expand(img,
    #                              border=args.size,
    #                              fill=fill)



# border_img.save(args.output)


# use numpy to add border

# save and close image

