#9-1 restaurant.py

class Restaurant():
	def __init__(self,name,cuisine_type):
		self.name = name.title()
		self.cuisine_type = cuisine_type.title()

	def describe_restaurant(self):
		print("Restaurant name: " + self.name)
		print("Cuisine type: " + self.cuisine_type)

	def open_restaurant(self):
		print(self.name + " is OPEN.")

restaurant = Restaurant('mcdonalds','hamburgers')

print(restaurant.name)
print(restaurant.cuisine_type + '\n')

restaurant.describe_restaurant()
print()
restaurant.open_restaurant()