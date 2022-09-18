import matplotlib.pyplot as plt
from ipywidgets import interactive
import numpy as np
import seaborn as sns

x = np.linspace(0, 200, 200)
y = np.linspace(0, 150, 200)
x, y = np.meshgrid(x, y)


def f(a, b):
    return (b - 4) * (50 - .5 * b + .2 * a)


z = f(x, y)
sns.set_style('white')
plt.title("Heat Map of Company Profits")
z[z < 0.] = np.NaN
ax = sns.heatmap(z, cmap="Greens")
ax.invert_yaxis()
