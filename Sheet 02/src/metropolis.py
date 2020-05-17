import numpy as np


def getMarkovChain(x, targetFunc):
    '''
    __doc__
        x: a numpy array of numbers
        targetFunc: a function
        returns: a markov chain
    '''

    init = np.random.uniform()
    markovX = []

    for i in range(len(x)):
        if i == 0:
            markovX.append(init)
        else:
            current = markovX[i-1]
            proposed = np.random.normal(current, 1)

            ratio = (targetFunc(proposed) / targetFunc(current))

            uniRand = np.random.uniform()
            if ratio > uniRand:
                # accept propsed
                markovX.append(proposed)
            else:
                # reject proposed
                markovX.append(current)

    return markovX
