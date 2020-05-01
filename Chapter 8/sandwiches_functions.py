#sandwiches_functions.py

def make_sandwich(sandwich, *items):
	print("Making a " + sandwich.title() + " sandwich...")
	
	if items:
		print("Adding items requested: ")
		for item in items:
			print("+ " + item.title())
	print("Your sandwich is ready!\n")