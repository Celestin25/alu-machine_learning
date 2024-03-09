#!/usr/bin/env python3
"""
Uses the (unofficial) SpaceX API to print the number of launches per rocket as:
<rocket name>: <number of launches>
ordered by the number of launches in descending order or,
if rockets have the same amount of launches, in alphabetical order
"""

import requests

def get_rocket_name(rocket_id):
    url = f'https://api.spacexdata.com/v4/rockets/{rocket_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('name', 'Unknown Rocket')
    return 'Unknown Rocket'

if __name__ == "__main__":
    url = 'https://api.spacexdata.com/v4/launches'
    launches = requests.get(url).json()
    
    rocket_counts = {}
    for launch in launches:
        rocket_id = launch.get('rocket')
        rocket_counts[rocket_id] = rocket_counts.get(rocket_id, 0) + 1

    # Fetch rocket names
    rocket_names = {}
    for rocket_id in rocket_counts:
        rocket_name = get_rocket_name(rocket_id)
        rocket_names[rocket_name] = rocket_counts[rocket_id]

    # Sort by number of launches and then alphabetically
    sorted_rockets = sorted(rocket_names.items(), key=lambda x: (-x[1], x[0]))

    for rocket in sorted_rockets:
        print(f"{rocket[0]}: {rocket[1]}")
