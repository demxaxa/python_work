#8-3 t_shirt.py

def make_shirt(size, text):
	"""Displays shirt size and message on it."""
	print("The size of the shirt is: " + size.title() + ".")
	print("The text printed on the shirt is: " + text.title())

make_shirt(text = 'apple', size = 'large')