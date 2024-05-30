#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees clockwise.
        Do not return anything. The matrix must be edited in-place.
        You can assume the matrix will have 2 dimensions and will not be empty.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Save the top element
            top = matrix[i][j]
            # Move left to top
            matrix[i][j] = matrix[n - j - 1][i]
            # Move bottom to left
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            # Move right to bottom
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            # Assign top to right
            matrix[j][n - i - 1] = top
