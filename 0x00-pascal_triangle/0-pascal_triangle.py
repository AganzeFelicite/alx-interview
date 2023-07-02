#!/usr/bin/python3
"""
that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    this is a function that returns a pascal
    is triangle in array form
    """
    arr = []
    if n <= 0:
        return []
    for i in range(n):
        temp_arr = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_arr.append(1)
            else:
                temp_arr.append(arr[i - 1][j - 1] + arr[i - 1][j])
        arr.append(temp_arr)
    return arr
