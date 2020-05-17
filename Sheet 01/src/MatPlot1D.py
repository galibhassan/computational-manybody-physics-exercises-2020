import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def generateMatrixPlot1D(data):
    nRow = 1
    nCol = data.shape[0]
    cmap = matplotlib.colors.ListedColormap(['white', 'gray'])
    plt.matshow(data, cmap=cmap)

    ax = plt.gca()
    # Minor ticks
    ax.set_xticks(np.arange(0.5, nCol, 1), minor=True)
    ax.set_yticks(np.arange(0.5, nRow, 1), minor=True)

    # Gridlines based on minor ticks
    ax.grid(which='minor', color='black', linewidth=3)
    return plt


def saveMatrixPlot1D(data, N, relPath, fileName):
    plt = generateMatrixPlot1D(data)
    # plt.show()

    fname = f'{relPath}/{fileName}_{N}.png'
    plt.savefig(fname, dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                metadata=None)
