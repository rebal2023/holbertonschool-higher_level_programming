#!/usr/bin/python3
"""Defines a Pascal Triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's triangle of n"""

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trg = triangles[-1]
        tmp = [1]
        for i in range(len(trg) - 1):
            tmp.append(trg[i] + trg[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
