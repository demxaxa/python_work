#5-11 ordinal_numbers.py

numbers = list(range(1,10))

for num in numbers:
	if num in range(1,3):
		print(str(num) + "nd")
	elif num == 3:
		print(str(num) + "rd")
	else:
		print(str(num) + "th")