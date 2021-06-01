#!/usr/bin/env python3
from typing import List
import requests
import math

base_url = "https://www.metaweather.com/api"


def search_locations(query: str) -> List[str]:
    """Return all the woeids for all cities containing the query string"""
    params = {'query': query}
    r = requests.get(base_url + '/location/search/', params=params)
    json = r.json()
    ids = [str(x['woeid']) for x in json]
    return ids


def temperatures_for_location(woeid: str) -> dict:
    """Return title and the_temps for a location"""
    r = requests.get(base_url + '/location/' + woeid)
    json = r.json()

    useful_keys = ("min_temp", "max_temp", "the_temp")
    output = {'title':json['title'], 'the_temp': []}
    for weather_info in json['consolidated_weather']:
        output['the_temp'].append(weather_info['the_temp'])
    return output

def calculate_temperature_average(temperature_values: List) -> float:
    return sum(temperature_values) / len(temperature_values)


def sum_digits(n: int) -> int:
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


def is_harshad_number(n: int) -> bool:
    """as defined by https://en.wikipedia.org/wiki/Harshad_number """
    return bool(n % sum_digits(n) == 0)


if __name__ == '__main__':
    query = 'San'
    ids = search_locations(query)
    max_temp = -math.inf
    harshad_temps = []
    for woeid in ids:
        data = temperatures_for_location(woeid)
        average_temp = calculate_temperature_average(data['the_temp'])
        # we do this because the prompt says to, but it's never used.
        if average_temp > max_temp:
            max_temp = average_temp
        if is_harshad_number(int(average_temp)):
            harshad_temps.append({data['title']:int(average_temp)})
    print(f"Harshad temperatures: {harshad_temps}")
