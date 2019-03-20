import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

# Create a new figure
fig = Figure()

# associate fig with the backend
canvas = FigureCanvasAgg(fig)

# add a subplot to the figure
ax = fig.add_subplot(111)

# plot the point (3, 2)
ax.plot(3, 2, '.')

# save the figure to test.png
canvas.print_png('test.png')