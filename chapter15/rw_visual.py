import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()

point_numbers = list(range(rw.num_points))
# plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens,
#            edgecolor='none', s=1)

plt.plot(rw.x_values, rw.y_values, linewidth=1, label="Losowa ścieżka")

plt.scatter(0, 0, c='green', edgecolors='none', s=100, label="Punkt początkowy")
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
            s=100, label="Punkt końcowy")

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.legend()

#plt.show()
plt.savefig('random_walk_plot.png')