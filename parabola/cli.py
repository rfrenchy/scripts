# description: visualise movement of 'ball' falling at different speeds
import argparse
import matplotlib.animation as animation

from parabola import Plotter

# command line argument set up
argp = argparse.ArgumentParser("parabola")

argp.add_argument("--pow", default=1, type=int)
argp.add_argument("-o", "--output", default="ball.gif")
args = argp.parse_args()

_, anim = Plotter(args.pow, args.output)

writer = animation.PillowWriter(fps=12, metadata=dict(artist="ry"),
                                bitrate=1800)

anim.save(args.output, writer=writer)
