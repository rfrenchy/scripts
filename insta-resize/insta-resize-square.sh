#!/bin/bash
# dependencies: imagemagick - sudo apt install imagemagick
# usage: ./insta-resize.sh image-name.png

# get original height and width
wx=$(identify "$1" | awk '{print $3}' | cut -f 1 -d x) 
hx=$(identify "$1" | awk '{print $3}' | cut -f 2 -d x)

# find the biggest of the two
dx=$((wx > hx ? wx : hx))
# 1:1 dimension string
dxx="${dx}x${dx}" 

IMAGE_OUTPUT_NAME=${1%.*} # Name of the image thats been input i.e. name without the file extension

# create temp white image and composite
convert -size $dxx xc: white-composite.png
composite "$1" white-composite.png "$IMAGE_OUTPUT_NAME"-comp.png

# scale to instagram sizes
convert "$IMAGE_OUTPUT_NAME"-comp.png -resize "1080x1080" "$IMAGE_OUTPUT_NAME"-insta-square.png

# MISC split by word for each line. at each word index for each line, find max word length at index, and fill all the others with spaces to max word length for that index
