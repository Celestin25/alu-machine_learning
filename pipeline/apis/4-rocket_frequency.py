#!/usr/bin/env python3
"""
Uses the (unofficial) SpaceX API to print the number of launches per rocket as:
<rocket name>: <number of launches>
ordered by the number of launches in descending order or,
if rockets have the same amount of launches, in alphabetical order
"""

import requests

def get_rocket_name(rocket_id):
    rocket_url = 'https://api.spacexdata.com/v4/rockets/{}'.format(rocket_id)
    response = requests.get(rocket_url).json()
    return response.get('name')

if __name__ == "__main__":
    launches_url = 'https://api.spacexdata.com/v4/launches'
    launches = requests.get(launches_url).json()
    rocket_frequency = {}

    for launch in launches:
        rocket_id = launch.get('rocket')
        rocket_name = get_rocket_name(rocket_id)

        if rocket_name:
            rocket_frequency[rocket_name] = rocket_frequency.get(rocket_name, 0) + 1

    sorted_rockets = sorted(rocket_frequency.items(), key=lambda x: (-x[1], x[0]))

    for rocket in sorted_rockets:
        print("{}: {}".format(rocket[0], rocket[1]))
