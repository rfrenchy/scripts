import math
import numpy as np
import matplotlib.pyplot as plt

from unit_circle import unit_circle

# what is within the sin function?

def print_table(v, sv, cv):
    th = "v\t\tsv\t\tcv\t"

    print("-" * len(th.expandtabs()))
    print(th)
    print("-" * len(th.expandtabs()))

    for i in range(len(v)):
        print(f"{v[i]:.4f}\t\t{sv[i]:.4f}\t\t{cv[i]:.4f}\t")

# generate plot data
total = 100
total_unit_circles = 3
unit_circle_translate = 2 # how much to translate circle by along x
ranges = (-2, total_unit_circles * unit_circle_translate)

v = np.linspace(ranges[0], ranges[1], total) # linear walk
sv = np.zeros(total) # sin values
cv = np.zeros(total) # cos values

# generate values from linear walk
for i in range(len(v)):
    sv[i] = math.sin(v[i])
    cv[i] = math.cos(v[i])

# create plot
fig, ax = plt.subplots()
ax.axis("equal")
ax.grid()

# add data to plot
plt.plot(v, sv, 'orange')
plt.plot(v, cv, 'green')

for i in range(total_unit_circles):
    cx, cy = unit_circle(i * 2)
    plt.plot(cx, cy, 'b')

# show plot 
plt.show()