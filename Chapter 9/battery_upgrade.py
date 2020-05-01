#9-9 battery_upgrade.py

#electric_car.py

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
		return long_name.title()

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


my_tesla = ElectricCar('tesla','model s',2016)

my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()

my_tesla.battery.get_range()






