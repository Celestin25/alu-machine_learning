#!/usr/bin/env python3
"""
Script to print the location of a GitHub user.
"""

import requests
import sys
from datetime import datetime

def get_user_location(url):
    response = requests.get(url)

    if response.status_code == 404:
        return "Not found"
    elif response.status_code == 403:
        reset_timestamp = int(response.headers.get('X-Ratelimit-Reset', 0))
        reset_time = datetime.utcfromtimestamp(reset_timestamp)
        remaining_time = (reset_time - datetime.utcnow()).total_seconds() // 60
        return f"Reset in {int(remaining_time)} min"
    elif response.status_code == 200:
        user_data = response.json()
        return user_data.get('location', 'Location not provided')
    else:
        return "Error occurred"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub user profile API URL>")
        sys.exit(1)

    user_api_url = sys.argv[1]
    print(get_user_location(user_api_url))
