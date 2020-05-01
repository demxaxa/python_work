#8-11 unchanges_magicians.py

def show_magicians(magicians):
	"""Prints the name of each magician in the list"""
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	""""Modifies list of magiciains"""
	great_magicians = []
	while magicians:
		magician = magicians.pop()
		great_magician = magician.title() + " the Great"
		great_magicians.append(great_magician)
	
	for great_magician in great_magicians:
		magicians.append(great_magician)

	return magicians


magicians = ['houdini','copperfield','robbins','blaine','jillette']
show_magicians(magicians)

print("\nGreat Magicians: ")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal Magicians: ")
show_magicians(magicians)