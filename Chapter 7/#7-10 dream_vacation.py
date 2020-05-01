#7-10 dream_vacation.py

poll = {}
active = True

while active:
	user = input("Name? ")
	prompt = "If you could visit one place in the world, where would you go? "
	response = input(prompt)

	poll[user] = response

	repeat = input("Does anyone else want to submit an answer? ")
	repeat = repeat.lower()
	print()
	if repeat == 'no':
		active = False

print("\n--- Poll Results ---")
for name,answer in poll.items():
	print(name.title() + " would like to visit " + answer.title() + ".")