#8-7 album.py

def make_album(name,album,tracks=""):
	"""Returns dictionary of album info"""
	dictionary={'Name':name.title(), 'Album':album.title()}
	if tracks:
		dictionary['Tracks'] = tracks
		tracks = int(tracks) 
	return dictionary

song = make_album('pink floyd','another brick in the wall')
print(song)

song = make_album('daft punk','RAM')
print(song)

song = make_album('ac/dc','back in black')
print(song)

song = make_album('eminem','encore',134)
print(song)
