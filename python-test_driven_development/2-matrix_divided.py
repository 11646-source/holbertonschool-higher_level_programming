#!/usr/bin/python3
"""
Module: matrix_divided
This module defines a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix of integers/floats
        div (int or float): The divisor

    Returns:
        list of lists: A new matrix with elements divided by div, rounded to 2 decimals

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
                   If rows of the matrix are not the same size
                   If div is not a number
        ZeroDivisionError: If div is zero
    """
    # Validate matrix type
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate matrix contents
    if not all(all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate row sizes
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and rounding
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
