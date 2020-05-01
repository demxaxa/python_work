#6-5 rivers.py

rivers = {
	'nile':'egypt',
	'amazon':'brazil',
	'yangtze':'china',
}

for river,country in sorted(rivers.items()):
	print("The " + river.title() + " river runs through " + country.title() + ".")
print()

for river in sorted(set(rivers)):
	print(river.title())
print()

for country in sorted(set(rivers.values())):
	print(country.title())