
# usage:
# description:

import argparse
import matplotlib.animation as animation

from overlap import Overlap

# command line argument set up
argp = argparse.ArgumentParser("overlap")

argp.add_argument("-o", "--output", default="./img/balls.gif")
args = argp.parse_args()

# command line argument set up
fig, anim = Overlap(24)

writer = animation.PillowWriter(fps=24, metadata=dict(artist="ry"),
                                bitrate=1800)

anim.save(args.output, writer=writer)
