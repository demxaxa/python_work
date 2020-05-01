#9-8 privileges.py

from user import User

class Privileges():
	def __init__(self, privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		if self.privileges:
			print("Privileges:")
			for privilege in self.privileges:
				print('- ' + privilege.title())
		else:
			print('This user has no privileges.')
		print()

class Admin(User):
	def __init__(self,first_name,last_name,email,location,username='admin'):
		super().__init__(first_name,last_name,username,email,location)
		self.privileges = Privileges()

