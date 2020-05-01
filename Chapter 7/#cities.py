#cities.py

prompt ="\nPlease enter the name of a city you have visited: "
prompt += "\n(Ener 'quit' when you are finished) "

while True:
	message = input(prompt)

	if message == 'quit':
		break
	else:
		print(message)