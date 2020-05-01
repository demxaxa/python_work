#pets.py

def describe_pet(pet_name,animal_type = 'dog'):
	"""Display info about pet."""
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")

describe_pet('willie')