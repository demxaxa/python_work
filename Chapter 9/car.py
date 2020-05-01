"""A class that can be used to represent a car."""

class Car():
	"""A simple attempt to represent a car."""

	def __init__(self,make,model,year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odomoter_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		print(long_name.title())

	def read_odomoeter(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odomoter_reading) + " miles on it.")

	def update_odometer(self,mileage):
		"""Set thte odometer"""
		if mileage > self.odomoter_reading:
			self.odomoter_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self,miles):
		self.odomoter_reading += miles