#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for one_d in matrix:
        new_matrix.append([square_it * square_it for square_it in one_d])
    return new_matrix

