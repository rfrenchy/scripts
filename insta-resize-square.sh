#!/bin/bash
# dependencies: imagemagick - sudo apt install imagemagick
# usage: ./insta-resize.sh image-name.png

# get original height and width
wx=$(identify $1 | awk '{print $3}' | cut -f 1 -d x) 
hx=$(identify $1 | awk '{print $3}' | cut -f 2 -d x)

# find the biggest of the two
dx=$(($1 > $2 ? $1 : $2))

# 1:1 dimension string
dxx="${x}x${x}" 

# create temp white image and composite
convert -size $dxx xc: white-composite.png
composite {$1} white-composite.png ${IMAGE_NAME}-comp.png

IMAGE_NAME=${1%.*} # Name of the image thats been input i.e. name without the file extension

# scale to instagram sizes
convert ${IMAGE_NAME}-comp.png -resize "1080x1080" ${IMAGE_NAME}-insta-square.png

# MISC split by word for each line. at each word index for each line, find max word length at index, and fill all the others with spaces to max word length for that index
