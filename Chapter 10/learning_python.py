#10-1 learning_python.py

filename = 'learning_python.txt'

with open(filename) as file_object:
	contents = file_object.read()
	print(contents)
	print()

with open(filename) as file_object:
	for line in file_object:
		print(line.strip())
	print()

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.strip())