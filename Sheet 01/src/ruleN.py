import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def getRule(decNum):
    # __doc__
    # param: decNum {Int} a decimal integer, 0 < decNum < 255.
    # returns: {Dictionary} a dict describing the Rule(decNum)

    if(decNum < 0 or decNum > 255):
        raise Exception('''
    
    ------------------------------
    Can not generate rule over 255.
    Please enter between 0 to 255.
    ------------------------------

    ''')

    triads = ['111', '110', '101', '100', '011', '010', '001', '000']

    binNum = dec_to_bin(decNum)
    nZerosInFront = 8-len(binNum)

    frontString = ''
    if(nZerosInFront > 0):
        for i in range(nZerosInFront):
            frontString += '0'

    binaryStringNum8 = frontString + binNum
    binStringArr = list(binaryStringNum8)

    dict = {}
    for i in range(len(triads)):
        dict.update({triads[i]: binStringArr[i]})

    return dict


def dec_to_bin(x):
    # copied from: https://stackoverflow.com/questions/3528146/convert-decimal-to-binary-in-python/#answer-11890306
    return bin(x)[2:]


def getTimeDependence(grid):
    return grid.sum()


def getOccupation(a, b, c, N):
    # __doc__
    # a, b, c are diagonal, vertical and off-diagonal entries in the previous row
    # N is the N from "Rule N"

    currentRule = getRule(N)
    if a == 0 and b == 0 and c == 0:
        return int(currentRule['000'])
    if a == 0 and b == 0 and c == 1:
        return int(currentRule['001'])
    if a == 0 and b == 1 and c == 0:
        return int(currentRule['010'])
    if a == 0 and b == 1 and c == 1:
        return int(currentRule['011'])
    if a == 1 and b == 0 and c == 0:
        return int(currentRule['100'])
    if a == 1 and b == 0 and c == 1:
        return int(currentRule['101'])
    if a == 1 and b == 1 and c == 0:
        return int(currentRule['110'])
    if a == 1 and b == 1 and c == 1:
        return int(currentRule['111'])


def occupyGrid(grid, N):
    for i in range(grid.shape[0]):
        # skip the first row
        if i == 0:
            continue

        for j in range(grid.shape[1]):

            # only interior
            # if i > 0 and i < grid.shape[0]-1 and j > 0 and j < grid.shape[1]-1:
            if i > 0 and j > 0 and j < grid.shape[1]-1:
                grid[i][j] = getOccupation(
                    grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1], N)


def generateMatrixPlot(data):
    nRow = data.shape[0]
    nCol = data.shape[1]
    cmap = matplotlib.colors.ListedColormap(['white', 'gray'])
    plt.matshow(data, cmap=cmap)

    ax = plt.gca()
    # Minor ticks
    ax.set_xticks(np.arange(0.5, nCol, 1), minor=True)
    ax.set_yticks(np.arange(0.5, nRow, 1), minor=True)

    # Gridlines based on minor ticks
    ax.grid(which='minor', color='#383838', linewidth=0.5)
    return plt


def showMatrixPlot(data):
    plt = generateMatrixPlot(data)
    plt.show()


def saveMatrixPlot(data, N, relPath, fileName):
    plt = generateMatrixPlot(data)
    # plt.show()

    fname = f'{relPath}/{fileName}_{N}.png'
    plt.savefig(fname, dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                metadata=None)
