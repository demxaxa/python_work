#8-4 large_shirts.py

def make_shirt(text = 'I love Python', size = 'large'):
	"""Displays shirt size and message on it."""
	print("The size of the shirt is: " + size.title() + ".")
	print("The text printed on the shirt is: " + text.title() + '\n')

make_shirt()
make_shirt(size = 'medium')
make_shirt('apple','small')