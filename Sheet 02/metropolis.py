import numpy as np
import matplotlib.pyplot as plt


def weightFunc(x):
    return (1/np.sqrt(np.pi)) * np.exp(-x**2)


def testFunc(x):
    return x


def metropolis(x, targetFunc):
    # init
    # init = np.random.uniform()
    init = x[0]
    markovX = []
    markovX.append(init)

    for i in range(len(x)-1):
        current = markovX[i]
        proposed = np.random.normal(current, 0.01)

        ratio = (targetFunc(proposed) / targetFunc(current))

        uniRand = np.random.uniform()
        if ratio > 1:
            # accept propsed
            markovX.append(proposed)
        else:
            # reject proposed
            markovX.append(current)

    return markovX


# test
minX = -1
maxX = 1
x = np.arange(minX, maxX, 0.01)
# plt.plot(x, weightFunc(x))
markovChain = metropolis(x, weightFunc)

print(len(x))
print(len(markovChain))
print(np.sum(markovChain)/len(x))


# plt.scatter(x, markovChain)

plt.hist(markovChain, range=(minX, maxX),  bins=10)
plt.show()
