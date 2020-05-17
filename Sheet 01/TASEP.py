import numpy as np
from src import MatPlot1D
from src import ruleN


# making the chain


def getChain(NCell, MIN_nParticals, MAX_nParticals):
    while True:
        chain = np.random.randint(2, size=NCell)
        if(chain.sum() >= MIN_nParticals and chain.sum() <= MAX_nParticals):
            return chain


def applyPBC1D(i, chain):
    # left
    if i < 0:
        i = chain.shape[0] - abs(i)  # should work for sufficiently small i
    # right
    if i >= chain.shape[0]:
        i = i % chain.shape[0]

    return i


def getDecision():
    return np.random.randint(2, size=1)[0]


def hopOrDont(inChain):
    outChain = inChain.copy()
    for i in range(len(inChain)):
        iPlus1 = applyPBC1D(i+1, inChain)
        if inChain[i] == 1 and inChain[iPlus1] == 0:
            currentDecision = getDecision()

            if currentDecision == 1:
                # hop!
                outChain[iPlus1] = 1
                outChain[i] = 0
    return outChain


def main():
    NCell = 50  # number of sites in 1D chain
    MIN_nParticals = 24  # number of particles
    MAX_nParticals = 26  # number of particles

    chain = getChain(NCell, MIN_nParticals, MAX_nParticals)

    for t in range(200):

        chain = hopOrDont(chain)
        ruleN.saveMatrixPlot(np.asmatrix(
            chain), t, './images/TASEP', 'tasep')


main()
