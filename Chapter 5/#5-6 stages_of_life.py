#5-6 stages_of_life.py

stage = ['baby', 'toddler','kid','teenager','adult','elder']

age = 65

if age<2:
	print(stage[0])
elif age>=2 and age<4:
	print(stage[1])
elif age>=4 and age<13:
	print(stage[2])
elif age>=13 and age<20:
	print(stage[3])
elif age>=20 and age<65:
	print(stage[4])
elif age>=65:
	print(stage[5])