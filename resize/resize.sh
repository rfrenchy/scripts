#!/bin/bash
# dependencies: imagemagick - sudo apt install imagemagick
# usage: ./insta-resize.sh image-name.png

# MISC split by word for each line. at each word index for each line, find max word length at index, and fill all the others with spaces to max word length for that index

# convert image into square instagramable image
square() {
    # echo "square mode (1:1)"

    wx=$(identify "$1" | awk '{print $3}' | cut -f 1 -d x)
    hx=$(identify "$1" | awk '{print $3}' | cut -f 2 -d x)


    # Find biggest dimension of either width or either,
    # then use to make 1:1 dimension string
    dx=$((wx > hx ? wx : hx))
    dxx="${dx}x${dx}"

    # Use the name of the image thats been input, minus the file extension
    # e.g. my-picture.png becomes my-picture
    IMAGE_OUTPUT_NAME=${1%.*}

    # Create a white image at the new calculated dimension and
    # composite with the original image
    convert -size $dxx xc: white-composite.png
    composite "$1" white-composite.png "$IMAGE_OUTPUT_NAME"-comp.png

    # Scale composited image to instagram's square measurements
    convert "$IMAGE_OUTPUT_NAME"-1x1.png -resize "1080x1080" "$IMAGE_OUTPUT_NAME"-insta-square.png
}

portrait() {
    echo "portrait mode (5:4)"
    #wx=1080 # default width to instagram portrait width
    #hx=1350 # default height to instagram portrait height

    # wx=$(identify "$1" | awk '{print $3}' | cut -f 1 -d x)
    hx=$(identify "$1" | awk '{print $3}' | cut -f 2 -d x)
    wx="$(((hx / 5) * 4))"
    dx="${wx}x${hx}"

    # Use the name of the image thats been input, minus the file extension
    # e.g. my-picture.png becomes my-picture
    IMAGE_OUTPUT_NAME=${1%.*}

    # Create a white image at the new calculated dimension and
    # composite with the original image
    convert -size "$dx" xc: white-composite.png
    composite "$1" white-composite.png "$IMAGE_OUTPUT_NAME"-comp.png

    # Scale composited image to instagram's portrait measurements
    convert "$IMAGE_OUTPUT_NAME"-comp.png -resize "1080x1350" "$IMAGE_OUTPUT_NAME"-insta-portrait.png

    #echo $1

    # if either width/height is less than instagrams 1080x1350 or a ratio is less that 1080x1350, make that the minimum and multiple the other
    #if [ "$1" -lt $wx ]; then
     #   echo "less than $wx"
    #fi

    # continue


    # n_wx=$((($2 / 5) * 4))
    # convert ${IMAGE_NAME}-comp.png -resize "1080x1350" ${IMAGE_NAME}-insta-portrait.png
}

landscape() {
    echo "landscape"

    # n_wx=$(echo "print(int($2 * 1.91))" | python3)
    # convert ${IMAGE_NAME}-comp.png -resize "1080x566" ${IMAGE_NAME}-insta-landscape.png
}


# Get original height and width
# TODO GET WORKING
# wx=$(identify "$1" | awk '{print $3}' | cut -f 1 -d x)
# hx=$(identify "$1" | awk '{print $3}' | cut -f 2 -d x)

case "$1" in
    square) square "$2" ;;
    portrait) portrait "$2" ;;
    landscape) landscape "$wx" "$hx" ;;
esac



