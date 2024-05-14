#!/usr/bin/python3
""" N Queens Problem
"""
import sys


def validateArgs(argv):
    """ Check if the input is invalid or not
        return True if input is valid, False otherwise
    """
    if len(argv) != 2:
        print("Usage: nqueens N")
        return False

    if isinstance(argv[1], int):
        print('N must be a number')
        return False

    if argv[1] < 4:
        print('N must be at least 4')
        return False

    return True


def validatePos(board, col, row, n):
    """ Validate position
    """
    if board[col][row] == 1:
        return False

    for i in range(col - 1, -1, -1):
        if board[i][row] == 1:
            return False

    for j in range(row - 1, -1, -1):
        if board[col][j] == 1:
            return False

    j = row - 1
    for i in range(col - 1, -1, -1):
        if j >= 0:
            if board[i][j] == 1:
                return False
        j -= 1

    j = row - 1
    for i in range(col + 1, n):
        if j >= 0:
            if board[i][j] == 1:
                return False
        j -= 1

    return True


def NQueensSolver(n, board, solution, row):
    """ Solve N Queens problem
    """
    if n == row:
        print(solution)
        solution = []
        return

    for i in range(n):
        if validatePos(board, i, row, n):
            board[i][row] = 1
            solution.append([row, i])
            NQueensSolver(n, board, solution, row + 1)
            board[i][row] = 0
            solution.remove([row, i])


def main():
    """ Main Function
    """
    if validateArgs(sys.argv):
        n = sys.argv[1]
        board = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)

            board.append(row)

        NQueensSolver(n, board, [], 0)
    else:
        exit(1)


if __name__ == '__main__':
    main()
