# usage: python3 parabola.py
# description: visualise movement of 'ball' falling at different speeds
import argparse

import numpy as np
import matplotlib.pyplot as plt

# command line argument set up
argp = argparse.ArgumentParser("parabola")

argp.add_argument("--pow", default=1)
argp.add_argument("-o", "--output", default="ball.png")
args = argp.parse_args()

# axis data
plt.xlabel("frames")
x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

plt.ylabel("distance-fallen")
y_start = np.array([0, -0.1, -0.19, -0.3, -0.575, -0.825, -1.225,
                    -1.650, -2.19, -2.75, -3.41, -4.125, -4.825])

y_final = np.negative(np.power(y_start, args.pow))

# plot
plt.scatter(x, y_final)
plt.grid()
plt.savefig(args.output)
