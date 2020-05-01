#9-14 dice.py

from random import randint

class Die():
	def __init__(self,sides=6):
		self.sides = sides

	def roll_die(self):
		return randint(1,self.sides)

results = []
d6 = Die()
for roll in range(10):
	x = d6.roll_die()
	results.append(x)
print(results)
print()


results = []
d10 = Die(sides=10)
for roll in range(10):
	x = d10.roll_die()
	results.append(x)
print(results)
print()

results = []
d20 = Die(sides=20)
for roll in range(10):
	x = d20.roll_die()
	results.append(x)
print(results)
print()



