#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

# 1. Turn string to array, use list() instead of split().
def gridChallenge(grid):
    # Write your code here
    new_grid = []
    for e in grid:
        ls = list(e)
        ls.sort()
        new_grid.append("".join(ls))
    n = len(new_grid)
    m = len(new_grid[0])
    for j in range(m):
        for i in range(n - 1):
            if new_grid[i][j] > new_grid[i + 1][j]:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()