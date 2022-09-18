import matplotlib.pyplot as plt
from ipywidgets import interactive
import numpy as np
import seaborn as sns

# Assign constraints to x and why values
x = np.linspace(0, 200, 200)
y = np.linspace(0, 150, 200)
x, y = np.meshgrid(x, y)


def f(a, b):
    """ Method feeds in native x and y values and returns values corresponding to the
    function to be graphed"""
    return (b - 4) * (50 - .5 * b + .2 * a)


#Instantiate the f function above

z = f(x, y)
sns.set_style('white')
plt.title("Heat Map of Company Profits")

# Exclude negative values
z[z < 0.] = np.NaN

# Draw heat map
ax = sns.heatmap(z, cmap="Greens")
ax.invert_yaxis()
