#8-13 user_profile.py

def build_profile(first,last,**user_info):
	profile = {}
	profile['first_name']=first
	profile['last_name']=last
	for key,value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('ahmed','mansour', 
							  college = 'AUC', 
							  grade ='junior',
							  gpa = 3.3)
print(user_profile)