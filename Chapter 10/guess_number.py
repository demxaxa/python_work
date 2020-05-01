#10-11 guess_number.py
import json

filename = 'stored_number.txt'

with open(filename) as f_obj:
	num = json.load(f_obj)

print("I know your favorite number! It's " + str(num))