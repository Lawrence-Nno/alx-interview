#!/usr/bin/python3
"""A script that rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise."""
    row = len(matrix)
    column = row - 1

    for i in range(0, int(row / 2)):
        for j in range(i, column - i):
            temp_matrix = matrix[i][j]
            matrix[i][j] = matrix[column - j][i]
            matrix[column - j][i] = matrix[column - i][column - j]
            matrix[column - i][column - j] = matrix[j][column - i]
            matrix[j][column - i] = temp_matrix
