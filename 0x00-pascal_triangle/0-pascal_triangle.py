#!/usr/bin/python3

"""Define a function pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""

    pasc_tri = []
    if n <= 0:
        return pasc_tri

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pasc_tri[i - 1][j] + pasc_tri[i - 1][j - 1])

        pasc_tri.append(row)

    return pasc_tri