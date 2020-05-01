#6-6 polling.py

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

people = ['ahmed','saber','mansour','sarah','phil']

for person in people:
	if person in favorite_languages:
		print("Thank you for responding, " + person.title())
	else:
		print("Please take the poll, " + person.title())
