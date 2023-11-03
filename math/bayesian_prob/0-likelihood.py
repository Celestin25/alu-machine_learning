#!/usr/bin/env python3
"""
This script defines a function to calculate the likelihood of observing
a specific number of patients with severe side effects among a total number
of observed patients, given various hypothetical probabilities.
"""

import numpy as np

def calculate_likelihood(severe_cases, total_patients, probabilities):
    """
    Calculates the likelihood of observing severe cases given different probabilities.

    Parameters:
        severe_cases (int): Number of patients with severe side effects.
        total_patients (int): Total number of patients observed.
        probabilities (numpy.ndarray): Array of hypothetical probabilities.

    Returns:
        numpy.ndarray: Array containing the likelihood of observing the data for each probability.
    """
    if not isinstance(total_patients, int) or total_patients <= 0:
        raise ValueError("Total patients must be a positive integer.")
    if not isinstance(severe_cases, int) or severe_cases < 0:
        raise ValueError("Number of severe cases must be a non-negative integer.")
    if severe_cases > total_patients:
        raise ValueError("Number of severe cases cannot exceed total patients.")
    if not isinstance(probabilities, np.ndarray) or len(probabilities.shape) != 1:
        raise TypeError("Probabilities must be a 1D numpy array.")
    if not all(0 <= p <= 1 for p in probabilities):
        raise ValueError("Probabilities must be within the range [0, 1].")

    # Calculate likelihood using the binomial distribution formula
    binomial_coefficient = np.math.comb(total_patients, severe_cases)
    likelihood = binomial_coefficient * (probabilities ** severe_cases) * ((1 - probabilities) ** (total_patients - severe_cases))

    return likelihood
