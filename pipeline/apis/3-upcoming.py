#!/usr/bin/env python3
import requests

def get_spacex_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching SpaceX data: {e}")
        return None

if __name__ == "__main__":
    upcoming_launches_url = "https://api.spacexdata.com/v4/launches/upcoming"
    launches = get_spacex_info(upcoming_launches_url)
    
    if not launches:
        exit()

    soonest_launch = min(launches, key=lambda x: x.get('date_unix', float('inf')))

    launch_name = soonest_launch.get('name')
    launch_date = soonest_launch.get('date_local')
    rocket_id = soonest_launch.get('rocket')
    launchpad_id = soonest_launch.get('launchpad')

    rocket_info = get_spacex_info(f"https://api.spacexdata.com/v4/rockets/{rocket_id}")
    launchpad_info = get_spacex_info(f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}")

    if rocket_info and launchpad_info:
        rocket_name = rocket_info.get('name')
        launchpad_name = launchpad_info.get('name')
        launchpad_locality = launchpad_info.get('locality')

        print(f"{launch_name} ({launch_date}) {rocket_name} - {launchpad_name} ({launchpad_locality})")
    else:
        print("Failed to retrieve launch details.")
