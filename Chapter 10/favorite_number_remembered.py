#10-12 favorite_number_remembered.py

#10-11 guess_number.py
import json

filename = 'stored_number.json'
try:
	with open(filename) as f_obj:
		num = json.load(f_obj)
except:
	num = input("What is your favorite number? ")
	num = int(num)
	filename = 'stored_number.json'
	with open(filename,'w') as f_obj:
		json.dump(num,f_obj)
	print("Thanks, I'll remember that.")
else:
	print("I know your favorite number! It's " + str(num))


