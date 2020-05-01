#6-11 cities.py

cities = {
	'cairo': {'country':'egypt','population':20000000,'fact':'largest city in africa'},
	'baku':{'country':'azerbaijan','population':2236000,'fact':'nicknamed city of the winds'},
	'paris': {'country':'france','population':2200000,'fact':'only has one stop sign in the entire city'},
}

for city, info in cities.items():
	print(city.title())
	print("\tCountry: " + info['country'].title())
	print("\tPopulation: " + str(info['population']))
	print("\tFact: " + info['fact'].title())