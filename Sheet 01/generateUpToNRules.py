# Exercise 1: Rule N
# (a)
import numpy as np

# custom modules
from src import ruleN

NLimit = 255

# specifying grid size and defining grid
NROW = 50
NCOL = 120
grid = np.ndarray([NROW, NCOL], dtype=int)*0

# initialization
grid[0][60] = 1

# generate the rule N

for N in range(NLimit):
    ruleN.occupyGrid(grid, N)
    ruleN.saveMatrixPlot(grid, N, './images/RuleNImages', "Rule")
