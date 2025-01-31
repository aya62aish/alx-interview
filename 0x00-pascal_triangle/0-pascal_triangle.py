#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Function to return pascal triangle of size n"""
    arr = []
    if n <= 0:
        return arr
    for i in range(0, n):
        arr2 = []
        for j in range(0, i+1):
            arr2.append(0)
        arr2[0] = 1
        for j in range(1, i):
            arr2[j] = arr[i - 1][j - 1] + arr[i-1][j]
        arr2[i] = 1
        arr.append(arr2)
    return arr
    