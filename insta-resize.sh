#!/bin/bash
# dependencies: imagemagick - sudo apt install imagemagick

IMAGE_NAME=$(echo $1 | cut -f 1 -d .)

# get and compare both dimensions and store biggest
wxh=$(identify $1 | awk '{print $3}')

w=$(echo $wxh | cut -f 1 -d x)
h=$(echo $wxh | cut -f 2 -d x)
x=$((w > h ? w : h))

# create temp white image and composite
convert -size ${x}x${x} xc: white-composite.png
composite {$1} white-composite.png ${IMAGE_NAME}-comp.png

# scale to instagram size (1024x1024)
convert ${IMAGE_NAME}-comp.png -resize 1024x1024 ${IMAGE_NAME}-insta-1x1.png

