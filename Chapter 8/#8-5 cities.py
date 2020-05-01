#8-5 cities.py

def describe_city(city, country = 'egypt'):
	"""Describes where a city is."""
	print(city.title() + " is in " + country.title() + '\n')

describe_city('cairo')
describe_city('alexandria')
describe_city('baku','azerbaijan')