import math
import numpy as np
import matplotlib.pyplot as plt


# what is within the sin function?

def print_table(v, sv, cv):
    th = "v\t\tsv\t\tcv\t"

    print("-" * len(th.expandtabs()))
    print(th)
    print("-" * len(th.expandtabs()))

    for i in range(len(v)):
        print(f"{v[i]:.4f}\t\t{sv[i]:.4f}\t\t{cv[i]:.4f}\t")


def print_plots(v, sv, cv):
    _, ax = plt.subplots()
    ax.axis("equal")
    # ax.set_ylim(-2, 2)
    ax.grid()

    for i in range(len(v)):
        plt.plot(v, sv, 'b')
        plt.plot(v, cv, 'r')

    plt.show()

total = 100

v = np.linspace(-5, 15, total) # linear walk
sv = np.zeros(total) # sin values
cv = np.zeros(total) # cos values

# generate values from linear walk
for i in range(len(v)):
    sv[i] = math.sin(v[i])
    cv[i] = math.cos(v[i])

print_plots(v, sv, cv)