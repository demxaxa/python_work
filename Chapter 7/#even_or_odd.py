#even_or_odd.py

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number is even.")
else:
	print("\nThe number is odd.")