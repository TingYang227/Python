import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure


# create a new figure
fig = Figure()

# associate fig with the backend
canvas = FigureCanvasAgg(fig)

# add a subplot to the fig
ax = fig.add_subplot(111)

# plot the point (3,2)
ax.plot(3, 2, '.')

# save the figure
canvas.print_png('test111.png')


# create a new figure
plt.figure()

# plot the point (3,2) using the circle marker
plt.plot(3, 2, 'o')

# get the current axes
ax = plt.gca()
print(ax)
# Set axis properties [xmin, xmax, ymin, ymax]
ax.axis([0, 6, 0, 10])
#plt.show()



# return the name of the current backend
print(mpl.get_backend())

plt.plot(3, 2, 'bo')

# show the figure
#plt.show()

# save the figure
plt.savefig("savefig.pdf")



import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y = x

# create a list of colors for each point to have
# ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'red']
colors = ['green'] * (len(x) - 1)
colors.append('red')

plt.figure()
plt.scatter(x, y, s=100, c=colors)


# convert the two lists into a list of pairwise tuples
zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])

x, y = zip(*zip_generator)
print(x)
print(y)


plt.figure()
# plot a data series 'Tall stusents' in red using the first two elements of x and y
plt.scatter(x[:2], y[:2], s=100, c='red', label='Tall students')
# plot a second data series 'Short students' in blue using the last three elements of x and y
plt.scatter(x[2:], y[2:], s=100, c='blue', label='Short students')

# add a label to the x axis
plt.xlabel('The number of times the child kicked a ball')
# add a label to the y axis
plt.ylabel('The grade of the student')
# add a title
plt.title('Relationship between ball kicking and grades')
# add a legend
plt.legend()

plt.legend(loc=4, frameon=True, title='Legend')
plt.show()