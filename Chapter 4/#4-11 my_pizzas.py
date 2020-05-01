#4-11 my_pizzas.py

pizzas = ['pepperoni', 'super supreme', 'margherita']
friends_pizzas = pizzas[:]

pizzas.append('seafood')
friends_pizzas.append('neapolitan')

print("My favorite pizzas are: ")
for pizza in pizzas:
	print("*"+pizza.title())

print("\nMy friend's favorite pizzas are: ")
for friends in friends_pizzas:
	print("*" + friends.title())