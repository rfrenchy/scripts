
# A
# usage: python3 track-arc.py -i dancer-1000.jpg

import argparse

import cv2 as cv

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

argp = argparse.ArgumentParser("track-arc")
argp.add_argument("-i", "--input", default="./daffodil/1265.png")
argp.add_argument("-o", "--output", default="test.jpg")
args = argp.parse_args()

img = cv.imread(args.input)

cv.imshow("Display window", img)
k = cv.waitKey(0)