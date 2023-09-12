#!/usr/bin/env python3

from 7-gettin_cozy import cat_matrices2D  # Import the cat_matrices2D function

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6]]
mat3 = [[7], [8]]

mat4 = cat_matrices2D(mat1, mat2)
mat5 = cat_matrices2D(mat1, mat3, axis=1)

print(mat4)  # Output: [[1, 2], [3, 4], [5, 6]]
print(mat5)  # Output: [[1, 2, 7], [3, 4, 8]]

mat1[0] = [9, 10]
mat1[1].append(5)
print(mat1)  # Output: [[9, 10], [3, 4, 5]]
print(mat4)  # Output: [[1, 2], [3, 4], [5, 6]]
print(mat5)  # Output: [[1, 2, 7], [3, 4, 8]]

