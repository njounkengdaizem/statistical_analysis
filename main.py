import matplotlib.figure
import matplotlib.pyplot as plt
from ipywidgets import interactive
import numpy as np
import seaborn as sns
import matplotlib.colors as mcolors
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import mplcursors

from matplotlib.colors import TwoSlopeNorm

# Assign constraints to x and why values
x = np.linspace(0, 200, 200)
y = np.linspace(0, 150, 200)
x, y = np.meshgrid(x, y)


def f(a, b):
    """ Method feeds in native x and y values and returns values corresponding to the
    function to be graphed"""
    quantity = (50 - .5 * b + .2 * a)
    price = b - 4
    # Exclude negative quantities
    quantity[quantity < 0.] = np.NaN
    return price * quantity


root = tk.Tk()
fig, axis = plt.subplots(figsize=(8, 7))

canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().place(x=60, y=60)
# Instantiate the f function above
z = f(x, y)

# Label Axis and Title
plt.title("Heat Map of Company Profits")

# Draw heat map
norm = mcolors.TwoSlopeNorm(vmin=-10, vcenter=0)
heatmap = axis.imshow(z, cmap='RdBu', norm=norm)
axis.invert_yaxis()
heatmap.axes.get_xaxis().set_visible(True)
heatmap.axes.get_yaxis().set_visible(True)
colorbar = fig.colorbar(heatmap)

from collections import namedtuple

_Event = namedtuple('_Event', 'xdata ydata')

cursor = mplcursors.cursor(hover=True)


@cursor.connect("add")
def on_mouse_move(sel):
    x = sel.target[0]
    y = sel.target[1]
    value = sel.artist.get_cursor_data(_Event(x, y))
    sel.annotation.set_text("value {} at ({:1.2f}, {:1.2f})".format(value, x, y))

on_mouse_move(z)

# on_mouse_move()


root.mainloop()
