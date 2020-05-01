#7-3 multiples_of_ten.py

num = input("Enter a number: ")
num = int(num)

if num % 10 == 0:
	print("\nThe number " + str(num) + " is a multiple of 10.")
else:
	print("\nThe number " + str(num) + " is NOT a multiple of ten.")