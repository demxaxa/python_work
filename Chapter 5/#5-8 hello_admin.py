#5-8 and 5-9 hello_admin.py

usernames = ['ahmed','saber','abdelkader','mansour','admin']

if usernames == []:
	print("We need to find some users!")
else:
	for username in usernames:
		if(username == 'admin'):
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello " + username.title() + ", thank you for logging in again.")

