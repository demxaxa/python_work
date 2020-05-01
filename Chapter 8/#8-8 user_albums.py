#8-8 user_albums.py

def make_album(name, album, tracks=""):
	"""Returns dictionary of album info"""
	dictionary={'Name':name.title(), 'Album':album.title()}
	if tracks:
		dictionary['Tracks'] = tracks
		tracks = int(tracks) 
	return dictionary

while True:
	name = input("Artist's name: ")
	print("(enter 'q' at any time to quit)")
	if name == 'q':
		break

	album = input ("Album: ")
	if album == 'q':
		break

	response = input("Do you want to enter # of tracks? ")
	response = response.lower()
	if response == 'q':
		break
	elif response == 'yes':
		tracks = input("# of Tracks: ")
		song = make_album(name,album,tracks)
		print(song + '\n')
	else:
		song = make_album(name,album)
		print(song + '\n')