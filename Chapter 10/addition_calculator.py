#10-6 addition_calculator.py

print("(Press 'q' to quit)")
while True:
	try:
		num1 = input("\nEnter first number: ")
		if num1 == 'q':
			break
		num1 = int(num1)


		num2 = input("Enter second number: " )
		if num1 == 'q':
			break
		num2 = int(num2)
		print()


	except ValueError:
		print("You must enter a number not a text")
	else:
		sum = num1 + num2
		print("Sum: " + str(sum) + "\n")