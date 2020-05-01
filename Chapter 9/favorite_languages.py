#favorite_languages.py


from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}



for name,value in favorite_languages.items():
	print(name.title() + "'s favorite language is " + value.title())
print('\n')

