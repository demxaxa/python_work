#9-4_number_served.py

class Restaurant():
	def __init__(self,name,cuisine_type):
		self.name = name.title()
		self.cuisine_type = cuisine_type.title()
		self.number_served = 25

	def describe_restaurant(self):
		print("Restaurant name: " + self.name)
		print("Cuisine type: " + self.cuisine_type)

	def open_restaurant(self):
		print(self.name + " is OPEN.")

	def served(self):
		print("Number of people served: " + str(self.number_served))

	def set_number_served(self,served):
		self.number_served = served 

	def increment_number_served(self,num):
		self.number_served += num

restaurant = Restaurant('mcdonalds','hamburgers')

restaurant.set_number_served(51900)
restaurant.served()

restaurant.increment_number_served(100)
restaurant.served()