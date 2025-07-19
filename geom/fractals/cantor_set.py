import numpy as np
import matplotlib.pyplot as plt

def cantor_set():
    # base line
    x = [0, 1]
    y = [0, 0]

    # plot
    plt.plot(x, y, "black", lw=3)

    def recurse(rx, ry, n):
      # next line is 1/3 width of previous line
      width = (np.max(rx) - np.min(rx)) / 3
      y_step = 0.333

      # construct
      rx1 = [np.min(rx), np.min(rx) + width] # first bar x
      rx2 = [np.max(rx) - width, np.max(rx)] # second bar x
      ry1 = [ry[0] - y_step, ry[1] - y_step] # y same for both

      # plot
      plt.plot(rx1, ry1, "black", lw=3)
      plt.plot(rx2, ry1, "black", lw=3)

      # recurse
      if n > 1:
        recurse(rx1, ry1, n-1)
        recurse(rx2, ry1, n-1)
  
    recurse(x, y, 4)

cantor_set()    
plt.axis("off")
plt.savefig("cantor_set")