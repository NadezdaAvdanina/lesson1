def get_answer(question):
	question = str(question)
	question = question.lower()
	answers = {'привет': 'И тебе привет!', 'как дела': 'Лучше всех', 'пока': 'Увидимся'}
	return answers.get (question, 'Повтори, пожалуйста')

inp = input("Напиши мне ")
x = get_answer(inp)
print(x)