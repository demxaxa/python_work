#10-10 common_words.py



with open('moby_dick.txt') as f:
	contents = f.read()

words = contents.split()

words = [word.lower() for word in words]

num = words.count('the')
print(num)
