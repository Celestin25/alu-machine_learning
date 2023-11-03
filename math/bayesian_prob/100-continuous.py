#!/usr/bin/env python3
"""
This script defines a function to calculate the posterior probability that
the various hypothetical probabilities of developing severe side effects fall
within a specific range given the data.
"""

from scipy import special

def calculate_posterior_within_range(severe_cases, total_patients, lower_bound, upper_bound):
    """
    Calculates the posterior probability that the hypothetical probabilities fall within a specific range given the data.

    Parameters:
        severe_cases (int): Number of patients with severe side effects.
        total_patients (int): Total number of patients observed.
        lower_bound (float): Lower bound of the probability range.
        upper_bound (float): Upper bound of the probability range.

    Returns:
        float: Posterior probability that probabilities fall within the range [lower_bound, upper_bound].
    """
    if not isinstance(total_patients, int) or total_patients <= 0:
        raise ValueError("Total patients must be a positive integer.")
    if not isinstance(severe_cases, int) or severe_cases < 0:
        raise ValueError("Number of severe cases must be a non-negative integer.")
    if severe_cases > total_patients:
        raise ValueError("Number of severe cases cannot exceed total patients.")
    if not (0 <= lower_bound <= 1) or not (0 <= upper_bound <= 1):
        raise ValueError("Bounds must be within the range [0, 1].")
    if upper_bound <= lower_bound:
        raise ValueError("Upper bound must be greater than lower bound.")

    # Calculate cumulative distribution function for beta distribution from 0 to upper_bound
    cdf_upper_bound = special.btdtr(severe_cases + 1, total_patients - severe_cases + 1, upper_bound)
    # Calculate cumulative distribution function for beta distribution from 0 to lower_bound
    cdf_lower_bound = special.btdtr(severe_cases + 1, total_patients - severe_cases + 1, lower_bound)

    # Calculate the posterior probability that probabilities fall within the specified range
    posterior_probability = cdf_upper_bound - cdf_lower_bound

    return posterior_probability
