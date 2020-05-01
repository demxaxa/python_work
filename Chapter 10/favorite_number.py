#10-11 favorite_number.py

import json

num = input("What is your favorite number? ")
num = int(num)

filename = 'stored_number.txt'

with open(filename,'w') as f_obj:
	json.dump(num,f_obj)