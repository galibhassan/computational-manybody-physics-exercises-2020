# Exercise 1: Rule N
# (a)
import numpy as np

# custom modules
from src import ruleN

# generate the rule N
N = 2

# specifying grid size and defining grid
NROW = 50
NCOL = 120
grid = np.ndarray([NROW, NCOL], dtype=int)*0

# initialization
grid[0][60] = 1


ruleN.occupyGrid(grid, N)

print(ruleN.getTimeDependence(grid))


ruleN.showMatrixPlot(grid)
