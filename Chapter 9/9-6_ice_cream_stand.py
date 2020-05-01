#9-6_ice_cream_stand.py

class Restaurant():
	def __init__(self,name,cuisine_type):
		self.name = name.title()
		self.cuisine_type = cuisine_type.title()
		self.number_served = 25

	def describe_restaurant(self):
		print("Restaurant name: " + self.name)
		print("Cuisine type: " + self.cuisine_type)
		print()
		
	def open_restaurant(self):
		print(self.name + " is OPEN.")

	def served(self):
		print("Number of people served: " + str(self.number_served))

	def set_number_served(self,served):
		self.number_served = served 

	def increment_number_served(self,num):
		self.number_served += num


class IceCreamStand(Restaurant):
	def __init__(self,name,cuisine_type='ice_cream'):
		super().__init__(name,cuisine_type)
		self.flavors = []

	def print_flavors(self):
		print("Ice Cream Flavors")
		for flavor in self.flavors:
			print("- " + flavor)


stand = IceCreamStand('baskin robbins')
stand.flavors=['vanilla','chocolate','mango','strawberry']

stand.describe_restaurant()
stand.print_flavors()