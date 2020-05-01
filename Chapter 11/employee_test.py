#11-3 employee_test.py

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.ahmed = Employee('ahmed','mansour',100000)

	def test_give_default_raise(self):
		self.ahmed.give_raise()
		self.assertEqual(self.ahmed.salary,105000)

	def test_give_custom_raise(self):
		self.ahmed.give_raise(10000)
		self.assertEqual(self.ahmed.salary,110000)

unittest.main()