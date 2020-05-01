#10-9 silent_cats_and_dogs.py

def read_file(filename):
	with open(filename) as f:
		contents = f.read()
	print(contents)


with open('cats.txt','w') as f_obj:
	f_obj.write('Garfield\n')
	f_obj.write('Tom\n')
	f_obj.write('Tiger\n')

with open('dogs.txt','w') as f_obj:
	f_obj.write('Goofy\n')
	f_obj.write('Oddie\n')
	f_obj.write('Snoopy\n')



filenames = ['cat.txt','dogs.txt']

for filename in filenames:
	try:
		read_file(filename)
	except FileNotFoundError:
		pass

