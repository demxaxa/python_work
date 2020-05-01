#10-4 guest_book.py

filename = 'guest_book.txt'

print("(Press 'q' to quit)")
while True:
	message = "Please enter your name: "
	name = input(message)
	if name == 'q':
		break
	else:
		with open(filename,'a') as f:
			f.write(name.title() + ' entered.\n')
		print("Welcome, " + name.title() + "!\n")