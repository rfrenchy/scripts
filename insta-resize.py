import getopt, sys 

from wand.image import Image

# TODO: colour to alpha?
# process iamge arg
# get image name 
opts, args = getopt.getopt(sys.argv[1:], "h")
# print(opts)

img = args[0]
img_name = img.split(".")[0]

# 1:1
def square(wx, hx):
    mx = wx if wx > hx  else hx # find the biggest of either height / width
    return f"{mx}x{mx}"         # return biggest as dimension string

# 1:1.91
def landscape(wx, hx):
    n_wx = hx * 1.91
    return f"{n_wx}x{hx}"

# 4:5
def portrait(wx, hx):
    n_wx = hx * 1.25
    return f"{n_wx}x{hx}"

# print(square(1028, 2345))
      
# create blank white image to composite with input image
# composite them

# output as an image  file
