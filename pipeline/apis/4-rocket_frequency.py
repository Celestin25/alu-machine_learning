#!/usr/bin/env python3
"""
Script to display the number of launches per rocket using the SpaceX API.
"""

import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: HTTP {response.status_code}")
        exit(1)

def get_rocket_name(rocket_id, rockets):
    return rockets.get(rocket_id, {}).get('name', 'Unknown Rocket')

if __name__ == '__main__':
    launches = fetch_data('https://api.spacexdata.com/v4/launches')
    rockets_info = fetch_data('https://api.spacexdata.com/v4/rockets')

    # Create a mapping of rocket IDs to rocket names
    rockets = {rocket['id']: rocket for rocket in rockets_info}

    # Count launches per rocket ID
    launch_counts = {}
    for launch in launches:
        rocket_id = launch['rocket']
        rocket_name = get_rocket_name(rocket_id, rockets)
        launch_counts[rocket_name] = launch_counts.get(rocket_name, 0) + 1

    # Sort and print the launch counts
    for rocket_name, count in sorted(launch_counts.items(), key=lambda item: (-item[1], item[0])):
        print(f"{rocket_name}: {count}")
