#8-6 city_names.py

def city_country(city, country):
	"""Displays city and country"""
	message = '"' + city.title() + ", " + country.title() + '"'
	return message

string = city_country('cairo','egypt')
print(string)

string =city_country('baku','azerbaijan')
print(string)

string = city_country('berlin','germany')
print(string)