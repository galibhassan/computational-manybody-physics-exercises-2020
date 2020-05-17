import numpy as np
import matplotlib.pyplot as plt
from src import metropolis


def weightFunc(x):
    return (1/np.sqrt(np.pi)) * np.exp(-x**2)


# test
minX = -3
maxX = 3
x = np.arange(minX, maxX, 0.001)
# plt.plot(x, weightFunc(x))
markovChain_unchangedXIncluded = metropolis.getMarkovChain(
    x, weightFunc,
    removeUnchanged=False
)
markovChain_unchangedXRemoved = metropolis.getMarkovChain(
    x, weightFunc, removeUnchanged=True)

# used for manually adjusting the fitting curve, NOT to be taken as a regression
scaleFactor = 350

plt.subplot(1, 2, 1)
plt.title('Duplicate values in markov chains included')
plt.ylabel('Count')
plt.hist(markovChain_unchangedXIncluded, range=(minX, maxX),  bins=100)
plt.plot(x, weightFunc(x)*scaleFactor)

# used for manually adjusting the fitting curve, NOT to be taken as a regression
scaleFactor = 200

plt.ylim(0, 300)
plt.subplot(1, 2, 2)
plt.title('Duplicate values in markov chains removed')
plt.hist(markovChain_unchangedXRemoved, range=(minX, maxX),  bins=100)
plt.plot(x, weightFunc(x)*scaleFactor)


plt.ylim(0, 300)
plt.xlabel('x')
plt.ylabel('Count')
plt.show()
