import numpy as np
from src import ruleN


# periodic boundary condition:


def getNeighboursAlive2D(i, j, grid2D):
    aliveNeighboursCount = 0
    if grid2D[i-1][j-1] == 1:
        aliveNeighboursCount += 1
    if grid2D[i-1][j] == 1:
        aliveNeighboursCount += 1
    if grid2D[i-1][j+1] == 1:
        aliveNeighboursCount += 1
    # -----------------------------
    if grid2D[i][j-1] == 1:
        aliveNeighboursCount += 1
    if grid2D[i][j+1] == 1:
        aliveNeighboursCount += 1
    # -----------------------------
    if grid2D[i+1][j-1] == 1:
        aliveNeighboursCount += 1
    if grid2D[i+1][j] == 1:
        aliveNeighboursCount += 1
    if grid2D[i+1][j+1] == 1:
        aliveNeighboursCount += 1

    return aliveNeighboursCount


def applyPBC(i, j, grid2D):
    # periodic boundary condition vertical
    # top
    if i < 0:
        i = grid2D.shape[0] - abs(i)  # should work for sufficiently small i
    # bottom
    if i >= grid2D.shape[0]:
        i = i % grid2D.shape[0]
    # periodic boundary condition horizontal
    # left
    if j < 0:
        j = grid2D.shape[1] - abs(j)  # should work for sufficiently small j
    # right
    if j >= grid2D.shape[1]:
        j = j % grid2D.shape[1]

    return [i, j]


def getMooreNbdIndices2D(i, j, grid2D):
    return [
        applyPBC(i-1, j-1, grid2D),
        applyPBC(i-1, j, grid2D),
        applyPBC(i-1, j+1, grid2D),
        applyPBC(i, j-1, grid2D),
        applyPBC(i, j+1, grid2D),
        applyPBC(i+1, j-1, grid2D),
        applyPBC(i+1, j, grid2D),
        applyPBC(i+1, j+1, grid2D),
    ]


def getMooreNbdValues2D(i, j, grid2D):
    mooreNbdIndices = getMooreNbdIndices2D(i, j, grid2D)
    mooreNbdValues = np.ndarray([8], dtype=int)

    for k in range(len(mooreNbdIndices)):
        _i = mooreNbdIndices[k][0]
        _j = mooreNbdIndices[k][1]
        # mooreNbdValues.insert(grid2D[_i][_j])
        # np.insert(mooreNbdValues, 1, grid2D[_i][_j])
        mooreNbdValues[k] = grid2D[_i][_j]
    return mooreNbdValues


def getMooreNbd(i, j, grid2D):
    return {
        "valuesWithPBC": getMooreNbdValues2D(i, j, grid2D),
        "indicesWithPBC": getMooreNbdIndices2D(i, j, grid2D),
        "neighboursAlive": getMooreNbdValues2D(i, j, grid2D).sum()
    }


def GOLTimeEvolution(grid3D):
    nSurf = grid3D.shape[0]
    nRow = grid3D.shape[1]
    nCol = grid3D.shape[2]

    for t in range(nSurf-1):
        currentGrid2D = grid3D[t][:][:]
        nextGrid2D = grid3D[t+1][:][:]

        # saving currentGrid image
        ruleN.saveMatrixPlot(currentGrid2D, t, './images/GameOfLife')

        for i in range(nRow):
            for j in range(nCol):
                # check how many neighbours are alive
                neighboursAlive = getMooreNbd(i, j, currentGrid2D)[
                    "neighboursAlive"]

                if(neighboursAlive == 3):  # strictly 3
                    nextGrid2D[i][j] = 1
                else:
                    nextGrid2D[i][j] = 0


# test ------------
TMAX = 5
NROW = 5
NCOL = 4

# GOL stands for Game Of Life
GOLGrid = np.ndarray([TMAX, NROW, NCOL], dtype=int)*0

# initialization
GOLGrid[0][0][0] = 1
GOLGrid[0][1][0] = 1
GOLGrid[0][1][1] = 1
GOLGrid[0][2][3] = 1
GOLGrid[0][2][2] = 1
GOLGrid[0][2][2] = 1


# print(getNeighboursAlive2D(1, 1, GOLGrid[0][:][:]))
# print(applyPBC(-1, -1, GOLGrid[0][:][:]))
# print(getMooreNbdIndices2D(1, 0, GOLGrid[0][:][:]))
# print(getMooreNbdValues2D(1, 0, GOLGrid[0][:][:]))
# print(getMooreNbdValues2D(1, 0, GOLGrid[0][:][:]))

GOLTimeEvolution(GOLGrid)

print(GOLGrid)

# ruleN.showMatrixPlot(GOLGrid[0][:][:])
