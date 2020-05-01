#language_survey.py

from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
dab = AnonymousSurvey(question)

dab.show_question()
print("enter 'q' at any time to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	dab.store_response(response)


print("\nThank you to everyone who participated in the survey!")
dab.show_results()