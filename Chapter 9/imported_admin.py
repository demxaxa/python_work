#9-11 imported_admin.py

from privileges import Admin

admin = Admin('ahmed','mansour','admin@gmail.com','egypt')
admin.describe_user()

admin.privileges.show_privileges()

admin.privileges.privileges = ['can reset passwords',
					'can add/remove posts',
					'can ban users',
					'can suspend users',
					]

admin.privileges.show_privileges()

