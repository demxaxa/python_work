#6-4 glossary_2.py

glossary = {
	'statement':'block of code',
	'variable':'placeholder for text and numbers',
	'PEP 8':'recommendations on how to write python code',
	'method':"function that runs on an object",
	'list comprehension':'compact way to process a sequence and return a list',
	'set':'similar to a list except each item must be unique'
}

for word, meaning in sorted(glossary.items()):
	print(word.title()+": " + meaning)