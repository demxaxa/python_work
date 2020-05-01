#7-5 movie_tickets.py

while True:
	age = input("How old are you? ")

	if age == 'quit':
		break

	age = int(age)

	if age < 3:
		ticket = 'free'
	elif age>=3 and age <=12:
		ticket = 10
	elif age > 12:
		ticket = 15
	
	print("Your movie ticket is for " + str(ticket))