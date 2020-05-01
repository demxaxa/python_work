#10-6 addition.py

try:
	num1 = input("Enter first number: ")
	num1 = int(num1)

	num2 = input("Enter second number: " )
	num2 = int(num2)
	print()
	
except ValueError:
	print("You must enter a number not a text")
else:
	sum = num1 + num2
	print("Sum: " + str(sum))