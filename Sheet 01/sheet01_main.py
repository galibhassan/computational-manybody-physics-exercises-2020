# Exercise 1: Rule N
# (a)
import numpy as np

# custom modules
from src import ruleN

# generate the rule N
N = int(input('''

    ---------------------------------
    Enter the integer "N" for Rule N
    ---------------------------------

'''))

# specifying grid size and defining grid
NROW = 50
NCOL = 120
grid = np.ndarray([NROW, NCOL], dtype=int)*0

# initialization
grid[0][60] = 1


ruleN.occupyGrid(grid, N)

# time dependence
print(f'''
Time dependence Rule {N} up to t = {NROW} iteration: ''')
print(ruleN.getTimeDependence(grid))


ruleN.showMatrixPlot(grid)
