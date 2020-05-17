import numpy as np
import matplotlib.pyplot as plt
from src import metropolis


def weightFunc(x):
    '''
        The gaussian form is taken from the exercise
    '''
    # return (1/np.sqrt(np.pi)) * np.exp(-x**2)
    return np.exp(-x**2)


# test
minX = -3
maxX = 3
x = np.arange(minX, maxX, 0.001)
# plt.plot(x, weightFunc(x))
markovChain = metropolis.getMarkovChain(x, weightFunc)

print(len(x))
print(len(markovChain))
print(np.sum(markovChain)/len(x))


# plt.scatter(x, markovChain)
plt.hist(markovChain, range=(minX, maxX),  bins=50)
scaleFactor = 400
plt.plot(x, weightFunc(x)*scaleFactor)
plt.show()
