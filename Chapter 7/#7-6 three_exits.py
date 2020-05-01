#7-6 three_exits.py

#Version 1 (Doesn't work)
prompt = ("How old are you? " )
age = ""


while str(age) != 'quit':
	age = input(prompt)
	
	age = int(age)

	if age < 3:
		ticket = 'free'
	elif age>=3 and age <=12:
		ticket = 10
	elif age > 12:
		ticket = 15
	
	print("Your movie ticket is for " + str(ticket))


#Version 2
prompt = ("How old are you? " )
active = True

while active:
	age = input(prompt)
	if age == 'quit':
		active = False
	else:
		age = int(age)

		if age < 3:
			ticket = 'free'
		elif age>=3 and age <=12:
			ticket = 10
		elif age > 12:
			ticket = 15
	
		print("Your movie ticket is for " + str(ticket))


#Version 3
prompt = ("How old are you? " )

while True:
	age = input(prompt)
	if age == 'quit':
		break
	else:
		age = int(age)

		if age < 3:
			ticket = 'free'
		elif age>=3 and age <=12:
			ticket = 10
		elif age > 12:
			ticket = 15
	
		print("Your movie ticket is for " + str(ticket))
