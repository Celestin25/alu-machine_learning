#!/usr/bin/env python3

from 8-ridin_bareback import mat_mul  # Import the mat_mul function

mat1 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

mat2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

result = mat_mul(mat1, mat2)

for row in result:
    print(row)

