#electric_cars.py module

from car import Car

class Battery():
	def __init__(self, battery_size=70):
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size"""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)

	def upgrade_battery(self):
		if self.battery_size < 85:
			self.battery_size = 85

class ElectricCar(Car):
	"""Rrepresents aspects of a car, specific to electric vehicles."""
	def __init__(self,make,model,year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes speicifc to electric car.
		"""
		super().__init__(make,model,year)
		self.battery = Battery()
