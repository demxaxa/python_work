#6-9 favorite_places.py

favorite_places = {
	'ahmed':'mcdonalds',
	'saber':'pizza hut',
	'mansour': 'kfc',
}

for person, food in list(sorted(favorite_places.items())):
	print("Name: " + person.title())
	print("Favorite place: " + food.title())