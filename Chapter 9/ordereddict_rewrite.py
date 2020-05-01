#9-13_ordereddict_rewrite.py

from collections import OrderedDict

glossary = OrderedDict()

glossary['statement'] = 'block of code'
glossary['variable'] = 'placeholder for text and numbers'
glossary['PEP 8'] = 'recommendations on how to write python code'
glossary['method'] = "function that runs on an object"
glossary['list comprehension'] = 'compact way to process a sequence and '
glossary['list comprehension']+= 'return a list'
glossary['set'] = 'similar to a list except each item must be unique'


for word, meaning in glossary.items():
	print(word.title()+": " + meaning + '\n')