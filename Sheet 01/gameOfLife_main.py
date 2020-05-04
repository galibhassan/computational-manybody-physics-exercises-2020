import numpy as np
from src import ruleN
OUTPUT_PATH = './images/GameOfLife'


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
        ruleN.saveMatrixPlot(currentGrid2D, t, OUTPUT_PATH, "GameOfLife")

        for i in range(nRow):
            for j in range(nCol):
                # check how many neighbours are alive
                neighboursAlive = getMooreNbd(i, j, currentGrid2D)[
                    "neighboursAlive"]

                if currentGrid2D[i][j] == 1:
                    if neighboursAlive == 2 or neighboursAlive == 3:
                        nextGrid2D[i][j] = 1
                    else:
                        nextGrid2D[i][j] = 0
                else:
                    if(neighboursAlive == 3):  # strictly 3
                        nextGrid2D[i][j] = 1
                    else:
                        nextGrid2D[i][j] = 0


def makeGOLGridAndInit(NROW, NCOL, TMAX, alivePairs):
    # alivePairs are of the form [[i1,j1], [i2,j2], ...]

    GOLGrid = np.ndarray([TMAX, NROW, NCOL], dtype=int)*0

    for k in range(len(alivePairs)):
        _i = alivePairs[k][0]
        _j = alivePairs[k][1]

        GOLGrid[0][_i][_j] = 1

    return GOLGrid


def main():
    TMAX = 200
    NROW = 20
    NCOL = 20

    alivePairsGlider = [
        # pairs for Glider pattern
        [1, 2],
        [2, 3],
        [3, 1],
        [3, 2],
        [3, 3]
    ]

    alivePairsBox = [
        # pairs for Glider pattern
        [11, 11],
        [11, 12],
        [12, 11],
        [12, 12]

    ]
    alivePairsDimond = [
        # pairs for Glider pattern
        [1, 2],
        [2, 1],
        [2, 3],
        [3, 2]
    ]
    alivePairsHorizontalLine = [
        # pairs for Glider pattern
        [10, 10],
        [10, 11],
        [10, 12],
    ]
    alivePairsInvertedZ = [
        # pairs for Glider pattern
        [10, 11],
        [10, 12],
        [10, 13],
        [11, 9],
        [11, 10],
        [11, 11],
    ]

    GOLGrid = makeGOLGridAndInit(NROW, NCOL, TMAX, alivePairsInvertedZ)
    GOLTimeEvolution(GOLGrid)


main()


print('------------------------------------')
print("The output images can be found in: ")
print(OUTPUT_PATH)
print('------------------------------------')
