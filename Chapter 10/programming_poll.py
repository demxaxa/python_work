#10-5 programming_poll.py

filename = 'responses.txt'

print("(Enter 'q' to quit)")
while True:
	reason = input("Why do you like prpogramming? ")
	if reason == 'q':
		break
	else:
		with open(filename,'a') as f:
			f.write(reason + '\n')