#!/usr/bin/env python3
"""
Calculate the sum of squared values
"""


def calculate_sum_of_squares(n):
    """ Calculate the sum of squares

    Args:
        n (int): The number up to which the sum of squares should be calculated.
        
    Returns:
        int or None: The sum of squares up to 'n' if 'n' is a positive integer, or None otherwise.
    """
    if n == 1:
        return 1
    if n < 1:
        return None
    else:
        result = (n * (n + 1) * (2 * n + 1)) // 6
        return result

# Example usage:
# print(calculate_sum_of_squares(5))

