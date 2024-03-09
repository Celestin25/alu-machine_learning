#!/usr/bin/env python3
"""
Script to display the number of launches per rocket using the SpaceX API.
"""

import requests

def get_launch_count_by_rocket():
    response = requests.get('https://api.spacexdata.com/v4/launches')
    if response.status_code != 200:
        return None

    launches = response.json()
    rocket_ids = [launch['rocket'] for launch in launches]

    rocket_count = {}
    for rocket_id in set(rocket_ids):
        count = rocket_ids.count(rocket_id)
        rocket_info = requests.get(f'https://api.spacexdata.com/v4/rockets/{rocket_id}').json()
        rocket_name = rocket_info.get('name', 'Unknown')
        rocket_count[rocket_name] = count

    return rocket_count

def main():
    rocket_count = get_launch_count_by_rocket()
    if rocket_count:
        for rocket, count in sorted(rocket_count.items(), key=lambda item: (-item[1], item[0])):
            print(f"{rocket}: {count}")

if __name__ == '__main__':
    main()
