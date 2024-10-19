#!/bin/bash
# dependencies: imagemagick - sudo apt install imagemagick
# usage: ./insta-resize.sh image-name.png

# Instagram defined image sizes
SQUARE="1080x1080"
LANDSCAPE="1080x566"
PORTRAIT="1080x1350"

# Name of the image thats been input i.e. name without the file extension
IMAGE_NAME=${1%.*}

wx=$(identify $1 | awk '{print $3}' | cut -f 1 -d x) # width of original image 
hx=$(identify $1 | awk '{print $3}' | cut -f 2 -d x) # height of original image 

# 1:1
square () {
    # find the biggest of the two
    x=$(($1 > $2 ? $1 : $2))
    
    # return new dimensions
    echo "${x}x${x}"
    
    # TODO return image from function with image magick
    # e.g. echo $(convert -size $(square $dx) xc: white-composite.png)
}

# 1:1.91
landscape () {
    # have min height of original image
    # make width 1.91 : of that
    # or add to height to make 1.19
    echo ((1.91 * $2))
}

echo $(landscape $wx $hx)

# 4:5
portrait () {
    echo ""

}

# create temp white image and composite
convert -size $(square $wx $hx) xc: white-composite.png
composite {$1} white-composite.png ${IMAGE_NAME}-comp.png

# TODO get difference between biggest and smallest dimension
# shift original image 1/2 in that direction on composite

# scale to instagram sizes
convert ${IMAGE_NAME}-comp.png    -resize ${SQUARE}    ${IMAGE_NAME}-insta-square.png
# convert ${IMAGE_NAME}-landscape.png -resize ${LANDSCAPE} ${IMAGE_NAME}-insta-landscape.png
# convert ${IMAGE_NAME}-portrait.png  -resize ${PORTRAIT}  ${IMAGE_NAME}-insta-portrait.png

# split by word for each line. at each word index for each line, find max word length at index, and fill all the others with spaces to max word length for that index

# remove temp white image
# rm ${IMAGE_NAME}-comp.png
