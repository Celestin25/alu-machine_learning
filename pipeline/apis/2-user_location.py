#!/usr/bin/env python3
"""
Script to print the location of a GitHub user.
Usage: ./2-user_location.py <github_api_user_url>
"""

import requests
from sys import argv
import time

def calculate_reset_duration(rate_limit_reset):
    """ Calculate the duration in minutes until rate limit resets """
    current_time = time.time()
    reset_duration = int(rate_limit_reset) - int(current_time)
    return max(reset_duration // 60, 0)

def get_user_location(url):
    """ Get the location of the GitHub user """
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('location', 'Location not available')
    elif response.status_code == 404:
        return 'Not found'
    elif response.status_code == 403:
        reset_duration = calculate_reset_duration(response.headers.get('X-Ratelimit-Reset', 0))
        return f'Reset in {reset_duration} min'
    else:
        return 'Error occurred'

if __name__ == "__main__":
    if len(argv) == 2:
        print(get_user_location(argv[1]))
    else:
        print("Usage: ./2-user_location.py <github_api_user_url>")
