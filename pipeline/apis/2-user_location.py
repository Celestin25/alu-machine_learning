#!/usr/bin/env python3
"""
Uses the GitHub API to print the location of a specific user.
The user's GitHub profile URL is passed as the first argument.
"""

import requests
from sys import argv
from time import time

def get_reset_time(headers):
    reset_timestamp = int(headers.get('X-Ratelimit-Reset', 0))
    current_time = int(time())
    return max(0, reset_timestamp - current_time) // 60

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./2-user_location.py <github_user_profile_url>")
        exit(1)

    url = argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        location = response.json().get('location')
        print(location if location else "User location not available")
    elif response.status_code == 404:
        print("User not found")
    elif response.status_code == 403:
        minutes = get_reset_time(response.headers)
        print(f"Rate limit exceeded. Reset in {minutes} min")
    else:
        print("Error occurred")

