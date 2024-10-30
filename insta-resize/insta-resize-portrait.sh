#!/bin/bash
# dependencies: imagemagick - sudo apt install imagemagick
# usage: ./insta-resize.sh image-name.png

wx=$(identify $1 | awk '{print $3}' | cut -f 1 -d x) # width of original image 
hx=$(identify $1 | awk '{print $3}' | cut -f 2 -d x) # height of original image 

# 4:5, simple case for now 
n_wx=$((($2 / 5) * 4))    

# new dimension string
dxx="${n_wx}x$hx"

IMAGE_NAME=${1%.*}

# create temp white image and composite
convert -size $dxx xc: white-composite.png
composite {$1} white-composite.png ${IMAGE_NAME}-comp.png

# scale to instagram sizes
convert ${IMAGE_NAME}-comp.png -resize "1080x1350" ${IMAGE_NAME}-insta-portrait.png
