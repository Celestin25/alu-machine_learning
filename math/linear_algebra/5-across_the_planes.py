#!/usr/bin/env python3

from 5-across_the_planes import add_matrices2D  # Import the add_matrices2D function

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add_matrices2D(mat1, mat2))  # Output: [[6, 8], [10, 12]]
print(mat1)  # Output: [[1, 2], [3, 4]]
print(mat2)  # Output: [[5, 6], [7, 8]]
print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))  # Output: None

