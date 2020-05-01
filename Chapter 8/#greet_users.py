#greet_users.py

def greet_users(names):
	"""Print a simple greeting to each user on list."""
	for name in names:
		print("Hello, " + name.title() + "!")

usernames = ['ahmed','saber','mansour']
greet_users(usernames)