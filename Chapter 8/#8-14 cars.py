#8-14 cars.py

def make_car(manufacturer,model, **other):
	info = {}
	info['Manufacturer'] = manufacturer.title()
	info['Model'] = model.title()
	for key, value in other.items():
		info[key] = value
	return info

car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)