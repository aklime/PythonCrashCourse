import matplotlib.pyplot as plt

x_values = list(range(5001))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors=None, s=40)

plt.title("Sześciany liczb", fontsize=24)
plt.xlabel("Wartość", fontsize=14)
plt.ylabel("Kwadraty wartości", fontsize=14)
plt.axis([0, 5100, 0, 5000 ** 3])

#plt.show()
plt.savefig('cubes_plot.png', bbox_inches='tight')
