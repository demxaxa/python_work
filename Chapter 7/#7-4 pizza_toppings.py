#7-4 pizza_toppings.py

active = True
while active:
	topping = input("Enter a pizza topping: ")
	if topping == 'quit':
		active = False
	else:
		print("Adding " + topping.title())