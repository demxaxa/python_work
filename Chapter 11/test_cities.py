#11-1 test_cities.py

import unittest
from city_functions import location

class LocationTestCase(unittest.TestCase):
	def test_city_country(self):
		place = location('santiago','chile')
		self.assertEqual(place,'Santiago, Chile')

	def test_city_country_population(self):
		place = location('santiago','chile',5000000)
		self.assertEqual(place,'Santiago, Chile - population 5000000')

unittest.main()