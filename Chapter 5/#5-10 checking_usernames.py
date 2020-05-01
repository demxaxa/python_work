#5-10 checking_usernames.py

#REMEMBER THIS!!!!!!

current_users = [current.lower() for current in ['ahmed','Saber','abdelkader',
'mansour','messi']]

new_users = [new.lower() for new in ['ahmed','saber','xavi','iniesta','modric']]


for new in new_users:
	if new in current_users:
		print("You will need to enter a new username.")
	else:
		print('The username "' + new.title() + '" is available.')