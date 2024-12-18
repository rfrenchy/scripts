# usage: python3 parabola.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# TODO slow-in-fast-out ?


def Plotter(pow=1, output="ball.gif") -> tuple[plt.Figure, animation.FuncAnimation]:

	# axis data
	x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

	y_start = np.array([0, -0.1, -0.19, -0.3, -0.575, -0.825, -1.225,
						-1.650, -2.19, -2.75, -3.41, -4.125, -4.825])

	# user operations
	y_pow = np.power(y_start, pow)

	# make sure y-data remain negative no matter pow value
	y_pow = -y_pow if pow % 2 == 0 else y_pow
	y_final = y_pow

	fig, ax = plt.subplots(width_ratios=[1], height_ratios=[1])

	ax.set_xlim([-5, 30])

	ax.spines.get('top').set_visible(False)
	ax.spines.get('right').set_visible(False)

	# ax.axis('off')
	# ax.set_aspect('equal', 'box')
	# ax.grid()

	# assumes negatives
	y_lim_start = np.min(y_final) - (np.min(y_final) % 5)
	ax.set_ylim([y_lim_start, 5])

	scat = ax.scatter(1, 0)

	ny = np.array([])

	y_work = y_final

	ymin = np.abs(min(y_work))

	if ymin < 0:
		y_work = np.add(y_work, ymin)

	for d in y_work:
		v = (d - min(y_work)) / (max(y_work) - min(y_work))
		ny = np.append(ny, v)

	ax.set_ylim([0, 1])

	def animate(i):
		scat.set_offsets((x[i], ny[i]))
		return scat,

	ani = animation.FuncAnimation(fig, animate, repeat=True,
								  frames=len(x) - 1, interval=100)

	return (fig, ani)


def parabolav2():
	fig, ax = plt.subplots()

	frames = 100

	x = np.linspace(-1, 1, frames)
	y = np.array([])
	vertex_x = 0
	vertex_y = 0
	a = -1

	# y = a * (x - h)** 2 + k
	for i in range(len(x)):
		y = np.append(y, a * (x[i] - vertex_x)**2 + vertex_y)


	def animate(i):
		ax.cla()
		ax.axis("equal")
		ax.plot(x, y)
		ax.scatter(x[i], y[i])

	# write the file image 
	anim = animation.FuncAnimation(fig, animate, repeat=True,
									frames=(frames - 1), interval=100)

	writer = animation.PillowWriter(fps=12, metadata=dict(artist="ry"),
									bitrate=1800)

	anim.save("parabolav2.gif", writer=writer)

	# fig.savefig("parabolav2.jpg")

parabolav2()