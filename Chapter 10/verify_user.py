#10-13 verify_user.py

#remember_me.py

import json

def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename,'w') as f_obj:
			json.dump(username,f_obj)
	return username

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	response = input(username + " -- is this the correct username? ")
	response = response.lower()
	if response != 'yes':
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

	elif username:
		print("Welcome back, " + username + "!")	
		
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

greet_user()