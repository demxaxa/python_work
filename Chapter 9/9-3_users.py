#9-3_users.py

class User():
	"""Creates user profile and displays info"""

	def __init__(self,first_name,last_name,username,email,location):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.email = email
		self.location = location.title()

	def describe_user(self):
		self.full_name = self.first_name + " " + self.last_name
		print(self.full_name)
		print("\tUsername: " + self.username)
		print("\tEmail: " + self.email)
		print("\tLocation: " + self.location)

	def greet_user(self):
		print("\nWelcome back to your user page, " + self.full_name + "!\n\n")

user1 = User('ahmed','mansour','mr.a.mansour','mr.a.mansour@gmail.com','egypt')
user1.describe_user()
user1.greet_user()

user2 = User('lionel','messi','messi','messi@barca.com','argentina')
user2.describe_user()
user2.greet_user()

user2 = User('john','cena','johncena','john@wwe.com','america')
user2.describe_user()
user2.greet_user()