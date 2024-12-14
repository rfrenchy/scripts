# README ME

import argparse

import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.animation as animation

argp = argparse.ArgumentParser("tracking", 
                               description="3 projectile path rotated from central point")
argp.add_argument("-i", "--input", default="")
argp.add_argument("-o", "--output", default="")

fig, ax = plt.subplots()

plt.show()

# fig.savefig("c2.jpg")