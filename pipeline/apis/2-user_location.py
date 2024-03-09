#!/usr/bin/env python3
"""
Uses the GitHub API to print the location of a specific user,
where user is passed as the first argument of the script with the full API URL

ex) "./2-user_location.py https://api.github.com/users/holbertonschool"
"""

import requests
from sys import argv
from time import time

if __name__ == "__main__":
    if len(argv) < 2:
        raise TypeError(
            "Input must have the full API URL passed in as an argument: {}{}".
            format('ex. "./2-user_location.py ',
                   'https://api.github.com/users/holbertonschool"'))

    url = argv[1]
    try:
        response = requests.get(url)

        if response.status_code == 404:
            print('Not found')
        elif response.status_code == 403:
            reset_time = int(response.headers.get('X-Ratelimit-Reset', 0))
            current_time = int(time())
            minutes = round((reset_time - current_time) / 60)
            print('Reset in {} min'.format(minutes))
        elif response.status_code == 200:
            location = response.json().get('location', 'Not found')
            print(location)
        else:
            print('Not found')
    except requests.RequestException as err:
        print('Not found')
