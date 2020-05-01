#11-1 city_functions.py

def location(city,country,population=0):
	if population:
		return(city.title() + ', ' + country.title() + ' - population ' + 
			   str(population)) 
	else:
		return(city.title() + ', ' + country.title())
