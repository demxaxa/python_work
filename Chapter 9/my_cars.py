#my_cars.py

from car import Car
from electric_cars import ElectricCar

gas = Car('volkswagen','beetle',2016)
gas.get_descriptive_name()

electric = ElectricCar('tesla','model s', 2016)
electric.get_descriptive_name()

