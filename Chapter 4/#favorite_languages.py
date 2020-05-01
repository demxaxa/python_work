#favorite_languages.py

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title())

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

for name,value in sorted(favorite_languages.items()):
	print(name.title() + ", thank you for taking the poll!. Your answer was: " + 
		value.title())
print('\n')

for value in sorted(set(favorite_languages.values())):
	print(value.title())