#no_pastrami.py

sandwich_orders = ['grilled cheese','tuna fish','chicken','ham','bacon']
sandwich_orders +=['pastrami','pastrami','pastrami']

finished_sandwiches = []

print("The deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')


while sandwich_orders:
	current = sandwich_orders.pop()
	print("I'm making your " + current.title() + " sandwich.")

	finished_sandwiches.append(current)

print("\nFinished sandwiches:")
for current in finished_sandwiches:
	print(current.title())