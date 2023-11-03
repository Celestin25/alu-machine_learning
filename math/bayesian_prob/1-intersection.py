#!/usr/bin/env python3
"""
This script defines a function to calculate the intersection of observing
a specific number of patients with severe side effects among a total number
of observed patients, given various hypothetical probabilities and priors.
"""

import numpy as np

def calculate_intersection(severe_cases, total_patients, probabilities, priors):
    """
    Calculates the intersection of observing severe cases with various probabilities and priors.

    Parameters:
        severe_cases (int): Number of patients with severe side effects.
        total_patients (int): Total number of patients observed.
        probabilities (numpy.ndarray): Array of hypothetical probabilities.
        priors (numpy.ndarray): Array of prior beliefs for probabilities.

    Returns:
        numpy.ndarray: Array containing the intersection of observing the data for each probability and prior.
    """
    if not isinstance(total_patients, int) or total_patients <= 0:
        raise ValueError("Total patients must be a positive integer.")
    if not isinstance(severe_cases, int) or severe_cases < 0:
        raise ValueError("Number of severe cases must be a non-negative integer.")
    if severe_cases > total_patients:
        raise ValueError("Number of severe cases cannot exceed total patients.")
    if not isinstance(probabilities, np.ndarray) or len(probabilities.shape) != 1:
        raise TypeError("Probabilities must be a 1D numpy array.")
    if not isinstance(priors, np.ndarray) or priors.shape != probabilities.shape:
        raise TypeError("Priors must be a numpy array with the same shape as probabilities.")
    if not all(0 <= p <= 1 for p in probabilities) or not all(0 <= pr <= 1 for pr in priors):
        raise ValueError("Probabilities and priors must be within the range [0, 1].")
    if not np.isclose([np.sum(priors)], [1]):
        raise ValueError("Priors must sum to 1.")

    # Calculate likelihood using the binomial distribution formula
    binomial_coefficient = np.math.comb(total_patients, severe_cases)
    likelihood = binomial_coefficient * (probabilities ** severe_cases) * ((1 - probabilities) ** (total_patients - severe_cases))

    # Calculate intersection of likelihood and priors
    intersection = likelihood * priors

    return intersection
