#!/usr/bin/env python3

import click
import requests

SAMPLE_API_KEY = 'afbabd3b403b0cb4785db46516e403a7'


def current_weather(location, api_key=SAMPLE_API_KEY):
	url = 'https://api.openweathermap.org/data/2.5/weather'

	query_params = {
		'q': location,
		'appid': api_key,
	}

	response = requests.get (url, params=query_params)

	return response.json ( )[ 'weather' ][ 0 ][ 'description' ]

def scramble(s1,s2):
    if s1 == s2:
        return True
        temp = 0
        for s in s2:
            a = s in s1
            if a:
                temp += 1
            if (temp == len(s2)):
                return True
    return False
@click.command ( )
@click.argument ('location')
@click.option (
	'--api-key', '-a',
	help='your API key for the OpenWeatherMap API',
)
def main(location, api_key):
	"""
	A little weather tool that shows you the current weather in a LOCATION of
	your choice. Provide the city name and optionally a two-digit country code.
	Here are two examples:
	1. London,UK
	2. Canmore
	You need a valid API key from OpenWeatherMap for the tool to work. You can
	sign up for a free account at https://openweathermap.org/appid.
	"""
	weather = current_weather (location, api_key)
	print ("The weather in %s right now: %s", location, weather)


if __name__ == "__main__":
	main ( )
