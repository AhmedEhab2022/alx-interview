#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """ Island Perimeter """
    perimeter = 0
    length = len(grid)
    width = len(grid[0])
    for i in range(length):
        for j in range(width):
            if grid[i][j] == 1:
                if i == 0 or (i > 0 and grid[i - 1][j] == 0):
                    perimeter += 1

                if i == length - 1 or (i < length - 1 and grid[i + 1][j] == 0):
                    perimeter += 1

                if j == 0 or (j > 0 and grid[i][j - 1] == 0):
                    perimeter += 1

                if j == width - 1 or (j < width - 1 and grid[i][j + 1] == 0):
                    perimeter += 1

    return perimeter
