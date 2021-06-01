# Python Coding Challenge

## Problem Description

This exercise consists on writing a Python application that uses an [**API**](https://www.metaweather.com/api/) to fetch, parse and expose data according to the following requirements:

- When provided with a specific query, find all the cities that match that query. The filter will be 'San'.
- Calculate the average temperature for each entry of the previous result (refer to the 'the_temp' value).
- Among the results, find the highest average temperature.
- Find the pairs in which the temperature is a Harshad Number. A [**Harshad number**](https://en.wikipedia.org/wiki/Harshad_number) is a number which is divisible by the sum of its digits. For example, `132` is divisible by `6` (1+3+2). By default the temperature value will be a float, in this case, you should disregard precision and cast it to a int.
- Create a docker image that ships the `conding_challenge.py` content and runs it in a containerized environment. It should print a list of the Harshad temperatures to the command line.

## Expected result:

``` bash
 > docker run challenge
Harshad temperatures: [{'San Diego': 20}, {'Santa Cruz': 24}, {'Santorini': 18}, {'Santander': 12}, {'Santa Cruz de Tenerife': 20}]
```

# Initial Setup
```python
from typing import List
import requests

base_url = "https://www.metaweather.com/api"


def search_locations(query: str) -> list:
    ...


def temperatures_for_location(woeid: str) -> dict:
    ...


def calculate_temperature_average(temperature_values: List) -> float:
    ...


def sum_digits(n: int) -> int:
    ...


def is_harshad_number(n: int) -> bool:
    ...


if __name__ == '__main__':
    ...
```
