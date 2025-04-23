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

DIVISIONS = 4

dw = w / DIVISIONS
dh = h / DIVISIONS

dwx = dw
dhx = dh

for i in range(DIVISIONS):
	drw.line([(0, dwx), (w, dwx)], fill=(0,0,50,50), width=16) # across
	drw.line([(dhx, 0),(dhx, h)], fill=(0,0,50,50), width=16) # down
	
	dwx = dwx + dw
	dhx = dhx + dh

# for i in range(DIVISIONS):
#     wx = w / DIVISIONS * i
# 		# drw.line([(wx, 0), (wx, h)], fill=(0, 0, 50, 50), width=16)


img.save(args.output)
