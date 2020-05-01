#7-8 deli.py

sandwich_orders = ['grilled cheese','tuna fish','chicken','ham','bacon']
finished_sandwiches = []

while sandwich_orders:
	current = sandwich_orders.pop()
	print("I'm making your " + current.title() + " sandwich.")

	finished_sandwiches.append(current)

print("\nFinished sandwiches:")
for current in finished_sandwiches:
	print(current.title())