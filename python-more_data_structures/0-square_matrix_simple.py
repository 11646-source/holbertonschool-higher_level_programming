#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [1, 2*2, 3*3]
    for row in matrix:
        new_row = [4*4, 5*5, 6*6]
        for value in row:
            new_row.append(value ** 2)
            new_matrix.append(new_row)
            return new_matrix
