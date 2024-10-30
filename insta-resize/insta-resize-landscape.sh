#!/bin/bash
# dependencies: imagemagick - sudo apt install imagemagick
# usage: ./insta-resize.sh image-name.png

wx=$(identify $1 | awk '{print $3}' | cut -f 1 -d x) # width of original image 
hx=$(identify $1 | awk '{print $3}' | cut -f 2 -d x) # height of original image 

# 1:1.91
landscape () {
    # height of original image * 1.91
    n_wx=$(echo "print(int($2 * 1.91))" | python3)

    echo "${n_wx}x$2"
}

# Name of the image thats been input i.e. name without the file extension
IMAGE_NAME=${1%.*}

# create temp white image and composite
convert -size $(landscape $wx $hx) xc: white-composite.png
composite {$1} white-composite.png ${IMAGE_NAME}-comp.png

# scale down to instagram size
convert ${IMAGE_NAME}-comp.png -resize "1080x566" ${IMAGE_NAME}-insta-landscape.png
