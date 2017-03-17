def get_answer(quation):
	quation = str(quation)
	quation = quation.lower()
	answer = { 'Привет': 'и тебе привет', 'как дела?': 'Лучше всех', 'пока': 'увидимся!' }
	return answer.get (quation, 'Повтори, пожалуйста')

inp = input('Напиши мне')
х = get_answer(inp)
print(x)
