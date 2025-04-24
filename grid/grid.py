import argparse
import re

from PIL import Image, ImageDraw

# command line argument set up
argp = argparse.ArgumentParser("grid", 
            description="overlays a grid on an image", 
            usage="grid.py -i ballerina.jpg -o ballerina-grid.jpg -x 4x4")
argp.add_argument(
    "-i", "--input", help="the url of the input image", type=str)
argp.add_argument("-o", "--output", 
    help="name of output image", type=str)
argp.add_argument("-x", "--dimensions", 
    help="dimension string", type=str)
argp.add_argument("-d", "--debug", help="print debug comments",
					action=argparse.BooleanOptionalAction)

args = argp.parse_args()

wid = 4
hei = 4

if args.dimensions is not None:
	dstring = re.search(r'(\d+)x(\d+)', args.dimensions)
	wid = int(dstring.group(1))
	hei = int(dstring.group(2))

# open the image for processing
img = Image.open(args.input)

# Image drawer
drw = ImageDraw.Draw(img, "RGBA")

# image dimensions
w, h = img.size
if args.debug:
	print(f"Image width: {w}, height: {h}")

# draw line across 'wid' times
dw = w / wid
dwx = dw

for i in range(wid):
	drw.line([(dwx, 0),(dwx, h)], fill=(0,0,50,50), width=16) # down
	dwx = dwx + dw

# draw line vertical 'hei' times
dh = h / hei
dhx = dh

for i in range(hei):
	drw.line([(0, dhx), (w, dhx)], fill=(0,0,50,50), width=16) 
	dhx = dhx + dh

# save output
img.save(args.output)
