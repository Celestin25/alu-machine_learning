#!/usr/bin/env python3
"""
Uses the (unofficial) SpaceX API to print the number of launches per rocket.
"""

import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
        exit(1)

if __name__ == "__main__":
    # Fetch list of all launches
    launches_url = "https://api.spacexdata.com/v4/launches"
    launches = fetch_data(launches_url)

    # Fetch list of all rockets for name mapping
    rockets_url = "https://api.spacexdata.com/v4/rockets"
    rockets = fetch_data(rockets_url)
    rocket_name_map = {rocket["id"]: rocket["name"] for rocket in rockets}

    # Count launches per rocket
    launch_count = {}
    for launch in launches:
        rocket_id = launch.get("rocket")
        rocket_name = rocket_name_map.get(rocket_id, "Unknown Rocket")
        launch_count[rocket_name] = launch_count.get(rocket_name, 0) + 1

    # Sort and print
    sorted_launches = sorted(launch_count.items(), key=lambda x: (-x[1], x[0]))
    for rocket, count in sorted_launches:
        print(f"{rocket}: {count}")
