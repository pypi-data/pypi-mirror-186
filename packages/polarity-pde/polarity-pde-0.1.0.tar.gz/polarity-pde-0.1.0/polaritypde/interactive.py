import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

"""
To do: 
- option to display or save movie
- jupyter and non-jupyter modes

"""


def interactive_fig(solns, times, labels=None):
    fig, ax = plt.subplots()
    ymax = 1.1 * max([np.max(i) for i in solns])

    if labels is None:
        labels = [None] * len(solns)

    @widgets.interact(time=(0, times[-1], 1))
    def update(time=0):
        ax.clear()
        tpoint = np.argmin(abs(times - time))
        for i, soln in enumerate(solns):
            ax.plot(soln[tpoint], label=labels[i])
        ax.set_ylim(0, ymax)
        ax.set_xlabel('Position')
        ax.set_ylabel('Concentration')
        ax.legend(loc='upper left')

    fig.set_size_inches(5, 3)
    fig.tight_layout()
