#!/usr/bin/env python3

from 4-line_up import add_arrays  # Import the add_arrays function

arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(add_arrays(arr1, arr2))  # Output: [6, 8, 10, 12]
print(arr1)  # Output: [1, 2, 3, 4]
print(arr2)  # Output: [5, 6, 7, 8]
print(add_arrays(arr1, [1, 2, 3]))  # Output: None

